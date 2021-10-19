import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def EnglishToFrench(english_text):
    if english_text== '':
        return ''
    translation = language_translator.translate(
    english_text,
    model_id='en-fr').get_result()
    french_text=translation['translations'][0]['translation']
    return french_text

def FrenchToEnglish(french_text):
    if french_text== '':
        return ''
    translation = language_translator.translate(
    french_text,
    model_id='fr-en').get_result()
    english_text=translation['translations'][0]['translation']
    return english_text
