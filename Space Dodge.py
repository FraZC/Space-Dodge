from tkinter import *
from random import randint
import random
import os
import time
import winsound



#Global data:        
highest = 0
points = ""
name = ""
#Program initiator#################################################################################
class Window:
    def __init__(self, master):
#Creates a new text file or search for the highest number of the high score table.
        global highest
        file=open("High score table.txt", "a+")
        file.close()
        file = open("High score table.txt", "r")
        persons = file.readlines()
#Immediately opens the menu window if there's no text.
        if persons ==[]:
            file.close()
            self.frame(Window1)
#Opens the menu window after get the highest score.
        else:
            self.list_points(persons, 0)
            highest = max(self.h)
            file.close()
            self.frame(Window1)
#Reads the info in the .txt file.             
    def list_points(self, persons, val):
        if val <len(persons):
            if persons[val]!= "":
                self.remove_str(persons[val])
                self.list_points(persons, val +1)
                
#Removes the string data of the text a creates a list of all the scores.
    def remove_str(self, string):        
        try:
            p=int(string[0])
            if isinstance (p, int):
                try:
                    self.h = [int(string[:-1])]+self.h
                except:
                    self.h = [int(string[:-1])]
        except: 
            self.remove_str(string[1:])
            
#This just open the main window.
    def frame(self, windowP):
        windowP(self)   
        
#Opens the sended window.
    def switch_frame(self, windowP):
        global name
        self.true = True
        self.all_string(name)
#It just works if the name meets all the requirements or if the sended window is not the game window.
        if (name != "" and len(name)<10 and self.true==True )or str(windowP) != "<class '__main__.Window4'>": 
            windowP(self)
            
#Checks if the inserted name have just string values
    def all_string(self, name):
        if name !="":
            try :
                int(name[0])
                self.true = False
            except:
                return self.all_string( name[1:])
        elif name=="":
            self.true = True
            
#Menu Window#################################################################################
class Window1:
    def __init__ (self, master):
        #Creates the canvas'''
        self.canvas = Canvas(width=800, height=350, highlightthickness=0, relief='ridge', bg='black')
        self.canvas.place(x=0,y=0)       
        #Title_Label'''
        self.presetation= Label(self.canvas, text= "Meteor dodge", font=("Courier New", 30, "bold"), fg="lawngreen", bg='black')
        self.presetation.place(x=225, y=40, width=350, height=40)       
        #Instert_name_Label and Instert_name_Entry''''''
        self.label_name = Label (self.canvas, text="Nombre:", font=("Courier New", 12), fg="lawngreen", bg='black')
        self.label_name.place(x=300, y=120, width=100, height=30)
        self.write_name = Entry(self.canvas)
        self.write_name.place(x=400, y=120, width=100, height=30)
        #Instructions window_Button'''
        self.button_inst = Button(self.canvas, text = "Instrucciones",font=("Courier New", 12),command =lambda: [ master.switch_frame(Window2)], bg="aquamarine4")
        self.button_inst.place(x=125,y=200, width=150,height=30)
        #Credits window_Button'''
        self.button_credits = Button(self.canvas, text = "Créditos",font=("Courier New", 12),command =lambda: [ master.switch_frame(Window5)], bg="aquamarine4")
        self.button_credits.place(x=660,y=300, width=110,height=30)
        #High Score window_Button'''
        self.button_highscore = Button(self.canvas, text = "Puntajes más altos",font=("Courier New", 10),command =lambda: [ master.switch_frame(Window3)], bg="aquamarine4")
        self.button_highscore.place(x=525,y=200, width=150,height=30)
        #Game_Button'''    
        self.button_game = Button(self.canvas, text = "Start game",font=("Courier New", 12),command =lambda: [self.all_ready(), self.del_win1(), master.switch_frame(Window4)], bg="aquamarine4")
        self.button_game.place(x=325,y=200, width=150,height=30)
        #Call al the starts
        self.meteor()
        #Plays the music
        winsound.PlaySound(os.path.join('Sounds', 'Prórroga de Tiempo C.wav'), winsound.SND_LOOP|winsound.SND_ASYNC | winsound.SND_ALIAS )


#Search for mistakes in the name entry        
    def all_ready(self):
        global name
        #Get the name
        name = self.write_name.get()
        #Define a boolean value, use for the all_string function
        self.true = True
        #Call the all_string function
        self.all_string(name)
        #If there is no name (all this labels have try/except because it erase the before name incorect information label)
        if name == "" and self.true == True:
            #Erase the before name incorect information label and calls the new one
            try:
                self.name.destroy()
                self.name= Label(self.canvas, text= "¡Introduce tu nombre primero!", font=("Courier New", 15, "bold"), fg="lawngreen", bg='black')
                self.name.place(x=225, y=80, width=350, height=23)
            #Call the name incorect information label
            except:
                self.name= Label(self.canvas, text= "¡Introduce tu nombre primero!", font=("Courier New", 15, "bold"), fg="lawngreen", bg='black')
                self.name.place(x=225, y=80, width=350, height=23)
        #If the name have more than nine string values
        elif len(name)>9 and self.true == True:
            #Erase the before name incorect information label and calls the new one
            try:
                self.name.destroy()
                self.name= Label(self.canvas, text= "¡Excede la cantidad de caracteres!", font=("Courier New", 15, "bold"), fg="lawngreen", bg='black')
                self.name.place(x=197, y=80, width=405, height=23)
            #Call the name incorect information label
            except:
                self.name= Label(self.canvas, text= "¡Excede la cantidad de caracteres!", font=("Courier New", 15, "bold"), fg="lawngreen", bg='black')
                self.name.place(x=197, y=80, width=405, height=23)
        #If the name have non string values
        elif self.true == False:
            #Erase the before name incorect information label and calls the new one
            try:
                self.name.destroy()
                self.name= Label(self.canvas, text= "¡Solo se permiten letras!", font=("Courier New", 15, "bold"), fg="lawngreen", bg='black')
                self.name.place(x=225, y=80, width=350, height=23)
            #Call the name incorect information label
            except:
                self.name= Label(self.canvas, text= "¡Solo se permiten letras!", font=("Courier New", 15, "bold"), fg="lawngreen", bg='black')
                self.name.place(x=225, y=80, width=350, height=23)
            
#Checks if the inserted name have just string values            
    def all_string(self, name):
        if name !="":
            try :
                int(name[0])
                self.true = False
            except:
                return self.all_string( name[1:])
        elif name=="":
            self.true = True
        
#"Close" the menu window        
    def del_win1(self):
        global name
        #Chek if all the name parameters are ok
        if name != "" and len(name)<9 and self.true==True:
            #Plays the music
            winsound.PlaySound(os.path.join('Sounds', '01 A Night Of Dizzy Spells.wav'), winsound.SND_LOOP|winsound.SND_ASYNC | winsound.SND_ALIAS )
            #Erase  and stop moving the stars for make the game run better
            self.canvas.delete("B")
            self.canvas.delete("M")
            self.canvas.delete("S")
            self.run= False
        
        

#Crate all the stars    
    def meteor(self):
        self.run = True  
