"""
Reinforcement learning maze example.

Red rectangle:          explorer.
Black rectangles:       hells       [reward = -1].
Yellow bin circle:      paradise    [reward = +1].
All other states:       ground      [reward = 0].

This script is the environment part of this example.
The RL is in RL_brain.py.

View more on my tutorial page: https://morvanzhou.github.io/tutorials/
"""

import numpy as np


class Para_env:
    def __init__(self):


        self.reward_added = 0
        self.reward_all = []

    def reset(self):
        self.reward_added = 0
        self.reward_table = np.loadtxt("./data/task_.txt")
        observation = list(range(0, len(self.reward_table)))
        print(observation)
        self.scale = 0
        return observation

    def step(self, s, action):
        # 计算并记录奖励

        temp = self.reward_table[action,:]
        reward = (0.5*temp[0]+0.3*temp[1]+0.2*temp[2]) * (10-self.scale)
        self.scale += 1
        self.reward_added += reward

        print(action, temp, reward)
        # 更新状态，判断是否结束
        s[action] = 0
        if np.sum(s) == 0:
            done = True
            self.reward_all.append(self.reward_added)
            print(self.reward_added)
            self.reward_added = 0
            np.savetxt("./result/reward.txt", np.array(self.reward_all), fmt="%f", delimiter=" ")
        else:
            done = False
        s_ = s
        return s_, reward, done
