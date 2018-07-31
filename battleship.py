from random import randint

board = []

# Build the board
for x in range(0, 5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print " ".join(row)

# Place the ship
def random_row(board):
  return randint(1, len(board))

def random_col(board):
  return randint(1, len(board[0]))

ship_row = random_row(board)
ship_col = random_col(board)

def player_guess():
  guess_row = int(raw_input("Guess Row: ")) - 1
  while guess_row > (len(board) - 1) \
  or guess_row < 0:
    guess_row = int(raw_input("Invalid. Try again: ")) - 1
  guess_col = int(raw_input("Guess Col: ")) - 1
  while guess_col > (len(board[0]) - 1) \
  or guess_col < 0:
    guess_col = int(raw_input("Invalid. Try again: "))
  return [guess_row, guess_col]

# Play the game.
numturns = 10
for turn in range(numturns):
  print
  print "Turn %d:" % (turn + 1)
  print_board(board)
  
  guesses = player_guess()
  guess_row = guesses[0]
  guess_col = guesses[1]
  while board[guess_row][guess_col] == "X":
    print "That square has already been guessed."
    guesses = player_guess()
    guess_row = guesses[0]
    guess_col = guesses[1]
  
  if guess_row == ship_row and guess_col == ship_col:
    print "Congratulations! You sank my battleship!"
    break
  else:
    print "You missed my battleship!"
    print
    print "----------------------------------------------------"
    board[guess_row][guess_col] = "X"
    if turn + 1 >= numturns:
      print
      print "******************************"
      print "*     Game Over, man!        *"
      print "******************************"
