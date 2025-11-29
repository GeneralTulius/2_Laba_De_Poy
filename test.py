import unittest
from reg import extract_mac_addresses
from mac import load_text_from_url

class TestFromMyUrlMac(unittest.TestCase):
    # Проверка работы с URL

    def test_real_url(self):
        # Проверка, что функция возвращает строку или None
        URL_SOURCE = ('https://gist.githubusercontent.com/GeneralTulius/'
                      'c2bbd7679c60a1b4f08def8acaa90976/raw/'
                      '54c4612d723be233650ffcbf68272c241437e3cd/gist.html'
                      )
        result = load_text_from_url(URL_SOURCE)
        self.assertTrue(isinstance(result, (str, type(None))))

    def test_invalid_url(self):
        # Проверка обработки недоступного URL
        url = "https://this-url-does-not-exist-404.com/"
        result = load_text_from_url(url)
        self.assertIsNone(result)


class TestFindMac(unittest.TestCase):
    # Проверка MAC-адресов

    def test_valid_macs(self):
        # Проверка формата и длины (6 групп по 2 шестнадцатеричных цифры(регистр не важен))
        text = "01:23:45:67:89:ab 12-34-56-78-9A-bC 1234.5678.9ABc 123456789ABC"
        results = extract_mac_addresses(text)
        self.assertIn("01:23:45:67:89:ab", results)
        self.assertIn("12-34-56-78-9A-bC", results)
        self.assertIn("1234.5678.9ABc", results)
        self.assertIn("123456789ABC", results)

    def test_invalid_signs_macs(self):
        # Проверка невалидных строк
        # (недопустимый символ, спецсимвол, смешанные разделители)
        text = "00:1G:2B:3C:4D:5E 00:1A:2B:3C:4D:5@ 00:1A-2B:3C-4D:5E"
        results = extract_mac_addresses(text)
        self.assertEqual(results, [])

    def test_invalid_length_macs(self):
        # Проверка невалидных строк (длина, нет символа в группе)
        text = "001A2B3C4D5 0:1A:2B:3C:4D:5E"
        results = extract_mac_addresses(text)
        self.assertEqual(results, [])

    def test_mixed_text(self):
        # Проверка MAC-адреса в тексте
        text = "Запишите: 00-E0-18-C3-11-89 и 00:26:57:00:1f:02"
        results = extract_mac_addresses(text)
        self.assertEqual(results, ["00-E0-18-C3-11-89", "00:26:57:00:1f:02"])

    def test_empty_string(self):
        # Проверка на отсутствие MAC-адреса
        results = extract_mac_addresses("Тут нет MAC-адресов")
        self.assertEqual(results, [])


class TestConsoleInputMac(unittest.TestCase):
    # Проверка с консоли

    def test_manual_input(self):
        # Проверка введенных MAC-адресов
        text = "AA:BB:CC:DD:EE:FF aa:bb:cc:dd:ee:ff"
        results = extract_mac_addresses(text)
        self.assertEqual(results, ["AA:BB:CC:DD:EE:FF", "aa:bb:cc:dd:ee:ff"])


if __name__ == "__main__":
    unittest.main()
