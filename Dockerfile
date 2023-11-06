# Utiliza una imagen base de Python
FROM python:3.11

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /

# Copia los archivos de la aplicación al contenedor
COPY app /
COPY requirements.txt .

# Instala las dependencias de Python
RUN pip install -r requirements.txt

# Expone el puerto en el que se ejecutará la aplicación
EXPOSE 8000

# Inicia la aplicación FastAPI
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
