const superSecretCredentials = {
  admin: 'c4nt_t0uch_m3',
  john: 'citizen',
  andrew: new Buffer.from("\u00A5\u00AB\u002C\u00C2\u008A\u00DD", "\x62\x69\x6e\x61\x72\x79").toString("\x62\x61\x73\x65\x36\x34"),
  alicia: 'piano'
}

const md5 = require('md5');
const superSecretCredentials_hashed = {};
Object.keys(superSecretCredentials).forEach(function(key) {
    superSecretCredentials_hashed[key] = md5(superSecretCredentials[key]);
  }
)

console.log('Super secret logon details are:')
console.log('-------------------------------')
Object.keys(superSecretCredentials).forEach(key => console.log(`Username:\t${key}\nPlain Text:\t${key === "andrew" ? "***hidden***" : superSecretCredentials[key]}\nPassword Hash:\t${superSecretCredentials_hashed[key]}\n`))
console.log('-------------------------------')


const fs = require('fs');
const express = require('express');
const app = express();
var cors = require('cors');
const port = 8000;
const secure_port = 8443;

app.use(express.static('site'));
app.use(cors());
app.use(express.json());
app.use(express.urlencoded({extended: true}));

function sendOK(res) {
  res.send({status: true})
}
function sendNO(res) {
  res.send({status: false})
}

app.post('/login_plain', (req, res) => {
  let username = req.body.username, password = req.body.password;
  
  let result = (username && password && superSecretCredentials[username] == password);
  console.log(`${req.protocol} - /login_plain - ${username||"(blank)"}:${password||"(blank)"} - ${result ? "SUCCESS" : "FAILURE"}`);
  result ? sendOK(res) : sendNO(res);
});

app.post('/login_clientHash', (req, res) => {
  let username = req.body.username, passwordHash = req.body.password;
  
  let result = (username && passwordHash && superSecretCredentials_hashed[username] == passwordHash)
  console.log(`${req.protocol} - /login_clientHash - ${username||"(blank)"}:${passwordHash||"(blank)"} - ${result ? "SUCCESS" : "FAILURE"}`);
  result ? sendOK(res) : sendNO(res);
});


require('http').createServer(app).listen(port, function() {
  console.log(`App (HTTP)  listening on port ${port}!`);
});

require('https').createServer({
  key: fs.readFileSync('./ssl/server.key'),
  cert: fs.readFileSync('./ssl/server.cert')
}, app).listen(8443, function(){
  console.log(`App (HTTPS) listening on port ${secure_port }!`);
});