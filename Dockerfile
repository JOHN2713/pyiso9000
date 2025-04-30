# Imagen base oficial de Python
FROM python:3.11-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar archivos del proyecto
COPY . .

# Instalar dependencias
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Exponer el puerto por defecto de Streamlit
EXPOSE 8501

# Comando de inicio
CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]
