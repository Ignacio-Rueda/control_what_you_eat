import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def Mcdonalds():
    df = pd.read_csv("fastfood.csv")

    #>>>>>Seleccionar todos los datos de Mcdonalds
    Mcdonalds = df[df["restaurant"]=="Mcdonalds"]
    #>>>>>Ordenar comidas de Mcdonalds por calorías:
    #Mcdonalds = Mcdonalds.set_index("item")
    #Mcdonalds = Mcdonalds.sort_values(by="item")
    #cabecera= Mcdonalds.columns.to_list()
    #>>>>>GRÁFICO
    calories = Mcdonalds["calories"][:]
    item = Mcdonalds ["item"][:]
    font={
        'family':'Arial',
        'weight':'bold',
        'size':10
    }
    plt.rc('font',**font)
    plt.title("Nutritional information (Mcdonalds)")
    plt.xlabel("Calories")

    plt.xticks()
    plt.ylabel("Menu")
    
   
    bar = plt.barh(item,calories)
    
    #>>Set position graphic 
    plt.subplots_adjust(left=0.2)
    #plt.show()



    Mcdonalds = Mcdonalds.sort_values(by="calories")
    

    
    #fila1=Mcdonalds.loc[380]
    #todasFilas=Mcdonalds.values
    #Introduzco una nueva coloumna que contiene una enumeración
    Mcdonalds.insert(loc=0,column="position",value=range(1,Mcdonalds.shape[0]+1))
    values = Mcdonalds.loc[:,["position","item","calories"]]
    values = values.to_numpy().tolist()
    #Utilizamos iloc para acceder a los datos a través de la posición númerica de las filas y las columnas
    position=Mcdonalds.loc[Mcdonalds['position']==1,"vit_c"].iloc[0]
    print(position)
   
    print(Mcdonalds)
    print(position)

    headings=["Position","Menu","Calories"]

    return headings,values

    
Mcdonalds()