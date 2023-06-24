import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics.pairwise import linear_kernel
import math



from fastapi import FastAPI

              
app = FastAPI(title = 'Proyecto Henry',
              description = 'Creación Api',
              version = '1.0.1')

@app.get("/")
async def index():
    return ('Construyendo mi Api')

@app.get('/about')
async def about():
    return ('Mi primer proyecto')

movies_df = None  # Variable global para almacenar los datos del archivo CSV

@app.on_event('startup')
async def load_data():
    global movies_df
    
    movies_df = pd.read_csv(r"C:\Users\Rossella\Desktop\PROYECTO-ML\movies_credits_transform2.csv")
    
@app.get("/cantidad_filmaciones_mes")
async def cantidad_filmaciones_mes(Mes: int):
    if Mes < 1 or Mes > 12:
        return {"mensaje": f"El número de mes '{Mes}' no es válido. Por favor, ingresa un número de mes válido (1-12)."}

    # Convierto la columna de fechas a formato datetime
    movies_df['release_date'] = pd.to_datetime(movies_df['release_date'])

    # Filtro las películas por el mes consultado
    filtro = movies_df['release_date'].dt.month == Mes
    peliculas_mes = movies_df[filtro]
    
    # Elimino los registros duplicados basándose en la columna 'id'
    peliculas_mes_unique = peliculas_mes.drop_duplicates(subset='id')

    # Para obtener la cantidad de películas en el mes consultado
    cantidad = len(peliculas_mes_unique)

    return {"mensaje": f"{cantidad} cantidad de películas fueron estrenadas en el mes número {Mes}"}

@app.get("/cantidad_filmaciones_dia")
async def cantidad_filmaciones_dia(Dia: str):
    # Convierto el día en idioma español a minúsculas
    dia_lower = Dia.lower()

    # Mapeo los nombres de los días en español a los nombres en inglés
    dias = {
        "lunes": "Monday",
        "martes": "Tuesday",
        "miércoles": "Wednesday",
        "jueves": "Thursday",
        "viernes": "Friday",
        "sábado": "Saturday",
        "domingo": "Sunday"
    }
    dia_ingles = dias.get(dia_lower)
    
    if not dia_ingles:
        return {"mensaje": f"El día '{Dia}' no es válido. Por favor, ingresa un día válido en español."}

    # Convierto la columna de fechas a formato datetime
    movies_df['release_date'] = pd.to_datetime(movies_df['release_date'])

    # Filtro las películas por el día consultado
    filtro = movies_df['release_date'].dt.day_name().str.lower() == dia_ingles.lower()
    peliculas_dia = movies_df[filtro]

    # Obtengo la cantidad de películas en el día consultado
    cantidad = len(peliculas_dia)

    return {"mensaje": f"{cantidad} cantidad de películas fueron estrenadas en el día {Dia}"}

@app.get("/score_titulo/{titulo_de_la_filmacion}")
async def score_titulo(titulo_de_la_filmacion: str):
    # Buscamos la película por título en el dataframe
    pelicula = movies_df[movies_df['title'] == titulo_de_la_filmacion]
    
    # Verifico si se encontró la película
    if pelicula.empty: # El método empty devuelve True si el DataFrame está vacío.
        return "Película no encontrada"
    
    # Obtengo los valores de título, año de estreno y score
    titulo = pelicula['title'].iloc[0] # iloc[0] sirve para acceder al primer registro
    año_estreno = str(pelicula['release_year'].iloc[0])
    score = str(pelicula['popularity'].iloc[0])
    
    # return f"La pelicula {titulo} fue estrenada en el año {año_estreno} con un score de {score}."
    return {'titulo':titulo, 'anio':año_estreno, 'popularidad':score}

