import http.client
 
conn = http.client.HTTPSConnection("api.ibm.com")
 
# payload = "{\"actions\":[{\"method\":\" \",\"name\":\" \",\"url\":\" \"}],\"folder\":[null],\"name\":\" \"}"
payload = "{\"actions\":[{\"method\":\"POST\",\"name\":\"replace\",\"url\":\"https://localhost:5443\"}],\"name\":\"NotasFiscaisFortaleza\"}"

# Obs: em 'authorization' escrever "Bearer <código do access tolken>
headers = {
    'x-ibm-client-secret': "P7qN7qP0mU1iG2vR0fL0hG0kP1qU6tQ1iA5cS8pP0vE3pT4vN6",
    'x-ibm-client-id': "c8840816-060a-4e38-9242-38f65bbf3eb9",
    'authorization': "Bearer 7PNcnCfIaKQbrAgOG+a575iUztIlzEcHfs/aasqqj44BmPlQE59DVmWKyrVvzNqHv5kZYSZnLS9T7MaGp0Q6yvpW4Z+RwNsKEbHMOsfQydmUYZnqWDlnaOO8QlFGhWQ6T7JfJOL3GZNJND9P4XnSiBoC5vle0l88SKG/XzAwrob0o0ZMMgHgOJI8vuLKcxu9PB5bmd5XNbcgAnp6uC6erUVu2OynjUNOY308EdS7+RkMxaFcF0Tws67Z+xKjBY+k+iErfhbyGSDCvoTQOJl1lMzBSZC6bGpUZgwHyVUKUf5lc2Cjuq2ei6lcvEWoT5e1/PNUcb6U9aGY03a0euFmWd333mXX4RKjhQRufAN4zRNM1sjaVk1D6K6m7p8uku8P8+Z38uhvuB4=;=;LS0=","token_type":"bearer","expires_in":"3600","scope":"userContext","refresh_token":"7jJ1bnc0fSR9S06ld3yyPKFJ+X6UDCtXd+8hzgoEnbQqvbl7jXyFkEvEXlZRKinpVj2rXdK4c42fcAfPWGYNbuGoFLfQcy52p8FQNCIW6DbhbHzU7py0U+bJxBFmfsx1/juzyqDGyYs+V9OGSuk0I/pjx85l9GkbQtrKkiZirZVKEiHjHi+9Ny4h/YDxFQ0K2KIvw1I2syR1Hq9pLQbub00UEIB+CeV6aV7C4IWgEvy5twFjvfznfvgOjdOLexld3TXPsIKAv4ouoTt1W8n385HifXvHtdCgckd79JR6pA5l+pk2kf+vIC4j+/2emhnx49vfUnQp/xYFLZhAA5Ey0OsVDtFXoX2wui0LxXDCHKkE+NwndRdxsripD4ULbfUG",
    'accept': "application/json",
    'content-type': "application/json"
    }
 
conn.request("POST", "/watsonanalytics/run/data/v1/datasets", payload, headers)
 
res = conn.getresponse()
data = res.read()
 
print(data.decode("utf-8"))