# PROYECTO-ML PROYECTO INDIVIDUAL Nº1

## INTRODUCCIÓN


### Debemos hacer un proyecto, en el cual desarrollaremos una API,y para ello, debemos cargar nuestros datos y transformarlos. 
### Tendremos que comenzar desde cero, haciendo un trabajo de Data Engineer. Crearemos luego un modelo de machine learning que cree un sistema de recomendación de películas, donde la  API  nos proporciona información, en base a funcionalidades de películas. 

## FUENTES DE DATOS
###  **- Dataset** : el cual incluye dos archivos que debemos importar y luego procesar(movies_dataset.csv y credits.csv)
### **- Diccionario de datos** : con algunas descripciones de las columnas que están disponibles en el dataset. [Fuente de datos](https://drive.google.com/drive/u/0/folders/18MPjjrabzfi6nt8Ijmznp2VFjlO_Rhvq)

## TRANSFORMACIONES ETL
### Comenzamos con la limpieza de los datos a analizar, donde nos solicitan diferentes transforamciones.
### **Dentro de las solicitadas:** 
### - Desanidado de datos de algunas de las columnas del dataset para su uso en las consultas de la API, creando las columnas que sean necesarias con los datos extraídos de las mismas
### - Rellena con 0 los valores nulos de algunas de las columnas.
### - Eliminación de valores nulos
### - Llevar la columna de fechas al formato AAAA-mm-dd y extraer en otra columna el año de esas fechas
### - Crearemos una columna llamada return con las columnas budget y revenue.
### Eliminaremos todas las columnas que no necesitaremos para nuestro análisis 

## ANÁLISIS EXPLORATORIO DE LOS DATOS - EDA
### Con este análisis trataremos de comprender la relación que existe entre las varialbes del dataset, buscando outliers, creando una matriz de correlación para un mejor análisis de los datos. También haremos un análisis estadístico así como la visualización de diferentes gráficos.

## REPOSITORIO 
### En github, creamos un repositorio donde tendremos todo los archivos de nuestro proyecto, el cual se conectará con Render con el servicio Web que creamos.

## DEPLOY
### Creamos un deploy en render para poder tener un entorno donde nuestra API, pueda ser consumida por cualquier persona.

## DESARRLLO DE LA API
### Utilizando el framework FastAPI, las consultas propuestas son :

### **- def cantidad_filmaciones_mes(mes)**
### **- def cantidad_fimaciones_dia(dia)**
### **- def score_titulo(titulo_de_la_filamacion)**
### **- def votos_titulo(titulo_de_la_filmacion)**
### **- def get_actor(nombre_actor)**
### **- def get_director(nombre_director)**
### Dejo el link a la api. [Desarrollo de la Api](https://fastapi-j9ta.onrender.com/docs)

## SISTEMA DE RECOMENDACIÓN
### Por último crearemos un modelo de Machine Learning para la recomendación de películas bqsándose en peliculas similares. Todo esto lo llevaremos con una fución a ser consumida por la API. La consulta será:
### **- def recomendacion(titulo)**

### He realizado un vídeo con una breve descripción del proyecto [Video](https://youtu.be/lkCT7-3aE9o)






