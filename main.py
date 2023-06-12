import discord
from Khazix import Khazix

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}')

@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.content.startswith('!check'):

        if len(message.content[7:]) < 3 or len(message.content[7:]) > 16:
            return await message.reply("O nome de invocador tem que ser maior que 3 e menor 16 digitos.")

        nickname = Khazix(message.content[7:])
        text = await nickname.search()  

        embed = discord.Embed(title="Resultado da Verificação", description=text, color=0x0099ff)
        embed.set_footer(text="discord.gg/voidstore")
        embed.set_thumbnail(url="https://imgs.search.brave.com/sCPiJ5ZUQJUhixS-by0gvcIE69ydLjs-SxPr2LJDnTk/rs:fit:512:512:1/g:ce/aHR0cHM6Ly9pbWFn/ZXMuY29udGVudHN0/YWNrLmlvL3YzL2Fz/c2V0cy9ibHQ3MzFh/Y2I0MmJiM2QxNjU5/L2JsdDZmMTg2ZGMz/Y2NhNzVmNTAvNjA0/YWVmZWJhOGM2NTg1/Y2RhMjRkZDY2LzMx/MzVfTWFnZV9UM19W/b2lkU3RhZmYucG5n")
        embed.set_image(url="https://imgs.search.brave.com/sltuyQG6tiNqMb2vCOavsYEfMWbY5q4rIAlfg3Kefzc/rs:fit:1200:600:1/g:ce/aHR0cHM6Ly9lc3Bv/cnRzLmFzLmNvbS8y/MDE4LzA5LzEzL3Nr/aW5zL2toYXppeC1j/aGFtcGlvbnNoaXAt/NzcweDQ1NDFfMTE3/MjI5Mjc2NV8xMDM1/OTNfMTQ0MHg2MDAu/anBn") # Substitua pela URL da sua imagem grande
        await message.reply(embed=embed)

client.run("")
