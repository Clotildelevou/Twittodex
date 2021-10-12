import pandas


def get_pokemon_info(national_number):
    pokemon_database = pandas.read_csv("data/pokemon.csv")
    return pokemon_database.loc[national_number]


def get_pokemon_pic(national_number):
    return "data/pokemon/" + str(national_number + 1) + ".png"


def build_text(national_number):
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

    return text
