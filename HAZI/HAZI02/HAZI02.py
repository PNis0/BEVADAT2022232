
import numpy as np


#FONTOS!!!

# CSAK OTT LEHET HASZNÁLNI FOR LOOP-OT AHOL A FELADAT KÜLÖN KÉRI!
# [1,2,3,4] --> ezek az értékek np.array-ek. Ahol listát kérek paraméterként ott külön ki fogom emelni!
# Ha végeztél a feladatokkal, akkor notebook-ot alakítsd át .py.
# A FÁJLBAN CSAK A FÜGGVÉNYEK LEGYENEK! (KOMMENTEK MARADHATNAK)


# Írj egy olyan fügvényt, ami megfordítja egy 2d array oszlopait. Bemenetként egy array-t vár.
# Be: [[1,2],[3,4]]
# Ki: [[2,1],[4,3]]
# column_swap()


def column_swap(array:np.array)->np.array:
    return np.fliplr(array)


# Készíts egy olyan függvényt ami összehasonlít két array-t és adjon vissza egy array-ben, hogy hol egyenlőek 
# Pl Be: [7,8,9], [9,8,7] 
# Ki: [1]
# compare_two_array()
# egyenlő elemszámúakra kell csak hogy működjön


def compare_two_array(arr1:np.array, arr2:np.array)->np.array:
    equals = np.equal(arr1, arr2)    
    equal_indexes = np.where(equals)[0]    
    return equal_indexes


# Készíts egy olyan függvényt, ami vissza adja string-ként a megadott array dimenzióit:
# Be: [[1,2,3], [4,5,6]]
# Ki: "sor: 2, oszlop: 3, melyseg: 1"
# get_array_shape()
# 3D-vel még műküdnie kell!, 


def get_array_shape(arr:np.array)->np.array:
    shape = np.shape(arr)
    if len(shape) == 1:
        return "sor: {}, oszlop: {}, melyseg: 1".format(shape[0], 1, 1)
    elif len(shape) == 2:
        return "sor: {}, oszlop: {}, melyseg: 1".format(shape[0], shape[1], 1)
    elif len(shape) == 3:
        return "sor: {}, oszlop: {}, melyseg: {}".format(shape[0], shape[1], shape[2])
    else:
        return "A tömb dimenziója nem támogatott"


# Készíts egy olyan függvényt, aminek segítségével elő tudod állítani egy neurális hálózat tanításához szükséges pred-et egy numpy array-ből. 
# Bementként add meg az array-t, illetve hogy mennyi class-od van. Kimenetként pedig adjon vissza egy 2d array-t, ahol a sorok az egyes elemek. Minden nullákkal teli legyen és csak ott álljon egyes, ahol a bementi tömb megjelöli. 
# Pl. ha 1 van a bemeneten és 4 classod van, akkor az adott sorban az array-ban a [1] helyen álljon egy 1-es, a többi helyen pedig 0.
# Be: [1, 2, 0, 3], 4
# Ki: [[0,1,0,0], [0, 0, 1, 0], [1, 0, 0, 0], [0, 0, 0, 1]]
# encode_Y()


def encode_Y(arr:np.array, num_classes) ->np.array:
    encoded_arr = np.zeros((len(arr), num_classes))
    for i in range(len(arr)):
        encoded_arr[i][arr[i]] = 1
    return encoded_arr


# A fenti feladatnak valósítsd meg a kiértékelését. Adj meg a 2d array-t és adj vissza a decodolt változatát
# Be:  [[0,1,0,0], [0, 0, 1, 0], [1, 0, 0, 0], [0, 0, 0, 1]]
# Ki:  [1, 2, 0, 3]
# decode_Y()


def decode_Y(y:np.array) ->np.array:
    decoded_y = np.argmax(y, axis=1)
    return decoded_y


# Készíts egy olyan függvényt, ami képes kiértékelni egy neurális háló eredményét! Bemenetként egy listát és egy array-t és adja vissza azt az elemet, aminek a legnagyobb a valószínüsége(értéke) a listából.
# Be: ['alma', 'körte', 'szilva'], [0.2, 0.2, 0.6]. # Az ['alma', 'körte', 'szilva'] egy lista!
# Ki: 'szilva'
# eval_classification()


