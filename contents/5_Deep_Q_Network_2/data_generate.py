"""
数据生成和预处理
"""
import os
import numpy as np

# 创建文件夹
if not os.path.exists("./data/"):
    os.makedirs("./data/")
if not os.path.exists("./result/"):
    os.makedirs("./result/")

# 待选数据
# num_test = 10000
# limit_time = np.random.randint(60, 300, size=(num_test,1))
# finish_time = np.random.randint(2, 10, size=(num_test,1))
# work_time_sum = np.sum(finish_time, axis=1)
# 实际数据
num_task = 10
# one_min,one_max = 20,100
# lim_min,lim_max = 600, 3000
task_ = np.zeros(shape=(num_task, 3), dtype=float)
# task_[:,0] = np.random.randint(one_min,one_max,size=(num_task))  # 工作时间
# task_[:,1] = np.random.randint(lim_min,lim_max,size=(num_task))  # 交货时间
# task_[:,2] = np.random.random(num_task) # 客户重要程度
# task_max = np.max(task_, axis=0)
# task_min = np.min(task_, axis=0)
# d_valve = task_max-task_min
# left_time = task_[:,1]-task_[:,0]
# left_time_max = np.max(left_time)
# left_time_min = np.min(left_time)
for i in range(num_task):
    task_[:,0] = np.random.random(num_task)  # 紧急度
    task_[:,1] = 0.8*task_[:,0] + 0.2  # 利润因子
    task_[:,2] = 0.2*task_[:,0] + 0.8*np.random.random(num_task)  # 客户重要程度

np.savetxt("./data/task_.txt", task_, delimiter=" ", fmt="%f")

# tt = np.loadtxt("./data/task_.txt")[:,:2].reshape(-1)
# print(tt[np.newaxis,:])

