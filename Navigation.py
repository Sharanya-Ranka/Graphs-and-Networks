# import turtle
# import tkinter as tk

# def forward():
#     t.forward(100)

# def back():
#     t.back(100)

# def left():
#     t.left(90)

# def right():
#     t.right(90)

# def drawpoint(event):
#   print(event.x,event.y)
#   t.penup()
#   x=canvas.canvasx(event.x)
#   y=-canvas.canvasy(event.y)
#   t.goto(x,y)
#   t.dot()


# root = tk.Tk()
# canvas = tk.Canvas(master = root, width = 500, height = 500)
# canvas.pack()

# t = turtle.RawTurtle(canvas)
# t.pencolor("#ff0000") # Red
# t.pensize(2)

# t.penup()   # Regarding one of the comments
# t.pendown() # Regarding one of the comments

# tk.Button(master = root, text = "Forward", command = forward).pack(side = tk.LEFT)
# tk.Button(master = root, text = "Back", command = back).pack(side = tk.LEFT)
# tk.Button(master = root, text = "Left", command = left).pack(side = tk.LEFT)
# tk.Button(master = root, text = "Right", command = right).pack(side = tk.LEFT)

# canvas.bind("<B1-Motion>",drawpoint)

# #t.onclick(drawpoint)

# root.mainloop()

import tkinter
import turtle
import math
import sys
import time
import random

class Vertex():
    def __init__(self,x,y,index,label="None",size=0):
        self.xcoor=x
        self.ycoor=y
        self.size=size
        self.index=index
        #adjacent_to uses format vertex:(via)edge
        #self.adjacent_to={}
        #self.key=key
        self.label=label

    def __str__(self):
        printedstr=""
        printedstr+="self.graph.add_vertex("+str(self.xcoor)+","+str(self.ycoor)+",'"+self.label+"')"#self.label+"("+str(self.xcoor)+","+str(self.ycoor)+")"
        return(printedstr)

    def distance_from(self,v):
        deltax=self.xcoor-v.xcoor
        deltay=self.ycoor-v.ycoor
        distance=math.sqrt(deltax**2+deltay**2)
        return(distance)

    def  get_edge_list(self):
        return(self.edge_list)


class Edge():
    def __init__(self,v1,v2,weight=None):
        self.v1=v1
        self.v2=v2
        if weight==None:
            self.weight=v1.distance_from(v2)
        else:
            self.weight=weight

        #Updating edge_list in v1 and v2
        #self.v1.adjacent_to[v2]=self
        #self.v2.adjacent_to[v1]=self

    def __str__(self):
        string="self.graph.add_edge("+str(self.v1.index)+","+str(self.v2.index)+","+str(self.weight)+")"#"(Undirected)Edge from "+str(self.v1)+" to "+str(self.v2)+" weight="+str(self.weight)
        return(string)



