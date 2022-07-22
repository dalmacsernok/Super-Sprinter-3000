import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story():
    list = []
    with open(DATA_FILE_PATH, 'r') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for row in reader:
            list.append(row)
    return list


def add_user_story(result):
    with open('data.csv', 'r+') as csvfile:
        id = len(csvfile.readlines())-1
        result['id'] = id
        result['status'] = 'planning'
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames)
        writer.writerow(result)


def update_user_story(result, id):
    datas = get_all_user_story()
    for item in datas:
        if str(item['id']) == str(id):
            datas[id-1] = result
            print("halló")
    with open('data.csv', 'w') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames)
        csvfile.write(",".join(DATA_HEADER)+'\n\n')
        for item in datas:
            writer.writerow(item)
