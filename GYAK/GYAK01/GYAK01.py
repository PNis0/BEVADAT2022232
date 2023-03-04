
#Készíts egy olyan függvényt ami paraméterként egy listát vár amiben egész számok vannak, 
#és el kell döntenie,hogy van-e benne páratlan szám. A visszatérésí érték egy bool legyen (True:van benne,False:nincs benne)
#Egy példa a bemenetre: [1,2,3,4,4,5]
#Egy példa a kimenetre: True
#return type: bool
#függvény neve legyen: contains_odd


numbers = [1,2,3,4,4,5]

def contains_odd(numbers):
    for index in numbers:
        if (index % 2 == 1):
            return True
    return False


#Készíts egy függvényt ami paraméterként egy listát vár amiben egész számok vannak,
#és eldönti minden eleméről, hogy páratlan-e. A kimenet egy lista legyen amiben True/False értékek vannak.
#Egy példa a bemenetre: [1,2,3,4,5]
#Egy példa a kimenetre: [True,False,True,False,True]
#return type: list
#függvény neve legyen: is_odd


numbers = [1,2,3,4,5]

def is_odd(numbers):
    list = []
    for index in numbers:
        if(index % 2 == 0):
            list.append(False)
        else:
            list.append(True)
    return list


#Készíts egy függvényt ami paraméterként 2 db listát vár, és kiszámolja a listák elemenként vett összegét.
#A függvény egy listával térjen vissza amiben a megfelelő indexen lévő lista_1 és lista_2 elemek összege van.
#Egy példa a bemenetekre: input_list_1:[1,2,3,4], input_list_2:[1,2,3,4]
#Egy példa a kimenetre: [2,3,4,8]
#return type: list
#függvény neve legyen: element_wise_sum


input_list_1=[1,2,3,4] 
input_list_2=[1,2,3,4]

def element_wise_sum(list1,list2):
    result = []
    for index in range(len(list1)):
        result.append(list1[index] + list2[index])
    return result



#Készíts egy függvényt ami paraméterként egy dictionary-t vár és egy listával tér vissza
#amiben a kulcs:érték párok egy Tuple-ben vannak.
#Egy példa a bemenetere: {"egy":1,"ketto":2,"harom":3}
#Egy példa a kimenetre: [("egy",1),("ketto",2),("harom",3)]
#return type: list
#függvény nevel egyen: dict_to_list


bemenet = {"egy":1,"ketto":2,"harom":3}

def dict_to_list(input: dict):
    result = []
    for key, value in input.items():
        result.append((key,value))
    return result


