import pandas
from matplotlib import pyplot as plt


def get_pokemon_info(national_number):
    pokemon_database = pandas.read_csv("data/pokemon.csv")
    return pokemon_database.loc[national_number]


def get_pokemon_pic(national_number):
    return "data/pokemon/" + str(national_number + 1) + ".png"


def get_pokemon_stats(national_number):
    return "data/stats/" + str(national_number + 1) + "_stats.png"


def build_desc(national_number):
    poke_data = get_pokemon_info(national_number)
    text = ""

    if poke_data.is_legendary == 1:
        text += "𝙇𝙚𝙜𝙚𝙣𝙙𝙖𝙧𝙮 𝙋𝙤𝙠𝙚𝙢𝙤𝙣\n"

    text += "Name: " + poke_data.english_name + ", " + poke_data.japanese_name + " N°" + str(national_number + 1) + "\n"

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


def get_weakness_color(value):
    case = lambda x: value == x
    if case(0):
        col = 'dimgray'
    elif case(0.25):
        col = 'forestgreen'
    elif case(0.50):
        col = 'greenyellow'
    elif case(1):
        col = 'white'
    elif case(2):
        col = 'orange'
    elif case(4):
        col = "indianred"
    else:
        col = 'dimgray'
    return col


def build_stats(national_number):
    poke_data = get_pokemon_info(national_number)

    # x-coordinates of left sides of bars
    left = [1, 2, 3, 4, 5, 6]
    height = [poke_data.attack, poke_data.defense, poke_data.hp, poke_data.sp_attack, poke_data.sp_defense,
              poke_data.speed]
    tick_label = ['Attack', 'Defense', 'HP', 'SpAttack', 'SpDefense', 'Speed']

    # clears plot
    plt.clf()

    # sets limits for same size graphs
    plt.ylim(0, 255)
    plt.autoscale(False)

    # plotting a bar chart
    plt.bar(left, height, tick_label=tick_label,
            width=0.8, color=[get_stat_color(poke_data.attack), get_stat_color(poke_data.defense),
                              get_stat_color(poke_data.hp), get_stat_color(poke_data.sp_attack),
                              get_stat_color(poke_data.sp_defense), get_stat_color(poke_data.speed)])

    # naming the y-axis
    plt.ylabel('Value')

    # plot title
    plt.title(poke_data.english_name + ' stats')

    # save as png image
    plt.savefig("data/stats/" + str(poke_data.pokedex_number) + "_stats")


def build_weaknesses(national_number):
    poke_data = get_pokemon_info(national_number)
    plt.clf()

    columns = ['against_bug', 'against_dark', 'against_dragon', 'against_electric', 'against_fairy', 'against_fight',
               'against_fire', 'against_flying', 'against_ghost', 'against_grass', 'against_ground', 'against_ice',
               'against_normal', 'against_poison', 'against_psychic', 'against_rock', 'against_steel', 'against_water']

    cell_info = [[poke_data.against_bug, poke_data.against_dark, poke_data.against_dragon, poke_data.against_electric,
                 poke_data.against_fairy, poke_data.against_fight, poke_data.against_fire, poke_data.against_flying,
                 poke_data.against_ghost, poke_data.against_grass, poke_data.against_ground, poke_data.against_ice,
                 poke_data.against_normal, poke_data.against_poison, poke_data.against_psychic, poke_data.against_rock,
                 poke_data.against_steel, poke_data.against_water]]

    cell_color = [[get_weakness_color(poke_data.against_bug), get_weakness_color(poke_data.against_dark),
                  get_weakness_color(poke_data.against_dragon), get_weakness_color(poke_data.against_electric),
                  get_weakness_color(poke_data.against_fairy), get_weakness_color(poke_data.against_fight),
                  get_weakness_color(poke_data.against_fire), get_weakness_color(poke_data.against_flying),
                  get_weakness_color(poke_data.against_ghost), get_weakness_color(poke_data.against_grass),
                  get_weakness_color(poke_data.against_ground), get_weakness_color(poke_data.against_ice),
                  get_weakness_color(poke_data.against_normal), get_weakness_color(poke_data.against_poison),
                  get_weakness_color(poke_data.against_psychic), get_weakness_color(poke_data.against_rock),
                  get_weakness_color(poke_data.against_steel), get_weakness_color(poke_data.against_water)]]

    cell_text = []
    for i in range(0, len(cell_info[0])):
        cell_text.append(str(cell_info[0][i]))

    fig, ax = plt.subplots(1, 1)
    ax.axis('tight')
    ax.axis('off')
    ax.table(cell_text, colLabels=columns, loc='center')
    plt.show()
