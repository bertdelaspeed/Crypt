from tkinter import *


coded=""
#Coded is an empty global variable that should get the encrypted message

#def crypter(texto,key):
def crypter ():
    i=0
    j=0
    
    #print("OKLJK") # This was just to test the command function in the GUI
    text=[]
    #Not able to get the text coming from the textbox. So I used the text=(input("your text")) to test the function and it works wells
    #text=(input("your text \n"))
    #the get function doesn't work. That seems to be the real problem. I get an error [ get() missing 1 required positional argument ]
    text=texto.get()
    key=[]
    #key=(input("key \n"))
    #Here again I used the .get() method but It doesn't work. I need to get the key from the Entry box with it but it ain't working
    key=code.get()
    
    length=len(text) #Here I get the length of the text
    length2=len(key) # Here i get the length of the key
    
    while(i!=length):
        if j==length2:
            j=0
        b=ord(key[j])-ord('a')
       
        if (ord(text[i])+b)<=ord('z'):      
            c=chr(ord(text[i])+b)
            coded+=c
            # In the empty global variable is appended all the encrypted characters
            
        else:
            c=(ord(text[i])+b)-26
            coded+=chr(c)            
        
        i+=1
        j+=1    

        print (coded)
        #You can copy this function and execute it alone to see how it works but its not wanting to work with the GUI
    

        
 
root=Tk()
root.title("LASPEED Crypter") #Window Name
root.geometry("600x250") #Window size

mess=Label(root,text="Input your Message")
mess.grid(row=4,column=1,sticky=W)

#This is the textbox in which the text needs to be inputed
texto=Text(root,width=50,height=5,wrap=WORD)

#texto=Entry(root)
texto.grid(row=4,column=2)

key=Label(root,text="Enter the key")
key.grid(row=7,column=1,sticky=W)

#This is the entry box receiving the key
code=Entry(root,show="*")
code.grid(row=7,column=2)

#And this button is supposed to call the crypter function upstairs
crypt=Button(root,text="Crypt now",command=crypter,bg="gray")

#crypt.bind("<Button-1>",crypter)
#lambdatest=Button(root,text="OK",command=crypter)
#lambdatest.grid(row=8,column=2)
''' These 3 comments where just some tests to check if the function worked '''
crypt.grid(row=8,column=2)


crypted=Label(root,text="Crypted message")
crypted.grid(row=17,column=1,sticky=W)

#This is the textbox finally getting the encrypted message
Mescod=Text(root,width=50,height=5,wrap=WORD)
Mescod.delete(0.0,END)
#Insert here is used to take the take value in the variable coded and insert it in the textbox
Mescod.insert(0.0,coded)
Mescod.grid(row=17,column=2)

           
root.mainloop()

