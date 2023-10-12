import csv 





dictionary = {}





with open('JeopardyOccupationsDraft4.txt', 'r') as file:
    for line in file:
        line = line.rstrip("\n")

        if line not in dictionary:
            dictionary[line] = 1
        elif line == " ":
            continue
        else:
            dictionary[line] += 1
        



sorted_dict = {}
sorted_keys = sorted(dictionary, key = dictionary.get)

for w in sorted_keys:
    sorted_dict[w] = dictionary[w]




writer = csv.writer(open("dictOutput.csv", "w"))

for key, val in sorted_dict.items():
    writer.writerow([key,val])




# for key, value in sorted_dict.items():
#     print(key, " : ", value)