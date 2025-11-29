from mac import load_text_from_url, URL_SOURCE
from reg import extract_mac_addresses

def show_menu():
    # Выбор пользователя
    print("Выберите режим работы:")
    print("  1 — Проверить MAC-адрес, при вводе с консоли")
    print("  2 — Найти все корректные MAC-адреса в тексте с веб-страницы")

def handle_manual_input():
    # Проверка MAC-адреса с консоли
    user_text = input("Введите строку для проверки: ")
    found = extract_mac_addresses(user_text)

    if found:
        print("Обнаружены корректные MAC-адреса:")
        print(*found, sep="\n")
    else:
        print("Корректных MAC-адресов не найдено.")

def handle_url_input():
    # Проверка корректных MAC-адресов с сайта
    content = load_text_from_url(URL_SOURCE)

    if not content:
        print("Не удалось загрузить данные по указанному адресу.")
        return

    found = extract_mac_addresses(content)

    if found:
        print("MAC-адреса, найденные на странице:")
        print(*found, sep="\n")
    else:
        print("Страница не содержит корректных MAC-адресов.")

def main():
    # Меню пользователя
    show_menu()
    choice = input("Введите номер пункта: ")

    if choice == "1":
        handle_manual_input()
    elif choice == "2":
        handle_url_input()
    else:
        print("Введён неверный номер. Попробуйте снова.")

if __name__ == "__main__":
    main()
