// Importar módulo HTTPS
var http = require("https");

// Criando variável/objeto de configuração para a requisição
// No atributo "path" é necessário enviar o código do "data asset" para o qual
// se quer enviar os arquivos, ficando portanto neste formato:
//  "path": "/watsonanalytics/run/data/v1/datasets/DATA_ASSET_ID/content?appendData=true"
// É necessário também enviar o seu código CLIENT-SECRET no lugar do atributo
// "x-ibm-client-secret", o seu código CLIENT-ID no lugar do atributo "x-ibm-client-id" e
// do seu código "token" de acesso no lugar do atributo "authorization" 
var options = {
  "method": "PUT",
  "hostname": "api.ibm.com",
  "port": null,
  "path": "/watsonanalytics/run/data/v1/datasets/323a1282-7dd4-44d3-b577-a8de9a4d6116/content?appendData=true",
  "headers": {
    "x-ibm-client-secret": "Y5vC5fH5sT8pA7qR3vI6dM1fU8mP3oI7jU2yS1nY5sE7eL5jH6",
    "x-ibm-client-id": "7827b854-04f3-4d87-a388-006957cadd19",
    "authorization": "Bearer H2BY4H5vxvGFS8w3lPch8aScI1IwmXvIFfJWayuO06Xmz1SWEwpYPo53irfC64FwRVpdM1yzrIUDC9MKg2RYdbxXhrlOddDv/WLKtaSz/N+XnSssVJIdpIQqe3hYiZ5/ef4xsSDIAV4dAtoouTLH9duTO7JeVV0//ajJcJJXPHUY81TbufVAhCoxiepmLMTxDHCyyN6Cgc/Oacn5BRXUxMYsKEBrxkSJxn4/7AnlRE7slYBO7155G3YAd3V9nqHSjzINxIGTZ1Yr1qUU6sQkP7Lt4bAMM1eT/9D+1kCTCLK4k3Qsyavt4qHM/8rVJxvo2VudGHIfcGNGt1KVZjAM10GtXfTsFtVYZvPQc5AZWJBRXwclhPhWc9/w1/tUidFNFXROAxWVRD4=;=;LS0=",
    "accept": "application/json",
    "content-type": "text/csv"
  }
};

// A Requisição é montada da mesma forma que na criação de um "data asset" vazio
var req = http.request(options, function (res) {
  var chunks = [];
 
  res.on("data", function (chunk) {
    chunks.push(chunk);
  });
 
  res.on("end", function () {
    var body = Buffer.concat(chunks);
    console.log(body.toString());
  });
});

// Para enviar os dados a configuração da função "write" é diferente, precisando apenas receber como
// parâmetro uma string com os dados a serem enviados
req.write("Province,Population density,Area,Population\nOntario,97,83858,8169929\nQuebec,337,30510,11007020\nAlberta,111,547030,63601002\nManitoba,233,357021,81799600\nBritish Columbia,393,41526,16824400");

// Função que realiza a requisição
req.end();