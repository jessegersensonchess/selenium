#### outputs ${FOLDER}/seznam.csv 
#### note: build and run assume this is run from linux; --network=host adds networking
#### build ####
# docker build --network=host -t selenium:firefox . 

#### run ####
# FOLDER=/tmp/downloads
# mkdir $FOLDER 
# chmod 777 $FOLDER
# docker run --network=host -v ${FOLDER}:/tmp/download -it --rm selenium:firefox

FROM debian:bullseye-slim
USER root
#### only needed to run pip ####
RUN apt-get update \
	&& apt-get install --no-install-recommends firefox-esr python3 pip -y \
	&& groupadd seluser \
	&& useradd --create-home --gid seluser seluser \
	&& chown --recursive seluser:seluser /home/seluser/
USER seluser

WORKDIR /home/seluser
COPY adisspr.mfcr.cz.py .
RUN 	mkdir /tmp/download \
	&& pip install webdriver_manager \
	&& pip install selenium
CMD ["python3", "adisspr.mfcr.cz.py"]
