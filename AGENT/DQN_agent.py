# DQN AGENT
class DQN(agent.Agent):

  def __init__():
    # reverb adder와 dataset 준비
    # policy network과 target network 준비하기 

    actor = actors.FeedForwardActor()
    learner = learning.DQNLearner()

    super().__init__(
        actor=actor,
        learner=learner)

  def update(self):
    super().update()
    