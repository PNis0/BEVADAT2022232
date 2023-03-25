
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


'''
FONTOS: Az első feladatáltal visszaadott DataFrame-et kell használni a további feladatokhoz. 
A függvényeken belül mindig készíts egy másolatot a bemenő df-ről, (new_df = df.copy() és ezzel dolgozz tovább.)
'''


'''
Készíts egy függvényt, ami egy string útvonalat vár paraméterként, és egy DataFrame ad visszatérési értékként.

Egy példa a bemenetre: 'test_data.csv'
Egy példa a kimenetre: df_data
return type: pandas.core.frame.DataFrame
függvény neve: csv_to_df
'''



def csv_to_df(file_path: str) -> pd.DataFrame:
    return pd.read_csv(file_path)


'''
Készíts egy függvényt, ami egy DataFrame-et vár paraméterként, 
és átalakítja azoknak az oszlopoknak a nevét nagybetűsre amelyiknek neve nem tartalmaz 'e' betüt.

Egy példa a bemenetre: df_data
Egy példa a kimenetre: df_data_capitalized
return type: pandas.core.frame.DataFrame
függvény neve: capitalize_columns
'''


def capitalize_columns(df):
    new_df = df.copy()
    new_columns = []
    for col in new_df.columns:
        if 'e' not in col:
            new_columns.append(col.upper())
        else:
            new_columns.append(col)
    df_capitalized = new_df.copy()
    df_capitalized.columns = new_columns
    return df_capitalized


'''
Készíts egy függvényt, ahol egy szám formájában vissza adjuk, hogy hány darab diáknak sikerült teljesíteni a matek vizsgát.
(legyen az átmenő ponthatár 50).

Egy példa a bemenetre: df_data
Egy példa a kimenetre: 5
return type: int
függvény neve: math_passed_count
'''


def math_passed_count(df):
    new_df = df.copy()
    return len(new_df[new_df['math score'] >= 50])


'''
Készíts egy függvényt, ahol Dataframe ként vissza adjuk azoknak a diákoknak az adatait (sorokat), akik végeztek előzetes gyakorló kurzust.

Egy példa a bemenetre: df_data
Egy példa a kimenetre: df_did_pre_course
return type: pandas.core.frame.DataFrame
függvény neve: did_pre_course
'''


def did_pre_course(df):
    new_df = df.copy()
    df_did_pre_course = new_df[new_df['test preparation course'] == 'completed']
    return df_did_pre_course


'''
Készíts egy függvényt, ahol a bemeneti Dataframet a diákok szülei végzettségi szintjei alapján csoportosításra kerül,
majd aggregációként vegyük, hogy átlagosan milyen pontszámot értek el a diákok a vizsgákon.

Egy példa a bemenetre: df_data
Egy példa a kimenetre: df_average_scores
return type: pandas.core.frame.DataFrame
függvény neve: average_scores
'''


def average_scores(df):
    new_df = df.copy()
    df_avg_scores = new_df.groupby('parental level of education').mean()
    return df_avg_scores


'''
Készíts egy függvényt, ami a bementeti Dataframet kiegészíti egy 'age' oszloppal, töltsük fel random 18-66 év közötti értékekkel.
A random.randint() függvényt használd, a random sorsolás legyen seedleve, ennek értéke legyen 42.

Egy példa a bemenetre: df_data
Egy példa a kimenetre: df_data_with_age
return type: pandas.core.frame.DataFrame
függvény neve: add_age
'''


import random

def add_age(df):
    random.seed(42)
    age = [random.randint(18, 67) for _ in range(len(df))]
    df_with_age = df.copy()
    df_with_age['age'] = age
    return df_with_age


'''
Készíts egy függvényt, ami vissza adja a legjobb teljesítményt elérő női diák pontszámait.

Egy példa a bemenetre: df_data
Egy példa a kimenetre: (99,99,99) #math score, reading score, writing score
return type: tuple
függvény neve: female_top_score
'''


def female_top_score(df):
    female_df = df[df['gender'] == 'female']
    top_score = female_df[['math score', 'reading score', 'writing score']].max()
    return tuple(top_score)


