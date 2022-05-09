class EnvironmentLoop():

    def __init__(self, environment, actor):
        self._environment = environment
        self._actor = actor

    def run_episode(self):
        ...
        return result

    def run(self, num_episodes, num_steps=None):
        ...
        episode_count, step_count = 0, 0
        
        while not should_terminate(episode_count, step_count):
            result = self.run_episode()
            episode_count += 1
            step_count += result['episode_length']
            # Log the given episode results.
            print(result)