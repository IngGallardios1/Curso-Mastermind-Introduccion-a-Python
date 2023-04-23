from pprint import pprint
from PokeLoad_FinalProject import get_all_pokemons
import random


def get_player_profile(pokemon_list):
    return {
        "player name": input("Cual es tu nombre?"),
        "pokemon_inventory": [random.choice(pokemon_list) for a in range(3)],
        "combats": 0,
        "pokeballs": 0,
        "health_potion": 0
    }


def any_player_pokemon_lives(player_profile):
    return sum([pokemon["current_health"] for pokemon in player_profile["pokemon_inventory"]]) > 0


def get_pokemon_info(pokemon):
    return "{} | lvl {} | hp {}/{}".format(pokemon["name"],
                                           pokemon["level"],
                                           pokemon["current_health"],
                                           pokemon["base_health"])


def choose_pokemon(player_profile):
    chosen = None
    while not chosen:
        print("Elige el pokemon")
        for index in range(len(player_profile["pokemon_inventory"])):
            print("{} - {}".format(index, get_pokemon_info(player_profile["pokemon_inventory"][index])))
        try:
            return player_profile["pokemon_inventory"][int(input("¿Cual eliges?"))]
        except (ValueError, IndexError):
            print("Opción Invalida")


def player_attack(player_pokemon, enemy_pokemon):
    pass


def enemy_attack(player_pokemon, enemy_pokemon):
    pass


def figth(player_profile, enemy_pokemon):
    print("--> NUEVO COMBATE <--")
    player_pokemon = choose_pokemon(player_profile)
    print("Contrincantes: {} VS {}".format(get_pokemon_info(player_pokemon),
                                           get_pokemon_info(enemy_pokemon)))
    while any_player_pokemon_lives(player_profile) and enemy_pokemon["current_health"] > 0:
        player_attack(player_pokemon, enemy_pokemon)
        enemy_attack(player_pokemon, enemy_pokemon)

    print("--> FIN DEL COMBATE <--")
    input("Presiona ENTER para continuar")


def main():
    pokemon_list = get_all_pokemons()
    player_profile = get_player_profile(pokemon_list)
    # pprint(player_profile)
    while any_player_pokemon_lives(player_profile):
        enemy_pokemon = random.choice(pokemon_list)
        figth(player_profile, enemy_pokemon)
    print("Has perdido en el combate n:{}".format(player_profile["combats"]))


if __name__ == "__main__":
    main()