########Big asteroids
        y= 263 
        x= 77
        points= [x,y+10,x+20,y+10,x+10,y+25]
        points2= [x,y+20,x+20,y+20,x+10,y+5]
        self.Btrian5 = self.canvas.create_polygon(points,width=2,outline="gold", fill="darkslategray", tags="B")	
        self.Btrian6 = self.canvas.create_polygon(points2,width=2,outline="darkslategray3", fill="darkslategray", tags="B")
        y= 69 
        x= 87
        points= [x,y+10,x+20,y+10,x+10,y+25]
        points2= [x,y+20,x+20,y+20,x+10,y+5]
        self.Btrian3 = self.canvas.create_polygon(points,width=2,outline="gold", fill="darkslategray", tags="B")	
        self.Btrian4 = self.canvas.create_polygon(points2,width=2,outline="darkslategray3", fill="darkslategray", tags="B")
        y=(334)
        x=(142)
        points= [x,y+10,x+20,y+10,x+10,y+25]
        points2= [x,y+20,x+20,y+20,x+10,y+5]
        self.Btrian17 = self.canvas.create_polygon(points,width=2,outline="gold", fill="darkslategray", tags="B")	
        self.Btrian18 = self.canvas.create_polygon(points2,width=2,outline="darkslategray3", fill="darkslategray", tags="B")
        y= 60 
        x= 250
        points= [x,y+10,x+20,y+10,x+10,y+25]
        points2= [x,y+20,x+20,y+20,x+10,y+5]
        self.Btrian7 = self.canvas.create_polygon(points,width=2,outline="gold", fill="darkslategray", tags="B")	
        self.Btrian8 = self.canvas.create_polygon(points2,width=2,outline="darkslategray3", fill="darkslategray", tags="B")
        y= 237 
        x= 374
        points= [x,y+10,x+20,y+10,x+10,y+25]
        points2= [x,y+20,x+20,y+20,x+10,y+5]
        self.Btrian15 = self.canvas.create_polygon(points,width=2,outline="gold", fill="darkslategray", tags="B")	
        self.Btrian16 = self.canvas.create_polygon(points2,width=2,outline="darkslategray3", fill="darkslategray", tags="B")
        y= 115 
        x= 384
        points= [x,y+10,x+20,y+10,x+10,y+25]
        points2= [x,y+20,x+20,y+20,x+10,y+5]
        self.Btrian11 = self.canvas.create_polygon(points,width=2,outline="gold", fill="darkslategray", tags="B")	
        self.Btrian12 = self.canvas.create_polygon(points2,width=2,outline="darkslategray3", fill="darkslategray", tags="B")
        y= 215 
        x= 556
        points= [x,y+10,x+20,y+10,x+10,y+25]
        points2= [x,y+20,x+20,y+20,x+10,y+5]
        self.Btrian19 = self.canvas.create_polygon(points,width=2,outline="gold", fill="darkslategray", tags="B")	
        self.Btrian20 = self.canvas.create_polygon(points2,width=2,outline="darkslategray3", fill="darkslategray", tags="B")
        y= 192 
        x= 667
        points= [x,y+10,x+20,y+10,x+10,y+25]
        points2= [x,y+20,x+20,y+20,x+10,y+5]
        self.Btrian9 = self.canvas.create_polygon(points,width=2,outline="gold", fill="darkslategray", tags="B")	
        self.Btrian10 = self.canvas.create_polygon(points2,width=2,outline="darkslategray3", fill="darkslategray", tags="B")
        y= 270 
        x= 787
        points= [x,y+10,x+20,y+10,x+10,y+25]
        points2= [x,y+20,x+20,y+20,x+10,y+5]
        self.Btrian13 = self.canvas.create_polygon(points,width=2,outline="gold", fill="darkslategray", tags="B")	
        self.Btrian14 = self.canvas.create_polygon(points2,width=2,outline="darkslategray3", fill="darkslategray", tags="B")
        points= [790,110,810,110,800,125]
        points2= [790,120,810,120,800,105]
        self.Btrian1 = self.canvas.create_polygon(points,width=2,outline="gold", fill="darkslategray", tags="B")	
        self.Btrian2 = self.canvas.create_polygon(points2,width=2,outline="darkslategray3", fill="darkslategray", tags="B")

########Small asteroids
        y= 15 
        x= 58
        points= [x,y+5,x+10,y+5,x+5,y+12.5]
        points2= [x,y+10,x+10,y+10,x+5,y+2.5]
        self.Strian3 = self.canvas.create_polygon(points,width=2,outline="gold", fill="darkslategray", tags="S")	
        self.Strian4 = self.canvas.create_polygon(points2,width=2,outline="darkslategray3", fill="darkslategray", tags="S")
        y= 141 
        x= 59
        points= [x,y+5,x+10,y+5,x+5,y+12.5]
        points2= [x,y+10,x+10,y+10,x+5,y+2.5]
        self.Strian13 = self.canvas.create_polygon(points,width=2,outline="gold", fill="darkslategray", tags="S")	
        self.Strian14 = self.canvas.create_polygon(points2,width=2,outline="darkslategray3", fill="darkslategray", tags="S")
        y= 284 
        x= 229
        points= [x,y+5,x+10,y+5,x+5,y+12.5]
        points2= [x,y+10,x+10,y+10,x+5,y+2.5]
        self.Strian17 = self.canvas.create_polygon(points,width=2,outline="gold", fill="darkslategray", tags="S")	
        self.Strian18 = self.canvas.create_polygon(points2,width=2,outline="darkslategray3", fill="darkslategray", tags="S")
        y= 330 
        x= 271
        points= [x,y+5,x+10,y+5,x+5,y+12.5]
        points2= [x,y+10,x+10,y+10,x+5,y+2.5]
        self.Strian5 = self.canvas.create_polygon(points,width=2,outline="gold", fill="darkslategray", tags="S")	
        self.Strian6 = self.canvas.create_polygon(points2,width=2,outline="darkslategray3", fill="darkslategray", tags="S")
        y= 257 
        x= 354
        points= [x,y+5,x+10,y+5,x+5,y+12.5]
        points2= [x,y+10,x+10,y+10,x+5,y+2.5]
        self.Strian11 = self.canvas.create_polygon(points,width=2,outline="gold", fill="darkslategray", tags="S")	
        self.Strian12 = self.canvas.create_polygon(points2,width=2,outline="darkslategray3", fill="darkslategray", tags="S")
        y= 304 
        x= 429
        points= [x,y+5,x+10,y+5,x+5,y+12.5]
        points2= [x,y+10,x+10,y+10,x+5,y+2.5]
        self.Strian9 = self.canvas.create_polygon(points,width=2,outline="gold", fill="darkslategray", tags="S")	
        self.Strian10 = self.canvas.create_polygon(points2,width=2,outline="darkslategray3", fill="darkslategray", tags="S")
        y= 127 
        x= 573
        points= [x,y+5,x+10,y+5,x+5,y+12.5]
        points2= [x,y+10,x+10,y+10,x+5,y+2.5]
        self.Strian1 = self.canvas.create_polygon(points,width=2,outline="gold", fill="darkslategray", tags="S")	
        self.Strian2 = self.canvas.create_polygon(points2,width=2,outline="darkslategray3", fill="darkslategray", tags="S")
        y= 185 
        x= 681
        points= [x,y+5,x+10,y+5,x+5,y+12.5]
        points2= [x,y+10,x+10,y+10,x+5,y+2.5]
        self.Strian15 = self.canvas.create_polygon(points,width=2,outline="gold", fill="darkslategray", tags="S")	
        self.Strian16 = self.canvas.create_polygon(points2,width=2,outline="darkslategray3", fill="darkslategray", tags="S")
        y= 266 
        x= 715
        points= [x,y+5,x+10,y+5,x+5,y+12.5]
        points2= [x,y+10,x+10,y+10,x+5,y+2.5]
        self.Strian19 = self.canvas.create_polygon(points,width=2,outline="gold", fill="darkslategray", tags="S")	
        self.Strian20 = self.canvas.create_polygon(points2,width=2,outline="darkslategray3", fill="darkslategray", tags="S")
        y= 80 
        x= 764
        points= [x,y+5,x+10,y+5,x+5,y+12.5]
        points2= [x,y+10,x+10,y+10,x+5,y+2.5]
        self.Strian7 = self.canvas.create_polygon(points,width=2,outline="gold", fill="darkslategray", tags="S")	
        self.Strian8 = self.canvas.create_polygon(points2,width=2,outline="darkslategray3", fill="darkslategray", tags="S")
        
