# ACME-STUDY
**Reinforcement Learning Framework**

In 2021 winter

1. Create an *Agent*  
2. Build *Policy* for mapping environment observations to actions  
3. Create an *Actor*  
  -Actor is a component of agent, which observes states and takes action according to policy. Another component of agent is learner, which consumes data collected by        actor to improve. This factorization facilitates distributed reinforcement learning, which is helpful when algorithm is complex  
4. Evaluate a random actor’s policy  
5. Learn from the evaluation and replay  

![ENV LOOP](https://user-images.githubusercontent.com/92682815/167327540-001cdf4f-e6d6-4c0b-8aa3-4a8d6146bada.png)
![ENV LOOP 2](https://user-images.githubusercontent.com/92682815/167327552-0fe111bc-9caf-4f94-b1ad-ac6315a80b25.png)
