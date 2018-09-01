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

def players_turn(boardString):
	print('Current Board State:')
	print('  ',boardString[0],' | ',boardString[1],' | ', boardString[2],' ')
	print(' -----+-----+----- ')
	print('  ',boardString[3],' | ',boardString[4],' | ', boardString[5],' ')
	print(' -----+-----+----- ')
	print('  ',boardString[6],' | ',boardString[7],' | ', boardString[8],' ')
	print('It is your turn. Enter your move by indexing into the board.')
	print("Obey zero-indexing. for example, entering in '1 1' will choose the center tile.")

	return 0


print("Hello, I am the Tic-Tac-Toe AI")
print("Type 'X' or 'O' to choose what you will play.")
G = nx.read_gexf("TicTacToeStates.gexf")
player = input()
boardString = '---------'
turnOrder = 3
while player != 'X' and player != 'O':
	print("Input invalid. Please type 'X' or 'O' to choose what you play:")
	player = input()

if player is 'X':
	turnOrder = 0
	players_turn(boardString)
	moveX = int(input('horizontal index: '))
	moveY = int(input('vertical index: '))
	while( (moveX > 2) or (moveX < 0) or (moveY > 2) or (moveY < 0) or (boardString[moveX+moveY*3] != '-') ):
		print("Index invalid, please enter a valid move.(remember it is zero-indexed)")
	moveIndex = moveX + moveY*3
	boardString[moveIndex] = 'X'

if player is 'O':
	turnOrder = 1
	boardString = get_next_state(G, boardString)

players_turn(boardString)
