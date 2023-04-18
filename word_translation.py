from googletrans import Translator
from main import ReadTxt

read_txt_file = ReadTxt()
words_dict = read_txt_file.read_file()
translator = Translator()

for key, value in words_dict.items():
    translated_text = translator.translate(key, dest='ru', src='en')
    print(translated_text.src)

