#### Selenium docker example 
 outputs ${FOLDER}/seznam.csv 

#### Build
 build and run assume this is run from linux; --network=host adds networking
 ```
 docker build --network=host -t selenium:firefox
 ```

#### Run
```
FOLDER='/tmp/downloads'
mkdir "$FOLDER"
chmod 777 "$FOLDER"
docker run --network=host -v ${FOLDER}:/tmp/download -it --rm selenium:firefox
```

#### Todo
 optimize docker image for smaller size. Currently 1.44 GB!?
