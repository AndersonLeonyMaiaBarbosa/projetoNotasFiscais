// Quando você esquecer de anotar o ID de um "data asset" utilize essa requisição
// para pesquisar por seu ID ele no serviço do Watson Analytics.
// Assim como as requisições anteriores esta também segue o mesmo padrão
var http = require("https");

// Para realizar a busca por determinado "data asset" é necessário passar dentre os parâmetros
// uma string que será utilizada para pesquisar pelo nome do "data asset".
// Essa string deve ser passada dentro do atributo "path" da seguinte forma:
// "path": "/watsonanalytics/run/data/v1/datasets/search?q=STRING_PARA_A_PESQUISA"
// As informações sobre os "data assets" encontrados virão como resposta da requisição.
var options = {
  "method": "GET",
  "hostname": "api.ibm.com",
  "port": null,
  "path": "/watsonanalytics/run/data/v1/datasets/search?q=2",
  "headers": {
    "authorization": "Bearer H2BY4H5vxvGFS8w3lPch8aScI1IwmXvIFfJWayuO06Xmz1SWEwpYPo53irfC64FwRVpdM1yzrIUDC9MKg2RYdbxXhrlOddDv/WLKtaSz/N+XnSssVJIdpIQqe3hYiZ5/ef4xsSDIAV4dAtoouTLH9duTO7JeVV0//ajJcJJXPHUY81TbufVAhCoxiepmLMTxDHCyyN6Cgc/Oacn5BRXUxMYsKEBrxkSJxn4/7AnlRE7slYBO7155G3YAd3V9nqHSjzINxIGTZ1Yr1qUU6sQkP7Lt4bAMM1eT/9D+1kCTCLK4k3Qsyavt4qHM/8rVJxvo2VudGHIfcGNGt1KVZjAM10GtXfTsFtVYZvPQc5AZWJBRXwclhPhWc9/w1/tUidFNFXROAxWVRD4=;=;LS0=",
    "x-ibm-client-id": "7827b854-04f3-4d87-a388-006957cadd19",
    "x-ibm-client-secret": "Y5vC5fH5sT8pA7qR3vI6dM1fU8mP3oI7jU2yS1nY5sE7eL5jH6",
    "accept": "application/json"
  }
};
 
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

req.end();