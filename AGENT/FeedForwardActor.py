# FEED FORWARD ACTOR
class FeedForwardActor():

  def __init__():

    # 진짜 agent에서 준비한 reverb adder 사용
    self._adder = adder
    self._variable_client = variable_client
    self._policy_network = policy_network

  def _policy():
    batched_observation = tf2_utils.add_batch_dim(observation)
    policy = self._policy_network(batched_observation)
    action = policy.sample() if isinstance(policy, tfd.Distribution) else policy
    return action

  def select_action(): # 진짜 select action, _policy를 이용함.
    action = self._policy(observation)
    return tf2_utils.to_numpy_squeeze(action)

  def observe_first(): # 진짜 observe_first
    if self._adder:
      self._adder.add_first(timestep)

  def observe(): # 진짜 observe
    if self._adder:
      self._adder.add(action, next_timestep)

  def update(): # _variable_client=None 이므로 의미없음. 아직 예제 없음(확인 필요)
    if self._variable_client:
      self._variable_client.update(wait)