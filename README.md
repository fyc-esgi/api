# Lancer le conteneur
`docker-compose up`

# Lancer en local
`$ pip install -r api/requirements.txt`
`$ python api/main.py`

# Compte par defaut grafana & Influxdb

ID : `admin`

PASSWORD :`admin`

# URL 
## Grafana
`http://localhost:3000/`
##Influxdb
`http://localhost:8086/query`
##Prometheus
`http://localhost:9090`
##API
`http://localhost:5050`

#Delete volume

`docker volume rm api_grafana-storage api_prometheus-storage`
