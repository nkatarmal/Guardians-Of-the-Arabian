import Tkinter as tk
import gui
root=tk.Tk()
frame=tk.Frame(root)
frame.pack()

frame1=tk.Frame(frame)
frame1.grid(row=0,column=0,columnspan=5)

button_list=[[0 for x in range(25)]for y in range(25)]
boat_map=[[0 for x in range(25)]for y in range(25)]
lengths=[2,3,4,5]
index=0
frame3= tk.Frame(frame)
frame3.grid(row=0, column=6)
def showGrid(i,j):
    global index
  #  row = b.grid_info()['row']      # Row of the button
   # column = b.grid_info()['column']   # grid_info will return dictionary with all grid elements (row, column, ipadx, ipday, sticky, rowspan and columnspan)
    for x in range(lengths[index]):
        bt=button_list[i][j+x]
        boat_map[i][j+x]=1
        bt['state']='disabled'
        bt["bg"]="red"
    index+=1
    print "Grid position of 'btn': "+str(i)+","+str(j)

for i in range(25):
    for j in range(25):
        b = tk.Button(frame1, text="  ",command=lambda i=i,j=j:showGrid(i,j))
        b.grid(row=i,column=j)
        button_list[i][j]=b

def boatSelection():
   
    if index==3:
        b['text']='next'
    elif index>=4:
        frame.destroy()
        gui.gameGui(boat_map)
    else:
        b['text']='length :'+str(lengths[index])
    
        
b = tk.Button(frame3, text="length:"+str(lengths[index]),command=boatSelection)
b.pack()

root.mainloop()
print "hello"