# -*- coding: utf-8 -*-
"""Actividad 1 // analisis exploratorio

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12XxIwJrI2dE6E-aiyf6FYHJI_GPYBSSC
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df=pd.read_csv("listings.csv")

df.info()

df["host_acceptance_rate"] = df["host_acceptance_rate"].str.replace("%","")
df["price"] = df["price"].str.replace("$","")
df["price"] = df["price"].str.replace(",","")


df["room_type"] = df["room_type"].str.replace("Entire home/apt","1")
df["room_type"] = df["room_type"].str.replace("Hotel room","2")
df["room_type"] = df["room_type"].str.replace("Private room","3")
df["room_type"] = df["room_type"].str.replace("Shared room","4")

df2 = df[['host_acceptance_rate','price','availability_365','number_of_reviews',
          'review_scores_rating','review_scores_cleanliness','review_scores_communication', 'room_type']]
df2.head()

df2['host_acceptance_rate'] = pd.to_numeric(df2['host_acceptance_rate'],errors = 'coerce')
df2['price'] = pd.to_numeric(df2['price'],errors = 'coerce')
df2['room_type'] = pd.to_numeric(df2['room_type'],errors = 'coerce')
df2.info()

dfn =df2.fillna(round(df.mean(),1))
dfn.head()

dfn = df2.fillna(method="bfill")
dfn.head()

sns.set_style('whitegrid')

plt.figure(dpi = 100, figsize = (50,70)) #resolucion
mask = np.triu(np.ones_like(df.corr(), dtype = bool))

sns.heatmap(df.corr(), mask = mask, annot = True)
plt.title('Correlation Heatmap')

y=dfn

percentile25=y.quantile(0.25) #Q1
percentile75=y.quantile(0.75) #Q3
iqr= percentile75 - percentile25

Limite_Superior_iqr= percentile75 + 8.5*iqr
Limite_Inferior_iqr= percentile25 - 8.5*iqr
print("Limite superior permitido: \n", Limite_Superior_iqr)
print("Limite inferior permitido: \n", Limite_Inferior_iqr)

df3= dfn[(y<=Limite_Superior_iqr)&(y>=Limite_Inferior_iqr)]
df3

df4=df3.copy()
df4=df4.fillna(round(df3.mean(),1))
df4= df4.dropna()
valores_nulos=df4.isnull().sum().sum()
valores_nulos

plt.figure(dpi = 80, figsize = (10,10)) #resolucion
mask = np.triu(np.ones_like(df4.corr(), dtype = bool))

sns.heatmap(df4.corr(), mask = mask, annot = True)
plt.title('Correlation Heatmap')

#Entire home = 1
entire_home = df4[df4['room_type'] == 1]
print(entire_home)
cor1 = entire_home.corr()

#hotel room = 2
hotel_room = df4[df4['room_type'] == 2]
print(hotel_room)
cor2 = hotel_room.corr()

#private_room
private_room = df4[df4['room_type'] == 3]
print(private_room)
cor3 = private_room.corr()

#shared room
shared_room= df4[df4['room_type'] == 4]
print(shared_room)
cor4 = shared_room.corr()

"""##Entire home"""

sns.scatterplot(x='number_of_reviews', y='host_acceptance_rate', color="orange", data=entire_home)
print('Coeficiente de correlacion: ',cor1['number_of_reviews']['host_acceptance_rate'])

sns.scatterplot(x='number_of_reviews', y='review_scores_rating', color="purple", data=entire_home)
print('Coeficiente de correlacion: ',cor1['number_of_reviews']['review_scores_rating'])

sns.scatterplot(x='number_of_reviews', y='price', color="green", data=entire_home)
print('Coeficiente de correlacion: ',cor1['number_of_reviews']['price'])

sns.scatterplot(x='number_of_reviews', y='review_scores_cleanliness', color="red", data=entire_home)
print('Coeficiente de correlacion: ',cor1['number_of_reviews']['review_scores_cleanliness'])

sns.scatterplot(x='number_of_reviews', y='availability_365', color="purple", data=entire_home)
print('Coeficiente de correlacion: ',cor1['number_of_reviews']['availability_365'])