@app.get("/votos_titulo")
async def votos_titulo(titulo_de_la_filmacion: str):
    # Filtra la película por el título
    filtro = movies_df['title'] == titulo_de_la_filmacion
    pelicula = movies_df[filtro]

    if pelicula.empty:
        return {"mensaje": f"No se encontró ninguna filmación con el título '{titulo_de_la_filmacion}'."}

    # Obtiene el título de la película
    titulo_de_la_filmacion = pelicula['title'].values[0]
    # Obtiene la cantidad de valoraciones de la película
    cantidad_votos = pelicula['vote_count'].values[0]
    
    if cantidad_votos < 2000:
        return {"mensaje": f"La filmación '{titulo_de_la_filmacion}' no cumple con la condición de tener al menos 2000 valoraciones."}

    # Obtiene el valor promedio de las votaciones de la película
    valor_promedio = pelicula['vote_average'].values[0]
    
    # Obtiene el año de estreno de la película
    año_estreno = pelicula['release_year'].values[0]

    return {"mensaje": f"La película '{titulo_de_la_filmacion}' fue estrenada en el año {año_estreno}. Cuenta con un total de {cantidad_votos} valoraciones, con un promedio de {valor_promedio}"}

@app.get("/get_actor")
async def get_actor(nombre_actor: str):
    for _, row in movies_df.iterrows():   # iteramos sobre las filas del dataframe
        actores = row["actores"]
        if nombre_actor.lower() in actores.lower():
            peliculas = len(actores.split(","))   # la cantidad de peliculas en la que ha participado un actor.
            retorno_total = row["return"]
            if peliculas > 0:
                retorno_promedio = retorno_total / peliculas
            else:
                retorno_promedio = 0

            return {
                "mensaje": f"El actor {nombre_actor} ha participado en {peliculas} películas, "
                           f"con un retorno total de {retorno_total} y un promedio de {retorno_promedio} por película."
            }
    return {"mensaje": f"No se encontró ningún actor con el nombre {nombre_actor}."}


@app.get("/get_director")
async def get_director(nombre_director: str):
    peliculas_director = []
    
    for _, row in movies_df.iterrows():
        directores = row["Directores"]
        if isinstance(directores, str) and nombre_director.lower() in directores.lower():
            titulo = row["title"]
            fecha_lanzamiento = row["release_date"]
            retorno = row["return"]
            if isinstance(retorno, float) and retorno == 0.0:
                retorno = "inf"
            pelicula = {
                "titulo": titulo,
                "fecha_lanzamiento": fecha_lanzamiento,
                "retorno": retorno
            }
            peliculas_director.append(pelicula)
    
    if len(peliculas_director) > 0:
        mensaje = f"El director {nombre_director} ha dirigido las siguientes películas:"
        return {"mensaje": mensaje, "peliculas": peliculas_director}
    
    return {"mensaje": f"No se encontró ninguna película dirigida por {nombre_director}."}


@app.on_event('startup')
async def load_data():
    global movies_ML


    movies_ML = pd.read_csv(r"C:\Users\Rossella\Desktop\PROYECTO-ML\movies_ML_parcial.csv")
    
# Defino la nueva función de recomendación con el nuevo dataset
@app.get('/recomendacion_nuevo_dataset/{title}')
async def get_recomendation_nuevo_dataset(title: str):
    # Creao una matriz TF-IDF para el texto del título y overview de las películas
    stopwords_custom = ["where","on","the", "at", "in", "of","and"]  # Agrega aquí stopwords personalizados
    tfidf = TfidfVectorizer(stop_words=stopwords_custom)
    tfidf_matrix = tfidf.fit_transform(movies_ML['title']+' '+ movies_ML['overview'])
    # Calculo la similitud del coseno entre los títulos de las películas
    cosine_similarities = linear_kernel(tfidf_matrix, tfidf_matrix)
    # Verifico si el título está en el DataFrame
    if title not in movies_ML['title'].values:
        return f"No se encontró ninguna película con el título '{title}'."
    # Encuentro el índice de la película con el título dado
    indices = pd.Series(movies_ML.index, index=movies_ML['title']).drop_duplicates()
    idx = indices[title]
    # Calculo las puntuaciones de similitud de todas las películas con la película dada
    sim_scores = list(enumerate(cosine_similarities[idx]))

    # Ordeno las películas por puntaje de similitud en orden descendente
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    # Obtengo los índices de las películas más similares (excluyendo la película dada)
    sim_scores = sim_scores[1:6]  # Obtener las 5 películas más similares
    movie_indices = [x[0] for x in sim_scores]

   # Devuelvo los títulos de las películas más similares
    respuesta_recomendacion = movies_ML['title'].iloc[movie_indices].tolist()
    return respuesta_recomendacion
  