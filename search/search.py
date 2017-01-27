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

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"

    stack = util.Stack()
    closeList = set()
    output = []

    start = (problem.getStartState() , None)
    stack.push(start)
    
    while not stack.isEmpty():
        actualNode = stack.pop()
        if actualNode[0] in closeList:
            continue
        else :
            if problem.isGoalState(actualNode[0]):
                while actualNode != start :
                    output.append(actualNode[1])
                    actualNode = actualNode[3]
                return output[::-1]
            else:
                childs = problem.getSuccessors(actualNode[0])
                for child in childs :
                    child = child + (actualNode, )
                    stack.push(child)
        closeList.add(actualNode[0])   

    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    queue = util.Queue()
    closeList = set()
    output = []

    start = (problem.getStartState(),None)
    queue.push(start)
    
    while not queue.isEmpty():
        actualNode = queue.pop()
        if actualNode[0] in closeList:
            continue
        else :
            if problem.isGoalState(actualNode[0]):
                while actualNode != start :
                    output.append(actualNode[1])
                    actualNode = actualNode[3]
                return output[::-1]
            else:
                childs = problem.getSuccessors(actualNode[0])
                for child in childs :
                    child = child + (actualNode, )
                    queue.push(child)
        closeList.add(actualNode[0])

    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    #Creamos las bases de lo que  usaremos para guardar la informacion
    queue = util.PriorityQueue()
    closeList = set()
    output = []
    
    #Insertamos el prrimer nodo 
    start = (problem.getStartState(),None,0,0,None)
    queue.push(start,0)

    #Recorremos nodo a nodo para expandirlos
    while not queue.isEmpty():
        #Sacamos el primer nodo de la lista de nodos a expandir
        actualNode = queue.pop()
        #Si hemos pasado ya por este nodo saltamos la iteracion
        if actualNode[0] in closeList:
            continue
        #Si no hemos pasado ya por el lo procesamos
        else :
            #Si es el GoalState Volvemos hacia atras para sacar la secuencia de pasos hasta aqui
            if problem.isGoalState(actualNode[0]):
                while actualNode != start :
                    output.append(actualNode[1])
                    actualNode = actualNode[4]
                return output[::-1]
            #Si no es goal State calculamos las fn(n) para decidir cual seguir expandiendo
            else:
                childs = problem.getSuccessors(actualNode[0])
                for child in childs :
                    #Calculamos el coste acumulado hasta este nodo
                    cost = child[2] + actualNode[3]
                    #calculamos el valor de la funcion f(n) con la heuristica = 0 y el coste acumulado
                    fn = cost
                    #Inserto informacion nueva en hijos
                    child = child + (cost,actualNode, )
                    #Inserto nodo en lista de prioridad
                    queue.push(child,fn)
        #inserto nodo visitado a la closeList
        closeList.add(actualNode[0])
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

    #Creamos las bases de lo que  usaremos para guardar la informacion
    queue = util.PriorityQueue()
    closeList = set()
    output = []
    
    #Insertamos el prrimer nodo 
    start = (problem.getStartState(),None,0,0,None)
    queue.push(start,heuristic(problem.getStartState(),problem))

    #Recorremos nodo a nodo para expandirlos
    while not queue.isEmpty():
        #Sacamos el primer nodo de la lista de nodos a expandir
        actualNode = queue.pop()
        #Si hemos pasado ya por este nodo saltamos la iteracion
        if actualNode[0] in closeList:
            continue
        #Si no hemos pasado ya por el lo procesamos
        else :
            #Si es el GoalState Volvemos hacia atras para sacar la secuencia de pasos hasta aqui
            if problem.isGoalState(actualNode[0]):
                while actualNode != start :
                    output.append(actualNode[1])
                    actualNode = actualNode[4]
                return output[::-1]
            #Si no es goal State calculamos las fn(n) para decidir cual seguir expandiendo
            else:
                childs = problem.getSuccessors(actualNode[0])
                for child in childs :
                    #Calculamos el coste acumulado hasta este nodo
                    cost = child[2] + actualNode[3]
                    #calculamos el valor de la funcion f(n) con la heuristica y el coste acumulado
                    fn = heuristic(child[0],problem) + cost
                    #Inserto informacion nueva en hijos
                    child = child + (cost,actualNode, )
                    #Inserto nodo en lista de prioridad
                    queue.push(child,fn)
        #inserto nodo visitado a la closeList
        closeList.add(actualNode[0])
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
