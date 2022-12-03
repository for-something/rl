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
        self.jiance = []

    def reset(self):
        self.reward_added = 0
        self.reward_table = np.loadtxt("./data/task_.txt")
        self.state = 0
        observation = self.reward_table.reshape(-1)
        return observation

    def step(self, s, action):
        # 计算并记录奖励

        temp = self.reward_table[action,:]
        reward = (0.5*temp[0]+0.3*temp[1]+0.2*temp[2]) * (10-self.state)
        self.reward_added += reward

        # debug
        # print(action, temp, reward)

        # 更新状态，判断是否结束
        s[action*3],s[action*3+1],s[action*3+2] = 0,0,0
        self.state += 1
        if self.state == 10:
            done = True
            self.reward_all.append(self.reward_added)
            print(self.reward_added)
            self.reward_added = 0
            np.savetxt("./result/reward.txt", np.array(self.reward_all), fmt="%f", delimiter=" ")
            self.jiance.append(s)
            np.savetxt("./result/jiance.txt", np.array(self.jiance), fmt="%f", delimiter=" ")
        else:
            done = False
        s_ = s
        return s_, reward, done
