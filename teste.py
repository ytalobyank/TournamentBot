import csv
import re

# Substitua 'seu_arquivo.csv' pelo caminho do seu arquivo CSV
caminho_arquivo = 'LCK2023Summer.csv'
players_data =[]
with open(caminho_arquivo, newline='', encoding='utf-8') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv, delimiter=',')
    
    # Itera sobre as linhas do arquivo CSV
    for linha in leitor_csv:
        # Verifica se a primeira coluna da linha é igual a 'TRLH3/10113'
      #print(linha)
      players_data.append(linha)


# Nome do jogador específico que você deseja obter as estatísticas
player_name = 'Aiming'

# Iterando sobre as estatísticas dos jogadores
contador99 = 0
for stats in players_data:
    if stats[2] == 'Support' and int(stats[3]) > 1:
        
        killsW = 5
        assistW= 9
        deathW= -5
        kdaW= 3
        
        # Obtendo o número do KDA e a % de winrate
        #winrate_digits = re.sub(r'\D', '', stats[4])
        #winrate = float(winrate_digits) if winrate_digits else 0# Converte a string de dígitos para float
        #kp_digits = re.sub(r'\D', '', stats[10])   
        #kp = float(kp_digits[:-1]) if winrate_digits else 0

        k = int(stats[6])/int(stats[3]) if stats[6].replace('.', '', 1).isdigit() else 0
        d = int(stats[7])/int(stats[3]) if stats[7].replace('.', '', 1).isdigit() else 0
        a = int(stats[8])/int(stats[3]) if stats[8].replace('.', '', 1).isdigit() else 0
        kda = float(stats[9]) if stats[9].replace('.', '', 1).isdigit() else 0
        print(f'Kills:{round(k*killsW,2)} Assists:{round(a*assistW,2)} Deaths:{round(d*deathW,2)} KDA: {round(kda*kdaW,2)}')
        # Fórmula simples para calcular a nota
        score = round((k*killsW)+(a*assistW)+(d*deathW)+(kda*kdaW))
        print(f'Atributo atual: {score}') 
        score = max(50, min(99, score))
        # Criando a string
        result_string = f"Jogador: {stats[0]}, Score:{score} "

        # Exibindo a string
        contador99 += 1 if score < 55 else 0
        print(result_string)
print(f'cartas 99 : {contador99}')
'''['Player', 'Team', 'Pos', 'GP', 'W%', 'CTR%', 'K', 'D', 'A', 'KDA', 'KP', 'KS%', 'DTH%', 'FB%', 'GD10', 'XPD10', 'CSD10', 'CSPM', 'CS%P15', 'DPM', 'DMG%', 'D%P15', 'EGPM', 'GOLD%', 'STL', 'WPM', 'CWPM', 'WCPM']
['', 'Nongshim RedForce', 'Support', '2', '0%', '0%', '1', '5', '20', '4.2', '84.0%', '4.0%', '16.1%', '0%', '234', '542', '30', '3', '8.4%', '162', '7.3%', 
'6.4%', '143', '13.4%', '0', '1.05', '0.24', '0.4']'''
