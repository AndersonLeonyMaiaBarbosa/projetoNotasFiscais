import pdftotext
import json
from datetime import datetime

# # Load your PDF 2018-08-02_09:25:21.753300
# with open("nota_em_pdf.pdf", "rb") as f:
#     pdf = pdftotext.PDF(f)

# # # If it's password-protected
# # with open("secure.pdf", "rb") as f:
# # pdf = pdftotext.PDF(f, "secret")

# # How many pages?
# print(len(pdf))

# # Iterate over all the pages
# for page in pdf:
#     print(page)
    
# # Read some individual pages
# print(pdf[0])
# # #print(pdf[1])

# #Read all the text into one string
# print("\n\n".join(pdf))

# f.writelines("\n\n".join(pdf))


#-------------#

cont = 0

numeroMinimoPosicoes = 37

# Por padrão, todos os campos da nota fiscal da prefeitura ocupam posições de 0 até 37 no arquivo JSON. 
# Entretando, este total pode aumentar, dependendo de quantas linhas existem após a posição 16, que
# corresponde ao campo "DISCRIMINAÇÃO DOS SERVIÇOS". Daí a necessidade de verificar o realTotalDePosicoes
# que cada documento possui. 
realTotalDePosicoes = 0

# Salva a data e horas atuais para incluir no nome dos arquivos que serão utilizados no WKS
# timeAndDateOfDocumentUpload = str(datetime.now()).replace(" ", "_").replace(":","-")
timeAndDateOfDocumentUpload = "{}_{}h{}m{}s".format(str(datetime.now())[0:10],str(datetime.now())[11:13],str(datetime.now())[14:16],str(datetime.now())[17:(str(datetime.now()).__len__())])

print("\n"+timeAndDateOfDocumentUpload+"\n")

jsonObject = "{"

jsonObjectData = " ";

docWks = ""
docWksToString = ""
docAnalytics = ""
numRPS = ""

construindoNotaParaWKS = ""
contruindoNotaParaAnalitycs_Nomes_Colunas = "Número do RPS,Data da Emissão,Nome Fantasia,CPF/CNPJ,Discriminação dos serviços,Valor dos Serviços R$\n"
contruindoNotaParaAnalitycs_Valores_Colunas = ""

pastaLocal = '/Users/Leony/Desktop/Arquivos aplicação python - extraindo texto de notas da prefeitura/'

# Load your PDF (notaFiscalUnifor notaExemplo)
with open(pastaLocal+"notaFiscalUnifor.pdf", "rb") as f:
    pdf = pdftotext.PDF(f)

# Cria ou abre um arquivo do tipo json (cada linha do pdf será um valor que terá como chave valores de 
# 0 até o total de linhas encontradas). Caso este arquivo não exista, será criado automaticamente e salvo 
# no repositório do arquivo Python que está localizado.
openJsonFile = open(pastaLocal+'visualisarJson.json', 'w')

# Abrirá ou criará automaticamente (caso ainda não exista) um arquivo do tipo csv que será adicionado futuramente ao WKS 
# (Watson Knowledge Studio), formado por 2 células: |nome_do_documento|valores_concatenados. (Obs: o 'w' habilita a edição
#  do documento)
# O nome do arquivo deve concatenar com o timestamp da data atual a fim de diferenciar os documentos criados
# openDocWksFile = open('docWks'+timeAndDateOfDocumentUpload+'.csv', 'w') 
openDocWksFile = open(pastaLocal+'docWks.csv', 'w')

# Abrirá ou criará automaticamente (caso ainda não exista) um arquivo do tipo csv, que será adicionado futuramente ao WA 
# (Watson Analitycs), onde cada campo do pdf será uma tabela (O WA reconhece um arquivo csv, onde a 1a linha corresponde 
# aos nomes das tabelas do banco de dados).(Obs: o 'w' habilita a edição do documento)
# openDocAnalyticsFile = open('docAnalitycs'+timeAndDateOfDocumentUpload+'.csv', 'w')
openDocAnalyticsFile = open(pastaLocal+'docAnalitycs.csv', 'w')

openDocAnalyticsToStringFile = open(pastaLocal+'openDocAnalyticsToStringFile.txt', 'w')

# Abrirá ou criará automaticamente (caso ainda não exista) um arquivo do tipo txt para que após o pdf ser lido ele seja
# salvo neste documento, que depois será varrido linha por linha para que cada linha ocupe uma posição no objeto Json.
# (Obs: o 'w' habilita a edição do documento) 
openTxtFile = open(pastaLocal+'testeTxt.txt', 'w')

# Escreve o arquivo pdf no arquivo .txt criado
openTxtFile.writelines("\n\n".join(pdf))

# Fecha a edição deste arquivo
openTxtFile.close()

# Criará uma lista onde cada posição da lista será preenchida por cada linha. O comando l.strp() retira os espaços em branco
# do início de cada linha até o primeiro caractere.
with open("testeTxt.txt", encoding="utf-8") as file:
            x = [l.strip() for l in file]

tamLista = x.__len__();

# Criará o objeto Json, varrendo cada linha e adicionando-as a chaves de 0 até tamLista - 1.
for item in x:
    key = "\""+str(cont)+"\""
    val = "\""+x.__getitem__(cont)+"\""
    objKeyVal = key+" : "+val
    
    if cont != x.__len__() - 1:
        jsonObjectData += objKeyVal + ","
        
    else :
        jsonObjectData += objKeyVal
        
    cont+=1
    realTotalDePosicoes+=1

