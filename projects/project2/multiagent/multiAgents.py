# multiAgents.py
# --------------
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


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

class ReflexAgent(Agent):
    """
      A reflex agent chooses an action at each choice point by examining
      its alternatives via a state evaluation function.

      The code below is provided as a guide.  You are welcome to change
      it in any way you see fit, so long as you don't touch our method
      headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {North, South, West, East, Stop}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """ Evaluation function for pacman reflex agent """
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newPosX, newPosY = newPos
        currFood = currentGameState.getFood()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]
        h,w = len(newFood[0][:]),len(newFood[:])
        score_escape_ghost  = -1000
        score_eat_ghost     =  1500
        score_eat_food      =   100
        score_eat_cap       =   100
        if action == "Stop": return -500                        # We care more about Pacman being on the move eating dots than staying put.
        score_ghost = 0.0                                       # Manage life or death scenarios first
        for ghost in newGhostStates:                            # Iterate through ghosts
          dist = manhattanDistance(newPos, ghost.getPosition()) # Get distance to ghost
          if ghost.scaredTimer > 0:                             # Ghost is scared. Time to go chomp chomp
            if dist == 0: score_ghost += score_eat_ghost        # We will eat ghost next turn here.  Incentivize!
            elif dist < 3: score_ghost += score_eat_ghost/2     # Ghost is nearby, eat if possible; make half the effort to catch the ghost
          else:                                                 # Ghost dangerous! spooky 
            if dist < 2: score_ghost += score_escape_ghost      # Run away! :o Let's get out of here. Take away points.
        score_food = 0.0                                        # Prioritize eating food
        for x in range(w):                                      # loop through food map width
          for y in range(h):                                    # loop through food map height
            if(currFood[x][y]):                                 # If food
              dist = manhattanDistance(newPos, (x,y))           # Check the distance
              if(dist == 0): score_food += score_eat_food       # Looks like we'll eat some points!
              else: score_food += 1.0/(dist * dist * dist)      # Inscentivize pacman to move towards food at diminished rate          
        score_cap = 0.0                                         # Initialize Capsule Score
        for cap in currentGameState.getCapsules():              # Look for capsules
          dist = manhattanDistance(newPos, cap)                 # Get distance to capsule
          if(dist == 0): score_cap += score_eat_cap             # Looks like we can get the capsule next turn. Incentivize!
          else: score_cap += 1.0/dist                           # Diminishing inscentivizaztiony                                
        return score_ghost * 1 + score_food * 1 + score_cap * 1 # Return the calculated score

def scoreEvaluationFunction(currentGameState):
    """
      This default evaluation function just returns the score of the state.
      The score is the same one displayed in the Pacman GUI.

      This evaluation function is meant for use with adversarial search agents
      (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
      This class provides some common elements to all of your
      multi-agent searchers.  Any methods defined here will be available
      to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

      You *do not* need to make any changes here, but you can if you want to
      add functionality to all your adversarial search agents.  Please do not
      remove anything, however.

      Note: this is an abstract class: one that should not be instantiated.  It's
      only partially specified, and designed to be extended.  Agent (game.py)
      is another abstract class.
    """

    def __init__(self, evFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
      Your minimax agent (question 2)
    """
    def minimax(self, gameState, depth, agentIndex):
      """ Returns the minimax action from the current gameState using self.depth and self.evaluationFunction. """
      POS_LARGE = 100000000
      NEG_LARGE = POS_LARGE * -1
      ba = 'null'                                       # Initialize best action
      if gameState.isWin() or gameState.isLose(): return self.evaluationFunction(gameState)   # Return immediately if game is over
      if agentIndex == 0:                                   # checks index of agent. is zero
        bv = NEG_LARGE                                   # Set this to very large neg vue
        actions = gameState.getLegalActions(agentIndex)                   # Obtain list of legal actions for state
        for action in actions:                               # Iterate through actions
            n = gameState.generateSuccessor(agentIndex, action)             # create successors testing action
            v = self.minimax(n, depth, agentIndex + 1)                 # take minimum
            if (bv < v):
              bv, ba = v, action
        if (depth == 1): return ba
      else:
        bv = POS_LARGE
        agents, actions = gameState.getNumAgents(), gameState.getLegalActions(agentIndex)
        for action in actions:
            n = gameState.generateSuccessor(agentIndex, action)
            if agentIndex == agents - 1:
              if depth == self.depth: v = self.evaluationFunction(n)
              else: v = self.minimax(n, depth+1, 0)
            else: v = self.minimax(n, depth, agentIndex+1)
            if bv > v: bv, ba = v, action
      return bv
                        
    def getAction(self, gameState):
      """ Returns the minimax action from the current gameState using self.depth and self.evaluationFunction. """
      return self.minimax(gameState, 1, 0)

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
      Your minimax agent with alpha-beta pruning (question 3)
    """
    def abpruning(self, gameState, depth, agentIndex,a,b):
      """ Returns the minimax action from the current gameState using self.depth and self.evaluationFunction. """
      POS_LARGE = 100000000
      NEG_LARGE = POS_LARGE * -1
      ba = 'null'                                       # Initialize best action
      if gameState.isWin() or gameState.isLose(): return self.evaluationFunction(gameState)   # Return immediately if game is over
      if agentIndex == 0:                                   # checks index of agent. is zero
        bv = NEG_LARGE                                   # Set this to very large neg vue
        actions = gameState.getLegalActions(agentIndex)                   # Obtain list of legal actions for state
        for action in actions:                               # Iterate through actions
            n = gameState.generateSuccessor(agentIndex, action)             # create successors testing action
            v = self.abpruning(n, depth, agentIndex + 1, a,b)                 # take minimum
            if v > b: return v
            if v > bv:  bv, ba = v, action
            a = max(bv, a)
        if (depth == 1): return ba
      else:
        bv = POS_LARGE
        agents, actions = gameState.getNumAgents(), gameState.getLegalActions(agentIndex)
        for action in actions:
            n = gameState.generateSuccessor(agentIndex, action)
            if agentIndex == agents - 1:
              if depth == self.depth: v = self.evaluationFunction(n)
              else: v = self.abpruning(n, depth+1, 0,a,b)
            else: v = self.abpruning(n, depth, agentIndex+1,a,b)
            if v < a: return v
            if bv > v: bv, ba = v, action
            b = min(bv, b)
      return bv
    def getAction(self, gameState):
        """ Returns the minimax action using self.depth and self.evaluationFunction """
        return self.abpruning(gameState, 1, 0, -10000000,1000000)

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
          Returns the expectimax action using self.depth and self.evaluationFunction

          All ghosts should be modeled as choosing uniformly at random from their
          legal moves.
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

def betterevaluationFunction(currentGameState):
    """
      Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
      evaluation function (question 5).

      DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

# Abbreviation
better = betterevaluationFunction