def eval_classification(labels, predictions:np.array)->np.array:
    max_index = np.argmax(predictions)
    return labels[max_index]


# Készíts egy olyan függvényt, ahol az 1D array-ben a páratlan számokat -1-re cseréli
# Be: [1,2,3,4,5,6]
# Ki: [-1,2,-1,4,-1,6]
# replace_odd_numbers()


def replace_odd_numbers(arr:np.array)->np.array:
    new_arr = np.copy(arr)
    new_arr[arr % 2 == 1] = -1
    
    return new_arr


# Készíts egy olyan függvényt, ami egy array értékeit -1 és 1-re változtatja, attól függően, hogy az adott elem nagyobb vagy kisebb a paraméterként megadott számnál.
# Ha a szám kisebb mint a megadott érték, akkor -1, ha nagyobb vagy egyenlő, akkor pedig 1.
# Be: [1, 2, 5, 0], 2
# Ki: [-1, 1, 1, -1]
# replace_by_value()


def replace_by_value(arr:np.array, value)->np.array:
    arr = np.where(arr < value, -1, 1)
    return arr


# Készíts egy olyan függvényt, ami egy array értékeit összeszorozza és az eredményt visszaadja
# Be: [1,2,3,4]
# Ki: 24
# array_multi()
# Ha több dimenziós a tömb, akkor az egész tömb elemeinek szorzatával térjen vissza


def array_multi(arr:np.array)->np.array:
    return np.prod(arr)


# Készíts egy olyan függvényt, ami egy 2D array értékeit összeszorozza és egy olyan array-el tér vissza, aminek az elemei a soroknak a szorzata
# Be: [[1, 2], [3, 4]]
# Ki: [2, 12]
# array_multi_2d()


def array_multi_2d(arr:np.array)->np.array:
    return np.product(arr, axis=1)


# Készíts egy olyan függvényt, amit egy meglévő numpy array-hez készít egy bordert nullásokkal. Bementként egy array-t várjon és kimenetként egy array jelenjen meg aminek van border-je
# Be: [[1,2],[3,4]]
# Ki: [[0,0,0,0],[0,1,2,0],[0,3,4,0],[0,0,0,0]]
# add_border()



def add_border(arr:np.array)->np.array:
    rows, cols = arr.shape
    new_arr = np.zeros((rows + 2, cols + 2))
    new_arr[1:-1, 1:-1] = arr
    
    return new_arr


# A KÖTVETKEZŐ FELADATOKHOZ NÉZZÉTEK MEG A NUMPY DATA TYPE-JÁT!


# Készíts egy olyan függvényt ami két dátum között felsorolja az összes napot és ezt adja vissza egy numpy array-ben. A fgv ként str vár paraméterként 'YYYY-MM' formában.
# Be: '2023-03', '2023-04'  # mind a kettő paraméter str.
# Ki: ['2023-03-01', '2023-03-02', .. , '2023-03-31',]
# list_days()


from datetime import datetime, timedelta

def list_days(start, end):
    start_date = datetime.strptime(start, '%Y-%m')
    end_date = datetime.strptime(end, '%Y-%m')

    days = np.array([], dtype='datetime64[D]')

    while start_date <= end_date:
        days = np.concatenate([days, np.array([np.datetime64(start_date)])])
        start_date += timedelta(days=1)

    return days.astype('datetime64[D]').astype(str)


# Írj egy fügvényt ami vissza adja az aktuális dátumot az alábbi formában: YYYY-MM-DD. Térjen vissza egy 'numpy.datetime64' típussal.
# Be:
# Ki: 2017-03-24
# get_act_date()


def get_act_date():
    return np.datetime64('today')


# Írj egy olyan függvényt ami visszadja, hogy mennyi másodperc telt el 1970 január 01. 00:02:00 óta. Int-el térjen vissza
# Be: 
# Ki: másodpercben az idó, int-é kasztolva
# sec_from_1970()


def sec_from_1970():
    epoch_start = np.datetime64('1970-01-01T00:00:00')
    now = np.datetime64('now')
    return int((now - epoch_start).astype('int64') / 10**9)


