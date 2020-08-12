# # PlottingProgram101.py
# try:
#     # Python2
#     import Tkinter as tk
# except ImportError:
#     # Python3
#     import tkinter as tk
# class FunctionFrame(object):
#     def __init__(self, root):
#         self._root = root
#         functionRow = tk.Frame(root, relief='sunken')
#         functionRow.grid(column=0, row=2)
#         g1 = tk.Label(functionRow, text='Function in X: ')
#         g1.pack(side='left')
#         functionInXInput = tk.Entry(functionRow, width=35)
#         functionInXInput.pack(side='left')
#         h1 = tk.Label(functionRow, text='       Function Colour: ')
#         h1.pack(side='left')
#         functionColourInput = tk.Entry(functionRow, width=20)
#         functionColourInput.pack(side='left')
#         space = tk.Label(functionRow, text='       ')
#         space.pack(side='left')
#         b1 = tk.Button(functionRow, text='Select', padx=5, 
#             command=createFunction())
#         b1.pack(side='right')
# class PlotFrame(object):
#     def __init__(self, root):
#         self._root = root
#         plotRow = tk.Frame(root, relief='sunken')
#         plotRow.grid(column=0, row=3, pady=20)
#         a = tk.Label(plotRow, text='Plot Settings   ')
#         a.pack(side='left')
#         b1 = tk.Label(plotRow, text='Start X: ')
#         b1.pack(side='left')
#         startXInput = tk.Entry(plotRow, width=10)
#         startXInput.pack(side='left')
#         c1 = tk.Label(plotRow, text='   End X: ')
#         c1.pack(side='left')
#         endXInput = tk.Entry(plotRow, width=10)
#         endXInput.pack(side='left')
#         d1 = tk.Label(plotRow, text='  Start Y: ')
#         d1.pack(side='left')
#         startYInput = tk.Entry(plotRow, width=10)
#         startYInput.pack(side='left')
#         e1 = tk.Label(plotRow, text='   End Y: ')
#         e1.pack(side='left')
#         endYInput = tk.Entry(plotRow, width=10)
#         endYInput.pack(side='left')
#         f1 = tk.Label(plotRow, text='   Steps: ')
#         f1.pack(side='left')
#         stepsInput = tk.Entry(plotRow, width=10)
#         stepsInput.pack(side='left')
# class PlotApp(object):
#     def __init__(self, root):
#         self._root = root
#         PlotFrame(root)
#         FunctionFrame(root)
#         self.createCanvas()
#     def createCanvas(self):
#         canvas = tk.Canvas(self._root, bg='white')
#         canvas.grid(column=0, row=1, sticky='nwes')
#         canvas.bind("<Button-1>", self.clicked)
#         canvas.bind("<Enter>", self.moved)
    
#     def clicked(self, event):
#         x, y = event.x, event.y
#         s = "Last point clicked at x=%s  y=%s" % (x, y)
#         self._root.title(s)
#     def moved(self, event):
#         x, y = event.x, event.y
#         s = "Cursor at x=%s  y=%s" % (x, y)
#         self._root.title(s)        
# def createFunction():
#     pass
# def main():
#     root = tk.Tk()
#     app = PlotApp(root)
#     root.mainloop()
# if  __name__ == '__main__':
#     main()



# import turtle
# import math

# class Vertex():
#     def __init__(self,x,y,size):
#         self.xcoor=x
#         self.ycoor=y
#         self.size=size
#         self.label="None"

#     def __str__(self):
#         return("Vertex at ("+str(self.xcoor)+','+str(self.ycoor)+")")

#     def distance_from(self,v):
#         deltax=self.xcoor-v.xcoor
#         deltay=self.ycoor-v.ycoor
#         distance=math.sqrt(deltax**2+deltay**2)
#         return(distance)


# class Edge():
#     def __init__(self,v1,v2,weight=None):
#         self.v1=v1
#         self.v2=v2
#         if weight==None:
#             self.weight=v1.distance_from(v2)
#         else:
#             self.weight=weight

#     def __str__(self):
#         string="(Undirected)Edge from "+str(self.v1)+" to "+str(self.v2)+" weight="+str(self.weight)
#         return(string)
















# clicked_flag=0
# dragged_flag=0
# released_flag=0

