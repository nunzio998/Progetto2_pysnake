# Specifico l'immagine da cui partire
FROM python:3.10

# setto una working directory nel container che verrà creato
WORKDIR .

# Copio tutti gli script e il contenuto della cartella 'data' nella working directory
COPY src .
COPY src/data .


# creo e attivo un virtual environment
RUN python -m venv ./env
ENV VIRTUAL_ENV /env
ENV PATH .:$PATH

# Aggiorno pip
RUN pip install --upgrade pip

# Copio e installo il file con le dipendenze necessarie
COPY requirements.txt .
RUN pip install -r requirements.txt

# All'avvio del container dopo la build dell'immagine verra eseguito lo script main.py
CMD ["python", "main.py"]

# Comando da abilitare se si vuole eseguire il run dei test
#CMD ["python", "test_01.py"]

# Disabilitando i due comandi precedenti e abilitando il sottostante si può lanciare il
# container e lanciare manualmente gli script.
#CMD sh


