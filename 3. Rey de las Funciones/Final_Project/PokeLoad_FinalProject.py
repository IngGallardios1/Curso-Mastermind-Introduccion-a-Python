import os
import pickle

from requests_html import HTMLSession

URL_BASE = "https://www.pokexperto.net/index2.php?seccion=nds/nationaldex/movimientos_nivel&pk="
pokemon_base = {
    "name": "",
    "current_health": 100,
    "base_health": 100,
    "level": 1,
    "type": None,
    "current_exp": 0,
    "attacks": None
}


def barr_progres(index):
    os.system("cls")
    porcen = int(index*100/150)
    n_diferencia = 10
    n_porcen = int(porcen/10)
    n_diferencia -=n_porcen
    barra=("""Cargando los pokemos en la base de datos: \n|{}{}|""".format("*"*n_porcen," "*n_diferencia,))
    print("{}  {}%, {} de 150 pokemos completado".format(barra,porcen,index))


def get_pokemon(index):
    url = "{}{}".format(URL_BASE, index)
    session = HTMLSession()
    pokemon_page = session.get(url)
    new_pokemon = pokemon_base.copy()

    new_pokemon["name"] = pokemon_page.html.find('.mini', first=True).text.split('\n')[0]
    new_pokemon["type"] = []
    new_pokemon["attacks"] = []

    for img in pokemon_page.html.find('.pkmain', first=True).find(".bordeambos", first=True).find("img"):
        new_pokemon["type"].append(img.attrs["alt"])

    for attack_item in pokemon_page.html.find(".pkmain")[-1].find("tr .check3"):
        attack = {
            "name": attack_item.find("td", first=True).find("a", first=True).text,
            "type": attack_item.find("td")[1].find("img", first=True).attrs["alt"],
            "min_level": attack_item.find("th", first=True).text,
            "damage": int(attack_item.find("td")[3].text.replace("--", "0")),
        }
        new_pokemon["attacks"].append(attack)
    return new_pokemon


def get_all_pokemons():
    try:
        with open("pokefile.pkl", "rb") as pokefile:
            all_pokemons = pickle.load(pokefile)
        print("Lista cargada")
    except FileNotFoundError:
        all_pokemons = []
        for index in range(150):
            barr_progres(index)
            all_pokemons.append(get_pokemon(index + 1))
        with open("pokefile.pkl", "wb") as pokefile:
            pickle.dump(all_pokemons, pokefile)
    return all_pokemons