########Medium asteroids       
        y= 91 
        x= 8
        points= [x,y+10*0.7,x+20*0.7,y+10*0.7,x+10*0.7,y+25*0.7]
        points2= [x,y+20*0.7,x+20*0.7,y+20*0.7,x+10*0.7,y+5*0.7]
        self.Mtrian1 = self.canvas.create_polygon(points,width=2,outline="gold", fill="darkslategray", tags="M")	
        self.Mtrian2 = self.canvas.create_polygon(points2,width=2,outline="darkslategray3", fill="darkslategray", tags="M")
        y= 64 
        x= 26
        points= [x,y+10*0.7,x+20*0.7,y+10*0.7,x+10*0.7,y+25*0.7]
        points2= [x,y+20*0.7,x+20*0.7,y+20*0.7,x+10*0.7,y+5*0.7]
        self.Mtrian25 = self.canvas.create_polygon(points,width=2,outline="gold", fill="darkslategray", tags="M")	
        self.Mtrian26 = self.canvas.create_polygon(points2,width=2,outline="darkslategray3", fill="darkslategray",  tags="M")
        y= 164 
        x= 122
        points= [x,y+10*0.7,x+20*0.7,y+10*0.7,x+10*0.7,y+25*0.7]
        points2= [x,y+20*0.7,x+20*0.7,y+20*0.7,x+10*0.7,y+5*0.7]
        self.Mtrian13 = self.canvas.create_polygon(points,width=2,outline="gold", fill="darkslategray", tags="M")	
        self.Mtrian14 = self.canvas.create_polygon(points2,width=2,outline="darkslategray3", fill="darkslategray", tags="M")
        y= 171 
        x= 180
        points= [x,y+10*0.7,x+20*0.7,y+10*0.7,x+10*0.7,y+25*0.7]
        points2= [x,y+20*0.7,x+20*0.7,y+20*0.7,x+10*0.7,y+5*0.7]
        self.Mtrian23 = self.canvas.create_polygon(points,width=2,outline="gold", fill="darkslategray", tags="M")	
        self.Mtrian24 = self.canvas.create_polygon(points2,width=2,outline="darkslategray3", fill="darkslategray", tags="M")
        y= 39 
        x= 190
        points= [x,y+10*0.7,x+20*0.7,y+10*0.7,x+10*0.7,y+25*0.7]
        points2= [x,y+20*0.7,x+20*0.7,y+20*0.7,x+10*0.7,y+5*0.7]
        self.Mtrian11 = self.canvas.create_polygon(points,width=2,outline="gold", fill="darkslategray", tags="M")	
        self.Mtrian12 = self.canvas.create_polygon(points2,width=2,outline="darkslategray3", fill="darkslategray", tags="M")
        y= 105 
        x= 218
        points= [x,y+10*0.7,x+20*0.7,y+10*0.7,x+10*0.7,y+25*0.7]
        points2= [x,y+20*0.7,x+20*0.7,y+20*0.7,x+10*0.7,y+5*0.7]
        self.Mtrian27 = self.canvas.create_polygon(points,width=2,outline="gold", fill="darkslategray", tags="M")
        self.Mtrian28 = self.canvas.create_polygon(points2,width=2,outline="darkslategray3", fill="darkslategray", tags="M")
        y= 204 
        x= 298
        points= [x,y+10*0.7,x+20*0.7,y+10*0.7,x+10*0.7,y+25*0.7]
        points2= [x,y+20*0.7,x+20*0.7,y+20*0.7,x+10*0.7,y+5*0.7]
        self.Mtrian9 = self.canvas.create_polygon(points,width=2,outline="gold", fill="darkslategray", tags="M")	
        self.Mtrian10 = self.canvas.create_polygon(points2,width=2,outline="darkslategray3", fill="darkslategray", tags="M")
        y= 127 
        x= 352
        points= [x,y+10*0.7,x+20*0.7,y+10*0.7,x+10*0.7,y+25*0.7]
        points2= [x,y+20*0.7,x+20*0.7,y+20*0.7,x+10*0.7,y+5*0.7]
        self.Mtrian7 = self.canvas.create_polygon(points,width=2,outline="gold", fill="darkslategray", tags="M")	
        self.Mtrian8 = self.canvas.create_polygon(points2,width=2,outline="darkslategray3", fill="darkslategray", tags="M")
        y= 276 
        x= 328
        points= [x,y+10*0.7,x+20*0.7,y+10*0.7,x+10*0.7,y+25*0.7]
        points2= [x,y+20*0.7,x+20*0.7,y+20*0.7,x+10*0.7,y+5*0.7]
        self.Mtrian17 = self.canvas.create_polygon(points,width=2,outline="gold", fill="darkslategray", tags="M")	
        self.Mtrian18 = self.canvas.create_polygon(points2,width=2,outline="darkslategray3", fill="darkslategray", tags="M")
        y= 176
        x= 449
        points= [x,y+10*0.7,x+20*0.7,y+10*0.7,x+10*0.7,y+25*0.7]
        points2= [x,y+20*0.7,x+20*0.7,y+20*0.7,x+10*0.7,y+5*0.7]
        self.Mtrian5 = self.canvas.create_polygon(points,width=2,outline="gold", fill="darkslategray", tags="M")	
        self.Mtrian6 = self.canvas.create_polygon(points2,width=2,outline="darkslategray3", fill="darkslategray", tags="M")
        y= 41 
        x= 497
        points= [x,y+10*0.7,x+20*0.7,y+10*0.7,x+10*0.7,y+25*0.7]
        points2= [x,y+20*0.7,x+20*0.7,y+20*0.7,x+10*0.7,y+5*0.7]
        self.Mtrian15 = self.canvas.create_polygon(points,width=2,outline="gold", fill="darkslategray", tags="M")	
        self.Mtrian16 = self.canvas.create_polygon(points2,width=2,outline="darkslategray3", fill="darkslategray", tags="M")
        y= 67 
        x= 644
        points= [x,y+10*0.7,x+20*0.7,y+10*0.7,x+10*0.7,y+25*0.7]
        points2= [x,y+20*0.7,x+20*0.7,y+20*0.7,x+10*0.7,y+5*0.7]
        self.Mtrian3 = self.canvas.create_polygon(points,width=2,outline="gold", fill="darkslategray", tags="M")	
        self.Mtrian4 = self.canvas.create_polygon(points2,width=2,outline="darkslategray3", fill="darkslategray", tags="M")
        y= 229 
        x= 710
        points= [x,y+10*0.7,x+20*0.7,y+10*0.7,x+10*0.7,y+25*0.7]
        points2= [x,y+20*0.7,x+20*0.7,y+20*0.7,x+10*0.7,y+5*0.7]
        self.Mtrian19 = self.canvas.create_polygon(points,width=2,outline="gold", fill="darkslategray", tags="M")	
        self.Mtrian20 = self.canvas.create_polygon(points2,width=2,outline="darkslategray3", fill="darkslategray", tags="M")
        y= 13 
        x= 786
        points= [x,y+10*0.7,x+20*0.7,y+10*0.7,x+10*0.7,y+25*0.7]
        points2= [x,y+20*0.7,x+20*0.7,y+20*0.7,x+10*0.7,y+5*0.7]
        self.Mtrian21 = self.canvas.create_polygon(points,width=2,outline="gold", fill="darkslategray", tags="M")	
        self.Mtrian22 = self.canvas.create_polygon(points2,width=2,outline="darkslategray3", fill="darkslategray", tags="M")
        
        #Especify the ID of the first object on all the stars
        self.posB=1
        self.posS=21
        self.posM=41
        #Call the moving stars functions
        self.meteors_loopM()
        self.meteors_loopS()
        self.meteors_loopB()
