# Assignment 1
### Fall 2020: Artificial Intelligence
### Author: Austin Derbique

# Exercises 

## Exercise 1.1
### Prompt
Suppose that the performance measure is concerned with just the first T time steps of the environment and ignores everything thereafter. Show that a rational agent’s action may depend not just on the state of the environment but also on the time step it has reached. Assume that the agent has access to time. 


### Response


### Prompt
For each of the following assertions, say whether it is true or false and support your answer with examples or counterexamples where appropriate. *Use our vacuum domain ONLY.*

a) An agent that senses only partial information about the state cannot be perfectly rational.
b) There exist task environments in which no pure reflex agent can behave rationally.
c) There exists a task environment in which every agent is rational.
d) Suppose an agent selects its action unformly at random from the set of possible actions. There exists a deterministic task evnironment in which this agent is rational.
e) Every agent is rational in an unobservable environment. 
### Response

## Exercise 1.3
### Prompt
Consider a modified version of the vacuum environmentin which the geography of the environment—its extent, boundaries, and obstacles—is unknown, as is the initial dirt configuration. The agent can go Up and Down as well as Left and Right.The agent can sense its current location and whether there is dirt in it. *The performance metric is to clean the space.*
### Response

### Exercise 1.4 (15pt)
You are to design an agent that moves from a start location to a goal location with obstacles in between. Assuming that your agent knows about the start and goal locations and can sense its current location. However, it can only detect an obstacle when it is next to it (i.e., tactile sensing). A simple method that allows the agent to solve the problem is to follow the procedure:

1) head toward goal
2) follow the contour of anobstacle encountered (in a fixed direction) until you can head toward the goal again
3) continue


a.) What is this type of agent? Can you specify the agent function? 
b.) Can this agent always reach the goal location? If your answer is yes,explain your answer. Otherwise, justify your answerby giving an environment where it won't work.