# vertex_pen_size=10

# drag_pos=[]

# vertexset=[]

# def check_edge():       ##Remove self edges(self loops)
#     global vertexset
#     global drag_pos
#     global vertex_pen_size
#     print("In check_edge\n Vertices:")
#     print(vertexset)
#     for v in vertexset:
#         print(v)
#     print("drag_pos",drag_pos)

#     start=drag_pos[0]
#     end=drag_pos[1]
#     startv=None
#     endv=None
#     for v in vertexset:
#         x_low=v.xcoor-vertex_pen_size
#         x_high=v.xcoor+vertex_pen_size
#         y_low=v.ycoor-vertex_pen_size
#         y_high=v.ycoor+vertex_pen_size
#         if start[0]>=x_low and start[0]<=x_high and start[1]>=y_low and start[1]<=y_high:
#             startv=v
#         elif end[0]>=x_low and end[0]<=x_high and end[1]>=y_low and end[1]<=y_high:
#             endv=v

#     if startv!=None and endv!=None:
#         turtle.penup()
#         turtle.goto(startv.xcoor,startv.ycoor)
#         turtle.pendown()
#         turtle.goto(endv.xcoor,endv.ycoor)
#         print("Made edge")
#         newe=Edge(startv,endv)
#         print(newe)

# def gothere(event):
    # print("Clicked")
    # turtle.penup()
    # x=c.canvasx(event.x)
    # y=-c.canvasy(event.y)
    # turtle.goto(x,y)
    # turtle.pendown()

# def drag(event):
#     global dragged_flag
#     c.unbind("<B1-Motion>")
#     #print("Dragging")
#     #print(dragged_flag)
#     dragged_flag=1
#     #print("Moving",event.x,event.y)
#     x=c.canvasx(event.x)
#     y=-c.canvasy(event.y)
#     if len(drag_pos)==0:
#         print("Drag starts at",x,y)
#         drag_pos.append((x,y))
    
#     #turtle.goto(x,y)
#     c.bind("<B1-Motion>", drag)

# def release(event):
#     global dragged_flag
#     global drag_pos
#     x=c.canvasx(event.x)
#     y=-c.canvasy(event.y)
#     if dragged_flag==0:
#         print("Released click")
#         newv=Vertex(x,y,vertex_pen_size)
#         print("Vertex created at(",x,",",y,")")
#         vertexset.append(newv)
#         ori=turtle.pensize()
#         turtle.pensize(vertex_pen_size)
#         turtle.dot()
#         turtle.pensize(ori)

#     elif dragged_flag==1:
#         print("Released drag")
        
#         if len(drag_pos)==1:
#             print("Drag ends at",x,y)
#             drag_pos.append((x,y))
#         check_edge()
#         drag_pos=[]
#         dragged_flag=0
#     print(event.x,event.y,event)

# def reset(event):
#     turtle.clear()




# turtle.reset()
# turtle.speed(0)

# c=turtle.getcanvas()

# print(turtle.pensize())
# c.bind("<Button-1>", gothere)
# c.bind("<B1-Motion>", drag)
# c.bind("<ButtonRelease-1>", release)
# c.bind("<Escape>",reset)



# s=turtle.Screen()
# s.listen()imp










# import tkinter as tk

# root = tk.Tk()

# servs = ['Gmail', 'Yahoo', 'Comcast', 'Verizon', 'AT&T', 'Outlook']
# svar = tk.StringVar()
# svar.set(servs[0])     #<-- Setting default item to servs's first item
# #sv = servs[0]          #<-- setting sv to default item
# def _get(cur):         #<-- function to run
#     svar.set(cur)          #<-- 'cur' is the selected value
#     #print("cur is",str(cur))

# drop = tk.OptionMenu(root, svar, command = _get, *servs)
# drop.grid(row=2, column=1)

# root.mainloop()
# \





# import tkinter as tk

# class Example(tk.Frame):
#     def __init__(self, parent):
#         tk.Frame.__init__(self, parent)

#         self.choices = ("one", "two", "three", "four", "five", 
#                         "six", "seven", "eight", "nine", "ten",
#                         "eleven", "twelve", "thirteen", "fourteen",
#                         "fifteen", "sixteen", "seventeen", "eighteen",
#                         "nineteen", "twenty")

