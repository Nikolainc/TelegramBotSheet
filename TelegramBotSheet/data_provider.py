from datetime import datetime

def ReadSheetData(user):
    DB = str(user) + '.csv'
    with open(DB, 'r') as file:
        data = file.read().split('\n')
        return data

def WriteSheetData(user, data):
    DB = str(user) + '.csv'
    with open(DB, 'w') as file:
        if data != "":
            for i in range(len(data)):
                file.write(f'{data[i][0]};{data[i][1]}\n')
        else:
            file.write(f'')