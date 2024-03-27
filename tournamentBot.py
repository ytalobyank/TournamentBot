import discord
import typing
from discord.ext import commands
from discord import app_commands
from tabela import *
from controller import *
from utility import *
from views import *
from config import bot_token

idAdmin = 830857697170685972;
canal_id = 1215445199099142147
tempo_slowmode = 1800
rounds= []
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='.', intents=intents)

@bot.event
async def on_ready():
    #Lembrar de usar o sincronizar pra sincronizar os slash commands
    print(f'{bot.user} has connected to Discord!')


#.sincronizar
@bot.command()
async def sincronizar(ctx:commands.Context):
    if ctx.author.id == idAdmin:
        sincs = await bot.tree.sync()
        await ctx.reply(f'{len(sincs)} comandos sincronizados',ephemeral=True)
    else:
        await ctx.reply(f'Você não pode acessar isto.')


@bot.tree.command(name='criartime', description="Crie um time com o nome que você digitar")
async def criartime(interaction: discord.Interaction, *, team: str):
    try:
        # Verifica o comprimento do nome do time
        if len(team) > 30:
            raise ValueError('O nome do time não pode ter mais de 30 caracteres.')

        # Verifica se o time já existe
        if checkTeam(team):
            await interaction.response.send_message(f'{interaction.user.mention} Já existe um time com o nome {team}.')
        else:
            # Cria o time
            createTeam(team)
            await interaction.response.send_message(f'{interaction.user.mention} O time {team} foi criado.')

    except ValueError as e:
        # Captura e trata o erro de comprimento do nome do time
        await interaction.response.send_message(str(e))

    except Exception as e:
        # Captura e trata outros erros inesperados
        await interaction.response.send_message(f'{interaction.user.mention} Ocorreu um erro inesperado ao criar o time.')


#.deletartime
@bot.tree.command(name="deletartime", description="Delete um time")
@app_commands.autocomplete(team=teamsAutocomplete)
async def deletartime(interaction:discord.Interaction, *, team:str):
    try:
        # Verifica se o usuário é o administrador
        if interaction.user.id != idAdmin:
            raise PermissionError('Você não tem permissão para acessar isso.')

        # Deleta o time e verifica se foi encontrado
        if deleteTeam(team):
            await interaction.response.send_message(f'{team} foi apagado.')
        else:
            await interaction.response.send_message(f'{team} não foi encontrado.')

    except PermissionError as e:
        # Captura e trata erro de permissão
        await interaction.response.send_message(str(e))

    except Exception as e:
        # Captura e trata outros erros inesperados
        await interaction.response.send_message('Ocorreu um erro inesperado ao deletar o time.')


'''#.criarRodada
@bot.command()
async def criarRodadas(ctx:commands.Context):
    if ctx.author.id == idAdmin:
        #global rounds 
        #rounds = createRounds(getTableTeams())  
         
        await ctx.reply(f'Rodadas criadas com sucesso.')
    else:
        await ctx.reply(f'Você não pode acessar isto.')'''


#.rodada
@bot.tree.command()
@app_commands.autocomplete(round_number=roundsAutoComplete)
async def rodada(interaction:discord.Interaction, round_number:int):
    
    global rounds 
    try:
        if round_number == 0:
            await interaction.response.send_message('Nada acontece',ephemeral=True)
            return
        if interaction.user.id == idAdmin: 
            if not rounds:
                rounds = createRounds(getTableTeams()) 
                if not rounds:
                    await interaction.response.send_message(f'As rodadas ainda não foram criadas.') 
            if round_number <= 0 or round_number > len(rounds):
                await interaction.response.send_message('Número de rodada inválido.')
            else:
                max_width = 0
                for i, round_matches in enumerate(rounds[round_number - 1:], start=round_number):
                    for match in round_matches:
                        max_width = max(len(match[0]), len(match[1])) if max_width < max(len(match[0]), len(match[1])) else max_width
                    for match in round_matches:
                        if match[0] and match[1] != 'descanso':
                            embed = discord.Embed(
                            description='',
                            color=discord.Color.blue()
                            )
                            embed.title=centerTitle(f'**Rodada {i}**', max_width)
                            embed.add_field(name='', value=f'`{match[0]:^{max_width}} VS {match[1]:^{max_width}}`\n\n', inline=False)
                            view = roundView(embed=embed, homeTeam=f'{match[0]}',awayTeam=f'{match[1]}')
                            await interaction.channel.send(embed=embed, view=view)   
                            if not interaction.response.is_done():
                                await interaction.response.send_message(f'.', ephemeral=True,delete_after=0)

                    break   
        else:
            await interaction.response.send_message(f'Você não pode acessar isto.')
    except Exception as e:
        await interaction.response.send_message(f'Ocorreu um erro ao processar o comando: {str(e)}')

#.tabela
@bot.command()
async def tabela(ctx:commands.Context):
    try:
        if ctx.author.id == idAdmin:
            times = getTableTeams()
            if not times:
                await ctx.send('A tabela está vazia. Certifique-se de ter times cadastrados.')
                return
            
            embed = discord.Embed(
                title=centerTitle(f'Tabela', 94),
                description='O ranking está da seguinte forma:',
                color=discord.Color.blue()
            )
            #Nome do time só pode ir até 30 caracteres
            embed.add_field(name='', value=createTable(times),inline=False)

            await ctx.send(embed=embed)
            
        else:
            await ctx.reply(f'Você não pode acessar isto.')
    except Exception as e:
        await ctx.reply(f'Ocorreu um erro ao processar o comando: {e}')

#/ajuda
@bot.tree.command(description='Lista de comandos do bot')

async def ajuda(interact:discord.Interaction):
    await interact.response.send_message(f'oi, você gosta de ')

bot.run(bot_token)
