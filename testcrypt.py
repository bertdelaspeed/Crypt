import getpass

i=0
j=0
coded=""

text=[]
text=(input("your text \n"))

key=[]
key=(input("key \n"))
#key=getpass.getpass(prompt='Key \n')

length=len(text)
length2=len(key)

while(i!=length):
    if j==length2:
        j=0
    b=ord(key[j])-ord('a')
   
    if (ord(text[i])+b)<=ord('z'):
        
        c=chr(ord(text[i])+b)
        coded+=c
        
    else:
        c=(ord(text[i])+b)-26
        coded+=chr(c)
   
    i+=1
    j+=1
print (coded)