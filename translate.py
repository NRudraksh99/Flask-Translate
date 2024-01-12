from googletrans import Translator

def ChangeLang(og,i_lang,t_lang):
    try:
        t=Translator()
        translation=t.translate(og,src=i_lang,dest=t_lang)
        return translation.text
    except:
        return "Error Occured...."

