# PROYECTO-ML PROYECTO INDIVIDUAL Nº1

## INTRODUCCIÓN


### Debemos hacer un proyecto poniéndonos en el papel de un MLOps Engineer. 
### Tendremos que comenzar desde cero, haciendo un trabajo de Data Engineer. Crearemos luego un modelo de machine learning que cree un sistema de recomendación de películas, para lo cual desarrollaremos una API que nos proporciona información, en base a funcionalidades de películas. 

## FUENTES DE DATOS
###  **- Dataset** : el cual incluye dos archivos que debemos importar y luego procesar(movies_dataset.csv y credits.csv)
### **- Diccionario de datos** : con algunas descripciones de las columnas que están disponibles en el dataset. [Fuente de datos](https://drive.google.com/drive/u/0/folders/18MPjjrabzfi6nt8Ijmznp2VFjlO_Rhvq)

## TRANSFORMACIONES ETL
### **Dentro de las solicitadas:** 
### - Desanidado de datos de algunas de las columnas del dataset para su uso en las consultas de la API, creando las columnas que sean necesarias con los datos extraídos de las mismas
### - Rellena con 0 los valores nulos de algunas de las columnas.
### - Eliminación de valores nulos
### - Llevar la columna de fechas al formato AAAA-mm-dd y extraer en otra columna el año de esas fechas
### - Crearemos una columna llamada return con las columnas budget y revenue.
### Eliminaremos todas las columnas que no necesitaremos para nuestro análisis 

## ANÁLISIS EXPLORATORIO DE LOS DATOS - EDA
### Con este análisis trataremos de comprender la relación que existe entre las varialbes del dataset, buscando outliers, creando una matriz de correlación para un mejor análisis de los datos. También haremos un análisis estadístico así como la visualización de diferentes gráficos.

## DESARRLLO DE LA API
### Utilizando el framework FastAPI, las consultas propuestas son :

### **- def cantidad_filmaciones_mes(mes)**
### **- def cantidad_fimaciones_dia(dia)**
### **- def score_titulo(titulo_de_la_filamacion)**
### **- def votos_titulo(titulo_de_la_filmacion)**
### **- def get_actor(nombre_actor)**
### **- def get_director(nombre_director)**

## SISTEMA DE RECOMENDACIÓN
### Por último crearemos un modelo de Machine Learning para la recomendación de películas bqsándose en peliculas similares. Todo esto lo llevaremos con una fución a ser consumida por la API. La consulta será:
### **- def recomendacion(titulo)**






