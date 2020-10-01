# Assignment 3
### Fall 2020: Artificial Intelligence
### Author: Austin Derbique

## Disclaimer
The following text shall not be used for the purposes of academic dishonesty. It is granted only for educational & archival purposes, not to be used by other students enrolled in an artificial intelligence class. This information is not guaranteed to be correct. Please consult the textbook [Artificial Intelligence A Modern Approach](https://www.amazon.com/Artificial-Intelligence-Modern-Approach-3rd/dp/0136042597) for up to date and accurate information.

# Exercises 

## Exercise 1.1 (9pt)
### Prompt
Given the following minimax tree discussed in class, answer the following questions about alpha-beta pruning, **and explain your answers** by providing alpha-beta values for `a` and `b` below. *Except for the root node, the labels for the edges can be used as labels for the corresponding child nodes.*

A.(3pt) Assuming we always explore from lef to right, can the leaf nodes at `j` and `k` be pruned when the ordering of the leaf nodes can be aribtrarily changed (similar to what you see in the exercised in our offline lecure)? If so, provide an ordering of the lead nodes. Otherwise, explain why.

B.(3pt) Given a, think about the optimal ordering of the leaf nodes (assuming the same structure) for alpha-beta pruning in this tree? What are the nodes that will be pruned?

C.(3pt) Observing `a` and `b` above, provide an intuitive answer to why alpha-beta pruning takes time O(2^(m/2)) with optimal ordering, where `m` is the maximum depth of the game tree.

## Exercise 1.2 (9pt)
### Prompt
On the minimax game tree below, answer the following questions about alpha-beta pruning assumning left to right traversal, **and explain your answers.**

A.(3pt) What are the values of `A`, `B`, and `C` that ensure that `X1` and its leaf nodes will **not** be pruned?

B.(3pt) For the node `n1` to be pruned, what is the requirement on the variables `A`, `B`, and `C`?

C.(3pt) For wthe node `n2` to be pruned, what is the requirement on the variables `A`, `B`, and `C`?

## Exercise 1.3 (14pt)
### Prompt
In the following, a "max" tree consists only of max nodes, whereas an "expectimax" tree consists of a max node at the root with alternating layers of chance and max nodes. At chance nodes, all outcome probabilities are nonzero. The goal is to find the value of the root with a bounded-depth search. For each of(a)-(f), either give an exmaple or explain why this is impossible.

1. (2pt) Assume that leaf values are finite but unbounded, is pruning (as in alpha-beta) ever possible in a max tree?  
2. (2pt) Is pruning ever possible in an expectimax tree under the same conditions?  
3. (2pt) If leaf values are all nonnegative, is pruning ever possible in a max tree? Give an example, or explain why not.  
4. (2pt) If leaf values are all nonnegative, is pruning ever possible in an expectimax tree? Give an example, or explain why not.  
5. (2pt) If leaf values are all in the range [0,1], is pruning ever possible in a max tree? Give an example, or explain why not.
6. (2pt) If leaf values are all in the range [0,1], is pruning ever possible in an expectimax tree?  
7. (2pt) Consider the outcomes of a chance node in an expectimax tree. Which of the following evaluation orders is most likely to yield pruning oppurtunities? Explain.  
    7.i. Lowest probability first
    7.ii. Highest probability first  
    7.iii Doesn't make any difference

## Exercise 1.4 (10pt)
### Prompt
Consider that you are playing a strategy video game:  

From the wiki: *"A strategy video game is a video game genre that focuses on skillful thinking and planning to achieve victory. It emphasizes strategic, tactical, and sometimes logistical challenges. Many games also offer economic challenges and exploration. They are generally categorized into four sub-types, depending on whether the game is turn-based or real-time, and whether the game focuses on strategy or tactics."*

There are a total of `M` players in this game, indexed by `i` Pi represenths the `i`th player, and Ui represents the utility returned for agent `i` under a terminal state, which is always positive.  

1. (2pt) Express the relationship of these players as *purely* competitive using the utility values only, and **not** as a standard zero-sum or constant-sum game.  
2. (4pt) Express the relationship of these players as *both* competitive and cooperative using Us only. Explain your solution.  
3. (4pt) How would you describe a game where you are in a team (P1 to Pi) playing against another (Pi+1 to Pm), which futher satisfies the following:  
    3.1. Only one team wins and the other team loses  
    3.2. Winning team may have members in its team defeated but one member undefeated  
    3.3. Losing team must have all its members defeated. Explain your solution.  

## Exercise 1.5 (8pt)
### Prompt
Which of the following are true and which are false? Give brief explanations.

1. (3pt) In a fully observable, turn-taking, zero-sum game between two perfectly rational players, it does not help the first player to know what strategy the second player is using-- that is, what move the second player will make, given the first player's move.
2. (3pt) In a partially observable, turn-taking, zero-sum game between two perfectly rational players, it does not help the first player to know what move the second player will make, given the first player's move.  
3. (2pt) A perfectly rational Pacman never loses.

### Reponse

