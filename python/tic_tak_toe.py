# create board - done

# display board - done

# handle input - done

# update board - done

# flip players - done

# check vin
  # check rows
  # check cols
  # check digs

# check Title

# Notify users of winner
# stop code from br


winner = None
gameRunning = True
currentPlayer = "X"


board = ["-","-","-",
          "-","-","-",
          "-","-","-"]

def displayBoard():

  print(board[0] + " | " + board[1] + " | " + board[2])
  print(board[3] + " | " + board[4] + " | " + board[5])
  print(board[6] + " | " + board[7] + " | " + board[8])

# def compOrUser():
#   print("1: Multiplayer ")
#   print("2: Computer")
#   player = input("Computer or Multiplayer?: ")

#   if player == "2":
#     pass 
#     computer()
#   else:
#     pass
#     flipPlayer()
  
# def computer():
#   return



def handleInput():

  valid = False

  pos = input("Choose a position from 1-9: ")

  while not valid:
    while pos not in ["1","2","3","4","5","6","7","8","9"]:
      pos = input("That position is invalid: Choose a position from 1-9: ")

    pos = int(pos) - 1

    if board[pos] != "-":
      print("You can't go there")
    else:
      valid = True

  board[pos] = currentPlayer

  displayBoard()

  return

def checkRows():
  global gameRunning
  global winner

  row1 = board[0] == board [1] == board[2] != "-"
  row2 = board[3] == board [4] == board[5] != "-"
  row3 = board[6] == board [7] == board[8] != "-"

  if row1 or row2 or row3 == True:
    gameRunning = False
    winner = currentPlayer
    
  if row1:
    return board[0]
  elif row2:
    return board[3]
  elif row3:
    return board[6]
  else:
    return None

def checkCols():
  global gameRunning
  global winner

  col1 = board[0] == board [3] == board[6] != "-"
  col2 = board[1] == board [4] == board[7] != "-"
  col3 = board[2] == board [5] == board[8] != "-"

  if col1 or col2 or col3 == True:
    gameRunning = False
    winner = currentPlayer

  if col1:
    return board[0]
  elif col2:
    return board[1]
  elif col3:
    return board[2]
  else:
    return None

def checkDiags():
  global gameRunning
  global winner

  diag1 = board[0] == board [4] == board[8] != "-"
  diag2 = board[3] == board [4] == board[6] != "-"

  if diag1 or diag2 == True:
    gameRunning = False
    winner = currentPlayer

  if diag1:
    return board[0]
  elif diag2:
    return board[3]
  else:
    return None

def checkTie():
  global gameRunning

  if "-" not in board:
    gameRunning = False

def checkWin():
  global winner
  
  checkRows()
  checkCols()
  checkDiags()
  return



def checkGameOver():
  checkWin()
  return

def flipPlayer():
  global currentPlayer

  if currentPlayer == "X":
    currentPlayer = "O"
  else:
    currentPlayer = "X"

  return


def playGame():
  displayBoard()
  # compOrUser()

  while gameRunning:
    handleInput()
    checkGameOver()
    flipPlayer()

  if winner == "X" or winner == "O":
    print( winner + " won")
  else:
    print("TIE")

playGame()