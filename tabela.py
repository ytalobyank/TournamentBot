from utility import *
def createTable(teams):
    nomeLength = max(5, max(len(time['nome']) for time in teams))
    vitoriaLength = 8
    derrotaLength = 8
    jogosLength = 5
    pontosLength = 6
    teams = sortTable(teams)
    cabecalho = f"`| {'Times':^{nomeLength}} | {'Pontos':^{pontosLength}} | {'Vitorias':^{vitoriaLength}} | {'Derrotas':^{derrotaLength}} | {'Jogos':^{jogosLength}} `\n"
    tabela = f"{cabecalho}"

    for time in teams:
        linha = f"`| {time['nome']:^{nomeLength}} | {str(time['vitorias']*3):^{pontosLength}} | {str(time['vitorias']):^{vitoriaLength}} | {str(time['derrotas']):^{derrotaLength}} | {str(time['jogos']):^{jogosLength}} `\n"
        tabela += linha
    return tabela


# Corta a string para apenas os primeiros 30 caracteres
def checkAndCut(string):
    if len(string) > 30:
        return string[:30]
    else:
        return string
    
#Cria sigla da string
def creatingTeamAcronym(teamName):
    words = teamName.split()
    acronyms = ''.join(word[0] for word in words)
    return acronyms

def createRounds(teamList):
    try:
        if not teamList or len(teamList) < 2:
            raise ValueError("A lista de equipes deve conter pelo menos duas equipes.")

        nameTeamsList = []
        for team in teamList:
            nameTeamsList.append(team['nome'])

        if len(nameTeamsList) % 2:
            nameTeamsList.append('descanso')

        numTeams = len(nameTeamsList)
        numRounds = (numTeams - 1) * 2
        metade = numTeams // 2

        rounds = []

        for i in range(numTeams - 1):
            round = []
            for j in range(metade):
                homeTeam = nameTeamsList[j]
                awayTeam = nameTeamsList[-j - 1]
                round.append((homeTeam, awayTeam))
            nameTeamsList.insert(1, nameTeamsList.pop())
            rounds.append(round)

        complete_rounds = rounds + [[(b, a) for a, b in round_matches] for round_matches in rounds]
        return complete_rounds

    except Exception as e:
        print(f"Erro ao criar rodadas: {e}")
        return None

