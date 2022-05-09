def compute_avg_return(env,policy,num_episodes =10):

  total_return = 0.0
  for _ in range(num_episodes):

    time_step = env.reset()
    episode_return = 0.0

    while not time_step.is_last():
      action_step = policy.action(time_step) # policy -> action
      time_step = env.step(action_step.action) # env.step(action)
      episode_return += time_step.reward # episode return
    total_return += episode_return # sum of episode returns

  avg_return = total_return / num_episodes  # tf.Tensor([avg_return_val],shape = (1,),dtype=float32)
  return avg_return.numpy()[0] # avg_return_val