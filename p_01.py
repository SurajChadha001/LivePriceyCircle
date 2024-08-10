rows=6
columns=7
board = [[' ' for _ in range(rows)]for _ in range (columns)]

def print_board(board):
  for row in range(rows-1, -1, -1):
    print("|",end="")
    for col in range(columns):
      print(board[col][row],end="|")
    print()
  print("-"*(2*columns+1))
def drop_piece(board,column,piece):
  for row in range(rows):
    if board[column][row]=='':
      board[column][row]=piece
      return True
  return False
print_board(board)
drop_piece(board,3,'X')
drop_piece(board,4,'O')
drop_piece(board,3,'X')
print_board(board)



