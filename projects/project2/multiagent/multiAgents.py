# multiAgents.py
# Austin Derbique
# aderbiqu
# CSE571 Fall 2020
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
        new_gs = currentGameState.generatePacmanSuccessor(action)
        new_pos = new_gs.getPacmanPosition()                    # New agent position
        new_posX, new_posY = new_pos                            # Broken into coordinates
        curr_food = currentGameState.getFood()                  # Where the current food is
        new_food = new_gs.getFood()                             # Where the new food is
        new_ghosts = new_gs.getGhostStates()                    # New ghost states
        h,w = len(new_food[0][:]),len(new_food[:])              # dimensions of food grid
        score_escape_ghost  = -1000                             # Set weight
        score_eat_ghost     =  1500                             # Set weight
        score_eat_food      =   100                             # Set weight
        score_eat_cap       =   100                             # Set weight
        if action == "Stop": return -500                        # We care more about Pacman being on the move eating dots than staying put.
        score_ghost = 0.0                                       # Manage life or death scenarios first
        for ghost in new_ghosts:                                # Iterate through ghosts
          dist = manhattanDistance(new_pos, ghost.getPosition())# Get distance to ghost
          if ghost.scaredTimer > 0:                             # Ghost is scared. Time to go chomp chomp
            if dist == 0: score_ghost += score_eat_ghost        # We will eat ghost next turn here.  Incentivize!
            elif dist < 3: score_ghost += score_eat_ghost/2     # Ghost is nearby, eat if possible; make half the effort to catch the ghost
          else:                                                 # Ghost dangerous! spooky 
            if dist < 2: score_ghost += score_escape_ghost      # Run away! :o Let's get out of here. Take away points.
        score_food = 0.0                                        # Prioritize eating food
        for x in range(w):                                      # loop through food map width
          for y in range(h):                                    # loop through food map height
            if(curr_food[x][y]):                                # If food
              dist = manhattanDistance(new_pos, (x,y))          # Check the distance
              if(dist == 0): score_food += score_eat_food       # Looks like we'll eat some points!
              else: score_food += 1.0/(dist * dist * dist)      # Inscentivize pacman to move towards food at diminished rate          
        score_cap = 0.0                                         # Initialize Capsule Score
        for cap in currentGameState.getCapsules():              # Look for capsules
          dist = manhattanDistance(new_pos, cap)                # Get distance to capsule
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

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """ Your minimax agent (question 2) """
    def minimax(self, gameState, depth, agentIndex):
      """ Returns the minimax action from the current gameState using self.depth and self.evaluationFunction. """
      POS_LARGE = 100000000                                                                   # A stupid large positive number
      NEG_LARGE = POS_LARGE * -1                                                              # A stupid large negative number
      ba = 'null'                                                                             # Initialize best action
      if gameState.isWin() or gameState.isLose(): return self.evaluationFunction(gameState)   # Return immediately if game is over
      if agentIndex == 0:                                                                     # checks index of agent. is zero
        bv = NEG_LARGE                                                                        # Set this to very large neg vue
        actions = gameState.getLegalActions(agentIndex)                                       # Obtain list of legal actions for state
        for action in actions:                                                                # Iterate through actions
            n = gameState.generateSuccessor(agentIndex, action)                               # create successors testing action
            v = self.minimax(n, depth, agentIndex + 1)                                        # take minimum
            if (bv < v):                                                                      # If best value < existing value
              bv, ba = v, action                                                              # Set new best value, action = existing ba, v
        if (depth == 1): return ba                                                            # base case
      else:                                                                                   # Otherwise
        bv = POS_LARGE                                                                        # Initialize bv to large number
        agents, actions = gameState.getNumAgents(), gameState.getLegalActions(agentIndex)     # get agents and actions
        for action in actions:                                                                # Iterate through allowable actions
            n = gameState.generateSuccessor(agentIndex, action)                               # Get successor game state node
            if agentIndex == agents - 1:                                                      # Check index
              if depth == self.depth: v = self.evaluationFunction(n)                          # If prev, value = evaluationFunction
              else: v = self.minimax(n, depth+1, 0)                                           # Otherwise, continue down minimax
            else: v = self.minimax(n, depth, agentIndex+1)                                    # Otherwise, continue to minimax
            if bv > v: bv, ba = v, action                                                     # If best value is better than existing value, set new max
      return bv                                                                               # Return best value
                        
    def getAction(self, gameState):
      """ Returns the minimax action from the current gameState using self.depth and self.evaluationFunction. """
      return self.minimax(gameState, 1, 0)

