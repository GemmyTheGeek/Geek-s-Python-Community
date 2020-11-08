# GUITranslator.py
from tkinter import *
from tkinter import ttk #ttk = theme of tk
#--------Google Translator---------
from googletrans import Translator
translator = Translator ()


GUI = Tk () #make main window
GUI.geometry ('767x300')
GUI.title('Offline Translator')
#Config
FONT = ('Angsana New',15)

#------Label-------

L = ttk.Label(GUI,text="Please enter the word you wish to transalate", font = FONT)
L.pack()



#Entry
v_vocab = StringVar() #Information Box
E1 = ttk.Entry(GUI,textvariable= v_vocab,font=FONT,width=40)
E1.pack(pady=20)



# ----Button----
def Translate():
                vocab = v_vocab.get()
                meaning = translator.translate(vocab,dest='th')
                print(vocab + ":" + meaning.text)
                print( meaning.pronunciation)
                v_result.set(vocab + ":" + meaning.text)


B1=ttk.Button(GUI,text='Translate',command=Translate) #create button
B1.pack(ipadx=20, ipady=10) #changes the size


#------Label-------

L = ttk.Label(GUI,text="Transalated Word", font = FONT)
L.pack()
#-------Result--------
FONT2 = ("Angsana New" ,20)
v_result = StringVar()
R1 = ttk.Label(GUI, textvariable=v_result,font=FONT)
R1.pack()






GUI.mainloop()#makes the program run forever






