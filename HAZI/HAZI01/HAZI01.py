
#Készíts egy függvényt ami paraméterként egy listát vár és visszatér ennek a listának egy rész listájával.
#Paraméterként lehessen megadni, hogy mettől-meddig akarjuk visszakapni a listát.
#Egy példa a bemenetre: input_list=[1,2,3,4,5], start=1, end=4
#Egy példa a kimenetre: [2,3,4]
#NOTE: ha indexelünk és 4-et adunk meg felső határnak akkor csak a 3. indexig kapjuk vissza az értékeket a 4. már nem lesz benne
#NOTE: és ez az elvárt viselkedés ebben a feladatban is
#return type: list
#függvény neve legyen: subset


input_list=[1,2,3,4,5] 
start=1 
end=4

def subset(input_list,start,end):
    output_list=[]
    for index in range(start,end,1):
        output_list.append(input_list[index])
    return output_list


#Készíts egy függvényt ami egy listát vár paraméterként és ennek a listának minden n-edik elemét adja vissza.
#Paraméterként lehessen állítani azt hogy hanyadik elemeket szeretnénk viszakapni.
#NOTE: a 0. elem is legyen benne
#Egy példa a bemenetre: input_list=[1,2,3,4,5,6,7,8,9], n=3
#Egy példa a kimenetre: [1,4,7]
#return type: list
#függvény neve legyen: every_nth


input_list=[1,2,3,4,5,6,7,8,9] 
n=3

def every_nth(input_list):
    output_list=[]
    for index in range(len(input_list)):
        if(index%n==0):
            output_list.append(input_list[index])
    return output_list


#Készíts egy függvényt ami paraméterként egy listát vár és eldönti, hogy a listában csak egyedi értékek vannak-e
#Egy bool-al térjen vissza: True:csak egyedi értékek vannak benne, False:van benne ismétlődés
#Egy példa a bemenetre: [1,2,3,4,5,6,7]
#Egy példa a kimenetre: True
#return type: bool
#függvény neve legyen: unique


numbers = [1,2,3,4,5,6,7]

def unique(numbers:list):
    numbers.sort()
    for i in range(len(numbers)-1):
        if(numbers[i]==numbers[i+1]):
            return False
    return True


#Készíts egy függvényt ami paraméterként egy 2 dimenziós listát vár és ezt a listát kitudja "lapítani"
#Egy olyan listával térjen vissza amelyben nincsen több kisebb lista, azaz egy egy dimenziós listával.
#Egy példa a bemenetre: [[1,2],[3,4],[5,6]]
#Egy példa a kimenetre: [1,2,3,4,5,6]
#NOTE: csak 2 dimenziós listát kezeljen nem kell ennél mélyebbet
#return type: list
#függvény neve legyen: flatten


input_list=[[1,2],[3,4],[5,6]]

def flatten(input_list):
    output_list=[]
    for i in input_list:
        for j in i:
            output_list.append(j)
    return output_list


#Készíts egy függvényt ami paraméterként n darab listát vár, és összfűzi ezeket a listákat.
#Egy olya listával térjen vissza ami 1 dimenziós és tartalmazza az össze bemeneti lista kértékét
#NOTE: sorrend nem számít
#HINT: használj *args-ot az input paraméternél
#Egy példa a bemenetre: lista_1 = [1,2,3], lista_2 = [4,5,6], ..... lista_n = [7,8,9]
#Egy példa a kimenetre: [1,2,3,4,5,6,7,8,9]
#return type: list
#függvény neve legyen: merge_lists


lista_1 = [1,2,3]
lista_2 = [4,5,6]
lista_3 = [7,8,9]

def merge_lists(*arg):
    output_list=[]
    for i in arg:
        output_list.extend(i)
    return output_list


#Készíts egy függvényt ami paraméterként egy listát vár amiben 2 elemet tartalmazó tuple-ök vannak,
#és visszatér ezeknek a tuple-nek a fordítottjával.
#Egy példa a bemenetre: [(1,2),(3,4)]
#Egy példa a kimenetre: [(2,1),(4,3)] 
#return type: list
#függvény neve legyen: reverse_tuples


input_list=[(1,2),(3,4)]

def reverse_tuples(input_list):
    output_list=[]
    for i in input_list:
       x,y = i
       output_list.append((x,y))
    return output_list


