from multiprocessing.sharedctypes import Value
from os import lstat
from re import L
from tkinter import *
from tkinter import messagebox
import random
from datetime import datetime
from setuptools import Command
import csv
import pandas


root = Tk()
root.geometry('600x600')

#date and time
now = datetime.today()
date_time_str = '18/09/19 01:55:19'
date_time_obj = now.strftime("%d/%m/%y %H:%M:%S")
print ("System date and time:", date_time_obj)

header = ["system_date_time","game_name","numbers"]

#game description
def LottoDesc():
    description = Label(root, text ="The oldest and the most popular number game in Poland.")
    description.place(x=150,y=40)

def LottoPopup():

        response = messagebox.askyesno("Lotto","Do you want to play Lotto?")
        #if yes (response == 1) draw six random numbers
        if response == 1:
            Label(root, text="My Lotto numbers:").place(x=120,y=80)
  

            r1 = random.randint(1,49)
            r2 = random.randint(1,49)
            r3 = random.randint(1,49)
            r4 = random.randint(1,49)
            r5 = random.randint(1,49)
            r6 = random.randint(1,49)
            n1 = Label(root, text="%i" % r1)
            n2 = Label(root, text="%i" % r2)
            n3 = Label(root, text="%i" % r3)
            n4 = Label(root, text="%i" % r4)
            n5 = Label(root, text="%i" % r5)
            n6 = Label(root, text="%i" % r6)
            n1.place(x=240, y=80)
            n2.place(x=260, y=80)
            n3.place(x=280, y=80)
            n4.place(x=300, y=80)
            n5.place(x=320, y=80)
            n6.place(x=340, y=80)

            lottoList = [r1,r2,r3,r4,r5,r6] 
            print(lottoList)
            with open('plik.csv','a', newline='') as file:
                    fieldnames = ['system_date_time','game_name','numbers']
                    writer = csv.DictWriter(file, fieldnames=fieldnames)

                    writer.writeheader()
                    writer.writerow({'system_date_time': date_time_obj, 'game_name':'Lotto', 'numbers': lottoList})

        else:
            Label(root, text="I don't want to play Lotto >_<").place(x=120,y=120)


        lottoList.clear()



#game name
Lotto = Label(root, text="Lotto")
Lotto.config(bg="yellow")
Lotto.place(x=30,y=10)

#show game description
showLotto = Button (root, text="Game Description", command=LottoDesc)
showLotto.place(x=30,y=40)

#play game
Button(root, text="Play Lotto", command=LottoPopup).place(x=30,y=80)


    
#game description
def MultiDesc():
    description = Label(root, text ="In Multi Multi it all depends on you. You decide how much you play.")
    description.place(x=150,y=240)

listOfLabels = []
multiList = []

def MultiPopup():

        response = messagebox.askyesno("MultiMulti","Do you want to play MultiMulti?")
        #if yes (response == 1) draw six random numbers
        if response == 1:
            
            Label(root, text="My MultiMulti numbers:").place(x=140,y=280)
            #rootD - space in second window
            rootD=Tk()
            rootD.geometry('200x240')

            # Create a listbox
            listbox = Listbox(rootD, width=40, height=10, selectmode=SINGLE)
 
            # Inserting the listbox items
            listbox.insert(1,"1")
            listbox.insert(2, "2")
            listbox.insert(3, "3")
            listbox.insert(4, "4")
            listbox.insert(5, "5")

            def selected_item():
                
                global listOfLabels    
                sel_items = listbox.curselection()
                boxesToCreate = 0
                if(len(sel_items) > 0):
                        boxesToCreate = sel_items[0] + 1
                else:
                        messagebox.showwarning(title="index selection", message="WRONG INDEX, NOTHING SELECTED, RETURNING 0")

               #clear
                for i in range(len(listOfLabels)):
                    listOfLabels[i].destroy()

                #clear multiList - list catching numbers from fields
                multiList.clear()

                #destroyed labels gone
                listOfLabels = []
                for i in range(boxesToCreate):
                    r1 = random.randint(1,80)
                    multiList.append(r1)
                    curLabel = Label(root, text=str(r1)) #pointer
                    curLabel.place(x=280 + i * 20,y=280) 
                    listOfLabels.append(curLabel)
                    
                    
                #multiList - list with newest random numbers in selected number of fields
                print(multiList)
                with open('plik.csv','a', newline='') as file:
                    fieldnames = ['system_date_time','game_name','numbers']
                    writer = csv.DictWriter(file, fieldnames=fieldnames)

                    writer.writeheader()
                    writer.writerow({'system_date_time': date_time_obj, 'game_name':'MultiMulti', 'numbers': multiList})
        
                     
            btn = Button(rootD, text='Create Boxes', command=selected_item)
            
            

            # Placing the button and listbox
            btn.pack(side='bottom')
            listbox.pack()
        else:
            Label(root, text="I don't want to play MultiMulti >_<").place(x=140,y=320)

#game name
Multi = Label(root, text="MultiMulti")
Multi.config(bg="violet")
Multi.place(x=30,y=210)

#show game description
showMulti = Button (root, text="Game Description", command=MultiDesc)
showMulti.place(x=30,y=240)

#play game
Button(root, text="Play MultiMulti", command=MultiPopup).place(x=30,y=280)



#game description
def EuroDesc():
    description = Label(root, text ="18 European countries take part in the game.")
    description.place(x=150,y=440)

def EuroPopup():

        response = messagebox.askyesno("Eurojackpot","Do you want to play Eurojackpot?")
        #if yes (response == 1) draw six random numbers
        if response == 1:
            Label(root, text="My Eurojackpot numbers:").place(x=140,y=480)
            r1 = random.randint(1,50)
            r2 = random.randint(1,50)
            r3 = random.randint(1,50)
            r4 = random.randint(1,50)
            r5 = random.randint(1,50)
            r6 = random.randint(1,12)
            r7 = random.randint(1,12)
            n1 = Label(root, text="%i" % r1)
            n2 = Label(root, text="%i" % r2)
            n3 = Label(root, text="%i" % r3)
            n4 = Label(root, text="%i" % r4)
            n5 = Label(root, text="%i" % r5)
            n6 = Label(root, text="%i" % r6)
            n6.config(bg="orange")
            n7 = Label(root, text="%i" % r7)
            n7.config(bg="orange")
            n1.place(x=280, y=480)
            n2.place(x=300, y=480)
            n3.place(x=320, y=480)
            n4.place(x=340, y=480)
            n5.place(x=360, y=480)
            n6.place(x=380, y=480)
            n7.place(x=400,y=480)

            euroList = [r1,r2,r3,r4,r5,r6,r7]
            print(euroList)
            with open('plik.csv','a', newline='') as file:
                    fieldnames = ['system_date_time','game_name','numbers']
                    writer = csv.DictWriter(file, fieldnames=fieldnames)

                    writer.writeheader()
                    writer.writerow({'system_date_time': date_time_obj, 'game_name':'Eurojackpot', 'numbers': euroList})
        else:
            Label(root, text="I don't want to play Eurojackpot >_<").place(x=140,y=520)
        euroList.clear()

#game name
Euro = Label(root, text="Eurojackpot")
Euro.config(bg="orange")
Euro.place(x=30,y=410)

#show game description
showEuro = Button (root, text="Game Description", command=EuroDesc)
showEuro.place(x=30,y=440)

#play game
Button(root, text="Play Eurojackpot", command=EuroPopup).place(x=30,y=480)

#while csv file is empty comment line 234
df = pandas.read_csv('plik.csv')
print(df)

root.mainloop()
    