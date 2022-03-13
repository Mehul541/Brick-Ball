from math import floor
import string
from unittest import result
ball=1


def stage():
    for i in range(0,size):
        for j in range(0,size):
            if(i==0 or j==0 or j==size-1):
                li[i][j]="W"
            elif(i==size-1 and not(j==size-1) and not(j==floor(size/2))):
                li[i][j]="G"
            elif(i==size-1 and j==floor(size/2)):
                li[i][j]="o"

def display():
    for i in li:
        for j in i:
            print(j,end=" ")
        print()
    print("Ball count is ",ball,".",sep="")

def brick():
    binput=list(map(int,input("Enter the brick's position and brick type\n (1,2,3,4 for DE,5 for DS):")))
    li[binput[0]][binput[1]]=binput[2]
    cont=input("Do you want to continue(Y or N)?")
    if cont=='Y':
        brick()
    elif cont=='N':
        global ball
        ball=int(input("Enter ball count:"))


def direction():
    d=input("Enter the direction in which the ball needs to traverse:")
    if d=="ST":
        for i in range(size-2,-1,-1):
            j=floor(size/2)
            if destroy(i,j)==1:
                return
            if i==0:
                global ball
                ball-=1

    elif d=="LD":
        i=size-1
        j=floor(size/2)
        count=0
        while count<2:
            i-=1
            j-=1
            if destroy(i,j)==1:
                return
            elif li[i][j]=='W':
                count+=1
                while count<2:
                    if destroy(i,j)==1:
                        return
                    elif li[i][j]=='W':
                        count+=1
                        break
                    else:
                        j-=1
        if count==2:
            ball-=1
                   
    elif d=="RD":
        i=size-1
        j=floor(size/2)
        count=0
        while count<2:
            i+=1
            j+=1
            if destroy(i,j)==1:
                return
            elif li[i][j]=='W':
                count+=1
                while count<2:
                    if destroy(i,j)==1:
                        return
                    elif li[i][j]=='W':
                        count+=1
                        break
                    else:
                        j+=1
        if count==2:
            ball-=1
    
def destroy(i,j):
    if li[i][j]==5:
        li[i][j]=" "
        li[i][j-1]=" "
        li[i][j+1]=" "
        li[i-1][j]=" "
        li[i-1][j-1]=" "
        li[i-1][j+1]=" "
        li[i+1][j]=" "
        li[i+1][j-1]=" "
        li[i+1][j+1]=" "
        return 1
    elif li[i][j]==4:
        li[i][j]=" "
        li[i][j-1]=" "
        li[i][j+1]=" "
        return 1
    elif li[i][j]==3:
        li[i][j]=2
        return 1
    elif li[i][j]==2:
        li[i][j]=1
        return 1
    elif li[i][j]==1:
        li[i][j]=" "
        return 1

def result():
    count=0
    for i in li:
        for j in i:
            if j not in('W','G','o',' '):
                count+=1
            if count>0:
                return True
    print("You won")
    return False

if __name__=="__main__":
    size=int(input("Enter size of NXN matrix:"))
    li=[[" " for __ in range(size)] for _ in range(size)] 
    stage()
    brick()
    display()
    while result():
        direction()
        display()
        if ball==0:
            print("Game over")
            break