import csv
import json

def csv_reader(filename):
    with open(filename, 'r') as file:
        reader = csv.DictReader(file, delimiter=',')
        return_list = []
        for row in reader:
            return_list.append(row)
    return return_list

def json_saver(list, filename):
    with open(filename, 'w') as file:
        json.dump(list, file, indent=4)

# def data_transformer(input_filename, output_filename, key, value):
#     csv_data = csv_reader(input_filename)
#     for row in csv_data:
#         row[key] = value
#     json_saver(csv_data, output_filename)


def data_transformer(input_filename, output_filename, key, value, csv_read_func, json_save_func):
    csv_data = csv_read_func(input_filename)
    for row in csv_data:
        row[key] = value
    json_save_func(csv_data, output_filename)

def test_data_transformer():
    def mock_csv_reader(arg):
        return [{'Name': 'Ben', 'Age': '26', 'Job': 'Consultant'}, {'Name': 'Bill', 'Age': '26', 'Job': 'Flowerpot Man'}]
    def mock_json_saver(list, filename):
        return

    data_transformer('dwaawdwdawdadwa-inj.csv', 'dawwdawwda-inj.json', "NumberOfPets", "0", mock_csv_reader, mock_json_saver)

test_data_transformer()
# data_transformer('dependency-inj.csv', 'dependency-inj.json', "NumberOfPets", "0", csv_reader, json_saver)
# testlist = csv_reader('dependency-inj.csv')
# json_saver(testlist, 'dependency-inj.json')