#Move all the big stars
    def movement3(self):
        #Move all the objects taged with "B" 
        self.canvas.move("B", -1, 0)
        #If some Big Star gets to the limit of the window, moves it into the other right limit.
        pos3 = self.canvas.coords(self.posB)
        if pos3[0]<=-10:
            self.canvas.move(self.posB, 790, 0)
            self.canvas.move(self.posB+1, 790, 0)
            #Reset the ID value when a Big Star toches the left canvas limit.
            if self.posB>18:
                self.posB= self.posB+-18
            else:
                self.posB= self.posB+2
#A loop to move the Big Stars            
    def meteors_loopB(self):
        if self.run == True:
            self.movement3()
            self.canvas.after(10, self.meteors_loopB)
#Move all the medium size stars
    def movement1(self):
        #Move all the objects taged with "M" 
        self.canvas.move("M", -1.8, 0)
        pos1 = self.canvas.coords(self.posM)
        #If some Medium Star gets to the limit of the window, moves it into the other right limit.
        if pos1[0]<=-10:
            self.canvas.move(self.posM, 790, 0)
            self.canvas.move(self.posM+1, 790, 0)
            #Reset the ID value when a Medium Star toches the left canvas limit.
            if self.posM>66:
                self.posM= self.posM+-26
            else:
                self.posM= self.posM+2
#A loop to move the Medium Stars
    def meteors_loopM(self):
        if self.run == True:
            self.movement1()
            self.canvas.after(10, self.meteors_loopM)
#Move all the small  stars        
    def movement2(self):
        #Move all the objects taged with "S" 
        self.canvas.move("S", -2.5, 0)
        pos2 = self.canvas.coords(self.posS)
        #If some Medium Star gets to the limit of the window, moves it into the other right limit.
        if pos2[0]<=-10:
            self.canvas.move(self.posS, 790, 0)
            self.canvas.move(self.posS+1, 790, 0)
            #Reset the ID value when a Medium Star toches the left canvas limit.
            if self.posS>38:
                    self.posS= self.posS+-18
            else:
                    self.posS= self.posS+2
#A loop to move the Small Stars
    def meteors_loopS(self):
        if self.run == True:
            self.movement2()
            self.canvas.after(10, self.meteors_loopS)

    
#Instructions Window#################################################################################    
class Window2:

    def __init__(self, master):
        #Creates a Frame
        self.frame = Frame(width=800,height=175)
        self.frame.place(x=0,y=174)
        #Creates a Canvas in the frame
        can = Canvas(self.frame, width = 800, height = 175, scrollregion= (0, 0 , 500, 500), highlightthickness=0)
        can.pack(side=LEFT,expand=True,fill=BOTH)
        #Creates a scrollbar in the frame
        vbar=Scrollbar(self.frame,orient=VERTICAL)
        vbar.place(x=784, y=0, height=174)
        vbar.config(command=can.yview)
        can.config(width=800,height=175)
        can.config( yscrollcommand=vbar.set)
        #Creates a Frame in the Canvas to move
        scrollable_frame = Frame(can, width = 800, height = 500,  bg="black")
        can.create_window((0, 0), window=scrollable_frame, anchor="nw")
        #Label for instrucctions1
        introduction = "¡Esquiba los obstaculos y ayuda a Doge a rescatar a sus anmiwos \n de la aterrible destrucción de su su nave modriza!"
        self.inst1= Label(scrollable_frame, text= introduction, font=("Courier New", 15, "bold"), fg="lavender", bg='black', justify=CENTER)
        self.inst1.place(x=0, y=40, width=800, height=40)
        #Label for instrucctions2
        instructions = '''Intenta rescatar la mayor cantidad de Doges espaciales, pero cuidado en \ntu misión; te encontraras con diferentes restos de la exploción de
la nave modriza los cuales te quitaran vida si llegan a chocar con el \ncentro de tu nave espacial.\nUna vez pierdas tres vidas es Game Over\n
-Los objetos turquesas son los más comunes y \nrestan una vida\n\n
-Los objetos rojos te seguirán cuando estén cerca de tí, \npero igual restan una vida\n\n
-Los objetos azul oscuro restan dos vidas\n\n
-Rescatar un Doge espacial suma 500 puntos!!!'''
        self.inst1= Label(scrollable_frame, text= instructions, font=("Courier New", 12, "bold"), fg="lavender", bg='black', justify=LEFT)
        self.inst1.place(x=10, y=100, width=800,)
        #Call and put all the objects to ilustrate
        picture1 = (PhotoImage(file= os.path.join('photos', "Waste1.png"))).subsample(7,7)
        label = Label(scrollable_frame, image=picture1, bg='black')
        label.image =  picture1
        label.place(x= 550, y= 185)
        picture2 = (PhotoImage(file= os.path.join('photos', "Waste2.png"))).subsample(7,7)
        label = Label(scrollable_frame, image=picture2, bg='black')
        label.image =  picture2
        label.place(x= 650, y= 260)
        picture3 = (PhotoImage(file= os.path.join('photos', "Waste3.png"))).subsample(7,7)
        label = Label(scrollable_frame, image=picture3, bg='black')
        label.image =  picture3
        label.place(x= 520, y= 320)
        picture4 = (PhotoImage(file= os.path.join('photos', "SDoge.png"))).subsample(7,7)
        label = Label(scrollable_frame, image=picture4, bg='black')
        label.image =  picture4
        label.place(x= 600, y= 380)

        #Come back_Button
        self.delete = Button(scrollable_frame, text = "Pantalla principal", command=lambda: self.erase(), font=("Courier New", 10), bg="aquamarine4")
        self.delete.place(x=600,y=450, width=150,height=30)
#Erase the info in all the frame
    def erase(self):
        self.frame.destroy()
        self.delete.destroy()
