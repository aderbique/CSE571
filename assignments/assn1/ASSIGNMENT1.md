# Assignment 1
### Fall 2020: Artificial Intelligence
### Author: Austin Derbique

## Disclaimer
The following text shall not be used for the purposes of academic dishonesty. It is granted only for educational & archival purposes, not to be used by other students enrolled in an artificial intelligence class. This information is not guaranteed to be correct. Please consult the textbook [Artificial Intelligence A Modern Approach](https://www.amazon.com/Artificial-Intelligence-Modern-Approach-3rd/dp/0136042597) for up to date and accurage information.

# Exercises 

## Exercise 1.1 (5pt)
### Prompt
Suppose that the performance measure is concerned with just the first T time steps of the environment and ignores everything thereafter. Show that a rational agent’s action may depend not just on the state of the environment but also on the time step it has reached. Assume that the agent has access to time. 

### Response
If the performance measure is concerned with only the first `T` time steps of the environment and ignores everything after, then it can be shown a rational agent may act differently based upon what information is available to it in the environment. Simply put, the rational agent makes decisions based on what it knows, and performance is measured up until time `T`. After this, the agent may act differently, regardless of the state of the environment. In the case of the vacuum cleaner, once Time `T` is reached, there is a possibility the vacuum did not clean all the dirt and did not meet the performance goal. That is why a rational agent's action must include Time `T` in the performance measure.

## Exercise 1.2 (15pt)
### Prompt
For each of the following assertions, say whether it is true or false and support your answer with examples or counterexamples where appropriate. *Use our vacuum domain ONLY.*

a) An agent that senses only partial information about the state cannot be perfectly rational.  
b) There exist task environments in which no pure reflex agent can behave rationally.  
c) There exists a task environment in which every agent is rational.  
d) Suppose an agent selects its action unformly at random from the set of possible actions. There exists a deterministic task evnironment in which this agent is rational.  
e) Every agent is rational in an unobservable environment.   

### Response

|Case|True/False|Supporting Explanation|
|----|----------|------------------|
|A|False|Say the agent cannot sense where dirt is and the performance metric requires all dirt to be cleaned, then the vacuum cannot guarantee it is making the rational decision when moving to each tile.|
|B|True| A relfex agent requires sensors and actuators to form its condition-action operations. If for example, there is not enough information available for a percept, then an irrational action can be made.|
|C|True|A task environment consists of PEAS: Performance metric, environment, actuators, sensors. In a scenario where the performance metric is to either move or stay still, then all agents will be performing rationally.|
|D|True|If chosen at random enough times, the agent will eventually choose an action that is rational.
|E|False|In an unobservable environment, percepts cannot be determined, and therefore there is no way to know if the agent is reaching its performance metric.|

## Exercise 1.3 (15pt)
### Prompt
Consider a modified version of the vacuum environmentin which the geography of the environment—its extent, boundaries, and obstacles—is unknown, as is the initial dirt configuration. The agent can go Up and Down as well as Left and Right.The agent can sense its current location and whether there is dirt in it. *The performance metric is to clean the space.*

a) Can a simple reflex agent be perfectly rational for this environment? Explain.  
b) Can a simple reflex agent with a *randomized* agent function (i.e., the action may be a random choice from a set) outperform a simple reflex agent?  
c) Can you design an environment in which your randomized agent will perform poorly, when movements are penalized?

### Response
|Case|Yes/No|Supporting Explanation|
|----|------|----------------------|
|A|No|Although it would seem logical to think the agent would be rational for the environment because it can continue to clean forever (unlimited tiles), it will never be known if all the tiles have been cleaned as it does not have knowledge of size, boundaries, etc. Therefore, it will never know if it has achieved the maximum expected value of performance measure, making it not perfectly rational.|
|B|Yes|After selecting enough random agent functions, the agent is bound to choose an agent function that outperforms a simple reflex agent. Although unlikely, it is possible. In a scenario where a simple reflex agent gets stuck on a wall, a random selecting agent may move, therefore getting unstuck and continuing on to a better performance metric.|
|C|Yes|Having a large area of potentially dirty squares on either side of a long and narrow walkway with zero dirty squares would cause massive penalties to walk to the other side of the room to clean the entire area. See `Figure 1.3c`|

#### Figure 3.1c
![Custom designed environment for poor performance in randomized agent](media/figure_1.3c.png)

### Exercise 1.4 (15pt)
You are to design an agent that moves from a start location to a goal location with obstacles in between. Assuming that your agent knows about the start and goal locations and can sense its current location. However, it can only detect an obstacle when it is next to it (i.e., tactile sensing). A simple method that allows the agent to solve the problem is to follow the procedure:

1) head toward goal
2) follow the contour of anobstacle encountered (in a fixed direction) until you can head toward the goal again
3) continue


a.) What is this type of agent? Can you specify the agent function? 
b.) Can this agent always reach the goal location? If your answer is yes,explain your answer. Otherwise, justify your answerby giving an environment where it won't work.