class Graph():
    def __init__(self):
        self.vertex_list=[]
        self.edge_list=[]
        #adjacent_to uses format vertex_index:(via)edge_index
        self.adjacent_to=[]



    def __str__(self):
        printedstr=""

        printedstr+="Vertices:\n"
        for v in self.vertex_list:
            printedstr+=str(v)+"\n"

        printedstr+="Edges:\n"
        for e in self.edge_list:
            printedstr+=str(e)+"\n"

        printedstr+="\n"
        return(printedstr)


    def add_vertex(self,x,y,label="None",size=0):
        self.adjacent_to.append({})
        newv=Vertex(x,y,len(self.vertex_list),label,size)
        self.vertex_list.append(newv)

    def add_edge(self,v1_ind,v2_ind,weight):
        # The indices will be given to this function by the calling statement
        # To make a vertex, we will have to iterate over vertex_list to find appropriate vertices
        # hence we will get vertex indices
        print("In add_edge. Indices are",v1_ind,v2_ind)
        v1=self.vertex_list[v1_ind]
        v2=self.vertex_list[v2_ind]
        newe=Edge(v1,v2,weight)
        self.edge_list.append(newe)
        edge_ind=len(self.edge_list)-1

        self.adjacent_to[v1_ind][v2_ind]=edge_ind
        self.adjacent_to[v2_ind][v1_ind]=edge_ind



    ##Function to draw a graph given the canvas, vertices and edges
    def draw_graph(self,canvas,vpsize,epsize):
        t=turtle.RawTurtle(canvas)
        t.hideturtle()
        t.speed(0)
        t.pensize(vpsize)
        t.penup()
        for v in self.vertex_list:
            t.color("Green")
            t.goto(v.xcoor,v.ycoor)
            t.dot()
            t.goto(v.xcoor,v.ycoor+15)
            t.color("Blue")
            t.write(v.label,font=("Arial", 13, "normal"),align="center")


        t.pensize(epsize)
        
        t.penup()
        for e in self.edge_list:
            t.color("Pink")
            t.goto(e.v1.xcoor,e.v1.ycoor)
            t.pendown()
            t.goto(e.v2.xcoor,e.v2.ycoor)
            t.penup()
            x_mid=(e.v1.xcoor+e.v2.xcoor)/2
            y_mid=(e.v1.ycoor+e.v2.ycoor)/2
            t.goto(x_mid,y_mid)
            t.color("Red")
            t.write(str(e.weight),font=("Arial", 13, "normal"),align="center")








    # A utility function to find the vertex with  
    # minimum distance value, from the set of vertices  
    # not yet included in shortest path tree 
    def minDistance(self, dist, sptSet): 
  
        # Initilaize minimum distance for next node 
        mind = math.inf 
  
        # Search not nearest vertex not in the  
        # shortest path tree 
        for v in range(len(self.vertex_list)): 
            if dist[v] < mind and sptSet[v] == False: 
                mind = dist[v] 
                min_index = v 
  
        return min_index 

# Funtion that implements Dijkstra's single source  
# shortest path algorithm for a graph represented  
# using adjacency matrix representation 
# Here srcv and destv are vertex indices in the vertex_list list
    def dijkstra(self,srcv,destv): 
        print("In dijkstra")
        print("Adjacency is")
        for i,v in enumerate(self.adjacent_to):
            print(i,"->",v)
  
        dist = [math.inf] * len(self.vertex_list)
        dist[srcv] = 0
        sptSet = [False] * len(self.vertex_list) 
        parent=[None]*len(self.vertex_list)
  
        for cout in range(len(self.vertex_list)): 
  
            # Pick the minimum distance vertex from  
            # the set of vertices not yet processed.  
            # u is always equal to src in first iteration 
            u = self.minDistance(dist, sptSet)
            print("NExt vertex chosen(index)=",u)

            #We do not need shortest_path to all vertices
            if u==destv:
                break
  
            # Put the minimum distance vertex in the  
            # shotest path tree 
            sptSet[u] = True


            # Update dist value of the adjacent vertices  
            # of the picked vertex only if the current  
            # distance is greater than new distance and 
            # the vertex in not in the shotest path tree 
            # Also record the parent vertex(to eventually find the path)

            for adjacentv in self.adjacent_to[u]:
                edge=self.edge_list[self.adjacent_to[u][adjacentv]]
                if sptSet[adjacentv]==False and dist[u]+edge.weight<dist[adjacentv]:
                        dist[adjacentv]=dist[u]+edge.weight
                        parent[adjacentv]=u




        # for v in range(self.V): 
        #     if self.graph[u][v] > 0 and sptSet[v] == False and \ 
        #     dist[v] > dist[u] + self.graph[u][v]: 
        #             dist[v] = dist[u] + self.graph[u][v] 

        ##Finding shortest path
        path=[destv]
        ind=destv
        print("Printing parent list")
        print(parent)
        while(ind!=srcv):
            print("Next index=",ind)
            ind=parent[ind]
            path.insert(0,ind)
        print("Path found",path)

        return(path)



