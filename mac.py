import requests
from bs4 import BeautifulSoup

# Ссылка на текстовый файл с возможными MAC-адресами
URL_SOURCE = ('https://gist.githubusercontent.com/GeneralTulius/'
              'c2bbd7679c60a1b4f08def8acaa90976/raw/'
              '54c4612d723be233650ffcbf68272c241437e3cd/gist.html'
             )


def load_text_from_url(url):
    # Получает текст страницы по заданному URL
    try:
        response = requests.get(url)
        response.raise_for_status()
        page = response.text
        soup = BeautifulSoup(page, "html.parser")
        return soup.get_text(" ", strip=True)

    except requests.RequestException as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    print(load_text_from_url(URL_SOURCE))
