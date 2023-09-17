# EduSphere_Flask
Flask REST API for EduSphere

Install dependencies
``` 
pip3 install psycopg
pip3 install psycopg-binary
```
Download CA Certificate
```
curl --create-dirs -o $HOME/.postgresql/root.crt 'https://cockroachlabs.cloud/clusters/<CERTIFICATE>'
```

Set secrets
```
export DATABASE_URL="<DATABASE_URL>"
export SECRET_KEY=<SECRET_KEY>
export ACCESS_TOKEN_EXPIRE_MINUTES=360
```