sns.scatterplot(x='number_of_reviews', y='review_scores_communication', color="blue", data=entire_home)
print('Coeficiente de correlacion: ',cor1['number_of_reviews']['availability_365'])

"""##Hotel room"""

sns.scatterplot(x='number_of_reviews', y='review_scores_communication', color="blue", data=hotel_room)
print('Coeficiente de correlacion: ',cor2['number_of_reviews']['availability_365'])

sns.scatterplot(x='number_of_reviews', y='review_scores_rating', color="purple", data=hotel_room)
print('Coeficiente de correlacion: ',cor2['number_of_reviews']['review_scores_rating'])

sns.scatterplot(x='number_of_reviews', y='price', color="green", data=hotel_room)
print('Coeficiente de correlacion: ',cor2['number_of_reviews']['price'])

sns.scatterplot(x='number_of_reviews', y='review_scores_cleanliness', color="red", data=hotel_room)
print('Coeficiente de correlacion: ',cor2['number_of_reviews']['review_scores_cleanliness'])

sns.scatterplot(x='number_of_reviews', y='availability_365', color="purple", data=hotel_room)
print('Coeficiente de correlacion: ',cor2['number_of_reviews']['availability_365'])

sns.scatterplot(x='number_of_reviews', y='review_scores_communication', color="blue", data=hotel_room)
print('Coeficiente de correlacion: ',cor2['number_of_reviews']['availability_365'])

"""##private_room"""

sns.scatterplot(x='number_of_reviews', y='review_scores_communication', color="blue", data=private_room)
print('Coeficiente de correlacion: ',cor3['number_of_reviews']['availability_365'])

sns.scatterplot(x='number_of_reviews', y='review_scores_rating', color="purple", data=private_room)
print('Coeficiente de correlacion: ',cor3['number_of_reviews']['review_scores_rating'])

sns.scatterplot(x='number_of_reviews', y='price', color="green", data=private_room)
print('Coeficiente de correlacion: ',cor3['number_of_reviews']['price'])

sns.scatterplot(x='number_of_reviews', y='review_scores_cleanliness', color="red", data=private_room)
print('Coeficiente de correlacion: ',cor3['number_of_reviews']['review_scores_cleanliness'])

sns.scatterplot(x='number_of_reviews', y='availability_365', color="purple", data=private_room)
print('Coeficiente de correlacion: ',cor3['number_of_reviews']['availability_365'])

sns.scatterplot(x='number_of_reviews', y='review_scores_communication', color="blue", data=private_room)
print('Coeficiente de correlacion: ',cor3['number_of_reviews']['availability_365'])

"""##shared room"""

sns.scatterplot(x='number_of_reviews', y='review_scores_communication', color="blue", data=shared_room)
print('Coeficiente de correlacion: ',cor4['number_of_reviews']['availability_365'])

sns.scatterplot(x='number_of_reviews', y='review_scores_rating', color="purple", data=shared_room)
print('Coeficiente de correlacion: ',cor4['number_of_reviews']['review_scores_rating'])

sns.scatterplot(x='number_of_reviews', y='price', color="green", data=shared_room)
print('Coeficiente de correlacion: ',cor4['number_of_reviews']['price'])

sns.scatterplot(x='number_of_reviews', y='review_scores_cleanliness', color="red", data=shared_room)
print('Coeficiente de correlacion: ',cor4['number_of_reviews']['review_scores_cleanliness'])

sns.scatterplot(x='number_of_reviews', y='availability_365', color="purple", data=shared_room)
print('Coeficiente de correlacion: ',cor4['number_of_reviews']['availability_365'])

sns.scatterplot(x='number_of_reviews', y='review_scores_communication', color="blue", data=shared_room)
print('Coeficiente de correlacion: ',cor4['number_of_reviews']['availability_365'])

"""##Resumen general"""

print('Correlacion Entire Home: \n',cor1['number_of_reviews'])
print()
print('Correlacion Hotel Room: \n',cor2['number_of_reviews'])
print()
print('Correlacion Private Room: \n',cor3['number_of_reviews'])
print()
print('Correlacion Private Room: \n',cor4['number_of_reviews'])

