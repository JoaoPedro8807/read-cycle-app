from googletrans import Translator

def translate_term(term: str, lang:str) -> str:
    """ method to translate the dianmic data, default django translate does not fit to do it """
    try:
        str_request = type(term)
        translator = Translator()
        return translator.translate(term, dest=lang)
    except Exception as e:
        print('ERRO AO TRADUZIR: ', e)
        return None

