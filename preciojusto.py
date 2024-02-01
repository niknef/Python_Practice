import random
from requests_html import HTMLSession
from speak_listen import speak


def main():
    speak("Bienvenido al precio justo, vamos a intentar "
          "adivinar los precios de algunos productos")
    session = HTMLSession()
    url = "https://www.pccomponentes.com/"
    main_site = session.get(url)
    categories = main_site.html.find(".mkt-menu-level3")
    category = random.choice(categories)

    while category.text == "Configurador de PCs":
        category = random.choice(categories)

    product_page = session.get(category.attrs["href"])


if __name__ == "__main__":
    main()