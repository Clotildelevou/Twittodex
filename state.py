import os


def get_state_file():
    path = "data/state/state.txt"
    if os.path.exists(path):
        return path
    file = open(path, "w")
    file.close()
    return path


def save_state(national_number, path):
    file = open(path, "a")
    file.write(str(national_number) + "\n")
    file.close()


def get_state(path):
    file = open(path, "r")
    poke_list = []
    for line in file:
        poke_list.append(int(line))

    return poke_list
