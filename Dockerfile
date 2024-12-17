# Usar una imagen base oficial de Python0000  
FROM python:3.9-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar los archivos de la aplicación al contenedor
COPY . /app

# Instalar las dependencias necesarias desde requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto que utilizará la aplicación Flask (5000)
EXPOSE 5000

# Definir el comando que ejecutará la aplicación Flask
CMD ["python", "app.py"]