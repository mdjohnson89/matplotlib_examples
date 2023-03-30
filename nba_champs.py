with open ('nba_champs.csv') as file:
    headers = file.readline()
    data = file.readlines()

data_dict = {}
for line in data:
    to_read = line.split(',')
    if to_read[1] not in data_dict:
        data_dict[to_read[1]] = []
        data_dict[to_read[1]].append(int(to_read[0]))
    else:
        data_dict[to_read[1]].append(int(to_read[0]))

print(data_dict)