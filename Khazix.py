import requests
from bs4 import BeautifulSoup

class Khazix:
    def __init__(self, nickname):
        self._nickname = nickname
        self._headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 OPR/97.0.0.0"
        }

    async def search(self):
        try:
            response = requests.get(f"https://lols.gg/pt/name/checker/br/{self._nickname}/", headers=self._headers)
        
            soup = BeautifulSoup(response.text, 'html.parser')
            tags = soup.find_all('h4', {'class': 'text-center'})
        
            if len(tags) == 0:
                return f"{self._nickname} provavelmente está disponível."

            for messages in tags:
                return messages.text
        except:
            print("Ocorreu um erro ao fazer a requisição. \nTente novamente dentro de alguns segundos. \nSe o erro persistir entre em contato com administração do servidor.")