import requests as uReq
from bs4 import BeautifulSoup as soup 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
import csv



path = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(path)


driver.get('https://www.j-archive.com/')
# driver.get('https://www.j-archive.com/showseason.php?season=29')


def find_num_episodes(seasonNumber):

    driver.get('https://www.j-archive.com/showseason.php?season={x}'.format(x = seasonNumber))

    i = 1
    while True:

        try:
            contestant =driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr[{number}]/td[2]".format(number = i)) 
            i += 1
        except:
            break


    #returns number of episodes in a season
    return i 

def write_list_to_file(contestant_list):
    with open('JeopardyOccupationsDraft4.txt', 'w') as filehandle:
        for listitem in contestant_list:
            filehandle.write('%s\n' % listitem)

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

def get_occupations_from_list(contestant_list):
    occupations_list = []
    
    for contestant in contestant_list:
        occupations_list.append(get_occupation(contestant))

    write_list_to_file(occupations_list)

def get_contestant_name(line):
    
    line_list = []

    line_list.append(line)

    list_split = line_list[0].split()
    
    name = list_split[:2]

    name = ' '.join(map(str, name))

    name = name[:-1]

    return name

def main_function(seasonNumber):
    
    

    contestant_list = []
    name_list = []
    



    i = 2
    while i <= seasonNumber+1:

        season_link = driver.find_element_by_xpath("/html/body/table/tbody/tr/td/p[2]/a[{number}]".format(number = i))


        season_link.click()



        num_episodes = find_num_episodes(i-1)
        x = 1
        while x < num_episodes:

            #within a season
            episode_link = driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr[{number}]/td[1]/a".format(number = x))
            episode_link.click()

            contestants = driver.find_elements_by_class_name('contestants')



            for item in contestants:
                
                contestant_line = item.text

                contestant_name = get_contestant_name(contestant_line)

                if contestant_name in name_list:
                    continue
                else:
                    # print(contestant_line)
                    contestant_list.append(contestant_line)
                    name_list.append(contestant_name)

            driver.back()
            x += 1
        driver.back()
        i += 1
    

    occupations_list = []

    for contestant in contestant_list:
        occupations_list.append(get_occupation(contestant))

    write_list_to_file(occupations_list)
        


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





if __name__ == "__main__":
    main_function(1)
    # find_num_episodes(20)


    # with open('contestantList.txt', 'r') as filehandle:
    #     for line in filehandle:
    #         get_occupation(line)



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



    for key, value in sorted_dict.items():
        print(key, " : ", value)
    