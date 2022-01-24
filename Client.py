import socket
import sys
HOST = "192.168.56.103"
PORT = 8888

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