class Visualisation():
    def __init__(self):
        self.root = tkinter.Tk()
        self.graph=Graph()
        

        self.menuframe=tkinter.Frame(master=self.root)
        self.menuframe.grid(row=0,column=0)

        self.menuoptionsframe=tkinter.Frame(master=self.root)
        self.menuoptionsframe.grid(row=1,column=0)

        self.canvasframe=tkinter.Frame(master=self.root,width=800,height=700)
        self.canvasframe.grid(row=2,column=0)

        self.createbutton=tkinter.Button(master=self.menuframe,text="Create Map",command=self.createmap)
        self.navbutton=tkinter.Button(master=self.menuframe,text="Navigate Map",command=self.navigatemap)
        self.createbutton.grid(row=0,column=0)
        self.navbutton.grid(row=0,column=1)

        self.createtoolbar=tkinter.Frame(master=self.menuoptionsframe)
        self.createtoolbar.grid(row=0,column=0)

        self.navigatetoolbar=tkinter.Frame(master=self.menuoptionsframe)
        self.navigatetoolbar.grid(row=0,column=0)

        self.canvas = tkinter.Canvas(master = self.canvasframe, width = 800, height = 600)
        self.canvas.place(width = 800, height = 600)#padx=2, pady=2, row=0, column=0)#rowspan=10, columnspan=10) # , sticky='nsew')

        
        

        

        

        # self.v_name=tkinter.StringVar()
        # self.v_name.trace("w",self.v_name_updated)
        # self.v_label=tkinter.Label(self.createtoolbar,text="Vertex Name:").grid(column=0,row=1)
        # self.v_entry=tkinter.Entry(self.createtoolbar,textvariable=self.v_name,state='disabled').grid(column=1,row=1)

        # self.e_weight=tkinter.StringVar()
        # self.e_weight.trace("w",self.e_weight_updated)
        # self.e_label=tkinter.Label(self.createtoolbar,text="Edge weight:").grid(column=2,row=1)
        # self.e_entry=tkinter.Entry(self.createtoolbar,textvariable=self.e_weight,state='disabled').grid(column=3,row=1)


        #draw = turtle.Turtle()
        self.draw = turtle.RawTurtle(self.canvas)
        self.draw.speed(0)
        self.vertex_pen_size=10
        self.edge_pen_size=2
        #self.defaultmap()
        self.root.mainloop()


    def defaultmap(self):
        # self.graph.add_vertex(-187.0,218.0,'a')
        # self.graph.add_vertex(-246.0,115.0,'b')
        # self.graph.add_vertex(229.0,132.0,'c')
        # self.graph.add_vertex(145.0,-53.0,'d')
        # self.graph.add_edge(0,1,118.7)
        # self.graph.add_edge(2,3,203.18)
        # self.graph.add_edge(3,1,425.56)
        # self.graph.add_edge(1,2,475.3)

        # #BIG TREE
        # self.graph.add_vertex(-32.0,262.0,'a')
        # self.graph.add_vertex(-235.0,184.0,'b')
        # self.graph.add_vertex(179.0,191.0,'c')
        # self.graph.add_vertex(-336.0,64.0,'d')
        # self.graph.add_vertex(-135.0,59.0,'e')
        # self.graph.add_vertex(85.0,65.0,'f')
        # self.graph.add_vertex(310.0,64.0,'g')
        # self.graph.add_vertex(-375.0,-74.0,'h')
        # self.graph.add_vertex(-302.0,-73.0,'i')
        # self.graph.add_vertex(-181.0,-65.0,'j')
        # self.graph.add_vertex(-96.0,-61.0,'k')
        # self.graph.add_vertex(52.0,-54.0,'l')
        # self.graph.add_vertex(118.0,-51.0,'m')
        # self.graph.add_vertex(269.0,-50.0,'n')
        # self.graph.add_vertex(353.0,-50.0,'o')

        # self.graph.add_edge(0,1,217.47)
        # self.graph.add_edge(0,2,222.63)
        # self.graph.add_edge(1,3,156.85)
        # self.graph.add_edge(1,4,160.08)
        # self.graph.add_edge(2,5,157.2)
        # self.graph.add_edge(2,6,182.46)
        # self.graph.add_edge(3,7,143.41)
        # self.graph.add_edge(3,8,141.16)
        # self.graph.add_edge(4,9,132.26)
        # self.graph.add_edge(4,10,126.18)
        # self.graph.add_edge(5,11,123.49)
        # self.graph.add_edge(5,12,120.6)
        # self.graph.add_edge(6,13,121.15)
        # self.graph.add_edge(6,14,121.84)
        # self.graph.add_edge(14,5,291.63)
        # self.graph.add_edge(13,4,218.49)
        # self.graph.add_edge(7,0,480.15)
        # self.graph.add_edge(8,2,548.69)

        ##BUTTERFLY
        # self.graph.add_vertex(-177.0,153.0,'a')
        # self.graph.add_vertex(-241.0,18.0,'b')
        # self.graph.add_vertex(97.0,134.0,'c')
        # self.graph.add_vertex(22.0,-41.0,'d')
        # self.graph.add_vertex(-66.0,52.0,'e')
        # self.graph.add_edge(0,1,149.4)
        # self.graph.add_edge(4,2,182.46)
        # self.graph.add_edge(2,3,190.39)
        # self.graph.add_edge(3,4,128.04)
        # self.graph.add_edge(4,0,150.07)
        # self.graph.add_edge(4,1,178.27)

        ##6-regular OCTAGON
        # self.graph.add_vertex(306.0,8.0,'a')
        # self.graph.add_vertex(-27.0,272.0,'b')
        # self.graph.add_vertex(-345.0,2.0,'c')
        # self.graph.add_vertex(-14.0,-255.0,'d')
        # self.graph.add_vertex(203.0,212.0,'e')
        # self.graph.add_vertex(-267.0,215.0,'f')
        # self.graph.add_vertex(-233.0,-164.0,'g')
        # self.graph.add_vertex(220.0,-167.0,'h')
        # self.graph.add_edge(0,4,228.53)
        # self.graph.add_edge(4,1,237.7)
        # self.graph.add_edge(1,5,246.68)
        # self.graph.add_edge(5,2,226.83)
        # self.graph.add_edge(2,6,200.25)
        # self.graph.add_edge(6,3,237.15)
        # self.graph.add_edge(3,7,250.0)
        # self.graph.add_edge(7,0,194.99)
        # self.graph.add_edge(0,1,424.95)
        # self.graph.add_edge(1,2,417.16)
        # self.graph.add_edge(2,3,419.06)
        # self.graph.add_edge(3,0,414.21)
        # self.graph.add_edge(4,5,470.01)
        # self.graph.add_edge(5,6,380.52)
        # self.graph.add_edge(6,7,453.01)
        # self.graph.add_edge(7,4,379.38)
        # self.graph.add_edge(0,5,609.24)
        # self.graph.add_edge(5,3,533.77)
        # self.graph.add_edge(3,4,514.95)
        # self.graph.add_edge(4,2,586.86)
        # self.graph.add_edge(2,7,589.73)
        # self.graph.add_edge(7,1,503.72)
        # self.graph.add_edge(1,6,482.22)
        # self.graph.add_edge(6,0,565.78)

        #RANDOM
        canvas_width=700
        canvas_height=500
        print("Input no. of vertices")
        v=int(input())
        print("Input no.of edges")
        e=int(input())
        edge_set=set()
        for i in range(v):
        	x=random.randint(0,canvas_width)
        	y=random.randint(0,canvas_height)
        	x=x-canvas_width//2
        	y=y-canvas_height//2
        	v_name="v"+str(i)
        	self.graph.add_vertex(x,y,v_name)

        j=0
        while(j<e):
        	ed=tuple(random.sample(range(0,v-1),2))
        	if ed not in edge_set:
        		edge_set.add(ed)
        		self.graph.add_edge(ed[0],ed[1],random.randint(1,100))
        		j+=1


        self.graph.draw_graph(self.canvas,self.vertex_pen_size,self.edge_pen_size)

    def createmap(self):
        self.navigatetoolbar.grid_forget()

        self.createtoolbar.grid(row=0,column=0)
        v_or_e=tkinter.IntVar()
        v_or_e.set(0)
        self.vertexbutton=tkinter.Radiobutton(master=self.createtoolbar,text="Vertex",variable=v_or_e,value=0,command=self.vertex_button_pressed)
        self.vertexbutton.grid(column=0,row=0,columnspan=1)
        self.somespace=tkinter.Label(self.createtoolbar,text="        ")
        self.somespace.grid(column=1,row=0)
        self.edgebutton=tkinter.Radiobutton(master=self.createtoolbar,text="Edge",variable=v_or_e,value=1,command=self.edge_button_pressed)
        self.edgebutton.grid(column=2,row=0,columnspan=1)
        self.somespace1=tkinter.Label(self.createtoolbar,text="        ")
        self.somespace1.grid(column=3,row=0)
        self.createtoolbar.lift()

    def navigatemap(self):
        pointer1=turtle.RawTurtle(self.canvas)
        pointer2=turtle.RawTurtle(self.canvas)
        pointer1.shape("circle")
        pointer1.shapesize(self.vertex_pen_size//10)
        pointer2.shape("circle")
        pointer1.shapesize(self.vertex_pen_size//10)
        pointer1.color("yellow")
        pointer2.color("yellow")
        pointer1.speed(0)
        pointer2.speed(0)
        pointer1.penup()
        pointer2.penup()
        self.createbutton.bind("<Button-1>",lambda ev:self.delete_turtles(pointer1,pointer2))

        pointer1.goto(self.graph.vertex_list[0].xcoor,self.graph.vertex_list[0].ycoor)
        pointer2.goto(self.graph.vertex_list[1].xcoor,self.graph.vertex_list[1].ycoor)
        
        self.createtoolbar.grid_forget()

        self.navigatetoolbar.grid(row=0,column=0)
        self.fromvertexlabel=tkinter.Label(self.navigatetoolbar,text="From Vertex")
        self.tovertexlabel=tkinter.Label(self.navigatetoolbar,text="To Vertex")
        self.fromvertexlabel.grid(row=0,column=0)
        self.tovertexlabel.grid(row=0,column=2)
        


        self.navigatetoolbar.lift()

        fromoptions=[v.label for v in self.graph.vertex_list]
        fromind=0
        fromv=tkinter.StringVar()
        fromv.set(fromoptions[fromind])
        def fromv_changed(*args):
            nonlocal fromind
            lab=fromv.get()
            fromind=fromoptions.index(lab)
            pointer1.goto(self.graph.vertex_list[fromind].xcoor,self.graph.vertex_list[fromind].ycoor)



        fromv.trace("w",fromv_changed)
        fromvertex_opmenu=tkinter.OptionMenu(self.navigatetoolbar,fromv,*fromoptions)

        tooptions=[v.label for v in self.graph.vertex_list]
        toind=1
        tov=tkinter.StringVar()
        tov.set(tooptions[toind])
        def tov_changed(*args):
            nonlocal toind
            lab=tov.get()
            toind=tooptions.index(lab)
            pointer2.goto(self.graph.vertex_list[toind].xcoor,self.graph.vertex_list[toind].ycoor)
        tov.trace("w",tov_changed)
        tovertex_opmenu=tkinter.OptionMenu(self.navigatetoolbar,tov,*tooptions)

        fromvertex_opmenu.grid(row=0,column=1)
        tovertex_opmenu.grid(row=0,column=3)

        self.shortestpathbutton=tkinter.Button(self.navigatetoolbar,text="Find Shortest Path",command=lambda :self.find_shortest_path(fromind,toind))
        self.shortestpathbutton.grid(row=1,column=0)


        print(self.graph)

    def vertex_button_pressed(self):
        self.canvas.bind("<Button-1>",self.makevertex)
   
    def makevertex(self,event):
        #Draw a dot on the canvas
        t=self.draw
        print("Making Vertex")
        t.penup()
        org=t.pensize()
        t.pensize(self.vertex_pen_size)
        x=self.canvas.canvasx(event.x)
        y=-self.canvas.canvasy(event.y)
        t.goto(x,y)
        t.color("Green")
        t.dot()
        t.pensize(org)

        #Ask user to input name of vertex
        writer = turtle.RawTurtle(self.canvas)
        writer.hideturtle()
        writer.color("Blue")
        v_name=tkinter.StringVar()

        def v_name_updated(self,a,b):
            nonlocal writer
            writer.clear()
            writer.penup()
            writer.goto(x,y+15)
            name=v_name.get()
            writer.write(name,font=("Arial", 13, "normal"),align="center")
            

        def save_and_destroy(ev):
            nonlocal writer
            print("In save_and_destroy")
            vertex_name=v_name.get()
            self.graph.add_vertex(x,y,vertex_name,self.vertex_pen_size)
            v_label.destroy()
            v_entry.destroy()
            writer.hideturtle()
            del(writer)
        
        
        v_name.trace("w",v_name_updated)
        v_label=tkinter.Label(self.canvasframe,text="Vertex Name:")
        v_label.place(x=event.x,y=event.y)
        v_entry=tkinter.Entry(self.canvasframe,textvariable=v_name)
        v_entry.place(x=event.x+100,y=event.y)
        v_entry.focus_set()
        #print("Hi1")
        v_entry.bind("<Return>",save_and_destroy)
        #print("Hi2")
        


        

    def edge_button_pressed(self):
        border=2
        tver1=turtle.RawTurtle(self.canvas)
        tver2=turtle.RawTurtle(self.canvas)
        tver1.shape("circle")
        tver1.shapesize(self.vertex_pen_size//10)
        tver2.shape("circle")
        tver1.shapesize(self.vertex_pen_size//10)
        tver1.hideturtle()
        tver2.hideturtle()
        tver1.color("yellow")
        tver2.color("yellow")
        tver1.speed(0)
        tver2.speed(0)
        vertex1ind=[]
        vertex2ind=[]
        self.canvas.bind("<Button-1>",lambda ev:self.makeedge(ev,tver1,tver2,vertex1ind,vertex2ind))
        self.vertexbutton.bind("<Button-1>",lambda ev:self.delete_turtles(tver1,tver2))
        
        edge_drawer=turtle.RawTurtle(self.canvas)
        edge_drawer.hideturtle()

    def makeedge(self,event,tver1,tver2,vertex1ind,vertex2ind):

        x=self.canvas.canvasx(event.x)
        y=-self.canvas.canvasy(event.y)
        def no_vertex_selected(tver,x,y):
            tnew=turtle.RawTurtle(self.canvas)
            tnew.hideturtle()
            tnew.penup()
            tnew.goto(x,y)
            tnew.write("No vertex selected",font=("Arial", 13, "normal"),align="center")
            time.sleep(1)
            tnew.clear()
            del(tnew)
        #Case 1: First vertex selection
        if tver1.isvisible()==False:
            vertexind,x,y=self.get_vertex_clicked(x,y)
            if vertexind==None:
                no_vertex_selected(tver1,x,y)
            else:
                #tver1.clear()
                vertex1ind.append(vertexind)
                tver1.penup()
                tver1.goto(x,y)
                tver1.showturtle()

        elif tver2.isvisible()==False:
            vertexind,x,y=self.get_vertex_clicked(x,y)
            if vertexind==None:
                no_vertex_selected(tver2,x,y)
            else:
                #tver2.clear()
                vertex2ind.append(vertexind)
                tver2.penup()
                tver2.goto(x,y)
                tver2.showturtle()
                
                v1pos=tver1.pos()
                v2pos=tver2.pos()
                distance=round(math.sqrt((v1pos[0]-v2pos[0])**2+(v1pos[1]-v2pos[1])**2),2)

                tver1.hideturtle()
                tver1.pendown()
                tver1.pensize(self.edge_pen_size)
                tver1.color("pink")
                tver1.goto(x,y)
                tver1.color("yellow")
                tver2.hideturtle()

                #Ask user to input weight of edge
                x=(v1pos[0]+v2pos[0])/2
                y=(v1pos[1]+v2pos[1])/2
                writer = turtle.RawTurtle(self.canvas)
                writer.hideturtle()
                writer.color("Red")
                e_weight=tkinter.StringVar()

                def e_weight_updated(self,a,b):
                    nonlocal writer
                    writer.clear()
                    writer.penup()
                    print("Writer xy",x,y)
                    writer.goto(x,y+3)
                    name=e_weight.get()
                    writer.write(name,font=("Arial", 13, "normal"),align="center")
                    

                def save_and_destroy(ev):
                    nonlocal writer,vertex1ind,vertex2ind
                    print("In save_and_destroy")
                    if e_weight.get()=="":
                        e_weight.set(str(distance))
                        e_weight_updated(None,None,None)

                    edge_weight=e_weight.get()

                    print(vertex1ind,vertex2ind,float(edge_weight))
                    self.graph.add_edge(vertex1ind[0],vertex2ind[0],float(edge_weight))
                    e_label.destroy()
                    e_entry.destroy()
                    del(writer)
                    tver1=None
                    tver2=None
                    vertex1ind.pop()
                    vertex2ind.pop()
                
                
                e_weight.trace("w",e_weight_updated)
                e_label=tkinter.Label(self.canvasframe,text="edge Weight:\n(default="+str(distance)+")")

                x0 = self.canvas.canvasx(0)
                y0 = self.canvas.canvasy(0)

                # given a canvas coordinate cx/cy, convert it to window coordinates:
                lx = x-x0
                ly =-( y+y0)

                print("Label xy",lx,ly)
                e_label.place(x=lx,y=ly)
                e_entry=tkinter.Entry(self.canvasframe,textvariable=e_weight)
                e_entry.place(x=lx+100,y=ly)
                e_entry.focus_set()
                #print("Hi1")
                e_entry.bind("<Return>",save_and_destroy)
                print("Vertex1ind=",vertex1ind)
                #print("Hi2")
                


        else:
            print("ERROR in makeedge function")





        
    def delete_turtles(self,*turts):
        for t in turts:
            t.hideturtle()
            del(t)

    def clear_del_turtles(self,*turts):
        for t in turts:
            t.clear()
            del(t)

    def get_vertex_clicked(self,x,y):

        for i,v in enumerate(self.graph.vertex_list):
            dis=math.sqrt((x-v.xcoor)**2+(y-v.ycoor)**2)
            if dis<self.vertex_pen_size:
                return(i,v.xcoor,v.ycoor)
        return(None,x,y)

    def find_shortest_path(self,fromind,toind):
        print("Shortest distance from",self.graph.vertex_list[fromind].label,"to",self.graph.vertex_list[toind].label)
        path_list=self.graph.dijkstra(fromind,toind)
        self.show_shortest_path(path_list)
        for ind in path_list:
            print(self.graph.vertex_list[ind].label,"->",end=" ")

        print()

    def show_shortest_path(self,path_list):
        
        path_turtle=turtle.RawTurtle(self.canvas)
        path_turtle.hideturtle()
        path_turtle.penup()
        path_turtle.goto(self.graph.vertex_list[path_list[0]].xcoor,self.graph.vertex_list[path_list[0]].ycoor)
        path_turtle.pendown()
        path_turtle.color("lime")
        path_turtle.pensize(2)
        self.shortestpathbutton.bind("<Button-1>",lambda ev:self.clear_del_turtles(path_turtle))
        self.createbutton.bind("<Button-1>",lambda ev:self.clear_del_turtles(path_turtle))
        for ind in path_list[1:]:
            x=self.graph.vertex_list[ind].xcoor
            y=self.graph.vertex_list[ind].ycoor
            path_turtle.goto(x,y)


# Python program for Dijkstra's single  
# source shortest path algorithm. The program is  
# for adjacency matrix representation of the graph 
  
# Library for INT_MAX 
Visualisation()

    
  
