# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """ 
    Search the deepest nodes in the search tree first. 

    ANS Problem 1: Exploration is what I expected. Pacman does not explore all nodes; it finds the first path to the deepest node. This is a least cost solution.
    
    """
    nv = []                                             # Initialize empty array for visited nodes
    s = util.Stack()                                    # Initialize LIFO stack for fringe
    s.push((problem.getStartState(), ()))               # Add initial location to stack
    while not s.isEmpty():                              # Loop until stack is empty
        cn = s.pop()                                    # Current node in search state
        cs, cp = cn[0], cn[1]                           # current state, current plan
        if problem.isGoalState(cs):                     # checks if current state is goal state
            return list(cp)                             # returns plan if true
        if not cs in nv:                                # Executes only if pacman hasn't already been to this state before
            nv.append(cs)                               # Adds node to list of visited nodes
            for path in problem.getSuccessors(cs):      # all paths known for current state
                np = list(cp)                           # grab new plan from current plan
                np.append(path[1])                      # add path to the new plan
                nn = (path[0], tuple(np))               # new node is the child 
                if not path[0] in nv:                   # if the new node isn't already visited
                  s.push(nn)                            # Push new node to stack
    util.raiseNotDefined()                              # If no solution is found, throw an error

def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    
    ANS Problem 2: BFS provides least cost solution."""
    nv = []                                             # Initialize empty array for visited nodes
    s = util.Queue()                                    # Initialize queue for fringe
    s.push((problem.getStartState(), ()))               # Add initial location to stack
    while not s.isEmpty():                              # Loop until stack is empty
        cn = s.pop()                                    # Current node in search state
        cs, cp = cn[0], cn[1]                           # current state, current plan
        if problem.isGoalState(cs):                     # checks if current state is goal state
            return list(cp)                             # returns plan if true
        if not cs in nv:                                # Executes only if pacman hasn't already been to this state before
            nv.append(cs)                               # Adds node to list of visited nodes
            for path in problem.getSuccessors(cs):      # all paths known for current state
                np = list(cp)                           # grab new plan from current plan
                np.append(path[1])                      # add path to the new plan
                nn = (path[0], tuple(np))               # new node is the child 
                if not path[0] in nv:                   # if the new node isn't already visited
                  s.push(nn)                            # Push new node to stack
    util.raiseNotDefined()                              # If no solution is found, throw an error

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    nv = []                                             # Initialize empty array for visited nodes
    s = util.PriorityQueue()                            # Initialize priority queue for fringe
    s.push((problem.getStartState(), ()), 0)            # Add initial location to stack with cost of 0
    while not s.isEmpty():                              # Loop until stack is empty
        cn = s.pop()                                    # Current node in search state
        cs, cp = cn[0], cn[1]                           # current state, current plan
        if problem.isGoalState(cs):                     # checks if current state is goal state
            return list(cp)                             # returns plan if true
        if not cs in nv:                                # Executes only if pacman hasn't already been to this state before
            nv.append(cs)                               # Adds node to list of visited nodes
            for path in problem.getSuccessors(cs):      # all paths known for current state
                np = list(cp)                           # grab new plan from current plan
                np.append(path[1])                      # add path to the new plan
                nn = (path[0], tuple(np))               # new node is the child 
                if not path[0] in nv:                   # if the new node isn't already visited
                  s.push(nn, problem.getCostOfActions(np))# Push new node to stack with associated cost
    util.raiseNotDefined()                              # If no solution is found, throw an error

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """
    Search the node that has the lowest combined cost and heuristic first.

    ANS Problem 4: For an open maze, A* search is optimal. It moves to the goal state in leasst moves possible.
    
    """
    nv = []                                             # Initialize empty array for visited nodes
    s = util.PriorityQueue()                            # Initialize priority queue for fringe
    s.push((problem.getStartState(), ()), 0)            # Add initial location to stack with cost of 0
    while not s.isEmpty():                              # Loop until stack is empty
        cn = s.pop()                                    # Current node in search state
        cs, cp = cn[0], cn[1]                           # current state, current plan
        if problem.isGoalState(cs):                     # checks if current state is goal state
            return list(cp)                             # returns plan if true
        if not cs in nv:                                # Executes only if pacman hasn't already been to this state before
            nv.append(cs)                               # Adds node to list of visited nodes
            for path in problem.getSuccessors(cs):      # all paths known for current state
                np = list(cp)                           # grab new plan from current plan
                np.append(path[1])                      # add path to the new plan
                nn = (path[0], tuple(np))               # new node is the child 
                if not path[0] in nv:                   # if the new node isn't already visited
                  s.push(nn, problem.getCostOfActions(np) + (heuristic(path[0], problem)))# Push new node to stack with associated cost
    util.raiseNotDefined()                              # If no solution is found, throw an error

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
