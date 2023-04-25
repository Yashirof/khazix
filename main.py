import requests
from bs4 import BeautifulSoup
import discord
from discord import Intents

intents = Intents.default()
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}')

@client.event
async def on_message(message):
    if message.content.startswith('!check'):
        name = message.content[7:]
        url = f'https://lols.gg/en/name/checker/BR/{name}'
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        div = soup.find('h4', class_='text-center')
        if div is None:
            span = soup.find('span', class_='not-available')
            if span is None:
                await message.channel.send('Nickname não encontrado no servidor BR')
            else:
                await message.channel.send(f'Name "{name}" is not available on BR server.')
        else:
            embed = discord.Embed(title="Resultado da Verificação", description=div.text, color=0x0099ff)
            embed.set_footer(text="discord.gg/voidstore")
            embed.set_thumbnail(url="https://imgs.search.brave.com/sCPiJ5ZUQJUhixS-by0gvcIE69ydLjs-SxPr2LJDnTk/rs:fit:512:512:1/g:ce/aHR0cHM6Ly9pbWFn/ZXMuY29udGVudHN0/YWNrLmlvL3YzL2Fz/c2V0cy9ibHQ3MzFh/Y2I0MmJiM2QxNjU5/L2JsdDZmMTg2ZGMz/Y2NhNzVmNTAvNjA0/YWVmZWJhOGM2NTg1/Y2RhMjRkZDY2LzMx/MzVfTWFnZV9UM19W/b2lkU3RhZmYucG5n")
            embed.set_image(url="https://imgs.search.brave.com/sltuyQG6tiNqMb2vCOavsYEfMWbY5q4rIAlfg3Kefzc/rs:fit:1200:600:1/g:ce/aHR0cHM6Ly9lc3Bv/cnRzLmFzLmNvbS8y/MDE4LzA5LzEzL3Nr/aW5zL2toYXppeC1j/aGFtcGlvbnNoaXAt/NzcweDQ1NDFfMTE3/MjI5Mjc2NV8xMDM1/OTNfMTQ0MHg2MDAu/anBn") # Substitua pela URL da sua imagem grande
            await message.channel.send(embed=embed)

client.run('')
