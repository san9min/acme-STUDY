import gym 
import acme
from acme import wrappers

env0 = gym.make(id='PongNoFrameskip-v0')
env1 = acme.wrappers.GymAtariAdapter(env0)
env2 = acme.wrappers.AtariWrapper(env1, 
            to_float=True,
            max_episode_len=1000,
            zero_discount_on_life_loss=True,)
env = acme.wrappers.SinglePrecisionWrapper(env2)

env_spec = acme.make_environment_spec(env)

from acme.agents.tf import dqn

agent = acme.agents.tf.dqn.DQN(env_spec, network)

loop = acme.EnvironmentLoop(env, agent)
loop.run(10)


'''
#gym install
!pip install -U gym > /dev/null
!pip install -U gym[atari,accept-rom-license] > /dev/null

#acme install
!pip install dm-acme > /dev/null
'''