class AlphaBetaAgent(MultiAgentSearchAgent):
    """ Your minimax agent with alpha-beta pruning (question 3) """
    def abpruning(self, gameState, depth, agentIndex,a,b):
      """ Returns the minimax action from the current gameState using self.depth and self.evaluationFunction. """
      POS_LARGE = 100000000
      NEG_LARGE = POS_LARGE * -1
      ba = 'null'                                                                             # Initialize best action
      if gameState.isWin() or gameState.isLose(): return self.evaluationFunction(gameState)   # Return immediately if game is over
      if agentIndex == 0:                                                                     # checks index of agent. is zero
        bv = NEG_LARGE                                                                        # Set this to very large neg vue
        actions = gameState.getLegalActions(agentIndex)                                       # Obtain list of legal actions for state
        for action in actions:                                                                # Iterate through actions
            n = gameState.generateSuccessor(agentIndex, action)                               # create successors testing action
            v = self.abpruning(n, depth, agentIndex + 1, a,b)                                 # take minimum
            if v > b: return v                                                                # Read Minimax for documentation on tree
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
    def expectimax(self, gameState, depth, agentIndex):
      POS_LARGE = 100000000
      NEG_LARGE = POS_LARGE * -1
      if depth == 0 or gameState.isWin() or gameState.isLose():
        res = self.evaluationFunction(gameState)
        return (res, '')
      else:
        ma = ''
        if agentIndex == gameState.getNumAgents() - 1: depth -= 1  
        if agentIndex == 0: am = NEG_LARGE
        else: am = 0
        index = (agentIndex + 1) % gameState.getNumAgents()
        actions = gameState.getLegalActions(agentIndex)
        for action in actions:
          output = self.expectimax(gameState.generateSuccessor(agentIndex, action), depth, index)
          if agentIndex == 0:
            if  output[0] > am:
              ma = action              
              am = output[0]
          else:
            ma = action
            am += 1.0/len(actions)*output[0]
        return (am, ma)  

    def getAction(self, gameState):
        """ Returns the expectimax action using self.depth and self.evaluationFunction """
        return self.expectimax(gameState, self.depth, 0)[1]

def betterEvaluationFunction(currentGameState):
    """Better Evaluation Function Based on appending scores from food, ghosts, and scared ghosts  """
    score = 0.0                                                                                                   # Initialize Score
    pos = currentGameState.getPacmanPosition()                                                                    # Get pacman position
    food = currentGameState.getFood().asList()                                                                    # Get all foods
    ghosts, sghosts, fdist, gdist, sgdist = ([] for i in range(5))                                                # Initialize Arrays to store values
    for ghost in currentGameState.getGhostStates():                                                               # Iterate trough ghost states
        if ghost.scaredTimer: sghosts.append(ghost)                                                               # Check if scared, add to scared list
        else: ghosts.append(ghost)                                                                                # Add to scary ghost lists
    score += ((2 * currentGameState.getScore()) - ((10 * len(food)) + (20 * len(currentGameState.getCapsules()))))# Perform Inscentiviations based on how many foods, ghosts, scary ghosts there are.
    [sgdist.append(manhattanDistance(pos,item.getPosition())) for item in ghosts]                                 # Append distace to ghosts
    [fdist.append(manhattanDistance(pos,item)) for item in food]                                                  # Append distance to foods
    [sgdist.append(manhattanDistance(pos,item.getPosition())) for item in sghosts]                                # Append dist to scared ghosts
    for dist in gdist:                                                                                            # Iterate through scary ghosts
        if dist <= 2: score += dist * 2.5                                                                         # if close by, inscentivize!
        elif dist <= 6: score += dist * 2.1                                                                       # if less close by, inscentivize less!
        else: score += dist * 0.5                                                                                 # super far away, inscentivize the least!
    for dist in sgdist:                                                                                           # Iterate through scared ghosts distances
        if dist <= 2: score += dist * -20                                                                         # Inscentivize!
        else: score += dist * -10                                                                                 # Inscentivize less!
    for dist in fdist:                                                                                            # Iterate through foods
        if dist <= 2: score += dist *-1                                                                           # if close by, inscentivize!
        if dist <= 6: score += dist * -0.5                                                                        # if less close by, inscentivize less!
        else: score += dist * -0.15                                                                               # super far away, inscentivize the least!
    return score                                                                                                  # Return overall score
# Abbreviation
better = betterEvaluationFunction

