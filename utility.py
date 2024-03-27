import discord
from discord import app_commands
from typing import List
from discord.app_commands import choices
from controller import getTableTeams

def centerTitle(title, total_width):
    left_spaces = (total_width - len(title)) // 2
    right_spaces = total_width - len(title) - left_spaces
    centered_title = f"\u200B{' ' * left_spaces}{title}{' ' * right_spaces}"
    return centered_title

def sortTable(teams):
    sorted_teams = sorted(teams, key=lambda x: (x['vitorias'], -x['derrotas']), reverse=True)
    return sorted_teams

async def teamsAutocomplete(interaction: discord.Interaction,current: str,) -> List[app_commands.Choice[str]]:
    teamList = getTableTeams()
    nameList = []
    for team in teamList:
        nameList.append(team['nome'])
    
    return [
        app_commands.Choice(name=name, value=name)
        for name in nameList if current.lower() in name.lower()
    ]
async def roundsAutoComplete(interaction: discord.Interaction,current: str,) -> List[app_commands.Choice[str]]:
    teamList = getTableTeams()
    if not teamList:
        return [app_commands.Choice(name=f"Não temos rodadas, tente adicionar times",value=0)]
    nameList = []
    for team in teamList:
        nameList.append(team['nome'])

    numRounds = (len(nameList) - 1) * 2
    
    return [
        app_commands.Choice(name=f'round {i}', value=i)
        for i in range(1, numRounds + 1) if current.lower() in str(i).lower()
    ]