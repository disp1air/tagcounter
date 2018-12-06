import pickle

def write_data_keys_to_file(filename, data):
    with open(filename, 'wb') as f:
        pickle.dump(tuple(data.keys()), f)

def write_data_values_to_file(filename, data):
    with open(filename, 'wb') as f:
        pickle.dump(tuple(data.values()), f)

def read_data_from_file(filename):
    with open(filename, 'rb') as k:
        data = pickle.load(k)
    return data