Vars_Indep= df4[['number_of_reviews']]
Var_Dep= df4[['host_acceptance_rate']]

from sklearn.linear_model import LinearRegression
model= LinearRegression()

model.fit(X=Vars_Indep, y=Var_Dep)
model.score(Vars_Indep,Var_Dep)

y_pred= model.predict(X=df4[['number_of_reviews']])
y_pred

df4.insert(0, 'Predicciones', y_pred)
df4.head()

sns.scatterplot(x='number_of_reviews', y='host_acceptance_rate', color="green", data=df4)
sns.scatterplot(x='number_of_reviews', y='Predicciones', color="orange", data=df4)
coef_Deter=model.score(X=Vars_Indep, y=Var_Dep)

coef_Correl=np.sqrt(coef_Deter)
print("Coeficiente de determinaci??n: ", coef_Deter)
print("Coeficiente de correlaci??n: ", coef_Correl)

"""##EJERCICIO REGRESION PARA BARCELONA"""

df= pd.read_csv("barcelona.csv")
df.head()

df["host_acceptance_rate"] = df["host_acceptance_rate"].str.replace("%","")
df["price"] = df["price"].str.replace("$","")
df["price"] = df["price"].str.replace(",","")

df["room_type"] = df["room_type"].str.replace("Entire home/apt","1")
df["room_type"] = df["room_type"].str.replace("Hotel room","2")
df["room_type"] = df["room_type"].str.replace("Private room","3")
df["room_type"] = df["room_type"].str.replace("Shared room","4")
df.head()

df_numerica = df[['host_acceptance_rate','price','availability_365','number_of_reviews',
          'review_scores_rating','review_scores_cleanliness','review_scores_communication', 'room_type']]
df_numerica.head()

df_numerica['host_acceptance_rate'] = pd.to_numeric(df_numerica['host_acceptance_rate'],errors = 'coerce')
df_numerica['price'] = pd.to_numeric(df_numerica['price'],errors = 'coerce')
df_numerica['room_type'] = pd.to_numeric(df_numerica['room_type'],errors = 'coerce')
df_numerica.info()

df_round =df_numerica.fillna(round(df.mean(),1))
df_round.head()

df_limpia=df_round.fillna(round(df.mean(),1))
df_limpia.head()

sns.set_style('darkgrid')

plt.figure(dpi = 80, figsize = (10,10)) #resolucion
mask = np.triu(np.ones_like(df_limpia.corr(), dtype = bool))

sns.heatmap(df_limpia.corr(), mask = mask, annot = True)
plt.title('Correlation Heatmap')

# Tipo de cuarto 1
cuarto1 = df_limpia[df_limpia['room_type'] == 1]
cuarto1.head()

sns.scatterplot(x='review_scores_rating', y='number_of_reviews', color="orange", data=df_limpia)
sns.scatterplot(x='review_scores_cleanliness', y='number_of_reviews', color="blue", data=df_limpia)
sns.scatterplot(x='review_scores_communication', y='number_of_reviews', color="green", data=df_limpia)

Vars_Indep= df_limpia[['review_scores_rating','review_scores_communication','review_scores_cleanliness']]
Var_Dep= df_limpia['number_of_reviews']

from sklearn.linear_model import LinearRegression
model= LinearRegression()
model.fit(X=Vars_Indep, y=Var_Dep)
model.score(Vars_Indep,Var_Dep)

y_pred= model.predict(X=df_limpia[['review_scores_rating','review_scores_communication','review_scores_cleanliness']])
y_pred

df_limpia.insert(0, 'PM room1', y_pred)
df_limpia.head()

sns.scatterplot(x='review_scores_rating', y='number_of_reviews', color="orange", data=df_limpia)
sns.scatterplot(x='review_scores_rating', y='PM room1', color="green", data=df_limpia)

coef_Deter=model.score(X=Vars_Indep, y=Var_Dep)
coef_Deter

coef_Correl=np.sqrt(coef_Deter)
coef_Correl

# Tipo de cuarto 2
cuarto2 = df_limpia[df_limpia['room_type'] == 2]
cuarto2.head()

