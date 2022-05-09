def run_episode(self) -> loggers.LoggingData:
    
    start_time = time.time()
    episode_steps = 0

    episode_return = np.zero() # return과 같은 모습의 vector
    timestep = self._environment.reset()

    # Run an episode.
    while not timestep.last():
      
      action = self._actor.select_action(timestep.observation)
      timestep = self._environment.step(action)

      self._actor.observe(action, next_timestep=timestep)
      
      if self._should_update:
        self._actor.update()

      # Book-keeping.
      episode_steps += 1

      episode_return += timestep.reward
                                          
    # Record counts.
    counts = self._counter.increment(episodes=1, steps=episode_steps)

    # Collect the results and combine with counts.
    steps_per_second = episode_steps / (time.time() - start_time)
    result = {
        'episode_length': episode_steps,
        'episode_return': episode_return,
        'steps_per_second': steps_per_second,
    }
    result.update(counts)
    for observer in self._observers:
      result.update(observer.get_metrics())
    return result