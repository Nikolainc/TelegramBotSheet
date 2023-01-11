from data_provider import ReadSheetData, WriteSheetData
from datetime import datetime

def GetSheetData(user, start = datetime.strptime("01.01.1970","%d.%m.%Y")):
    return GetMessageForSend(CreateDataView(user, start))

def AddToSheetData(msg, user):
    result = msg.split()
    data = CreateDataView(user, start = datetime.strptime("01.01.1970","%d.%m.%Y"))
    data.append((str(result[1]), " ".join(result[2:])))
    WriteSheetData(user, data)

def DelFromSheetData(msg, user):
    result = msg.split()
    data = CreateDataView(user, start = datetime.strptime("01.01.1970","%d.%m.%Y"))
    new_data = []
    for i in range(len(data)):
        if i == int(result[1]):
            continue
        else:
            new_data.append(data[i])
    WriteSheetData(user, new_data)

def CreateDataView(user, start):
    data = ReadSheetData(user)
    new_data = []
    for i in range(len(data)):
        if data[i] != "":
            new_data.append(data[i].split(";"))
        else:
            continue
    return SelectDataByTime(new_data, start)

def SelectDataByTime(data, start):
    data_for_view = []
    for j in range(len(data)):
        if start < datetime.strptime(data[j][0],"%d.%m.%y"):
            data_for_view.append(data[j])
    for i in data_for_view:
        i = str(i)
    return data_for_view

def GetMessageForSend(data):
    msg = f'Расписание сформировано в {datetime.now().strftime("%d.%m.%y %H:%M:%S")}\n\n'
    for i in range(len(data)):
        msg += f'Запись N{i}\n'
        msg += str(data[i][0]) + '\n'
        msg += str(data[i][1]) + '\n\n'
    return msg
