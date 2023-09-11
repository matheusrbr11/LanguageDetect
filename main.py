from langdetect import detect
import pycountry

def get_language(language_code):
    language = pycountry.languages.get(alpha_2=language_code)
    return language.name


text = "This is a example."

language = detect(text)
print('The detected language is: {}'.format(get_language(language)))