#         self.entryVar = tk.StringVar()
#         self.entry = tk.Entry(self, textvariable=self.entryVar)
#         self.listbox = tk.Listbox(self)
#         self.listbox.insert("end", *self.choices)

#         self.entry.pack(side="top", fill="x")
#         self.listbox.pack(side="top", fill="both", expand=True)

#         self.entryVar.trace("w", self.show_choices)
#         self.listbox.bind("<<ListboxSelect>>", self.on_listbox_select)

#     def on_listbox_select(self, event):
#         """Set the value based on the item that was clicked"""
#         index = self.listbox.curselection()[0]
#         data = self.listbox.get(index)
#         self.entryVar.set(data)

#     def show_choices(self, name1, name2, op):
#         """Filter choices based on what was typed in the entry"""
#         pattern = self.entryVar.get()
#         choices = [x for x in self.choices if x.startswith(pattern)]
#         self.listbox.delete(0, "end")
#         self.listbox.insert("end", *choices)

# if __name__ == "__main__":
#     root = tk.Tk()
#     Example(root).pack(fill="both", expand=True)
#     root.mainloop()









# import tkinter as tk #import Tkinter as tk #change to commented for python2

# root = tk.Tk()
# root.title("ROOT")
# extra = tk.Toplevel()
# label = tk.Label(extra, text="extra window")
# label.pack()

# lower_button = tk.Button(root,
#                          text="lower this window",
#                          command=root.lower)
# lower_button.pack()

# root.mainloop()

# import turtle

# screen = turtle.Screen()

# answer = screen.textinput("Welcome to Bowling!", "Are you ready to bowl?")

# if answer is None or answer.lower().startswith('n'):
#     print("Goodbye!")
#     screen.clear()
#     screen.bye()
# else:
#     print("Start!")


# from turtle import Turtle, mainloop

# BUTTON_SIZE = 60
# CURSOR_SIZE = 20
# FONT_SIZE = 18
# FONT = ('Arial', FONT_SIZE, 'bold')
# STATES = (('red', 'OFF'), ('green', 'ON'))
# INITIAL_STATE = STATES[0]

# def toggle_power(x, y):
#     color, state = STATES[button.fillcolor() == 'red']

#     button.fillcolor(color)
#     marker.undo()
#     marker.write(state, align='center', font=FONT)

# color, state = INITIAL_STATE

# button = Turtle('circle')
# button.shapesize(BUTTON_SIZE / CURSOR_SIZE, outline=2)
# button.color('black', color)
# button.penup()
# # button.goto(-200, 200)  # move the button into position

# marker = Turtle(visible=False)
# marker.penup()
# marker.goto(button.xcor(), button.ycor() - BUTTON_SIZE/2 - FONT_SIZE - 2)
# marker.write(state, align='center', font=FONT)

# button.onclick(toggle_power)

# mainloop()






import tkinter as tk
import time
root=tk.Tk()
root.geometry("600x600")
root.title("User Interface Monitor")
rpm=tk.StringVar(root)
tim=tk.StringVar(root)
def  enter():
    global rpm,tim
    root.rpmLabel=tk.Label(root,text="enter rpm value:")
    root.rpmLabel.grid(row=0)
    root.timeLabel=tk.Label(root,text="enter time in sec")
    root.timeLabel.grid(row=1)
    root.e1 = tk.Entry(root,textvariable=rpm)
    root.e1.grid(row=0,column=1)
    root.e2 = tk.Entry(root,textvariable=tim)
    root.e2.grid(row=1,column=1)
    #rpm=rpm.get()
    #tim=tim.get()
    #return rpm,tim
def gett():
    global rpm, tim
    rpm1 = rpm.get()
    tim1 = tim.get()
    print(rpm1)
    print(tim1)
    root.e1.destroy()
    root.e2.destroy()
    root.rpmLabel.destroy()
    root.timeLabel.destroy()
    #e1.pack()
    #e2.pack()
root.Button1=tk.Button(root,text="MODE1",command=enter)
root.Button1.pack()
root.Button1.place(x=200,y=200)
root.Button2=tk.Button(root,text="Enter",command=gett)#root.Button2.pack()
root.Button2.place(x=260,y=200)
root.mainloop()
