import discord
from discord.ext import commands
from controller import *
import datetime

class roundView(discord.ui.View):
    def __init__(self, embed: discord.Embed,homeTeam:str,awayTeam:str):
        super().__init__()
        self.homeTeam = homeTeam
        self.awayTeam = awayTeam
        self.embed = embed
    
    @discord.ui.button(label='Casa', style=discord.ButtonStyle.blurple, custom_id='house_button')
    async def houseButton(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            # Atualiza o campo de descrição do embed
            self.clear_items()
            if interaction.response:
                await interaction.response.defer()
            for field in self.embed.fields:
                if self.homeTeam in field.value:
                    updateAfterGame(self.homeTeam,self.awayTeam)
                    self.embed.title += f'\n O Time {self.homeTeam} ganhou'
                    await interaction.edit_original_response(embed=self.embed, view=self)
                    return
        except discord.HTTPException as e:
            # Lidar com exceção específica para erros HTTP
            print(f'Erro ao editar resposta original: {e}')
        except Exception as e:
            # Lidar com outras exceções não previstas
            print(f'Erro não previsto: {e}')

    @discord.ui.button(label='Fora', style=discord.ButtonStyle.red, custom_id='away_button')
    async def awayButton(self, interaction: discord.Interaction, button: discord.ui.Button ):
        try:
            # Atualiza o título da embed e atualiza o dado no banco.
            self.clear_items()
            if interaction.response:
                await interaction.response.defer()
            teamList = getTableTeams()
            for team in teamList:
                for field in self.embed.fields:
                    if self.awayTeam in field.value:
                        updateAfterGame(self.awayTeam,self.homeTeam)
                        self.embed.title += f'\n O Time {self.awayTeam} ganhou'
                        await interaction.edit_original_response(embed=self.embed, view=self)
                        
                        return
        except discord.HTTPException as e:
            # Lidar com exceção específica para erros HTTP
            print(f'Erro ao editar resposta original: {e}')
        except Exception as e:
            # Lidar com outras exceções não previstas
            print(f'Erro não previsto: {e}')
