from enum import Enum
import random

class Piece(Enum):
	niu_black = 0
	niu_red = 1
	ju_black = 2
	ju_red = 3
	ma_black = 4
	ma_red = 5
	xiang_black = 6
	xiang_red = 7
	shi_black = 8
	shi_red = 9
	gou_black = 10
	gou_red = 11

# Player Private Info
# 0-11: count of pieces of a type the player holds (0-3)
# 12-22: count of pieces of a type the player give-ups (0-3)

# Game State Vector Public: indicate the current state the player are able to see:
# 0: current player playing (0-2)
# 1: current player position (0-2)
# 2: current playing state: deciding if the player wants to keep playing or deciding what piece the player wants to play (0-1)
# 3: first player want to play: (0-1)
# 4: second player want to play: (0-1)
# 5: thid player want to play: (0-1)
# 6: current round count (0-7)
# 7: current pillar count (0-7)
# 8: second player give ups: (0-1)
# 9-20: num of pieces the first player in this round plays (0-3)
# 21-32: num of pieces the second player in this round plays (0-3)
# 33: num of pieces the second player in this round give ups (0-3)

# Game History Vector for a Round
# 0: first player: (0-2)
# 1: first player wants to play: (0-1)
# 2: second player wants to play: (0-1)
# 3: third player wants to play: (0-1)
# 4: if the second player give ups (0-1)
# 5: if the third player give ups (0-1)
# 6: pillar count (1-3)
# 7: player index that owns the pillars (0-2)
# 8-19: number of each type of pieces the first player plays (0-3)
# 20-31: number of each type of pieces the second player plays/give ups. (0-3) All 0 if send to player other than the second pos one and the second player give ups.
# 32-43: number of each type of pieces the third player plays/give ups. (0-3) All 0 if send to player other than the second pos one and the third player give ups.

# Player Plays Vector
# 0: want to play: (0-1)
# 1: want to give up: (0-1)
# 2-13: number of each type of pieces the first player plays

class PillarSet:
	def __init__(self, iFirstPlayer, iPillarCount, ePieceType, iPillarID): # what pieces first player plays
		self.iPillarID = iPillarID
		self.iOwner = iFirstPlayer
		self.iPillarCount = iPillarCount
		self.iFirstPlayerID = iFirstPlayer
		self.aPieceTypes = [ePieceType]

class Player:
	owned_pillar = []
	def __init__(self, hGame, iPlayerID):
		self.aCurrentPieceHold = [0,0,0,0,0,0,0,0,0,0,0,0] #piece hold, only visible to player self
		self.aCurrentPieceGiveUp = [0,0,0,0,0,0,0,0,0,0,0,0]
		self.hGame = hGame
		self.iPlayerID = iPlayerID

class Game:
	players = []
	def __init__(self, pick_player_idx):
		#deal piece, decide first player
		self.players[0] = Player(self, 0)
		self.players[1] = Player(self, 1)
		self.players[2] = Player(self, 2)
		piece_pool = [0,0,0,1,1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,11]

# This function updates the game state vector and game history vector with legal plays.
def XianqiMainEngine(aGameState = None, aGameHistory = None, aPlayerPrivateInfos = None, iPlayerDeciding = None, iUpdateTo = None):

	if aGameState[1] == 0:
		pass

def CheckPlayLegal(aGameState = None, aGameHistory = None, aPlayerPrivateInfos = None, iPlayerDeciding = None, iUpdateTo = None):
# whether the game goes on
	if aGameState[1] == 0:
		

		return False
	
def CalculatePay(aGameHistory = None):
	pass
	
	
	
	
	
	
	
	
	
	
	
	
	
