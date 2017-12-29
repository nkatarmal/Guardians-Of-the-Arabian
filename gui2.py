import Tkinter as tk
import socket
import threading
import json
import gui
import gui1


strdata=''
server_ready=False
root=tk.Tk()
frame=tk.Frame(root)
frame.pack()
frame1= tk.Frame(frame)
frame1.grid(row=0, column=0,)
frame2= tk.Frame(frame)
frame2.grid(row=1, column=0)
frame3= tk.Frame(frame)
frame3.grid(row=0, column=1)
root.geometry('300x300')
def sendThread(clientsocket):
    """
    sends messages to server
    :param clientsocket:
    :return:
    """
    global strdata
    while True:
      #  print server_ready
       # msg=raw_input("")
       # clientsocket.send(msg)

        if server_ready:
            print "server ready"
            root.destroy()
            gui1.call_guiboat(clientsocket)
            #clientsocket.send(json.dumps('grid'))
            #clientsocket.send(strdata)
            #print strdata
            break
    
    #while not(gui1.select_done):
    #    pass
    #clientsocket.send(json.dumps('grid'))
    #clientsocket.send(json.dumps(gui1.boat_map))
        

def recvThread(clientsocket):
    """
    receives messages sent by server
    :param clientsocket:
    :return:
    """
    global server_ready
    global strdata
    while True:
        msg= json.loads(clientsocket.recv(512))
        print msg
        if(msg =="ready"):
            print "hello"
            server_ready=True
            #arr=[[11 for x in range(25)] for y in range(25)]
            #strdata=json.dumps(arr)
def review():
  
    try:
        #creates a client socket and makes a connection to server
        clientsocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        clientsocket.connect(('172.16.4.132',12345))
        sthread=threading.Thread(target=sendThread,args=[clientsocket])
        sthread.start()
        rthread=threading.Thread(target=recvThread,args=[clientsocket])
        rthread.start()
        rthread.join()
        sthread.join()
    except Exception as e:
        print e.message
    w = tk.Label(frame2, text="Please wait until another client be ready...")
    w.pack()


b1=tk.Button(frame1, text="      Start New Game      ",command=review)

b1.pack()

root.mainloop()