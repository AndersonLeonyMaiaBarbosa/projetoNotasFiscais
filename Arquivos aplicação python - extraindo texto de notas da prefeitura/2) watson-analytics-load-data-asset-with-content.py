#2.a Upload data (one segment)
import http.client
import pdftotext
import json
from datetime import datetime
 
conn = http.client.HTTPSConnection("api.ibm.com")
 
headers = {
    'x-ibm-client-secret': "P7qN7qP0mU1iG2vR0fL0hG0kP1qU6tQ1iA5cS8pP0vE3pT4vN6",
    'x-ibm-client-id': "c8840816-060a-4e38-9242-38f65bbf3eb9",
    'authorization': "Bearer 7PNcnCfIaKQbrAgOG+a575iUztIlzEcHfs/aasqqj44BmPlQE59DVmWKyrVvzNqHv5kZYSZnLS9T7MaGp0Q6yvpW4Z+RwNsKEbHMOsfQydmUYZnqWDlnaOO8QlFGhWQ6T7JfJOL3GZNJND9P4XnSiBoC5vle0l88SKG/XzAwrob0o0ZMMgHgOJI8vuLKcxu9PB5bmd5XNbcgAnp6uC6erUVu2OynjUNOY308EdS7+RkMxaFcF0Tws67Z+xKjBY+k+iErfhbyGSDCvoTQOJl1lMzBSZC6bGpUZgwHyVUKUf5lc2Cjuq2ei6lcvEWoT5e1/PNUcb6U9aGY03a0euFmWd333mXX4RKjhQRufAN4zRNM1sjaVk1D6K6m7p8uku8P8+Z38uhvuB4=;=;LS0=","token_type":"bearer","expires_in":"3600","scope":"userContext","refresh_token":"7jJ1bnc0fSR9S06ld3yyPKFJ+X6UDCtXd+8hzgoEnbQqvbl7jXyFkEvEXlZRKinpVj2rXdK4c42fcAfPWGYNbuGoFLfQcy52p8FQNCIW6DbhbHzU7py0U+bJxBFmfsx1/juzyqDGyYs+V9OGSuk0I/pjx85l9GkbQtrKkiZirZVKEiHjHi+9Ny4h/YDxFQ0K2KIvw1I2syR1Hq9pLQbub00UEIB+CeV6aV7C4IWgEvy5twFjvfznfvgOjdOLexld3TXPsIKAv4ouoTt1W8n385HifXvHtdCgckd79JR6pA5l+pk2kf+vIC4j+/2emhnx49vfUnQp/xYFLZhAA5Ey0OsVDtFXoX2wui0LxXDCHKkE+NwndRdxsripD4ULbfUG",
    'accept': "application/json",
    'content-type': "text/csv"
    }

# pegando o arquivo csv para enviar ao wks
pastaLocal = '/Users/Leony/Desktop/Arquivos aplicação python - extraindo texto de notas da prefeitura/'
with open(pastaLocal+'openDocAnalyticsToStringFile.csv', 'r') as myFile:
    openDocAnalyticsToStringFile = myFile.read()

#conn.request("PUT", "/watsonanalytics/run/data/v1/datasets/{id_string}/content?appendData=string", headers=headers)
#conn.request("PUT", "/watsonanalytics/run/data/v1/datasets/237c8dd0-71fd-48ff-95a7-10759a37eee4/content?appendData=Número do RPS,Data da Emissão,Nome Fantasia,CPF/CNPJ,Discriminação dos serviços,Valor dos Serviços R$\n925991,05/07/17,-,07.373.434/0001-86,Referente a mensalidade do aluno Anderson Leony Maia Barbosa, matricula 1420443/1 no curso de Ciencia Da Computacao( Graduacao ),699.3", headers=headers)

conn.request("PUT", "/watsonanalytics/run/data/v1/datasets/cce33d94-e30c-430c-87e1-d56f1b17604b/content?appendData="+str(openDocAnalyticsToStringFile), headers=headers)

res = conn.getresponse()
data = res.read()
res.status
 
print(data.decode("utf-8"))