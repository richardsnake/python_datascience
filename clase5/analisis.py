import pandas as pd

serie = pd.Series([1,"hola",3,False,5,6.0,"Richard",8,9])
print(serie)
dic1 = {
    "nombre" :  "Richard",
    "sexo": "M",
    "edad":  36
}
dic2 = {
    "nombre" :  "Heberth",
    "sexo": "M",
    "edad":  35
}

dic3 = {
    "nombre" :  "Male",
    "sexo": "F",
    "edad":  25
}

df = pd.DataFrame(dic1,dic2,dic3)
print(df)

data = pd.read_csv("base.csv")
print(data.head(10))

frecuencia_sexo = data["Sexo"].value_counts()
frecuencia_sexo_norm = data["Sexo"].value_counts(normalize=True)
print(frecuencia_sexo)

distribucion = pd.DataFrame({"frecuencia": frecuencia_sexo, 
"Procentaje (%)": frecuencia_sexo_norm})
sexo = {0: "Masculino", 1:"Femenino"}
distribucion.rename(index=sexo, inplace=True)
print(distribucion)