// Importa módulo HTTPS, para realizar as requisições para o Watson Analytics
var httpsModule = require("https");

// Variável/Objeto que guarda as configurações a serem aplicadas as requisições
// Substitua "x-ibm-client-secret" pelo seu código CLIENT-SECRET,
// "x-ibm-id" pelo seu código CLIENT-ID e
// "authorization" pelo seu código TOKEN de acesso
var requestConfig = {
  "method": "POST",
  "hostname": "api.ibm.com",
  "port": null,
  "path": "/watsonanalytics/run/data/v1/datasets",
  "headers": {
    "x-ibm-client-secret": "Y5vC5fH5sT8pA7qR3vI6dM1fU8mP3oI7jU2yS1nY5sE7eL5jH6",
    "x-ibm-client-id": "7827b854-04f3-4d87-a388-006957cadd19",
    "authorization": "Bearer H2BY4H5vxvGFS8w3lPch8aScI1IwmXvIFfJWayuO06Xmz1SWEwpYPo53irfC64FwRVpdM1yzrIUDC9MKg2RYdbxXhrlOddDv/WLKtaSz/N+XnSssVJIdpIQqe3hYiZ5/ef4xsSDIAV4dAtoouTLH9duTO7JeVV0//ajJcJJXPHUY81TbufVAhCoxiepmLMTxDHCyyN6Cgc/Oacn5BRXUxMYsKEBrxkSJxn4/7AnlRE7slYBO7155G3YAd3V9nqHSjzINxIGTZ1Yr1qUU6sQkP7Lt4bAMM1eT/9D+1kCTCLK4k3Qsyavt4qHM/8rVJxvo2VudGHIfcGNGt1KVZjAM10GtXfTsFtVYZvPQc5AZWJBRXwclhPhWc9/w1/tUidFNFXROAxWVRD4=;=;LS0=",
    "accept": "application/json",
    "content-type": "application/json"
  }
};

// Guarda na variável/objeto "httpsRequest" a requisição HTTPS de acordo com a 
// configuração definida pela variável/objeto "requestConfig"
// Passa 2 parâmetros para a função "request"
// O primeiro é a configuração da requisição, definida pela variável "requestConfig"
// e o segundo é uma função de callback, que será executada quando uma resposta for recebida
// A função de callback recebe como parâmetro uma variável/objeto chamada "response" que receberá
// a resposta da requisição quando esta chegar
var httpsRequest = httpsModule.request(requestConfig, function (response) {

  // Variável/array que irá armazenar os dados que chegarem como resposta da requisição
  var chunks = [];
 
  // Esta função será executada para cada objeto da resposta buscando verificar seu identificador
  // e para cada objeto da resposta que estiver com o identificador "data" a função de callback será executada
  // Ela recebe como primeiro parâmetro, um identificador do objeto de resposta e como segundo parâmetro
  // uma função de callback
  response.on("data", function (chunk) {
    // Adiciona ao array "chunks" cada objeto encontrado na resposta
    chunks.push(chunk);
  });
 
  // Esta função será executada para cada objeto da resposta buscando verificar seu identificador
  // e para cada objeto da resposta que estiver com o identificador "end" a função de callback será executada
  response.on("end", function () {
    // Concatena todos os objetos do array "chunks" e armazena em uma variável/objeto chamado "body"
    var body = Buffer.concat(chunks);
    // Exibe a variável/objeto "body"
    console.log(body.toString());
  });
});
 
// Configura os dados a serem enviados no corpo da requisição, que neste caso é do tipo "POST", de acordo com
// o que foi definido no inicio deste arquivo
// O corpo da requisição para o Watson Analytics para a criação de "data assets" vazios deve seguir este padrão
// O corpo da requisição neste caso será composta por um objeto que possui dois atributos,
// o primeiro é o "actions" que contém a configuração da ação que será realizada no Watson Analytics,
// para esta requisição devem se manter estas configurações, modificando apenas a URL que deverá ser igual
// a que foi definida no primeiro passo do tutorial.
// O segundo parâmetro se trata do nome do "data asset" a ser criado
// O método "stringfy" do objeto "JSON" tem a função de receber um JSON (uma representação de um objeto)
// e convertê-lo em string, para que possa ser enviado na requisição como um texto comum
httpsRequest.write(JSON.stringify({ 
  actions: [ { 
      method: 'POST', 
      name: 'replace', 
      url: 'https://localhost:5443' 
    }],
  name: 'Data Asset Test 2' 
}));

// Realiza a requisição
httpsRequest.end();