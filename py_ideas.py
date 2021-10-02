import random, io, os

path = "py_idea_list.txt"

silent = True

def read_ideas():
    return open(path, "r").readlines()

def wipe_ideas():
    if(os.path.exists(path)):
        os.remove(path)

def add_idea(idea):
    f = open(path, "a+")
    f.write(idea+"\n")
    f.flush()
    f.close()
    if(not silent):
        print("-\nIdea added\n\n"+idea+"\n-")

print("\nh for help\n\nType anything to add it as an idea.\n")
while True:
    if(not os.path.exists(path)):
        c = input("The file does not exist at the moment.\nQuit (q) or create the file (c) to hold ideas? ")
        c = c.lower()
        if(c == "q"):
           break
        elif(c == "c"):
            open(path, "w")
            print("The file has been created and it is empty.")
        else:
            print("Tou entered an invalid option.")
            continue
    c = input(":")
    if(not len(c) < 3):
        add_idea(c)
        continue
    c = c.lower()
    if(c in ["q","quit","e","exit"]):
        break
    elif (c in ["h","help","-h","-help","--h","--help"]):
        silentplaceholder = "On"
        if(not silent):
            silentplaceholder = "Off"
        print("-Command Help-\n* r to read ideas\n* s to toggle silent mode ("+silentplaceholder+")\n* c! to delete the file.\n* q to quit")
        continue
    elif (c == "c!"):
        print("Clearing file...")
        wipe_ideas()
    elif (c == "r"):
        print("")
        for idea in read_ideas():
            print(" "+idea)
        continue
    elif(c == "s"):
        silent = not silent
    elif (len(c) > 0):
        print(" Invalid command. Your idea should have a minimum length of 3 characters.")
        continue
    else:
        continue
    print(" - Done!")
