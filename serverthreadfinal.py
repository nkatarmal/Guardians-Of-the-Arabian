import socket
import select
import sys
from thread import *
import json
from threading import Lock

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind(('172.16.4.132', 12345))
server.listen(100)
client_found=False
no_of_client=0
list_of_clients = []
list_ip=[]
data1=False
client1_map=[]
client2_map=[]
lock=Lock()
def read_data(conn,addr):
	if not(data1):
		data1=True
		try:
			msg=conn.recv(2048)
			print msg
			client1_map=json.loads(msg)
			print "client data"
			print client1_map[:][:]

		except expression as identifier:
			pass	
	else:
		pass
	

def clientthread(conn, addr):

	global data1
	# sends a message to the client whose user object is conn
	#conn.send("Welcome to this chatroom!")
	while not(client_found):
		continue
	conn.send(json.dumps("ready"))
	while True:
			try:
				message = json.loads(conn.recv(2048))
				print message
				if message=='grid':
					#print "grid received"
					#read_data(conn,addr)
					if not(data1):
						data1=True
						try:
							lock.acquire()
							msg=conn.recv(4096)
							#print msg
							client1_map=json.loads(msg)
							print "client1 data"
							print client1_map
							lock.release()
						except Exception as e:
							print e
								
					else:
						try:
							lock.acquire()
							msg=conn.recv(4096)
							#print msg
							client2_map=json.loads(msg)
							print "client2 data"
							print client2_map
							lock.release()
						except Exception as e:
							print e
						
					"""prints the message and address of the
					user who just sent the message on the server
					terminal"""
					#print "<" + addr[0] + "> " + message

					# Calls broadcast function to send message to all
					message_to_send = "<" + addr[0] + "> " + message
				#	broadcast(message_to_send, conn)

				else:
					"""message may have no content if the connection
					is broken, in this case we remove the connection"""
					#remove(conn)

			except:
				continue
while True:

	
	conn, addr = server.accept()

	no_of_client+=1
	list_of_clients.append(conn)
	list_ip.append(addr[0])
	# prints the address of the user that just connected
	print addr[0] + " connected"

	# creates and individual thread for every user 
	# that conne
	if no_of_client==2:
		client_found=True
	start_new_thread(clientthread,(conn,addr)) 

def check(row,column):
	while hits != ships:
    os.system("cls")                
    print(" " + result + " [Ships: " + str(ships) + ", Size: " + str(gridSize) + ", Hits: " + str(hits) + "]\n")
    print(xLabel)                   
    for x in range(gridSize):
        print(" " + str(x) + " ",end="")
        for y in range(gridSize):
            print(" " * 2 if getGrid(x,y) == 'C' else getGrid(x,y) + " ",end="")
        print("")

    xGuess = int(input("\n X: "))
    yGuess = int(input(" Y: "))

    if getGrid(xGuess,yGuess) == 'C':
        result = "Hit! (" + str(xGuess) + ":" + str(yGuess) + ")"
        setGrid(xGuess,yGuess,'H')
        hits += 1
    else:
        result = "Miss! (" + str(xGuess) + ":" + str(yGuess) + ")"
        setGrid(xGuess,yGuess,'M')

print("\nCongratulations, you won the game!")
os.system("pause >nul")