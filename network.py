from keras.models import Sequential
from keras.layers import Dense, Dropout, Conv2D, MaxPooling2D, Activation, Flatten
from keras.callbacks import TensorBoard
from keras.optimizers import Adam
from collections import deque
import numpy as np
import time
import tensorflow as tf
import random
import os
from tqdm import tqdm
from game import Game
from field import Field

widthPixel = 90
heightPixel = 90
networkActionCount = 8


if not os.path.isdir('models'):
    os.makedirs('models')


class ModifiedTensorBoard(TensorBoard):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.step = 1
        self.writer = tf.summary.FileWriter(self.log_dir)

    def set_model(self, model):
        pass

    def on_epoch_end(self, epoch, logs=None):
        self.update_stats(**logs)

    def on_batch_end(self, batch, logs=None):
        pass

    def on_train_end(self, _):
        pass

    def update_stats(self, **stats):
        self._write_logs(stats, self.step)


class DQNAgent:
    DISCOUNT = 0.99
    REPLAY_MEMORY_SIZE = 50000
    MIN_REPLAY_MEMORY_SIZE = 1000
    MINIBATCH_SIZE = 64
    UPDATE_TARGET_EVERY = 5
    MODEL_NAME = 'test'
    MIN_REWARD = -200
    MEMORY_FRACTION = 0.20

    AGGREGATE_STATS_EVERY = 50

    EPISODES = 20_000

    epsilon = 0.2
    EPSILON_DECAY = 0.99975
    MIN_EPSILON = 0.001

    ep_rewards = [-200]

    def __init__(self):

        self.model = self.create_model()

        self.target_model = self.create_model()
        self.target_model.set_weights(self.model.get_weights())

        self.replay_memory = deque(maxlen=self.REPLAY_MEMORY_SIZE)

        self.tensorboard = ModifiedTensorBoard(log_dir="logs/{}-{}".format(self.MODEL_NAME, int(time.time())))

        self.target_update_counter = 0

    def create_model(self):
        model = Sequential()

        model.add(Conv2D(256, (3, 3), input_shape=(widthPixel, heightPixel, 3)))
        model.add(Activation('elu'))
        model.add(MaxPooling2D(pool_size=(2, 2)))
        model.add(Dropout(0.2))

        model.add(Conv2D(128, (3, 3)))
        model.add(Activation('elu'))
        model.add(MaxPooling2D(pool_size=(2, 2)))
        model.add(Dropout(0.2))

        model.add(Flatten())
        model.add(Dense(64))

        model.add(Dense(networkActionCount, activation='linear'))
        model.compile(loss="mse", optimizer=Adam(lr=0.001), metrics=['accuracy'])
        return model

    def update_replay_memory(self, transition):
        self.replay_memory.append(transition)

    def train(self, terminal_state, step):
        if len(self.replay_memory) < self.MIN_REPLAY_MEMORY_SIZE:
            return

        minibatch = random.sample(self.replay_memory, self.MINIBATCH_SIZE)

        current_states = np.array([transition[0] for transition in minibatch]) / 255
        current_qs_list = self.model.predict(current_states)

        new_current_states = np.array([transition[3] for transition in minibatch]) / 255
        future_qs_list = self.target_model.predict(new_current_states)

        X = []
        y = []

        for index, (current_state, action, reward, new_current_state, done) in enumerate(minibatch):
            if not done:
                max_future_q = np.max(future_qs_list[index])
                new_q = reward + self.DISCOUNT * max_future_q
            else:
                new_q = reward

            current_qs = current_qs_list[index]
            current_qs[action] = new_q

            X.append(current_state)
            y.append(current_qs)

        self.model.fit(np.array(X) / 255, np.array(y), batch_size=self.MINIBATCH_SIZE, verbose=0, shuffle=False, callbacks=[self.tensorboard] if terminal_state else None)

        if terminal_state:
            self.target_update_counter += 1

        if self.target_update_counter > self.UPDATE_TARGET_EVERY:
            self.target_model.set_weights(self.model.get_weights())
            self.target_update_counter = 0

    def get_qs(self, state):
        return self.model.predict(np.array(state).reshape(-1, *state.shape) / 255)[0]


agent = DQNAgent()

canvas = Field(widthPixel, heightPixel)

game = Game(canvas, widthPixel, heightPixel)

for episode in tqdm(range(1, agent.EPISODES + 1), ascii=True, unit='episodes'):
    agent.tensorboard.step = episode

    episode_reward = 0
    step = 1

    current_state = game.reset()

    done = False
    while not done:
        if np.random.random() > agent.epsilon:
            action = np.argmax(agent.get_qs(current_state))
        else:
            action = np.random.randint(0, 8)

        new_state, reward, done = game.update(action)

        episode_reward += reward

        agent.update_replay_memory((current_state, action, reward, new_state, done))
        agent.train(done, step)

        current_state = new_state
        step += 1

    agent.ep_rewards.append(episode_reward)
    if not episode % agent.AGGREGATE_STATS_EVERY or episode == 1:
        average_reward = sum(agent.ep_rewards[-agent.AGGREGATE_STATS_EVERY:]) / len(agent.ep_rewards[-agent.AGGREGATE_STATS_EVERY:])
        min_reward = min(agent.ep_rewards[-agent.AGGREGATE_STATS_EVERY:])
        max_reward = max(agent.ep_rewards[-agent.AGGREGATE_STATS_EVERY:])
        agent.tensorboard.update_stats(reward_avg=average_reward, reward_min=min_reward, reward_max=max_reward, epsilon=agent.epsilon)

        if min_reward >= agent.MIN_REWARD:
            agent.model.save(f'models/{agent.MODEL_NAME}__{max_reward:_>7.2f}max_{average_reward:_>7.2f}avg_{min_reward:_>7.2f}min__{int(time.time())}.model')

    if agent.epsilon > agent.MIN_EPSILON:
        agent.epsilon *= agent.EPSILON_DECAY
        agent.epsilon = max(agent.MIN_EPSILON, agent.epsilon)
