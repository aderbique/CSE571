# Assignment 2
### Fall 2020: Artificial Intelligence
### Author: Austin Derbique

## Disclaimer
The following text shall not be used for the purposes of academic dishonesty. It is granted only for educational & archival purposes, not to be used by other students enrolled in an artificial intelligence class. This information is not guaranteed to be correct. Please consult the textbook [Artificial Intelligence A Modern Approach](https://www.amazon.com/Artificial-Intelligence-Modern-Approach-3rd/dp/0136042597) for up to date and accurate information.

# Exercises 

## Exercise 1.1 (8pt)
### Prompt
Sometimes MDPs are formulated with the reward function R(s,a) that depends only on the current state and action taken or with a reward function R(s) that only dpeends on the current state.  
A. (2pt) Write the Bellman equations for these formulations *for the optimal value function.*  
B. (3pt) Show how an MDP with reward function R(s,a,s<sup>'</sup>) can be transformed into a different MDP with a reward function R(s,a), such that optimal policies in the new MDP correspond exactly to optimal policies in the original MDP. **You must formally define the new MDP (its components) based on the old MDP.**  
C. (3pt) Now do the same to convert MDPs with R(s,a,s') into MDPs with R(s). **You must formally define the new MDP (its components) based on the old MDP.**  

### Response

## Exercise 1.2 (10pt)
### Prompt
Consider the 3 x 3 world shown below. The transition model is the same as in our robot domain: 80% of the time the agent goes in the direction it selects; the rest of the time it moves at right angles to the intended direction.
Insert Figure Here

Use discounted rewards with a discount factor of 0.99. Show the policy obtained in each case. **Explain intuitively** why the value of r leads to each policy.
A. r = 100  
B. r = -3  
C. r = 0  
D. r = +3  

### Response

## Exercise 1.3 (8pt)
### Prompt
Consider the 101 x 3 world shown below. In the start state the agent has a choice of two deterministic actions, Up or Down, but in the other states the agent has one deterministic action, Right. Assuming a discounted reward function, for what values of the discount `v` should the agent choose Up and for which Down? Compute the utility of each action as a function of `v`. (Note that this simple example actually reflects many real-world situations in which one must weight the value of an immediate action versus the potential continual long-termin consequences, such as choosing to dump pollutants into a lake.)

<Inser fiogure here>

### Reponse

## Exercise 1.4 (12pt)
### Prompt
Apply policy iteration, showing each step in full, to determine the optimal policy when the *initial policy* is pi(cool) = Slow and pi(warm) = fast. **Show both the policy evaluation and policy improvement steps cleary until convergence.** Assuming a discount factor of 0.5.


### Reponse

## Exercise 1.5 (12pt)
### Prompt
<<Inser Figure>
Consider the car domain above (without knowing the T or R) and given the following experiences:  
|----|----|----|----|
|Episode 1|
|cool|slow|cool|+1|
|cool|slow|cool|+1|
|cool|fast|cool|+2|
|cool|fast|cool|+2|
|cool|fast|warm|+2|
|warm|fast|overheated|-10|
|Episode 2|
|warm|slow|warm|+1|
|warm|slow|cool|+1|
|cool|slow|cool|+1|
|cool|fast|warm|+2|
|warm|slow|warm|+1|
|warm|slow|warm|+1|
|warm|fast|overheated|-10|

A. (2pt) Estimating the parameters for T and R for model-based reinforcement learning.  
B. (2pt) Use MC reinforcement learning method (direct evaluation) to estimate the V function, assuming $\gamma=1.0.  
C. (4pt) Assuming that the initial state values are allk zeros, compute the updates *in TD learning for policy evaluation (passive RL)* to the state values after running through episode 1 and 2 in sequence. Show steps for $\alpha = 0.5 and $\gamma = 1.0.  
D. (4pt) Assumning that the initial Q values are all zeros, compute the updates *in Q learning (active RL) to the Q values after running through episode 1 and 2 in sequence. Show steps for $\alpha=0.5 and $\gamma=1.0. 
