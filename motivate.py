import random
import os


def read_file(file_name):
    """Openning the txt file containing the scriptures
    Args:
        file_name (txt): scriptures text file
    Returns:
        list: List of the scriptures
    """    
    file = open(file_name, "r")
    return file.readlines()

def print_one_verse(scriptures):
    os.system("echo '-------------------------------------------------------------------'")
    os.system("echo '=====Good Morning and Win Today, Win Tomorrow and Win Forever!====='")
    os.system("echo '-------------------------------------------------------------------'")
    list_of_scriptures = []
    for i in scriptures:
        list_of_scriptures.append(i)
    return list_of_scriptures

def select_one_randomly(list_of_scriptures):
    """Selecting the random scripture from the list of the scriptures
    Args:
        list_of_scriptures (list): The list carrying the scriptures
    """    
    message = random.choice(list_of_scriptures)
    mssg = message.split("-")  
    title = mssg[0]
    msg = mssg[1]
    os.system("echo " + title)
    os.system("echo '-----------------------'")
    os.system("echo " + msg)
    os.system("echo '------------------------------------------------------------------'")  


if __name__ == "__main__":
    scriptures_ = "scriptures.txt"
    breakthrough = read_file(scriptures_)
    list_of_verses = print_one_verse(breakthrough)
    select_one_randomly(list_of_verses)
    