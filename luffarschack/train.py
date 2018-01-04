from keras.models import Sequential
from keras.layers.core import Dense
from keras.optimizers import sgd

from luffarschack import LuffarSchack
import numpy as np
import time

epochs = 250
memory = 5
hidden_size = 100

model = Sequential()
model.add(Dense(hidden_size, input_shape=(3, 3), activation='relu'))
model.add(Dense(hidden_size, activation='relu'))
model.add(Dense(3))
model.compile(sgd(lr=.2), "mse")

for epoch in range(epochs):
    ls = LuffarSchack()
    winner = 0
    states = list()
    targets = list()
    reward_targets = list()
    while winner == 0:
        empty_moves = ls.empty()
        if empty_moves.shape[0] == 0:
            winner = -1
            break
        # Player 1 random move
        random_move = np.random.choice(empty_moves, 1)[0]
        ls.move(1, random_move)

        # Player 2 random move
        random_move = np.random.choice(empty_moves, 1)[0]
        z = list()
        state = np.copy(ls.board)
        z.append(state)
        prediction = np.copy(model.predict(np.array(z)))
        if epoch > epochs - 2:
            print(state)
            print("prediction")
            print(prediction)
            print("-------")

        states.append(state)
        target = np.copy(ls.move(2, random_move))
        targets.append(target)
        if epoch > 23:
            pass
            #print(state)
            #print(target)
        #print("-----")

        winner = ls.winner()
        if winner > 0:
            print("Player {0} won.".format(winner))

    reward = 0.5 # draw
    if winner == 1:
        reward = 0.1
    if winner == 2:
        reward = 0.9

    for t in targets:
        reward_targets.append(ls.create_target(t, reward))

    i = np.array(states)
    t = np.array(reward_targets)

    #print(i)
    #print(t)
    model.train_on_batch(i, t)
    #print(reward_targets)
