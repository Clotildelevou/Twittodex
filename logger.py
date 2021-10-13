import os.path
from datetime import datetime
from colorama import Fore


def gen_logfile():
    id = 1
    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
    path = "data/logs/" + str(id) + "_log.txt"

    while os.path.exists(path):
        id += 1
        path = "data/logs/logger" + str(id) + ".log"

    file = open(path, "x")
    file.write("[CREATION] " + date_time + "\n")
    file.close()

    return path


def pokemon_posted(filename, name):
    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")

    file = open(filename, "a")
    file.write("[BOT] " + date_time + " Posted " + name + "\n")
    file.close()
    print(Fore.GREEN + "[BOT] " + date_time + Fore.RESET + " Posted " + name)


def stats_posted(filename, name):
    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")

    file = open(filename, "a")
    file.write("[BOT] " + date_time + " Posted " + name + " stats.\n")
    file.close()
    print(Fore.GREEN + "[BOT] " + date_time + Fore.RESET + " Posted " + name + " stats.")


def weaknesses_posted(filename, name):
    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")

    file = open(filename, "a")
    file.write("[BOT]" + date_time + " Posted " + name + " weaknesses.\n")
    file.close()
    print(Fore.GREEN + "[BOT] " + date_time + Fore.RESET + " Posted " + name + " weaknesses.")


def err_pokemon_posted(filename, name, error):
    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")

    file = open(filename, "a")
    file.write("[ERROR] " + date_time + "Couldn't post " + name + ": " + error + "\n")
    file.close()
    print(Fore.RED + "[ERROR] " + date_time + Fore.RESET + " Couldn't post " + name + ": " + error)


def err_stats_posted(filename, name, error):
    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")

    file = open(filename, "a")
    file.write("[ERROR] " + date_time + "Couldn't post " + name + "'s stats: " + error + "\n")
    file.close()
    print(Fore.RED + "[ERROR] " + date_time + Fore.RESET + " Couldn't post " + name + "'s stats: " + error)


def err_weaknesses_posted(filename, name, error):
    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")

    file = open(filename, "a")
    file.write("[ERROR] " + date_time + "Couldn't post " + name + "'s weaknesses: " + error + "\n")
    file.close()
    print(Fore.RED + "[ERROR] " + date_time + Fore.RESET + " Couldn't post " + name + "'s weaknesses: " + error)
