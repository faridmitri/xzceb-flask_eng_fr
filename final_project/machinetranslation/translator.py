"""
module
"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

APIKEY = os.environ['apikey']
URL = os.environ['url']

authenticator = IAMAuthenticator(APIKEY)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(URL)

def EnglishToFrench(englishText):
    """A dummy docstring."""
    if englishText == '':
        return ''
    translation = language_translator.translate(englishText,
     model_id='en-fr').get_result()
    frenchText=translation['translations'][0]['translation']
    return frenchText

def FrenchToEnglish(frenchText):
    """A dummy docstring."""
    if frenchText == '':
        return ''
    translation = language_translator.translate(frenchText, model_id='fr-en').get_result()
    englishText=translation['translations'][0]['translation']
    return englishText
