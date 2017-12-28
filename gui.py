
def gameGui(boat_map):
    import Tkinter as tk

    root = tk.Tk()
    frame = tk.Frame(root)
    frame.pack()
    frame1= tk.Frame(frame)
    frame1.grid(row=0, column=0, columnspan=5)

    frame2= tk.Frame(frame)
    frame2.grid(row=0, column=7, columnspan=5)

    frame3= tk.Frame(frame)
    frame3.grid(row=0, column=6)

    b = tk.Button(frame3, text="  Fire  ")
    b.pack()
    button_array=[[0 for x in range(25)]for y in range(25)]
    for i in range(25):
        for j in range(25):
            if boat_map[i][j]==1:
                b = tk.Button(frame1, text="  ",bg='red')
                b.grid(row=i, column=j)
            else:
                b = tk.Button(frame1, text="  ")
                b.grid(row=i, column=j)

    def showGrid(i,j):
        row    = b.grid_info()['row']      # Row of the button
        column = b.grid_info()['column']   # grid_info will return dictionary with all grid elements (row, column, ipadx, ipday, sticky, rowspan and columnspan)
        print "Grid position of 'btn': "+str(i)+","+str(j)
    for i in range(25):
        for j in range(25):
            b = tk.Button(frame2, text="  ",command=lambda i=i,j=j:showGrid(i,j))
            b.grid(row=i, column=j)

    root.mainloop()