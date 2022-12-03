# import matplotlib.pyplot as plt
# import numpy as np


# print(np.loadtxt("./data/task_.txt")[0, :])

import matplotlib.pyplot as plt
import numpy as np

print(list(range(0, len(np.loadtxt("./data/task_.txt")))))

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

if __name__ == '__main__':
    reward = np.loadtxt("./result/reward.txt")
    plt.plot(np.arange(len(reward)), reward, "green")
    plt.ylabel('Reward奖励')
    plt.xlabel('训练步')
    plt.show()
    plt.savefig("./result/reward.png")

    loss = np.loadtxt("./result/loss.txt")
    plt.plot(np.arange(len(loss)), loss, "red")
    plt.ylabel('Loss损失')
    plt.xlabel('训练步')
    plt.show()
    plt.savefig("./result/loss.png")
