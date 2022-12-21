from random import randint

#create a list of play options
t = ["x", "y", "S"]

g=0
p=0
e=0
nb=int(input("sasir le nombrebre de repetition"))
for i in range (0,nb+1):
 player1 = t[randint(0,2)]
 player2 = t[randint(0,2)]

 if player1=="x":
    if player2=="x":

        e=e+1
    elif player2=="y":
        g=g+1
    else: 
        p=p+1
 elif player1=="y":
    if player2=="x":  
         p=p+1
    elif player2=="y":
        e=e+1
    else: 
        g=g+1  
 else:
    if player2=="x":        
         g=g+1
    elif player2=="y":
        p=p+1
    else:
        e=e+1
print (" proba gagner:",g/nb)  
print ("proba  perdre:",p/nb)      
print ("proba egalité:",e/nb)        