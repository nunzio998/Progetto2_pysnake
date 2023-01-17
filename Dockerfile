FROM python:3.10

# set a directory for the app
WORKDIR .

ADD src/main.py .

# create a virtual environment
RUN python -m venv ./env
# activate the virtual environment
ENV VIRTUAL_ENV /env
ENV PATH .:$PATH
# update pip if needed

RUN pip install --upgrade pip
RUN pip freeze > requirements.txt

##################################################################
# WARNING volumes to be mounted must be specified as absolute path
# in the form HOSTVOLUME:IMAGEVOLUME:ro/rw
##################################################################

# create mount points of input data and results
VOLUME src/data

# run the command
CMD ["python", "main.py"]
