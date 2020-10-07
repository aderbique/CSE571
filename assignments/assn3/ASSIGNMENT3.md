# Assignment 3
### Fall 2020: Artificial Intelligence
### Author: Austin Derbique

## Disclaimer
The following text shall not be used for the purposes of academic dishonesty. It is granted only for educational & archival purposes, not to be used by other students enrolled in an artificial intelligence class. This information is not guaranteed to be correct. Please consult the textbook [Artificial Intelligence A Modern Approach](https://www.amazon.com/Artificial-Intelligence-Modern-Approach-3rd/dp/0136042597) for up to date and accurate information.

# Exercises 

## Exercise 1.1 (9pt)
### Prompt
Given the following minimax tree discussed in class, answer the following questions about alpha-beta pruning, **and explain your answers** by providing alpha-beta values for `a` and `b` below. *Except for the root node, the labels for the edges can be used as labels for the corresponding child nodes.*

1. (3pt) Assuming we always explore from lef to right, can the leaf nodes at `j` and `k` be pruned when the ordering of the leaf nodes can be aribtrarily changed (similar to what you see in the exercised in our offline lecure)? If so, provide an ordering of the lead nodes. Otherwise, explain why.
2. (3pt) Given a, think about the optimal ordering of the leaf nodes (assuming the same structure) for alpha-beta pruning in this tree? What are the nodes that will be pruned?
3. (3pt) Observing `a` and `b` above, provide an intuitive answer to why alpha-beta pruning takes time O(2^(m/2)) with optimal ordering, where `m` is the maximum depth of the game tree.

### Response
1. Yes, this is entirely possible. By moving leaf node `j` to the very right, and rearranging the positions of `n` and `m`, we can prune both j and k. An example structure would be `C-D-F-G-M-K-N-J`.
2. In an optimal ordering, we must maximime the number of occurrences of (alpha > beta). This creates pruning oppurtunities.  Applying this technique, we can achieve four values pruned. An example structure would be `J-M-F-D-C-N-G-K`.
3. Alpha-Beta pruning is capable of O(2^(m/2)) time complexity with optimal ordering by reducing the number of subbranches it needs to calculate.  The effective branching factor is reduced to the square root of branch m, otherwise known as O(2^(m/2)).

## Exercise 1.2 (9pt)
### Prompt
On the minimax game tree below, answer the following questions about alpha-beta pruning assumning left to right traversal, **and explain your answers.**

1. (3pt) What are the values of `A`, `B`, and `C` that ensure that `X1` and its leaf nodes will **not** be pruned?
2. (3pt) For the node `n1` to be pruned, what is the requirement on the variables `A`, `B`, and `C`?
3. (3pt) For wthe node `n2` to be pruned, what is the requirement on the variables `A`, `B`, and `C`?

### Response
1. Nodes `A` and `B` must be 8 or larger for the minimax tree to search to leaf node of value 7. Once this is complete, value C must be the value greater than 7.
2. For node `n1` to be pruned, the values of `A`, `B`, and `C` must all be less than or equal to 7. This is because of the leaf node with a value of 7 to the left of `C`. Contents of `C` must be less than or equal to 7, so the 7 on the left is always maximized.
3. For the node `n2` to be pruned, the values of `A`, `B` must be greater than or equal to zero. Under this condition, `C` can be any value as it does not matter. This causes a pruning oppurtunity where the alpha value of the root node is zero. Given that, n2 will be pruned.

## Exercise 1.3 (14pt)
### Prompt
In the following, a "max" tree consists only of max nodes, whereas an "expectimax" tree consists of a max node at the root with alternating layers of chance and max nodes. At chance nodes, all outcome probabilities are nonzero. The goal is to find the value of the root with a bounded-depth search. For each of(a)-(f), either give an exmaple or explain why this is impossible.

1. (A) (2pt) Assume that leaf values are finite but unbounded, is pruning (as in alpha-beta) ever possible in a max tree?  
2. (B) (2pt) Is pruning ever possible in an expectimax tree under the same conditions?  
3. (C) (2pt) If leaf values are all nonnegative, is pruning ever possible in a max tree? Give an example, or explain why not.  
4. (D) (2pt) If leaf values are all nonnegative, is pruning ever possible in an expectimax tree? Give an example, or explain why not.  
5. (E) (2pt) If leaf values are all in the range [0,1], is pruning ever possible in a max tree? Give an example, or explain why not.
6. (F) (2pt) If leaf values are all in the range [0,1], is pruning ever possible in an expectimax tree?  
7. (G) (2pt) Consider the outcomes of a chance node in an expectimax tree. Which of the following evaluation orders is most likely to yield pruning oppurtunities? Explain.  
    (G) (7.i. Lowest probability first
    (G) 7.ii. Highest probability first  
    (G) 7.iii Doesn't make any difference

### Response
1. (A) No. Pruning is not possible. A pruning oppurtunity arises when you have a max of a lower min level. And in that min level, we know we need not expand the node, as the max will already choose the other existing value. When running a max only tree, you will never know if the the node to the right is bigger, therefore you always need to expand the node.
2. (B) No. Similar to part A (1), pruning is not possible as there are no pruning oppurtunities. Alternating between max and chance does not guarantee that a node need not be visited. This is because there is always a possibilty the next node might be larger than the current max node.
3. (C) No. Even when all leaf nodes are nonnegative, pruning is never possible in a max tree for the same reasons as A (1).
4. (D) No. Even if all leaf nodes are nonnegative for an expectimax tree, pruning is never possible for the same reasons as B (2).
5. (E) Yes. When all values are [0,1] in a max tree, pruning is possible. This is because when the alpha value will be set to 1, and remaining successors must be pruned.
6. (F) Yes. When all values are [0,1] in an expectimax tree, pruning is possible. Similary to F (5), the alpha value will be set to 1. Once this occurs, remaining successors will be pruned.
7. (G) Highest probability first will yield best pruning oppurtunities. The larger the bound, the more oppurtunity for pruning oppurtunities.

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

### Response
1.  In a purely competitve, non-zero-sum game, there may be only one winner. The winner is determined by the player that has the largest utility. Therefore, we can express the winner `W` as having the max utility out of all players `U` where `U` is a set of all players' utilities. We can describe this relationship as `W = max(U)`.
2. In order to define a relationship that satisfies both competitive and coopeartive, we must define each individually. In a competitive game, players compete for the highest utility. A cooperative game, similar to a team game, is where there can be more than one winner. An example of this might be two-player pacman. Each player has their own score, and these players are both competing for the highest score, but when the two players beat a level, they both win.  We can describe this relationship as players `P0` to `Pi` competing competitively and cooperatively to achieve a utility of the summation of all of their utilities.  Therefore, the winner(s) may be ranked from highest utility to lowest utility with a reverse sort of utility. `W[]` with a size `M` containing a `reverse_sort(U)`.
3. This game may be defined as purely competitive version of a cooperative game. Also known as competitive(cooperative(P1-Pi),cooperative(P(i+1),Pm)), where cooperative(P1-Pi) represents the first team of players P1 to Pi, and the second team cooperative(P(i+1),Pm) represents players P(i+1) to Pm. Because utility is defined by not dying, Ie (the team with the last surviving player(s) win), we can say utility of an individual player is 1 when alive and drops to 0 when they die. A team's utility is representated as the summation of its players' utliities. The first team with a collective utility of zero is the loser. Therefore, the other team is declared the winner. 

## Exercise 1.5 (8pt)
### Prompt
Which of the following are true and which are false? Give brief explanations.

1. (3pt) In a fully observable, turn-taking, zero-sum game between two perfectly rational players, it does not help the first player to know what strategy the second player is using-- that is, what move the second player will make, given the first player's move.
2. (3pt) In a partially observable, turn-taking, zero-sum game between two perfectly rational players, it does not help the first player to know what move the second player will make, given the first player's move.  
3. (2pt) A perfectly rational Pacman never loses.

### Response

1. (A) True.  With two perfectly rational players in a strategy game and fully observable environment, we can infer that the opposing player will try to maximize their utility by minimizing ours. We already know this, and it adds no benefit to us to predict their next move.
2. (B) True. In a partially observable, turn-taking, zero-sum game, the first player may not know what current state they are in. Because of this, it may be impossible to guarantee that knowing the second players next move will be helpful to the first player.
3. (C) False. There is a possibility that a win is not possible. Although the agent is perfectly rational, the is a small but random chance that the pacman may lose. This could be because it is trapped by ghosts and has no escape. 
