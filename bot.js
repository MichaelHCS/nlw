
const express = require('express');
const TelegramBot = require('node-telegram-bot-api');


const app = express()
app.use(express.json());

app.get('/', (req, res) => {
    return res.json({});
})

app.post('/github-webhook', (req, res) => {
    console.log(res)
    const pr = req.body.pull_request.html_url;
    const token = 'TOKEN';
    const bot = new TelegramBot(token, { polling: false });

    const chatId = ID; // Id do chat para onde a mensagem será enviada
    const mensagem = "Foi aberto um PR Link: " + pr; 


    bot.sendMessage(chatId, mensagem)
        .then(() => res.send('Mensagem enviada com sucesso!'))
        .catch((error) => res.status(500).send(`Erro ao enviar mensagem: ${error}`));
});

app.listen(3001, () => {
    console.log('Servidor do Express iniciado na porta 3001!');
  });