sns.scatterplot(x='review_scores_rating', y='number_of_reviews', color="green", data=cuarto2)
sns.scatterplot(x='review_scores_cleanliness', y='number_of_reviews', color="orange", data=cuarto2)
sns.scatterplot(x='review_scores_communication', y='number_of_reviews', color="purple", data=cuarto2)

Vars_Indep= cuarto2[['review_scores_rating','review_scores_communication','review_scores_cleanliness']]
Var_Dep= cuarto2['number_of_reviews']
from sklearn.linear_model import LinearRegression
model= LinearRegression()
model.fit(X=Vars_Indep, y=Var_Dep)

model.score(Vars_Indep,Var_Dep)
y_pred2= model.predict(X=cuarto2[['review_scores_rating','review_scores_communication','review_scores_cleanliness']])
y_pred2

cuarto2.insert(0, 'PM room2', y_pred2)
cuarto2.head()

sns.scatterplot(x='review_scores_rating', y='number_of_reviews', color="orange", data=cuarto2)
sns.scatterplot(x='review_scores_rating', y='PM room2', color="green", data=cuarto2)

coef_Deter=model.score(X=Vars_Indep, y=Var_Dep)
coef_Deter

#Cuarto 3
cuarto3 = df_limpia[df_limpia['room_type'] == 3]
cuarto3.head()

sns.scatterplot(x='review_scores_rating', y='number_of_reviews', color="orange", data=cuarto3)
sns.scatterplot(x='review_scores_cleanliness', y='number_of_reviews', color="pink", data=cuarto3)
sns.scatterplot(x='review_scores_communication', y='number_of_reviews', color="green", data=cuarto3)

Vars_Indep= cuarto3[['review_scores_rating','review_scores_communication','review_scores_cleanliness']]
Var_Dep= cuarto3['number_of_reviews']

from sklearn.linear_model import LinearRegression
model= LinearRegression()

model.fit(X=Vars_Indep, y=Var_Dep)

y_pred3= model.predict(X=cuarto3[['review_scores_rating','review_scores_communication','review_scores_cleanliness']])
y_pred3

cuarto3.insert(0, 'PM room3', y_pred3)
cuarto3.head()

sns.scatterplot(x='review_scores_rating', y='number_of_reviews', color="orange", data=cuarto3)
sns.scatterplot(x='review_scores_rating', y='PM room3', color="green", data=cuarto3)

coef_Deter=model.score(X=Vars_Indep, y=Var_Dep)
coef_Deter

coef_Correl=np.sqrt(coef_Deter)
coef_Correl

"""##EJERCICIO REGRESION PARA GIRONA"""

df= pd.read_csv("girona.csv")
df.head()

df["host_acceptance_rate"] = df["host_acceptance_rate"].str.replace("%","")
df["price"] = df["price"].str.replace("$","")
df["price"] = df["price"].str.replace(",","")

df["room_type"] = df["room_type"].str.replace("Entire home/apt","1")
df["room_type"] = df["room_type"].str.replace("Hotel room","2")
df["room_type"] = df["room_type"].str.replace("Private room","3")
df["room_type"] = df["room_type"].str.replace("Shared room","4")
df.head()

df_numerica = df[['host_acceptance_rate','price','availability_365','number_of_reviews',
          'review_scores_rating','review_scores_cleanliness','review_scores_communication', 'room_type']]
df_numerica.head()

df_numerica['host_acceptance_rate'] = pd.to_numeric(df_numerica['host_acceptance_rate'],errors = 'coerce')
df_numerica['price'] = pd.to_numeric(df_numerica['price'],errors = 'coerce')
df_numerica['room_type'] = pd.to_numeric(df_numerica['room_type'],errors = 'coerce')
df_numerica.info()

df_round =df_numerica.fillna(round(df.mean(),1))
df_round.head()

df_limpia=df_round.fillna(round(df.mean(),1))
df_limpia.head()

sns.set_style('darkgrid')

plt.figure(dpi = 80, figsize = (10,10)) #resolucion
mask = np.triu(np.ones_like(df_limpia.corr(), dtype = bool))

sns.heatmap(df_limpia.corr(), mask = mask, annot = True)
plt.title('Correlation Heatmap')

