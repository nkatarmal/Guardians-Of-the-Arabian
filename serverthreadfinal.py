import socket
import select
import sys
from thread import *
import json
from threading import Lock

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind(('192.168.43.173', 12345))
server.listen(100)
client_found=False
no_of_client=0
list_of_clients = [0,0]
list_ip=[]
data1=False
client1_map=[]
client2_map=[]
client1_turn=False
client2_turn=False
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
	global list_of_clients
	global client1_turn
	global client2_turn
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
							list_of_clients[0]=conn
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
							list_of_clients[1]=conn
							print "client2 data"
							print client2_map
							lock.release()
							temp_conn=list_of_clients[0]
							temp_conn.send(json.dumps('start'))
							client1_turn=True	
							print "start send"
						except Exception as e:
							print e
						first_only=True
						cl1=list_of_clients[0]
						cl2=list_of_clients[1]
						while True:
							while client1_turn:
								ms=json.loads(cl1.recv(512))
								print "msg"+ms
								if ms =="cor":
									print 'cor received'
									pos=json.loads(cl1.recv(512))
									client1_turn=False
									client2_turn=True
									print pos
									if first_only:
										list_of_clients[1].send(json.dumps('start'))
										first_only=False
							while client2_turn:
								ms=json.loads(cl2.recv(512))
								if ms=='cor':
									pos=json.loads(cl2.recv(512))
									client1_turn=True
									client2_turn=False
									print pos

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
