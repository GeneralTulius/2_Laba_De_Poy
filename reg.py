import re

# Регулярные выражения для MAC-адресов
MAC_PATTERN = re.compile(
    r"\b(?:"
        r"(?:[0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}"
        r"|"
        r"(?:[0-9A-Fa-f]{2}-){5}[0-9A-Fa-f]{2}"
        r"|"
        r"[0-9A-Fa-f]{12}"
        r"|"
        r"(?:[0-9A-Fa-f]{4}\.){2}[0-9A-Fa-f]{4}"
    r")\b"
)

def extract_mac_addresses(text):
    # Возвращает все корректные MAC-адреса из текста.
    matches = re.finditer(MAC_PATTERN, text)
    return [m.group() for m in matches]


if __name__ == "__main__":
    # Пример проверки
    sample_text = "MAC: 01:23:45:67:89:AB и 1234.5678.9ABC"
    print(extract_mac_addresses(sample_text))