# Tipo de cuarto 1
cuarto1 = df_limpia[df_limpia['room_type'] == 1]
cuarto1.head()

sns.scatterplot(x='review_scores_rating', y='number_of_reviews', color="orange", data=df_limpia)
sns.scatterplot(x='review_scores_cleanliness', y='number_of_reviews', color="blue", data=df_limpia)
sns.scatterplot(x='review_scores_communication', y='number_of_reviews', color="green", data=df_limpia)

Vars_Indep= df_limpia[['review_scores_rating','review_scores_communication','review_scores_cleanliness']]
Var_Dep= df_limpia['number_of_reviews']

from sklearn.linear_model import LinearRegression
model= LinearRegression()
model.fit(X=Vars_Indep, y=Var_Dep)
model.score(Vars_Indep,Var_Dep)

y_pred= model.predict(X=df_limpia[['review_scores_rating','review_scores_communication','review_scores_cleanliness']])
y_pred

df_limpia.insert(0, 'PM room1', y_pred)
df_limpia.head()

sns.scatterplot(x='review_scores_rating', y='number_of_reviews', color="orange", data=df_limpia)
sns.scatterplot(x='review_scores_rating', y='PM room1', color="green", data=df_limpia)

coef_Deter=model.score(X=Vars_Indep, y=Var_Dep)
coef_Deter

coef_Correl=np.sqrt(coef_Deter)
coef_Correl

# Tipo de cuarto 2
cuarto2 = df_limpia[df_limpia['room_type'] == 2]
cuarto2.head()

sns.scatterplot(x='review_scores_rating', y='number_of_reviews', color="green", data=cuarto2)
sns.scatterplot(x='review_scores_cleanliness', y='number_of_reviews', color="orange", data=cuarto2)
sns.scatterplot(x='review_scores_communication', y='number_of_reviews', color="purple", data=cuarto2)

Vars_Indep= cuarto2[['review_scores_rating','review_scores_communication','review_scores_cleanliness']]
Var_Dep= cuarto2['number_of_reviews']
from sklearn.linear_model import LinearRegression
model= LinearRegression()
model.fit(X=Vars_Indep, y=Var_Dep)

model.score(Vars_Indep,Var_Dep)
y_pred2= model.predict(X=cuarto2[['review_scores_rating','review_scores_communication','review_scores_cleanliness']])
y_pred2

cuarto2.insert(0, 'PM room2', y_pred2)
cuarto2.head()

sns.scatterplot(x='review_scores_rating', y='number_of_reviews', color="orange", data=cuarto2)
sns.scatterplot(x='review_scores_rating', y='PM room2', color="green", data=cuarto2)

coef_Deter=model.score(X=Vars_Indep, y=Var_Dep)
coef_Deter

#Cuarto 3
cuarto3 = df_limpia[df_limpia['room_type'] == 3]
cuarto3.head()

sns.scatterplot(x='review_scores_rating', y='number_of_reviews', color="orange", data=cuarto3)
sns.scatterplot(x='review_scores_cleanliness', y='number_of_reviews', color="pink", data=cuarto3)
sns.scatterplot(x='review_scores_communication', y='number_of_reviews', color="green", data=cuarto3)

Vars_Indep= cuarto3[['review_scores_rating','review_scores_communication','review_scores_cleanliness']]
Var_Dep= cuarto3['number_of_reviews']

from sklearn.linear_model import LinearRegression
model= LinearRegression()

model.fit(X=Vars_Indep, y=Var_Dep)

y_pred3= model.predict(X=cuarto3[['review_scores_rating','review_scores_communication','review_scores_cleanliness']])
y_pred3

cuarto3.insert(0, 'PM room3', y_pred3)
cuarto3.head()

sns.scatterplot(x='review_scores_rating', y='number_of_reviews', color="orange", data=cuarto3)
sns.scatterplot(x='review_scores_rating', y='PM room3', color="green", data=cuarto3)

coef_Deter=model.score(X=Vars_Indep, y=Var_Dep)
coef_Deter

coef_Correl=np.sqrt(coef_Deter)
coef_Correl