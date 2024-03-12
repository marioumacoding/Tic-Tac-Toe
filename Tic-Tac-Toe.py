from helpers import drawBoard , checkTurn , checkForWin
import os

#this is a dictionary 
spots = {1: '1' , 2: '2', 3: '3' , 4: '4' , 5: '5' ,
         6: '6' , 7: '7' , 8: '8' , 9: '9'}

playing = True
complete = False
turn = 0 
prevTurn = -1

while(playing):
  # to avoid drawing the whole board each time we need to clear our screen --> depending on our os  
  os.system('cls' if os.name == 'nt' else 'clear')
  drawBoard(spots)
  if prevTurn == turn: 
    print("Invalid move, pick another spot")
  prevTurn = turn
  print("Player " + str( (turn % 2) + 1 ) + "'s turn: Pick your spot or press q to quit")
  # Get input from the player
  choice = input() 
  if choice == 'q':
    playing = False
  #this is a function from the string library and only returns true if the digit is non decimal
  elif str.isdigit(choice) and int(choice) < 10:
    # check if the spot has already been taken
    if not spots[int(choice)] in {"X","O"}:
      # Valid input , update the board
      turn += 1
      spots[int(choice)] = checkTurn(turn)
  else: print("Invalid move, pick another spot")
  if checkForWin(spots): playing , complete = False,True
  if turn > 8: playing = False

os.system('cls' if os.name == 'nt' else 'clear')
drawBoard(spots)

# If there was a winner , say who won 
if complete: 
  if checkTurn(turn) == 'X' : print("Player 1 wins!")
  else: print("Player 2 wins!")
else: print("TIE!")
print("Thanks for playing")