import pandas
from matplotlib import pyplot as plt


def get_pokemon_info(national_number):
    pokemon_database = pandas.read_csv("data/pokemon.csv")
    return pokemon_database.loc[national_number]


def get_pokemon_pic(national_number):
    return "data/pokemon/" + str(national_number + 1) + ".png"


def build_desc(national_number):
    poke_data = get_pokemon_info(national_number)
    text = ""

    if poke_data.is_legendary == 1:
        text += "𝙇𝙚𝙜𝙚𝙣𝙙𝙖𝙧𝙮 𝙋𝙤𝙠𝙚𝙢𝙤𝙣\n"

    text += "Name: " + poke_data.english_name + ", " + poke_data.japanese_name + " N°" + str(national_number) + "\n"

    text += "Classification: " + poke_data.classification + "\n"

    text += "Type : " + poke_data.type1
    if poke_data.type2 != "NaN":
        text += ", " + poke_data.type2
    text += "\n"

    text += poke_data.english_name + " appeared in generation " + str(poke_data.generation) + ", weights " \
            + str(poke_data.weight_kg) + "kgs and is " + str(poke_data.height_m) + " meters height." + "\n"

    if poke_data.percentage_male < 50.0:
        text += "There are more females than males in the nature.\n"
    elif poke_data.percentage_male == 50.0:
        text += "There are as much females as males in the nature.\n"
    else:
        text += "There are less females than males in the nature.\n"

    return text


def get_stat_color(value):
    case = lambda x: value < x
    if case(50):
        col = 'darkred'
    elif case(80):
        col = 'indianred'
    elif case(100):
        col = 'orange'
    elif case(110):
        col = 'gold'
    elif case(120):
        col = 'greenyellow'
    elif case(200):
        col = "forestgreen"
    else:
        col = 'dimgray'
    return col


def build_stats(national_number):
    poke_data = get_pokemon_info(national_number)

    # x-coordinates of left sides of bars
    left = [1, 2, 3, 4, 5, 6]

    # heights of bars
    height = [poke_data.attack, poke_data.defense, poke_data.hp, poke_data.sp_attack, poke_data.sp_defense,
              poke_data.speed]

    # labels for bars
    tick_label = ['Attack', 'Defense', 'HP', 'SpAttack', 'SpDefense', 'Speed']

    # plotting a bar chart
    plt.bar(left, height, tick_label=tick_label,
            width=0.8, color=[get_stat_color(poke_data.attack), get_stat_color(poke_data.defense),
                              get_stat_color(poke_data.hp), get_stat_color(poke_data.sp_attack), get_stat_color(poke_data.sp_defense),
                              get_stat_color(poke_data.speed)])

    # naming the y-axis
    plt.ylabel('Value')
    # plot title
    plt.title(poke_data.english_name + ' stats')

    # function to show the plot
    plt.show()