#High Score Window#################################################################################
class Window3:
    def __init__(self, master):
        #Call the highest score
        global highest
        #Create a new Canvas
        self.canvas = Canvas(width=795, height=170, relief='groove', bg='black')
        self.canvas.place(x=0,y=175)
        #Come back_Button
        self.delete = Button(self.canvas, text = "Pantalla principal", command=lambda: self.erase(), font=("Courier New", 10), bg="aquamarine4")
        self.delete.place(x=10,y=5, width=150,height=30)

        #"Best games"_Label
        self.Highscore= Label(self.canvas, text= "¡Best\ngames!", font=("Courier New", 20, "bold"), fg="lawngreen", bg='black')
        self.Highscore.place(x=10, y=50, width=150, height=65)
        #Put the muscle doge image
        highest_dogo = (PhotoImage(file= os.path.join('photos', "muscle_doge.png"))).subsample(5,5)
        dimage = Label(self.canvas, image=highest_dogo, bg='black')
        dimage.image =  highest_dogo
        dimage.place(x= 170, y= 10, width=150, height=160)

        #Reads the file line by line 
        file = open("High score table.txt", "r")    
        person1 = file.readline()
        person2 = file.readline()
        person3 = file.readline()
        person4 = file.readline()
        person5 = file.readline()
        person6 = file.readline()
        person7 = file.readline()
        #Create a directory whit the winners
        self.winners ={"1":person1, "2":person2, "3":person3, "4":person4, "5":person5, "6":person6, "7":person7,
                       "10":"", "11":"", "12":"", "13":"", "14":"", "15":"", "16":""}
        file.close()
        #If there's no winners yet
        if person1== "":
            dimage.destroy()
            self.Highscore= Label(self.canvas, text= "No hay puntajes por el momento :(", font=("Courier New", 15, "bold"), fg="lawngreen", bg='black')
            self.Highscore.place(x=200, y=100, width=200, height=20)
        #If there are winners
        else:
            #Call a function to create a list without strings
            self.list_points(self.winners, 1)
            #Accommodate the list and get the highest score
            self.h.sort()
            self.h.reverse()
            highest = max(self.h)
            #Transdorm the some values into a new ones 
            self.new_dir(self.winners, 1)
            #All the score labels
            self.Highscore1= Label(self.canvas, text= self.winners["10"], font=("Courier New", 13, "bold"), fg="gold", bg='black')
            self.Highscore1.place(x=165, y=70, width=180, height=30)
            self.Highscore2= Label(self.canvas, text= "2-" +self.winners["11"], font=("Courier New", 13, "bold"), fg="lawngreen", bg='black', justify=LEFT)
            self.Highscore2.place(x=350, y=25, width=180, height=30)
            self.Highscore3= Label(self.canvas, text= "3-" +self.winners["12"], font=("Courier New", 13, "bold"), fg="lawngreen", bg='black', justify=LEFT)
            self.Highscore3.place(x=550, y=30, width=180, height=30)
            self.Highscore4= Label(self.canvas, text= "4-" +self.winners["13"], font=("Courier New", 13, "bold"), fg="lawngreen", bg='black', justify=LEFT)
            self.Highscore4.place(x=360, y=65, width=180, height=30)
            self.Highscore5= Label(self.canvas, text= "5-" +self.winners["14"], font=("Courier New", 13, "bold"), fg="lawngreen", bg='black', justify=LEFT)
            self.Highscore5.place(x=560, y=70, width=180, height=30)
            self.Highscore6= Label(self.canvas, text= "6-" +self.winners["15"], font=("Courier New", 13, "bold"), fg="lawngreen", bg='black', justify=LEFT)
            self.Highscore6.place(x=370, y=105, width=180, height=30)
            self.Highscore7= Label(self.canvas, text= "7-" +self.winners["16"], font=("Courier New", 13, "bold"), fg="lawngreen", bg='black', justify=LEFT)
            self.Highscore7.place(x=570, y=110, width=180, height=30)


#Erase the canvas
    def erase(self):
        self.canvas.destroy()
        self.delete.destroy()

#Count the values and call the function that creates the list        
    def list_points(self, d, val):
        if val<8 and d[str(val)]!= "":
            self.remove_str(d[str(val)])
            self.list_points(d, val +1)
#Create a directory whit the winners            
    def new_dir (self, d, val): 
        if val<8 and d[str(val)]!= "":
            self.compare_remove((d[str(val)]))
            if self.h[0]==self.value and "" == self.winners["10"]:
                self.winners["10"] =  d[str(val)][:-1]
            elif self.h[1]==self.value and "" == self.winners["11"]:
                self.winners["11"] =  d[str(val)][:-1]
            elif self.h[2]==self.value and "" == self.winners["12"]:
                self.winners["12"] =  d[str(val)][:-1]
            elif self.h[3]==self.value and "" == self.winners["13"]:
                self.winners["13"] =  d[str(val)][:-1]
            elif self.h[4]==self.value and "" == self.winners["14"]:
                self.winners["14"] =  d[str(val)][:-1]
            elif self.h[5]==self.value and "" == self.winners["15"]:
                self.winners["15"] =  d[str(val)][:-1]
            elif self.h[6]==self.value and "" == self.winners["16"]:
                self.winners["16"] =  d[str(val)][:-1]

            self.new_dir (d, val+1)
#Remove the string values        
    def compare_remove(self, string):             
        try:
            p=int(string[0])
            if isinstance (p, int):
                self.value = int(string)
                return self.value                
        except:
            self.compare_remove(string[1:])
#Remove the string values and creates a list que the string values                  
    def remove_str(self, string):        
        try:
            p=int(string[0])
            if isinstance (p, int):
                try:
                    self.h = [int(string[:-1])]+self.h
                except:
                    self.h = [int(string[:-1])]
        except: 
            self.remove_str(string[1:])
   

        
#Game Window#######################################################################
class Window4:
    def __init__(self, master):

##########Space window (all the objets in this window are "self.can").
        self.can = Canvas(width = 800, height = 350,highlightthickness=0, relief='ridge',bg='black' )
        self.can.place(x=0,y=0)
##########Text window (all the objets in this window are "self.canvas").        
        self.canvas = Canvas(width = 800, height = 150,highlightthickness=0, relief='ridge', bg= 'paleturquoise4')
        self.canvas.place(x=0,y=200)
        
##########Create the dog image :       
        self.doge = (PhotoImage(file= os.path.join('photos', "doge.png"))).subsample(10,10)
        self.canvas.create_image(580, 80, image= self.doge)
        
        

        
######The hearth polygons :
        points= [790,20, 780,10, 780,5, 785,0, 790,5, 795,0, 800,5, 800,10]
        self.canvas.create_polygon(points,width=2.5,outline="black", fill="red", tags="hearth1")
        points= [760,20, 750,10, 750,5, 755,0, 760,5, 765,0, 770,5, 770,10]
        self.canvas.create_polygon(points,width=2.5,outline="black", fill="red", tags="hearth2")
        points= [730,20, 720,10, 720,5, 725,0, 730,5, 735,0, 740,5, 740,10]
        self.canvas.create_polygon(points,width=2.5,outline="black", fill="red", tags="hearth3")
        self.lifes = "hearth1"
        
           