jsonObject = "{"+jsonObjectData+"}"

data = json.loads(jsonObject)

openJsonFile.writelines(jsonObject)

#---Posicao 4 -> Número do RPS--------#
strRemovendoTitulo = str(data["4"]).replace("Número do RPS", "").lstrip()
campoTitulo = "Número do RPS: "
campoValor = ""
cont = 0

while strRemovendoTitulo[cont] != " ":
    campoValor += strRemovendoTitulo[cont]
    cont+=1

construindoNotaParaWKS += campoTitulo + campoValor + " | "
contruindoNotaParaAnalitycs_Valores_Colunas += campoValor + ","
numRPS = campoValor

#---Posicao 3 -> Data de Emissão--------#
strRemovendoTitulo = str(data["3"]).replace("Data e Hora da Emissão", "").lstrip()
campoTitulo = "Data da Emissão:"
campoValor = " "
cont = 0

while strRemovendoTitulo[cont] != " ":
    campoValor += strRemovendoTitulo[cont]
    cont+=1

construindoNotaParaWKS += campoTitulo + campoValor + " | "
contruindoNotaParaAnalitycs_Valores_Colunas += campoValor + ","

#---Posicao 7 -> Nome Fantasia----------#
strRemovendoTitulo = str(data["7"]).replace("Nome Fantasia", "").lstrip()
campoTitulo = "Nome Fantasia:"
campoValor = " "
cont = 0

while cont < strRemovendoTitulo.__len__():
    campoValor += strRemovendoTitulo[cont]
    cont+=1

construindoNotaParaWKS += campoTitulo + campoValor + " | "
contruindoNotaParaAnalitycs_Valores_Colunas += campoValor + ","

#---Posicao 8 -> CPF/CNPJ--------------------#
strRemovendoTitulo = str(data["8"]).replace("CPF/CNPJ", "").lstrip()
campoTitulo = "CPF/CNPJ:"
campoValor = " "
cont = 0

while strRemovendoTitulo[cont] != " ":
    campoValor += strRemovendoTitulo[cont]
    cont+=1

construindoNotaParaWKS += campoTitulo + campoValor+ " | "
contruindoNotaParaAnalitycs_Valores_Colunas += campoValor + ","

#---Posicao 16 -> Discriminação dos serviços--------#
posicaoInicioPegarValoresDiscriminacaoDeServico = 17
posicaoFinalPegarValoresDiscriminacaoDeServico = "CÓDIGO DE ATIVIDADE CNAE"
campoTitulo = "Discriminação dos serviços:"
campoValor = " "

while data[str(posicaoInicioPegarValoresDiscriminacaoDeServico)] != posicaoFinalPegarValoresDiscriminacaoDeServico:
    campoValor+=data[str(posicaoInicioPegarValoresDiscriminacaoDeServico)] +"\n"
    posicaoInicioPegarValoresDiscriminacaoDeServico+=1

campoValor = campoValor.replace(".","")
construindoNotaParaWKS += campoTitulo + campoValor + "| "
contruindoNotaParaAnalitycs_Valores_Colunas += "\"" + campoValor + "\","

#---Posicao padrão = 25 -> Valor dos Serviços R$--------#
posicaoRealCampoValorDosServicos = 25

if realTotalDePosicoes != 37:
    posicaoRealCampoValorDosServicos = 25 + (realTotalDePosicoes - numeroMinimoPosicoes - 1)

strRemovendoTitulo = str(data[str(posicaoRealCampoValorDosServicos)]).replace("Valor dos Serviços R$", "").lstrip()
campoTitulo = "Valor dos Serviços R$:"
campoValor = " "
cont = 0

while strRemovendoTitulo[cont] != " ":
    campoValor += strRemovendoTitulo[cont]
    cont+=1

campoValor = campoValor.replace(".","")
construindoNotaParaWKS += campoTitulo + campoValor
campoValor = campoValor.replace(",",".")
contruindoNotaParaAnalitycs_Valores_Colunas += campoValor

print("VALOR = R$ "+campoValor)

# Construindo documento para enviar ao WKS
docWks = numRPS + "," + "\"" + construindoNotaParaWKS + ".\""
openDocWksFile.writelines(docWks)
openDocWksFile.close()

#Construindo documento para enviar ao Analitycs
docAnalytics = contruindoNotaParaAnalitycs_Nomes_Colunas + contruindoNotaParaAnalitycs_Valores_Colunas
openDocAnalyticsFile.writelines(docAnalytics)
openDocAnalyticsFile.close()

docAnalytics = docAnalytics.replace("ç", 'c')
docAnalytics = docAnalytics.replace("ã", 'a')
docAnalytics = docAnalytics.replace("â", 'a')
docAnalytics = docAnalytics.replace("ú", 'u')

openDocAnalyticsToStringFile.write(docAnalytics)
openDocAnalyticsToStringFile.close()

print("------------------- Arquivo para o WKS ----------------\n" + docWks + "\n\n------------------- Arquivo para o Analytics ----------------\n" + docAnalytics + "\n")

# for key, value in data.items():
    
#     print(key)

#     if int(key) > 16:

#     if key is '2':
        
#         print(construindoNotaParaWKS)

#     print(key +":"+value+"\n")

# print(jsonObject)