'''
Készíts egy függvényt, ami a bementeti Dataframet kiegészíti egy 'grade' oszloppal. 
Számoljuk ki hogy a diákok hány százalékot ((math+reading+writing)/300) értek el a vizsgán, és osztályozzuk őket az alábbi szempontok szerint:

90-100%: A
80-90%: B
70-80%: C
60-70%: D
<60%: F

Egy példa a bemenetre: df_data
Egy példa a kimenetre: df_data_with_grade
return type: pandas.core.frame.DataFrame
függvény neve: add_grade
'''


def add_grade(df):
    df_data = df.copy()

    total_scores = df_data['math score'] + df_data['reading score'] + df_data['writing score']
    
    percentages = total_scores / 300
    
    df_data['grade'] = ''
    
    df_data.loc[percentages >= 0.9, 'grade'] = 'A'
    df_data.loc[(percentages >= 0.8) & (percentages < 0.9), 'grade'] = 'B'
    df_data.loc[(percentages >= 0.7) & (percentages < 0.8), 'grade'] = 'C'
    df_data.loc[(percentages >= 0.6) & (percentages < 0.7), 'grade'] = 'D'
    df_data.loc[percentages < 0.6, 'grade'] = 'F'
    
    return df_data


'''
Készíts egy függvényt, ami a bemeneti Dataframe adatai alapján elkészít egy olyan oszlop diagrammot,
ami vizualizálja a nemek által elért átlagos matek pontszámot.

Oszlopdiagram címe legyen: 'Average Math Score by Gender'
Az x tengely címe legyen: 'Gender'
Az y tengely címe legyen: 'Math Score'

Egy példa a bemenetre: df_data
Egy példa a kimenetre: fig
return type: matplotlib.figure.Figure
függvény neve: math_bar_plot
'''


def math_bar_plot(df_input):
    df = df_input.copy()
    avg_math_by_gender = df.groupby('gender')['math score'].mean()

    fig, ax = plt.subplots()
    ax.bar(avg_math_by_gender.index, avg_math_by_gender.values)

    ax.set_title('Average Math Score by Gender')
    ax.set_xlabel('Gender')
    ax.set_ylabel('Math Score')

    return fig


''' 
Készíts egy függvényt, ami a bemeneti Dataframe adatai alapján elkészít egy olyan histogramot,
ami vizualizálja az elért írásbeli pontszámokat.

A histogram címe legyen: 'Distribution of Writing Scores'
Az x tengely címe legyen: 'Writing Score'
Az y tengely címe legyen: 'Number of Students'

Egy példa a bemenetre: df_data
Egy példa a kimenetre: fig
return type: matplotlib.figure.Figure
függvény neve: writing_hist
'''


def writing_hist(df):
    df_data = df.copy()
    fig, ax = plt.subplots()
    ax.hist(df_data['writing score'], bins=10)
    
    ax.set_title('Distribution of Writing Scores')
    ax.set_xlabel('Writing Score')
    ax.set_ylabel('Number of Students')
    
    return fig


''' 
Készíts egy függvényt, ami a bemeneti Dataframe adatai alapján elkészít egy olyan kördiagramot,
ami vizualizálja a diákok etnikum csoportok szerinti eloszlását százalékosan.

Érdemes megszámolni a diákok számát, etnikum csoportonként,majd a százalékos kirajzolást az autopct='%1.1f%%' paraméterrel megadható.
Mindegyik kör szelethez tartozzon egy címke, ami a csoport nevét tartalmazza.
A diagram címe legyen: 'Proportion of Students by Race/Ethnicity'

Egy példa a bemenetre: df_data
Egy példa a kimenetre: fig
return type: matplotlib.figure.Figure
függvény neve: ethnicity_pie_chart
'''



def ethnicity_pie_chart(df):
    df_data = df.copy()
    count_by_ethnicity = df_data['race/ethnicity'].value_counts()
    
    fig, ax = plt.subplots()
    ax.pie(count_by_ethnicity, labels=count_by_ethnicity.index, autopct='%1.1f%%')
    
    ax.set_title('Proportion of Students by Race/Ethnicity')
    
    return fig


