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
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newPosX, newPosY = newPos
        currFood = currentGameState.getFood();
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]
        #newFoodList = newFood.asList()  
        #newDistToGhosts = [manhattanDistance(newPos, ghostState.configuration.getPosition()) for ghostState in newGhostStates]
        #newNearestGhostScaredTime = newScaredTimes[newDistToGhosts.index(min(newDistToGhosts))]
        w = len(newFood[:])
        h = len(newFood[0][:])

        score_escape_ghost  = -1000
        score_eat_ghost     =  1500
        score_eat_food      =    100
        score_eat_cap       =   100

        if action == "Stop":    #We care more about Pacman being on the move eating dots than staying put.
          return -500
        score_ghost = 0.0                                       # Manage life or death scenarios first
        for ghost in newGhostStates:                            # Iterate through ghosts
          dist = manhattanDistance(newPos, ghost.getPosition()) # Get distance to ghost
          if ghost.scaredTimer > 0:                             # Ghost is scared. Time to go chomp chomp
            if dist == 0:                                       # We will eat ghost next turn here.  Incentivize!
              score_ghost += score_eat_ghost                    # Eat the ghost, it's good for you!
            elif dist < 3:                                      # Ghost is nearby, eat if possible
              score_ghost += score_eat_ghost/2                  # Make half the effort to catch the ghost
          else:                                                 # Ghost dangerous! spooky 
            if dist < 2:                                        # Run away! :o
              score_ghost += score_escape_ghost                 # Let's get out of here. Take away points.
        score_food = 0.0                                        # Prioritize eating food
        for x in range(w):                                      # loop through food map width
          for y in range(h):                                    # loop through food map height
            if(currFood[x][y]):                                 # If food
              dist = manhattanDistance(newPos, (x,y))           # Check the distance
              if(dist == 0):                                    # Looks like we'll eat some points!
                score_food += score_eat_food                    # Inscentivize pacman to move here
              else:                                             # Food is further away
                score_food += 1.0/(dist * dist * dist)          # Inscentivize pacman to move towards food at diminished rate
        score_cap = 0.0                                         # Initialize Capsule Score
        for cap in currentGameState.getCapsules():              # Look for capsules
          dist = manhattanDistance(newPos, cap)                 # Get distance to capsule
          if(dist == 0):                                        # Looks like we can get the capsule next turn. Incentivize!
            score_cap += score_eat_cap                          # ooh, extra points
          else:                                                 # No capsules nearby
            score_cap += 1.0/dist                               # Diminishing inscentivizaztion
        return score_ghost * 1 + score_food * 1 + score_cap * 1             # Return the calculated score

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

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
      Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action from the current gameState using self.depth
          and self.evaluationFunction.

          Here are some method calls that might be useful when implementing minimax.

          gameState.getLegalActions(agentIndex):
            Returns a list of legal actions for an agent
            agentIndex=0 means Pacman, ghosts are >= 1

          gameState.generateSuccessor(agentIndex, action):
            Returns the successor game state after an agent takes an action

          gameState.getNumAgents():
            Returns the total number of agents in the game
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
      Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

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

def betterEvaluationFunction(currentGameState):
    """
      Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
      evaluation function (question 5).

      DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

# Abbreviation
better = betterEvaluationFunction

