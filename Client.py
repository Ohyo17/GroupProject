import socket
import sys
HOST = "192.168.56.103"
PORT = 8888

print("---------Welcome to Speed ROCK, PAPER, SCISSOR---------------")
print("-----There is no limit when playing this game----")
print("Enter [r] for Rocks")
print("Enter [p] for Paper")
print("Enter [s] for Scissors")
print("Enter [exit] to end the program")
print("The program also will be end if opponent enter [exit]")
print("Waiting for another player\n")

def rocks(x,y):
      global win,loss
      move = x
      opponent = y

      if move == opponent:

              print("It's Tie\n")
              win = win + 1
              loss = loss + 1
              print("Player:",win,"\tOpponent:",loss,"\n")

      elif move == 'r' and opponent == 's':

              print("You win\n")
              win = win + 1
              print("Player:" ,win, "\tOpponent:", loss,"\n")

      elif move == 'r' and opponent == 'p':

              print("You lose\n")
              loss = loss + 1
              print("Player:",win,"\tOpponent",loss,"\n")

      else:
              print("Invalid move Rocks\n")


def paper(x,y):
      global win,loss
      move = x
      opponent = y

      if move == opponent:
               print("It's a Tie\n")

               win = win + 1
               loss = loss + 1
               print("Player:",win,"\tOpponent:",loss,"\n")

      elif move == 'p' and opponent == 's':

               print("You lose\n")
               loss = loss + 1
               print("Player:" , win,"\tOpponent:", loss,"\n")

      elif move == 'p' and opponent == 'r':

               print("You win\n")
               win = win + 1
               print("Player:",win,"\tOpponent:",loss,"\n")
      else:
           print("Invalid move Paper\n")



def scissor(x,y):
      global win,loss
      move = x
      opponent = y

      if move == opponent:
               print("It's a Tie\n")

               win = win + 1
               loss = loss + 1
               print("Player:",win,"\tOpponent:",loss,"\n")

      elif move == 's' and opponent == 'p':

               print("You win\n")
               win = win + 1
               print("Player:" , win,"\tOpponent:", loss,"\n")

      elif move == 's' and opponent == 'r':
               print("You lose\n")
               loss = loss + 1

               print("Player:",win,"\tOpponent:",loss,"\n")
      else:
               print("Invalid move Scissors")


def score():
      global win,loss

      if(win>loss):
               print("You are the winner")
               print("Thank you for playing Speed Rocks,Paper,Scissor\n")
               s.close()

      elif(win == loss):
               print("It's Deuce")
               print("Thank you for playing Speed Rocks,Paper,Scissor\n")
               s.close()

      else:
               print("You are the loser")
               print("Thank you for playing Speed Rocks,Paper,Scissor\n")
               s.close()



with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        
        while True:
               data = b""
               while data != b"\n":
                     data = s.recv(1024)

               move = input("r ,p ,s: ")
               s.sendall(str.encode(move))
               print("Waiting for opponent move\n")

               data = b""
               while not data:
                     data = s.recv(1024)

               opponent = data.decode('utf-8')
               
               print("Received:", opponent)
               if move == 'exit' or opponent == 'exit':
                       score()
                       break
                       sys.exit()

               if move == 'r':
                       rocks(move,opponent)

               elif move == 'p':
                       paper(move,opponent)

               elif move == 's':
                       scissor(move,opponent)

               else:
                   print("Invalid Move or words\n")
