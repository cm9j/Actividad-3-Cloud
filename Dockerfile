# Usamos una imagen oficial de Python
FROM python:3.10
#RUN pip install uvicorn
#RUN pip install --upgrade pip

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar los archivos de requisitos e instalarlos
COPY requirements/base.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copiar
RUN pip install --no-cache-dir black==24.1.0 ruff==0.1.14
RUN black .

RUN pip install aerich

COPY . /app
# Comando por defecto para ejecutar la aplicación
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]




