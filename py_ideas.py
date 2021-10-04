#  Copyright (c) 2021.

import configparser
import os

version = "1.2.0"

config_dir = os.path.expanduser('~') + "/.config/mydea"
os.makedirs(config_dir, 0o777, True)
config_path = config_dir + "/conf.ini"
config = configparser.ConfigParser()
config["DEFAULT"] = {
    "IPath": config_dir + "/py_idea_list.txt",
    "IsSilent": "y"
}
default_config = config["DEFAULT"]


def toggle_silent():
    if config["DEFAULT"]["IsSilent"] == "y":
        config["DEFAULT"]["IsSilent"] = "n"
    else:
        config["DEFAULT"]["IsSilent"] = "y"


def is_silent():
    return config["DEFAULT"]["IsSilent"] == "y"


def update_path():
    config["DEFAULT"]["IPath"] = path


def save_config():
    f = open(config_path, "w")
    config.write(f)
    f.flush()
    f.close()
    print("Config saved.")


def init_config():
    if not os.path.exists(config_path):
        save_config()
        print("The configuration file has been created at:\n\t" + config_path)
    else:
        print("Loading config...")
        config.read(config_path)


init_config()

path = config["DEFAULT"]["IPath"]

if not os.path.exists(path):
    open(path, "w").close()
    print("Idea text file has been created at: \n\t" + path)


def read_ideas():
    return open(path, "r").readlines()


def wipe_ideas():
    if os.path.exists(path):
        os.remove(path)


def add_idea(text):
    f = open(path, "a+")
    f.write(text + "\n")
    f.flush()
    f.close()
    if not is_silent():
        print("-\nIdea added\n\n" + text + "\n-")


print("\nWelcome to mydea " + version + "!\nh for help\n\n")
while True:
    while not os.path.exists(path):
        c = input("The file could not be found (" + path + ")."
                  + "\nType c to create a blank replacement with the same path"
                  + " or q to quit.\n:")
        c = c.lower()
        if c == "q":
            break
        elif c == "c":
            open(path, "w").close()
            print("The file has been created and it is empty. Entering default idea space. Type h for help.")
        elif c == "h":
            print("- Options -\n* q to quit."
                  + "\n* c to create the file.")
        else:
            print("Tou entered an invalid option.")
            continue
    c = input(":")
    if not len(c) < 3:
        add_idea(c)
        continue
    c = c.lower()
    if c in ["q", "quit", "e", "exit"]:
        break
    elif c in ["h", "help", "-h", "-help", "--h", "--help"]:
        silentPlaceholder = "On"
        if not is_silent():
            silentPlaceholder = "Off"
        print("-Help-\nType a sentence to add it as an idea, or type a"
              + "\nletter from the list below to execute a command."
              + "\n-Commands-\n* r to read ideas"
              + "\n* p to change the global file path for ideas"
              + "\n* s to toggle silent mode (" + silentPlaceholder
              + ")\n* c! to delete the file."
              + "\n* q to quit")
        continue
    elif c == "p":
        print("Changing the system-wide filepath to store ideas in..."
              + "\nThe current path is " + path)
        c = input("Enter the new path in full or type c to cancel.")
        c = c.lower()
        if c == "c":
            print("Operation cancelled.")
        else:
            if not os.path.exists(c):
                try:
                    open(c, "w")
                    print("Successfully created the file!"
                          + " You are now using the file " + c)
                    path = c
                    update_path()
                except OSError:
                    print("Error! Could not create the file!"
                          + " Make sure any directories exist.")
            else:
                print("Successfully switched to " + c)
                path = c
                update_path()
        continue

    elif c == "c!":
        print("Clearing file...")
        wipe_ideas()
    elif c == "r":
        print("")
        for idea in read_ideas():
            print(" " + idea)
        continue
    elif c == "s":
        toggle_silent()
    elif len(c) > 0:
        print(" Invalid command. Your idea should have a minimum length of 3 characters.")
        continue
    else:
        continue
    print(" - Done!")

print("Saving settings...")
save_config()
