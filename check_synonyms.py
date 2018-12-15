import yaml

synonyms_dict = yaml.load(open("address.yaml"))

def check_synonyms(name):
    if name in synonyms_dict.keys():
        return synonyms_dict[name]
    else:
        return name

    