######The space ship polygons :        
        points= [8,86, 8,78, 40,78, 40,86]
        self.space_ship3 = self.can.create_polygon(points,width=1,outline="aquamarine4", fill="deepskyblue", tags="ship")
        points= [8,118, 8,110, 40,110, 40,118]
        self.space_ship4 = self.can.create_polygon(points,width=1,outline="aquamarine4", fill="deepskyblue", tags="ship")
        points= [0,110, 0,86, 16,94, 16,102]
        self.space_ship1 = self.can.create_polygon(points,width=2,outline="gold", fill="orangered2", tags="ship")
        points= [8,110, 16,102, 16,94, 8,86, 48,86, 48,94, 56,94, 56, 102, 48,102, 48,110]
        self.space_ship2 = self.can.create_polygon(points,width=1,outline="deepskyblue", fill="aquamarine4", tags="ship")
######This is like the backbone of the game, if any of this is changed or moved, the game stops working :
        #This value define how comond will be the double damage object
        self.value= 45
        #This value define how comond will be the space doge object
        self.value2= 21
        #This value is for add the 500 points in the points value
        self.plus_doge = 0
        #If this value doesn't exist  the objects don't move
        self.run = True
        #This value define the start of counting seconds
        self.seconds= "0"
        #Call the points_time fuction
        self.points_time()
        #This value define how fast the objects move in the beginning of the game
        self.speed = -1
        #Call the space_waste and its loop fuction(turquoise objects)
        self.space_waste()
        self.Waste_loop()
        #Call the parner fuction (doge text)
        self.parner(1)
        
        #Call the diagonal_waste and its loop fuction(red objects)
        self.can.after(10000, lambda :[self.diagonal_waste(), self.Waste_loop2()])
        #Call the more_damage_waste and its loop fuction(blue objects)
        self.can.after(30000, lambda :[self.more_damage_waste(), self.Waste_loop3()])
        #Call the space_doge and its loop fuction
        self.can.after(7000, lambda :[self.space_doge(), self.Waste_loop4()])

        #Move the space ship
        Pwindow.bind("<KeyPress-Down>", lambda a: self.down(a))
        Pwindow.bind("<KeyPress-Up>", lambda a: self.up(a))
        Pwindow.bind("<KeyPress-Left>", lambda a: self.left(a))
        Pwindow.bind("<KeyPress-Right>", lambda a: self.right(a))
        
#####All the calls to move the space ship:    
    def right(self, event):
        if self.run == True:
            #for no moving out the limits
            p=self.can.coords("ship")
            if p[6]<800:
                self.can.move("ship", 10, 0)
                #More speed
                if self.speed>-4:
                    self.speed = self.speed-0.5
    def left(self, event):
        if self.run == True:
            #for no moving out the limits
            p=self.can.coords("ship")
            if p[0]>0:
                self.can.move("ship", -10, 0)
                #Brake
                if self.speed<-1:
                    self.speed = self.speed+0.5
    def up(self, event):
        if self.run == True:
            #for no moving out the limits
            p=self.can.coords("ship")
            if p[3]>3:
                self.can.move("ship", 0, -20)	
    def down(self, event):
        if self.run == True:
            #for no moving out the limits
            p=self.can.coords("ship")
            if p[1]<161:
                self.can.move("ship", 0, 20)

#####Time and points labels:        
    def points_time(self):
        if self.run == True:
            global points
            global name
            #Define seconds
            self.seconds= str(int(self.seconds)+1)
            #Define points
            points = str(int(self.seconds)*5+self.plus_doge)
            #Playing time_Label
            self.ptime= Label(self.canvas, text= "Tiempo\n de juego  " +self.seconds, font=("Courier New", 15, "bold"), fg="white", bg ="paleturquoise4")
            self.ptime.place(x=620, y=20)
            #Puntaje_Label
            self.ptime= Label(self.canvas, text= "Puntaje " +points, font=("Courier New", 15, "bold"), fg="white", bg ="paleturquoise4")
            self.ptime.place(x=630, y=90)
            #One second loop
            self.canvas.after(1000, self.points_time)
        else:
            #Call all the score/write .txt file function
            self.val = 0
            self.new_high()
            
        

    def new_high (self):
        global points
        global name
        global highest
        #Open High score table.txt file
        with open("High score table.txt",'r+') as file:
            compare = file.readlines()
            #If the file is empty
            if compare == []:
                file.close()
                #New highest score
                highest = int(points)
                self.game_over= Label(self.canvas, text= "¡New record!", font=("Courier New", 30, "bold"), fg="gold", bg='paleturquoise4')
                self.game_over.place(x=50, y=40, width=350, height=40)
                winsound.PlaySound(os.path.join('Sounds', 'winner.wav'), winsound.SND_ASYNC | winsound.SND_ALIAS )
                self.doge = (PhotoImage(file= os.path.join('photos', "t_doge.png"))).subsample(9,9)
                self.canvas.create_image(500, 70, image= self.doge)
                #Write the score
                with open("High score table.txt",'a+') as file:
                    file.write(name + "   " + points+"\n")
                    file.close()
            #If the file isn't empty        
            else:
                #If there less than 7 lines of text
                if len(compare)<7:
                    file.close()
                    with open("High score table.txt",'a+') as file:
                        #If the puntaje is lower than the highest score
                        if  int(points) < highest:
                            file.write( name + "   " + str(points)+"\n")
                            file.close()
                        #If the puntaje is higher than the highest score
                        else:
                            #New highest score
                            self.game_over= Label(self.canvas, text= "¡New record!", font=("Courier New", 30, "bold"), fg="gold", bg='paleturquoise4')
                            self.game_over.place(x=50, y=40, width=350, height=40)
                            winsound.PlaySound(os.path.join('Sounds', 'winner.wav'), winsound.SND_ASYNC | winsound.SND_ALIAS )
                            self.doge = (PhotoImage(file= os.path.join('photos', "t_doge.png"))).subsample(9,9)
                            self.canvas.create_image(500, 70, image= self.doge)
                            highest = int(points)
                            file.write( name + "   " + str(points)+"\n")
                            file.close()
                                
                #If there more than 6 lines of text                
                else:
                    #All scores read acquire their own variable
                    person1 = compare[0]
                    person2 = compare[1]
                    person3 = compare[2]
                    person4 = compare[3]
                    person5 = compare[4]
                    person6 = compare[5]
                    person7 = compare[6]
                    self.winners ={"1":person1, "2":person2, "3":person3, "4":person4, "5":person5, "6":person6, "7":person7,
                       "10":"", "11":"", "12":"", "13":"", "14":"", "15":"", "16":""}
                    #Create a list of the scores
                    self.list_points(self.winners, 1)
                    #Reacomodate the list of scores and get the highest score
                    self.h.sort()
                    highest = max(self.h)
                    #Call new_dir function
                    self.new_dir(self.winners, 1)
                    #Erase the text in the "High score table.txt" file
                    file.truncate(0)
                    file.close()
                    with open("High score table.txt",'a+') as file:
                        self.compare_remove(compare[self.val-1])
                        #If the score is higher thant the highest score
                        if int(points) >= highest:
                            #New highest score and write all the scores without the last one
                            self.game_over= Label(self.canvas, text= "¡New record!", font=("Courier New", 30, "bold"), fg="gold", bg='paleturquoise4')
                            self.game_over.place(x=50, y=40, width=350, height=40)
                            winsound.PlaySound(os.path.join('Sounds', 'winner.wav'), winsound.SND_ASYNC | winsound.SND_ALIAS )
                            self.doge = (PhotoImage(file= os.path.join('photos', "t_doge.png"))).subsample(9,9)
                            self.canvas.create_image(500, 70, image= self.doge)
                            file.write( self.winners["16"] + self.winners["15"] + self.winners["14"]+ self.winners["13"] + self.winners["12"] + self.winners["11"] + name + "   " + str(points)+"\n")
                            file.close()
                        #If the score is higher thant the lowest score
                        elif int(points) >= min(self.h):
                            #Write all the scores without the last one
                            file.write( self.winners["16"] + self.winners["15"] + self.winners["14"]+ self.winners["13"] + self.winners["12"] + self.winners["11"] + name + "   " + str(points)+"\n")
                            file.close()
                        #If the score is higher thant the lowest score
                        else:
                            #Write all the scores wuthout the new one
                            file.write( self.winners["16"]+ self.winners["15"] + self.winners["14"] + self.winners["13"]+ self.winners["12"] + self.winners["11"] + self.winners["10"])
                            file.close()
                        
