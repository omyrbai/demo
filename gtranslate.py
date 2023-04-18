import googletrans
from googletrans import Translator
#lib install pip install googletrans

print(googletrans.LANGUAGES)
translator = Translator()
text = "this is a sample text"
print(translator.detect(text))
