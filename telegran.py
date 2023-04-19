import time
import telegram


# Token do seu bot do Telegram
telegram_token = '5897063253:AAEvHFH5IfS8yg18gZti0q-VfL6h2GayMN0'

# Seu token de acesso pessoal do GitHub
github_token = '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'

# Nome do seu usuário no GitHub e o nome do seu repositório
github_username = 'MichaelHCS'
github_repo_name = 'nlw-esports-explorer'

# Inicialize o bot do Telegram
bot = telegram.Bot(token=telegram_token)

# Inicialize o objeto do GitHub
g = Github(github_token)

# Defina a mensagem que será enviada para o Telegram
message = 'Uma nova versão do seu repositório do GitHub foi criada!'

# Obtenha o objeto de repositório do GitHub
repo = g.get_user(github_username).get_repo(github_repo_name)

# Obtenha o número da última versão do repositório
last_commit = repo.get_commits()[0]
last_commit_number = last_commit.commit.message.split(' ')[0]

# Defina um loop para verificar se há novas versões a cada minuto
while True:
    # Obtenha o número da última versão do repositório
    commit = repo.get_commits()[0]
    commit_number = commit.commit.message.split(' ')[0]
    
    # Se houver uma nova versão, envie uma mensagem para o Telegram
    if commit_number != last_commit_number:
        bot.send_message(chat_id='TestBot', text=message)
        last_commit_number = commit_number
    
    # Aguarde 1 minuto antes de verificar novamente
    time.sleep(60)
