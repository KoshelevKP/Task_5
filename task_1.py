import requests

def translate_it(file_in, file_out, language_in, language_out = 'ru'):

    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    key = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'

    language = language_in + '-' + language_out

    with open(file_in, encoding='utf-8') as f:
      text = f.read()

    params = {
        'key': key,
        'lang': language,
        'text': text,
    }
    response = requests.get(url, params=params).json()

    with open(file_out, 'w') as f:
      f.write(' '.join(response.get('text', [])))

    return ' '.join(response.get('text', []))


a = translate_it('DE.txt','OUT_DE-RU.txt','de')
print(a)
print('--------------------------------------------------')
a = translate_it('ES.txt','OUT_ES-RU.txt','es')
print(a)
print('--------------------------------------------------')
a = translate_it('FR.txt','OUT_FR-RU.txt','fr')
print(a)
