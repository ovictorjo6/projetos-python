from translate import Translator
#pip install translate

translator = Translator(from_lang='pt-br',to_lang='english')

palavra = input('Qual a palavra deseja traduzir? ')

#enter the text to translate
result = translator.translate(palavra) 
print(result)
