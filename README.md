# tf_classification
A Classification problem using TensorFlow Estimator API.

[Dataset used.](https://www.kaggle.com/rashikrahmanpritom/heart-attack-analysis-prediction-dataset)

# 1. Installation

## 1.1 Docker Installation
Run [this script](https://get.docker.com/) to install Docker.


## 1.2 Build Image
Build the project image:

```console
cd ./Docker
docker build -t tf_classification .
```

## 1.3 Run Docker Container

```console
docker container run -it --name tf_classification tf_classification
```