#Készíts egy függvényt ami paraméterként egy listát vár, és eltávolítja az ismétlődéseket a listából.
#Egy olyan listával térjen vissza amiben csak a bemeneti lista egyedi értékei vannak benne.
#Egy példa a bemenetre: [1,2,3,3,4,5]
#Egy példa a kimenetre: [1,2,3,4,5]
#return type: list
#függvény neve legyen: remove_duplicates


input_list=[1,2,3,3,4,5]

def remove_duplicates(input_list):
    return list(dict.fromkeys(input_list))


#Készíts egy olyan függvényt ami paraméterként egy 2 dimenziós mátrixot vár és visszater a mátrix transzponáltjával.
#Egy példa a bemenetre: [[1,2,3],
#                        [4,5,6],
#                        [7,8,9]]
#
#Egy példa a kimenetre: [[1,4,7],
#                        [2,5,8],
#                        [3,6,9]]
#return type: list
#függvény neve legyen: transpose


input_mtx=[[1,2,3],
           [4,5,6],
           [7,8,9]]

def transpose(input_mtx):
    return [[input_mtx[j][i] for j in range(len(input_mtx))] for i in range(len(input_mtx[0]))]



#Készíts egy függvényt ami paraméterként egy listát vár és visszatér a lista csoportosított változatával.
#Egy olyan listával térjen vissza amiben a paraméterként átadott chunk_size méretű listák vannak.
#Egy példa a bemenetre: [1,2,3,4,5,6,7,8]
#Egy példa a kimenetre: [[1,2,3],[4,5,6],[7,8]]
#NOTE: ha nem mindegyik lista elemet lehet chunk_size méretű listába tenni akkor a maradékot a példában látott módon kezeljétek
#return type: list
#függvény neve legyen: split_into_chunks


input_list = [1,2,3,4,5,6,7,8]
chunk_size = 3

def split_into_chunks(input_list, chunk_size):
    output_list = []
    tmp_list =[]
    count = 0
    for i in range(len(input_list)):        
        if (count == chunk_size):
            count = 0
            output_list.append(tmp_list)
            tmp_list = [] 

        tmp_list.append(input_list[i])
        count = count+1

        if (i == len(input_list) - 1):
            output_list.append(tmp_list)

    return output_list 


#Készíts egy függvényt ami paraméterként n darab dictionary-t vár és visszatér egy darab dictionary-vel.
#Egy olyan dict-el térjen vissza miben az n darab bemeneti dict értékei benne vannak.
#Egy példa a bemenetre: dict_1: {"one":1,"two":2}, dict_2: {"four":4,"three":3}
#Egy példa a kimenetre: {"one":1,"two":2,"four":4,"three":3}
#HINT: használj *args-ot
#függvény neve legyen: merge_dicts


dict_1= {"one":1,"two":2}
dict_2= {"four":4,"three":3}

def merge_dicts(*args):
    output_dict:dict={}
    for i in args:
        output_dict.update(i)
    return output_dict


#Készíts egy függvényt ami paraméterként egy listát vár amiben egész számok vannak és visszatér egy dict-el amiben szét vannak szedve paritás szerint.
#Egy példa a bemenetre: [1,2,3,4,5,6]
#Egy példa a kimenetre: {"event":[2,4,6],"odd":[1,3,5]}
#return type: dict
#függvény neve legyen: by_parity


input_list=[1,2,3,4,5,6]

def by_parity(input_list):
    output_dict={}
    for i in input_list:
        if(i%2==0):
            output_dict["even"]=i
        else:
            output_dict["odd"]=i
    return output_dict


#Készíts egy függvényt ami paraméterként egy dict-et vár és visszatér egy dict-el amiben az egyes kulcsokhoz tartozó értékek átlaga van.
#Egy példa a bemenetre:{"some_key":[1,2,3,4],"another_key":[1,2,3,4]}
#Egy példa a kimenetre: {"some_key":2.5,"another_key":2.5}
#return type: dict
#függvény neve legyen: mean_key_value


input_dict={"some_key":[1,2,3,4],"another_key":[1,2,3,4]}

def mean_key_value(input_dict):
    output_dict={}
    for key,value in input_dict.items():
        output_dict[key]= sum(value)/len(value)
    return output_dict


