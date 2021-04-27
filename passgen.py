from random import choice
from time import sleep 
import os.path
def passgen(x):
    number=[str(xy) for xy in range(0,10)]
    string=list("abcdefghijklmnopqrstuvwxyz")
    string2=[xz.upper() for xz in string ]
    char=list("@!#$%=&*+<>?")
    num=[x for x in range(0,4)]
    newpass=[]
    for y in range(1,x+1):
        numturn=choice(num)
        if numturn==0:
            newpass.append(choice(string))
        elif numturn==1:
            newpass.append(choice(number))
        elif numturn==2:
            newpass.append(choice(char))
        elif numturn==3:
            newpass.append(choice(string2))
            numturn*=0
        else:
            None
    return "".join(newpass)

def mainbegin():
    inputrept=int(input("How many password do you want? (In number): "))
    inputlong=int(input("How long the password do you want?(In number n min 6) : "))
    assert inputlong>=6 ,"the length of password must be more than 6 "
    passcollect=[]
    print("Please wait few minutes to gain passwords")
    sleep(float(inputrept))
    for reptturn in range(1,inputrept+1):
        if reptturn==1:
            print("*"*inputlong)
            print(passgen(inputlong))
            passcollect.append(passgen(inputlong))
        else:
            print(passgen(inputlong))
            passcollect.append(passgen(inputlong))
    print("")     
    print("*"*inputlong)
    save=False
    while save==False:
        if os.path.isfile(yourfileTxt)==True:
            print("The file exists")
            inputin=input("do you want to replace the rexent txt ? (Y/N) \n")
            if inputin.upper()=="Y":
                print("Please wait ")
                sleep(4)
                with open(yourfileTxt,"w") as file2:
                    for read in passcollect:
                        file2.write(read+"\n")
                save=True
                print("the saving process is finished")
            elif inputin.upper()=="N":
                print("Please wait ")
                sleep(4)
                with open(yourfileTxt,"a+") as file:
                    for read in passcollect:
                        file.write(read+"\n")
                save=True
                print("the saving process is finished")
            else:
                print("Invalid")
                save=False
        else:
            print("file is not existed")
            print("Please wait")
            sleep(4)
            with open(yourfileTxt,"w+") as file2:
                for read in passcollect:
                    file2.write(read+"\n")
            save=True
            print("the saving process is finished")
    return passcollect 
mainbegin()