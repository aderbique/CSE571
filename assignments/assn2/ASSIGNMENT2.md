# Assignment 2
### Fall 2020: Artificial Intelligence
### Author: Austin Derbique

## Disclaimer
The following text shall not be used for the purposes of academic dishonesty. It is granted only for educational & archival purposes, not to be used by other students enrolled in an artificial intelligence class. This information is not guaranteed to be correct. Please consult the textbook [Artificial Intelligence A Modern Approach](https://www.amazon.com/Artificial-Intelligence-Modern-Approach-3rd/dp/0136042597) for up to date and accurate information.

# Exercises 

## Exercise 1.1 (6pt)
### Prompt
Prove each of the following statements, or give a counterexample:  

A) Breadth-first search is a special case of uniform-cost search.  
B) Depth-first search is a special case of best-first search.  
C) Uniform-cost search is a special case of A* search.  

### Response
In the textbook, **uniform-cost search** is defined to expand node *n* with the *lowest path cost g(n)*. This means that uniform-cost search expands nodes in order of their optimal path cost.

|Case|True/False|Supporting Claim|
|----|----------|----------------|
|A|True|Breadth-first search always expands the *shallowest* unexpanded node, whereas in contrast uniform-cost search expands by *lowest path cost*. Although uniform-cost search is an improvement upon BFS because of only exploring nodes with lowest path cost, the results are effectively the same. Therefore, BFS is a special case of uniform-cost search and uniform-cost search is the generalization. |
|B|False|**Depth-First Search** is considered an `uninformed search strategy`, wheres **Best-First Search** explores a graph by expanding the most promising node according to a specified rule. Source: [Wikipedia](https://en.wikipedia.org/wiki/Best-first_search)|
|C|True|**Uniform-Cost Search** has a function `F(n) = g(n)`, and **A\* Search** has a function `F(n) = g(n) + h(n)`. If all costs are the same, then UCS and A*S are identical.|


## Exercise 1.2 (18pt)
### Prompt

Consider the unbound version of regular 2D grid shown above. The start state is at the origin, *(0,0)*, and the goal state is at *(x,y)*. The agent can choose action North, South, East, West **or Stay** in any state.  
Consider ***tree search*** below (unless noted otherwise):

A) What is the branching factor or *b*?  
B) How many distinc states are there at depth *k* (for *k > 0*) in the search tree?  
C) What is the maximum number of nodes expanded by breadth-first search?  
D) What is the maximum number of distinct nodes expanded by breadth-frst search?  
E) What is the maximum number of nodes expanded by breadth-first ***graph*** search?  
F) Is `h = |u - x| + |v-y` an admissable heuristic for a state at `(u,v)`? Explain.  
G) How many nodes are expanded by A* graph search using `h` in `(f)`?  
H) Does *h* remain admissible if some links are removed? Explain.  
I) Does *h* remain admissible if some links are added between nonadjacent states? Explain.  

### Response

|Case|True/False|Supporting Explanation|
|----|----------|------------------|
|A|
|B|
|C|
|D|
|E|
|F|
|G|
|H|
|I|

## Exercise 1.3 (15pt)
### Prompt


### Response
|Case|Yes/No|Supporting Explanation|
|----|------|----------------------|
|A|
|B|
|C|
|D i|
|D ii|
|D iii|

## Exercise 1.4 (11pt)
### Prompt
### Figure 1.4



### Response

### References


