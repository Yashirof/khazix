# Kha'Zix Bot
O Kha'Zix Bot é um bot de verificação de nick para o jogo League of Legends. Ele utiliza técnicas de web scraping para checar a disponibilidade de um nick no site https://lols.gg/. Com este bot, você pode verificar se um determinado nick está disponível, ou até mesmo descobrir em quantos dias ele ficará disponível.

# Comandos
Para usar o bot, você deve digitar o seguinte comando no seu servidor do Discord:

!check nickname

Substitua nickname pelo nome do nick que você deseja verificar. O bot irá então fazer uma consulta ao site https://lols.gg/ e retornará uma resposta com a disponibilidade do nick e, se aplicável, a previsão de quando o nick estará disponível.

Requisitos
Antes de executar o bot, certifique-se de ter as seguintes dependências instaladas:

Python 3.x
discord.py
BeautifulSoup
requests

# configuração 

No arquivo config.py, adicione o token do seu bot do Discord:

TOKEN = 'seu_token_aqui'

este token você consegue adiquirir no site https://discord.com/developers/applications basta criar uma aplicação ir na sessão bot e reset token 

# Contribuição
Se você encontrar algum problema ou tiver sugestões de melhoria, fique à vontade para abrir uma issue ou enviar um pull request para este repositório.
