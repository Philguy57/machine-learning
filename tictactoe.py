import numpy as np
import scipy as sp
import networkx as nx
import random

def check_for_win(board):
    if board[0 : 3] == [1, 1, 1] or board[0 : 3] == [2, 2, 2]:
        return True
    if board[3 : 6] == [1, 1, 1] or board[3 : 6] == [2, 2, 2]:
        return True
    if board[6 : 8] == [1, 1, 1] or board[6 : 8] == [2, 2, 2]:
        return True
    if board[0] == 1 and board[3] == 1 and board[6] == 1:
        return True
    if board[0] == 2 and board[3] == 2 and board[6] == 2:
        return True
    if board[1] == 1 and board[4] == 1 and board[7] == 1:
        return True
    if board[1] == 2 and board[4] == 2 and board[7] == 2:
        return True
    if board[2] == 1 and board[5] == 1 and board[8] == 1:
        return True
    if board[2] == 2 and board[5] == 2 and board[8] == 2:
        return True
    if board[0] == 1 and board[4] == 1 and board[8] == 1:
        return True
    if board[0] == 2 and board[4] == 2 and board[8] == 2:
        return True
    if board[2] == 1 and board[4] == 1 and board[6] == 1:
        return True
    if board[2] == 2 and board[4] == 2 and board[6] == 2:
        return True
    return False

def get_next_state(graph, node):
    if node in graph:
        weightMax = -60000
        nextNode = ''
        neighbors = graph.neighbors(node)
        for n in neighbors:
            if graph[node][n]['weight'] > weightMax:
                weightMax = graph[node][n]['weight']
                nextNode = n

        return nextNode
    else:
        return ''


print("Welcome to the Tic-Tac-Toe AI")
print("Type 'X' or 'O' to choose what you play.")
G = nx.read_gexf("TicTacToeStates.gexf")
player = input()
while player != 'X' and player != 'O':
	print("Input invalid. Please type 'X' or 'O' to choose what you play:")
	player = input()

if player is 'X':
	print('X')
if player is 'O':
	print('O')
