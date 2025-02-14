# 1️⃣ Usar una imagen oficial de Python como base
FROM python:3.9

# 2️⃣ Instalar Git para clonar el repositorio
RUN apt-get update && apt-get install -y git

# 3️⃣ Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# 4️⃣ Clonar el repositorio de GitHub dentro del contenedor
RUN git clone https://github.com/tu_usuario/openmeteo-docker.git .

# 5️⃣ Instalar las dependencias desde `requirements.txt`
RUN pip install --no-cache-dir -r requirements.txt

# 6️⃣ Ejecutar el script cuando el contenedor se inicie
CMD ["python", "app.py"]
