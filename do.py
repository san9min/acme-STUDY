from acme.agents.tf import dqn

agent = acme.agents.tf.dqn.DQN(env_spec, network)

loop = acme.EnvironmentLoop(env, agent)
loop.run(10)