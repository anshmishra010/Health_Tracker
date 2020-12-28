# Fitness Management System
# This program makes separate folder for the person.As it enhances the tracking .

client_list = {1:"Ansh", 2:"Pratik", 3:"Prakhar"}  #members name in the dictonary
log_list = {1:"Exercise", 2:"Diet"} # Activity to be tracked

def getdate():
    import datetime
    return datetime.datetime.now()  # to get exact date and time for better activity track.

try:
    print("Select your name : ")
    for key,value in client_list.items():
        print("Press",key,"for",value,"\n",end="")
    client_name = int(input())
    print("Selected name : ",client_list[client_name],"\n",end="")
    print("Press 1 for entry the details : ")
    print("Press 2 for see the details : ")
    op=int(input())

    if op is 1:
        for key,value in log_list.items():
            print("Press ",key," for ",value," details to add ","\n",end="")
        log_name = int(input())
        print("Selected category to add the details ",log_list[log_name])
        f = open(client_list[client_name]+"_"+log_list[log_name]+".txt","a")
        k='y'
        while(k is not "n"):
            print("Enter ",log_list[log_name],"\n",end="")
            mytext=input()
            f.write("[ "+str(getdate())+" ] : "+mytext +"\n")
            k=input("Do you want to add Add More ?y/n")
            continue
        f.close()

    elif op is 2:
        for key,value in log_list.items():
            print("Press ",key," to view ",value,"\n",end="")
        log_name =int(input())
        print(client_list[client_name],"_",log_list[log_name],"Report : ","\n",end="")
        f=open(client_list[client_name]+"_"+log_list[log_name]+".txt")
        contents = f.readlines()
        for line in contents:
            print(line,end="")
        f.close()
    else:
        print("Invalid option ")
except Exception as e:
    print("Wrong input !! ")






