# Utiliza una imagen base de Python
FROM python:3.11

# Establece el directorio de trabajo en /app
WORKDIR /

# Copia el archivo de requisitos e instala las dependencias
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copia el contenido de la carpeta pokeberries en el directorio de trabajo del contenedor
COPY / .

# Expone el puerto en el que se ejecutará la aplicación FastAPI
EXPOSE 8000

# Ejecuta la aplicación FastAPI
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
