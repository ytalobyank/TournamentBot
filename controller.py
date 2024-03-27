import json
import functools

def getData():
    try:
        with open("database.json", "r") as arquivo_json:
            dados = json.load(arquivo_json)
    except FileNotFoundError:
        dados = []
    return dados

def saveData(dados):
    with open("database.json", "w") as arquivo_json:
        json.dump(dados, arquivo_json, indent=2)

def createTeam(name, wins=0, loses=0):
    dados = getData()
    team = {"nome": name, "vitorias": wins, "derrotas": loses}
    dados.append(team)
    saveData(dados)

def getTableTeams():
    times = []
    dados = getData()
    if not dados:
        return
    for team in dados:
        team['jogos'] = team['vitorias'] + team['derrotas'] 
        times.append(team)

    return times

def checkTeam(name):
    dados = getData()
    for team in dados:
        if name.lower() == team['nome'].lower():
            return 1
        return 0

def updateAfterGame(teamWinner, teamLoser) :
    dados = getData()
    for time in dados:
        if time['nome'] == teamWinner:
            time['vitorias'] += 1
        if time['nome'] == teamLoser:
            time['derrotas'] += 1
        saveData(dados)


def deleteTeam(teamName):
    dados = getData()
    for time in dados:
        if time['nome'] == teamName:
            dados.remove(time)
            saveData(dados)
            return 1
    return 0        

#print(f'{getTableTeams()}')