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

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    # 0. Initialize the search tree using the initial state of the problem
    start_state = problem.getStartState()
    fringe = util.Stack()
    fringe.push((start_state, []))
    closed_set = set();
    print("Start of depth first search")
    while True:
      # 1. If there is no candidate for expantion then return false
      if fringe.isEmpty():
        print("End of depth first search(FAILED)")
        return []
      # 2. Choose a leaf node for expantion according to stratgy
      leaf = fringe.pop()
      # 3. If the node contains a goal state then return the corresponding
      #    solution
      if problem.isGoalState(leaf[0]):
        print("End of depth first search(SUCCEEDED)")
        return leaf[1]
      # 4. Else expand the node and add the resulting nodes to the search tree
      else:
        if leaf[0] in closed_set:
          continue;
        else:
          closed_set.add(leaf[0])
          successors = problem.getSuccessors(leaf[0])
          for successor in successors:
            fringe_terminal_state = successor[0]
            fringe_solution = leaf[1].copy()
            fringe_solution.append(successor[1])
            fringe.push((fringe_terminal_state, fringe_solution ))

    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    # 0. Initialize the search tree using the initial state of the problem
    start_state = problem.getStartState()
    fringe = util.Queue()
    fringe.push((start_state, []))
    closed_set = set();
    print("Start of breadth first search")
    while True:
      # 1. If there is no candidate for expantion then return false
      if fringe.isEmpty():
        print("End of breadth first search(FAILED)")
        return []
      # 2. Choose a leaf node for expantion according to stratgy
      leaf = fringe.pop()
      # 3. If the node contains a goal state then return the corresponding
      #    solution
      if problem.isGoalState(leaf[0]):
        print("End of breadth first search(SUCCEEDED)")
        return leaf[1]
      # 4. Else expand the node and add the resulting nodes to the search tree
      else:
        if leaf[0] in closed_set:
          continue;
        else:
          closed_set.add(leaf[0])
          successors = problem.getSuccessors(leaf[0])
          for successor in successors:
            fringe_terminal_state = successor[0]
            fringe_solution = leaf[1].copy()
            fringe_solution.append(successor[1])
            fringe.push((fringe_terminal_state, fringe_solution ))

    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    # 0. Initialize the search tree using the initial state of the problem
    start_state = problem.getStartState()
    fringe = util.PriorityQueue()
    fringe.push((start_state, [], 0),0)
    closed_set = set();
    print("Start of uniform cost search")
    while True:
      # 1. If there is no candidate for expantion then return false
      if fringe.isEmpty():
        print("End of uniform cost search(FAILED)")
        return []
      # 2. Choose a leaf node for expantion according to stratgy
      leaf = fringe.pop()
      # 3. If the node contains a goal state then return the corresponding
      #    solution
      if problem.isGoalState(leaf[0]):
        print("End of uniform cost search(SUCCEEDED)")
        return leaf[1]
      # 4. Else expand the node and add the resulting nodes to the search tree
      else:
        if leaf[0] in closed_set:
          continue;
        else:
          closed_set.add(leaf[0])
          successors = problem.getSuccessors(leaf[0])
          for successor in successors:
            fringe_terminal_state = successor[0]
            fringe_solution = leaf[1].copy()
            fringe_solution.append(successor[1])
            fringe_cost = leaf[2] + successor[2]
            fringe.push((fringe_terminal_state, fringe_solution, fringe_cost), fringe_cost)
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    # 0. Initialize the search tree using the initial state of the problem
    start_state = problem.getStartState()
    fringe = util.PriorityQueue()
    fringe.push((start_state, [], 0), heuristic(start_state, problem))
    closed_set = set();
    print("Start of A* search")
    while True:
      # 1. If there is no candidate for expantion then return false
      if fringe.isEmpty():
        print("End of A* search(FAILED)")
        return []
      # 2. Choose a leaf node for expantion according to stratgy
      leaf = fringe.pop()
      # 3. If the node contains a goal state then return the corresponding
      #    solution
      if problem.isGoalState(leaf[0]):
        print("End of A* search(SUCCEEDED)")
        return leaf[1]
      # 4. Else expand the node and add the resulting nodes to the search tree
      else:
        if leaf[0] in closed_set:
          continue;
        else:
          closed_set.add(leaf[0])
          successors = problem.getSuccessors(leaf[0])
          for successor in successors:
            fringe_terminal_state = successor[0]
            fringe_solution = leaf[1].copy()
            fringe_solution.append(successor[1])
            fringe_cost = leaf[2] + successor[2]
            fringe.push((fringe_terminal_state, fringe_solution, fringe_cost),
                         fringe_cost + heuristic(fringe_terminal_state, problem))
    util.raiseNotDefined()

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
