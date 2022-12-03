from maze_env import Para_env
from RL_brain import DeepQNetwork


def run_env():
    step = 0
    for episode in range(4000):
        print("step=", step, "episode", episode // 50 * "=")
        observation = env.reset()

        while True:

            action = RL.choose_action(observation)

            observation_, reward, done = env.step(observation, action)

            RL.store_transition(observation, action, reward, observation_)

            if (step > 100) and (step % 10 == 0):
                RL.learn()

            observation = observation_

            step += 1
            if done:
                break
    print('game over')


if __name__ == "__main__":
    env = Para_env()
    RL = DeepQNetwork(10, 10)
    run_env()