#Count the values and call the function that creates the list 
    def list_points(self, d, val):
        if val<8 and d[str(val)]!= "":
            self.remove_str(d[str(val)])
            self.list_points(d, val +1)
#Create a directory whit the winners         
    def new_dir (self, d, val): 
        if val<8 :
            self.compare_remove((d[str(val)]))
            if self.h[0]==self.value and "" == self.winners["10"]:
                self.winners["10"] =  d[str(val)]
            elif self.h[1]==self.value and "" == self.winners["11"]:
                self.winners["11"] =  d[str(val)]
            elif self.h[2]==self.value and "" == self.winners["12"]:
                self.winners["12"] =  d[str(val)]
            elif self.h[3]==self.value and "" == self.winners["13"]:
                self.winners["13"] =  d[str(val)]
            elif self.h[4]==self.value and "" == self.winners["14"]:
                self.winners["14"] =  d[str(val)]
            elif self.h[5]==self.value and "" == self.winners["15"]:
                self.winners["15"] =  d[str(val)]
            elif self.h[6]==self.value and "" == self.winners["16"]:
                self.winners["16"] =  d[str(val)]

            self.new_dir (d, val+1)
#Remove the string values         
    def compare_remove(self, string):             
        try:
            p=int(string[0])
            if isinstance (p, int):
                self.value = int(string[:-1])
                return self.value                
        except:
            self.compare_remove(string[1:])
#Remove the string values and creates a list que the string values                      
    def remove_str(self, string):        
        try:
            p=int(string[0])
            if isinstance (p, int):
                try:
                    self.h = [int(string[:-1])]+self.h
                except:
                    self.h = [int(string[:-1])]
        except: 
            self.remove_str(string[1:])
            
        



           
#1####This part have the sequence of movement of the one line objects:
#Creation of the object:        
    def space_waste(self):
        if self.run == True:
            options =[5,40,75,105, 135, 165]
            y = random.choice(options)
            points1= [770,y+30, 770,y+10, 780,y+10, 780,y+0, 800,y+0, 800,y+30]
            points2= [770,y+30, 770,y+0, 790,y+0, 790,y+10, 800,y+10, 800,y+30]
            points3= [770,y+30, 770,y+0, 800,y+0, 800,y+20, 790,y+20, 790,y+30]
            points4= [780,y+30, 780,y+20, 770,y+20, 770,y+0, 800,y+0, 800,y+30]
            self.dicc={"1": points1, "2": points2, "3": points3, "4": points4}
            self.ramd =str(randint(1, 4))
            self.figure=self.dicc[self.ramd]
            self.waste1 = self.can.create_polygon(self.figure,width=2,outline="gold", fill="turquoise4", tags= "waste")
#Movement of the object:
    def movement(self):
#If the object touches the spaceship:
        crash=self.can.bbox(self.space_ship2)
        touch=self.can.find_overlapping(crash[0], crash[1], crash[2], crash[3])        
        try:
            variable =self.can.gettags(touch[4])
            if variable[0] == 'waste':
                self.can.delete(touch[4])
                self.canvas.delete(self.lifes)
                self.lifes = (self.lifes[:6]+str(int(self.lifes[-1])+1))
                if int(self.lifes[-1])>=4:
                    self.game_over()
#Movement:                
        except:
            self.can.move("waste", self.speed, 0)
#Creation of another object:
            posc = self.can.coords(self.waste1)
            try:
                if 510>posc[0]>500:
                    self.space_waste()
            except:
                self.space_waste()
#Loop:                
    def Waste_loop(self):
        if self.run == True:
            self.movement()
            self.can.after(10,self.Waste_loop)



#2####This part have the sequence of movement of the changing direction (diagonal) objects:
#Creation of the object:
    def diagonal_waste(self):
        if self.run == True:
            options =[140, 110, 80, 50, 20]
            y = random.choice(options)
            points5= [776,y+15, 784,y, 788,y+7.5, 792,y, 800,y+15, 792,y+30, 788,y+22.5, 784,y+30]
            self.waste2 = self.can.create_polygon(points5,width=2,outline="gold", fill="red4", tags= "waste1")
#Movement of the object:
    def movement2(self):
        posc = self.can.coords("waste1")
        crash=self.can.bbox(self.space_ship2)
        touch=self.can.find_overlapping(crash[0], crash[1], crash[2], crash[3])
#If the object is near of the spaceship:
        if crash[0]-10<posc[0]<crash[2]+150:
            if crash[3]<posc[1]:
                self.can.move("waste1", -1.5, -0.5)
            elif crash[3]>posc[1]:
                self.can.move("waste1", -1.5, 0.5)
#If the object is position is out of the window range:
        elif posc[0]<-30:
            self.can.delete("waste1")
#If the object touches the spaceship:
        try:
            variable =self.can.gettags(touch[4])
            if variable[0] == 'waste1':
                self.can.delete(touch[4])
                self.canvas.delete(self.lifes)
                self.lifes = (self.lifes[:6]+str(int(self.lifes[-1])+1))
                if int(self.lifes[-1])>=4:
                    self.game_over()
#Movement:                
        except:
            self.can.move("waste1", self.speed, 0)

#Loop:
    def Waste_loop2(self):
        if self.run == True:
            try:
                self.movement2()
            except:
                self.diagonal_waste()
            self.can.after(10, self.Waste_loop2)

            
#3####This part have the sequence of movement of the doble damage objects:
#Creation of the object:
    def more_damage_waste(self):
        if self.run == True:
            options =[50, 100]
            y = random.choice(options)
            points6= [779,y+21, 793,y+14, 800,y, 807,y+14, 821,y+21, 807,y+28, 800,y+42, 793,y+28]
            self.waste3 = self.can.create_polygon(points6,width=2,outline="lawngreen", fill="midnightblue", tags= "waste2")
#Movement of the object:
    def movement3(self):
        posc = self.can.coords("waste2")
        crash=self.can.bbox(self.space_ship2)
        touch=self.can.find_overlapping(crash[0], crash[1], crash[2], crash[3])
#If the object is position is out of the window range:
        if posc[0]<-42:
            self.can.delete("waste2")
