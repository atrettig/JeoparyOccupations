



def get_occupation(contestant_string):
    
    # print("Original: ", contestant_string)

        
    
    new_string = contestant_string.split('from')
    new_string = new_string[0].split('originally')
    new_string = new_string[0].split(',')

    # print(new_string)


    # print(new_string)

    # print("Final: ",new_string[1])
    # print("\n---------------------------------\n")

    return new_string[1]



def get_contestant_name(line):
    
    line_list = []

    line_list.append(line)

    list_split = line_list[0].split()
    
    name = list_split[:2]

    name = ' '.join(map(str, name))

    name = name[:-1]

    return name



with open('contestantList.txt', 'r') as filehandle:
    contestant_list = []
    name_list = []
    for line in filehandle:

        contestant_name = get_contestant_name(line)

        if contestant_name in name_list:
            continue

        else: 
            contestant_list.append(line)
            name_list.append(contestant_name)
    
    for item in contestant_list:
        print(item)


