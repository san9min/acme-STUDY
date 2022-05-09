# DQN Learner
class DQNLearner():

  def __init__():

  def _step():
    # 진짜 agent에서 준비한 reverb dataset 사용
    # dataset을 사용하며, algorithm 구현의 핵심 파트 
    # 주어진 횟수마다 target을 update. 이곳이 진짜 업데이트 부분.
    if tf.math.mod(self._num_steps, self._target_update_period) == 0:
      for src, dest in zip(self._network.variables,
                           self._target_network.variables):
        dest.assign(src)

  def step():
    result = self._step()

  def get_variables():
  def state():