#If the object touches the spaceship:
        try:
            variable =self.can.gettags(touch[4])
            if variable[0] == 'waste2':
                self.can.delete(touch[4])
                self.canvas.delete(self.lifes)
                self.canvas.delete(self.lifes[:6]+str(int(self.lifes[-1])+1))
                self.lifes = (self.lifes[:6]+str(int(self.lifes[-1])+2))
                if int(self.lifes[-1])>=4:
                    self.game_over()
#Movement:                
        except:
            self.can.move("waste2", -1.5, 0)
#Loop:
    def Waste_loop3(self):
        if self.run == True:
            try:
                self.movement3()
            except:
                if int(self.seconds)>=self.value:
                    self.value= self.value+15
                    self.more_damage_waste()
                
            self.can.after(10,self.Waste_loop3)   
#4####This part have the sequence of movement of the giver points objects:
#Creation of the object:
    def space_doge(self):
        global name
        if self.run == True:
            self.parner(0)
            options =[60,126]
            y = random.choice(options)
            self.space_d = (PhotoImage(file= os.path.join('photos', "space_doge.png"))).subsample(25,25)
            self.image_position = self.can.create_image(790, y, image= self.space_d, tags='Sdoge')
        
#Movement of the object:
    def movement4(self):
        crash=self.can.bbox(self.space_ship2)
        touch=self.can.find_overlapping(crash[0], crash[1], crash[2], crash[3])
        posc = self.can.coords(self.image_position)
#If the object is position is out of the window range:
        if posc[0]< -20:
            self.can.delete(self.image_position)
#If the object touches the spaceship:
        try:
            variable =self.can.gettags(touch[4])
            
            if variable[0] == 'Sdoge':
                self.can.delete(touch[4])
                self.plus_doge = self.plus_doge+ 500
                self.plus= Label(self.can, text= "+500!", font=("Courier New", 14, "bold"), fg="white", bg='black')
                self.plus.place(x=crash[2], y=crash[3])
                self.counting = 1
                self.erase_label()
#Movement:                
        except:
            self.can.move(self.image_position, self.speed, 0)
#Loop:
    def Waste_loop4(self):
        if self.run == True:
            try:
                self.movement4()
            except:
                if int(self.seconds)>=self.value2:
                    self.value2= self.value2+14
                    self.space_doge()
                
            self.can.after(10,self.Waste_loop4)
#Erase the "+500!" label after a time
    def erase_label(self):
        if self.counting >300:
            self.plus.destroy()
        else:
            self.counting=self.counting+1
            self.can.after(1,self.erase_label)
#Doge text labes
    def parner(self, val):
        #Fist dialogue
        if val == 1:
            self.text = "-Hola, soy Doge#1-14-13-9-24-16, pero mis compañeros\n me dicen Doge  yo voy a ser tu compañero\n y copiloto en este viaje \n\n Un placer conocerte " +name
            self.dogetext= Label(self.canvas, text= self.text, font=("Courier New", 12, "bold"), fg="white", bg ="gray29", justify=LEFT)
            self.dogetext.place(x=10, y=10)
        #Others dialogues
        elif val==0:
            self.dogetext.destroy()
            text1= "-¡Oh!¡Un Bad Doge! ¡A esos Doges no les\n gusta tener anmiwos >:v!\n\n *Susurros(si quieres lo dejas mbotado >:v)"
            text2= "-Mira a Doge#3-01-19-12-16-20,\n ¿¿¿No lo hambíamos jumtado ya???"
            text3= "-Vanmos a por ese"
            text4= "-*Tararea una canción trite mientras\n ve la lluvia de restos"
            text5= "-¿Ya has notado que el timtulo del juewo\n es um juewo de mpalambras?"
            text6= "-Me mprewunto que hambrá causado la explosióm\n de la nave modriza"
            text7= "-Mira umna Dogenena ¬u¬"
            text8= "-Uno más para la carnita asada"
            text9= "-¿Sambías que desmpués de la casi extimción\n de los hunmanos en el 2020 los Doges tonmaron\n el donminio del mundo?"
            text10= "-Mi color famvorito es el dorado,\n aumnque no sé conmo se ve"
            self.dir={"1": text1, "2": text2, "3": text3, "4": text4, "5": text5, "6": text6, "7": text7, "8": text8, "9": text9, "10": text10}
            
            self.ram =str(randint(1, 10))
            self.text =self.dir[self.ram]
            self.dogetext= Label(self.canvas, text= self.text, font=("Courier New", 12, "bold"), fg="white", bg ="gray29", justify=LEFT)
            self.dogetext.place(x=30, y=40)

#####Game over fuction:        
    def game_over(self):
        winsound.PlaySound(None, winsound.SND_FILENAME)
        self.dogetext.destroy()
        self.run = False
        self.game_over= Label(self.can, text= "Game Over", font=("Courier New", 30, "bold"), fg="red", bg='black')
        self.game_over.place(x=250, y=40, width=350, height=40)
#Credits Window#######################################################################
class Window5(Tk):
    def __init__(self, master):
        #Creation of a new window
        self.Window5= Toplevel(Pwindow)
        self.Window5.title("Creditos")
        self.Window5.geometry("+200+150")
        self.Window5.minsize(800, 350)
        #Create a Canvas
        self.canvas = Canvas(self.Window5, width=800, height=350, relief='groove', bg='black', highlightthickness=0)
        self.canvas.place(x=0,y=0)
        #Delete Button
        self.delete = Button(self.canvas, text = "Pantalla principal", command=lambda: self.erase(), font=("Courier New", 10), bg="aquamarine4")
        self.delete.place(x=10,y=5, width=150, height=30)
        self.x=200
        self.y=350
        self.run = True
        #Text
        self.info ='''Lugar de Desarrollo\nCosta Rica\n\nInstituto Tecnológico de Costa Rica\nIngeniería en Computadores\n
Grupo\nCE-1102 Taller de Programación
\nGrupo#5\n\nDocente Tutor\nIng. Luis Barboza Artavia\n\nVersión\nSpace Dodge v1.0.0\n\nBasado en los juegos reales\nRoad Fighter
by Konami®\n\nand\n\nSpace Impact\nby Nokia®\n\nAutor\nFrancisco Zamora Corrales\n\nAño de desarrollo\n2020\n\n\n¡Gracias por Jugar!'''
        self.move_labels()

    def move_labels(self):
        #Text label
        self.text= Label(self.canvas, text= self.info, font=("Courier New", 12, "bold"), fg="lawngreen", bg='black')
        self.text.place(x=self.x, y=self.y, width=400)
        Pwindow.update()
        time.sleep(0.01)
        #Animation
        if self.run == True:
            if self.y > -610:
                try:
                    self.text.destroy()
                    self.y= self.y-1
                    self.move_labels()
                #If is Window is closed before the credits end
                except:
                    print("Gracias por jugar")
            #Close the window at the end of the animation 
            else:
                self.erase()
               


        
#Delete the window    
    def erase(self):
        self.Window5.destroy()
        self.run = False
        self.canvas.destroy()
        self.delete.destroy()
        
        
        
        

 
if __name__=="__main__":
    Pwindow = Tk()
    window = Window(Pwindow)
    Pwindow.title("Espace Doged")
    Pwindow.geometry("+250+190")
    Pwindow.minsize(800, 350)
    Pwindow.mainloop()

