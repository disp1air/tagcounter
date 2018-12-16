import yaml

try:
    synonyms_dict = yaml.load(open("address.yaml"))
except Exception:
    synonyms_dict = {
        'ya': 'ya.ru',
        'ydx': 'yandex.ru',
        'ggl': 'google.com',
        'onl': 'onliner.by',
        '4pda': '4pda.ru',
        'habr': 'habr.com',
        'git': 'github.com'
    }

def check_synonyms(name):
    if name in synonyms_dict.keys():
        return synonyms_dict[name]
    else:
        return name

    