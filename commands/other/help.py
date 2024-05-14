import traceback

from discord import Color, Embed, Interaction
from commands.functions.commands_read import read_commands

async def help(interaction: Interaction):
    try:
        # Leer comandos y ordenarlos por nombre
        commands = sorted(read_commands().values(), key=lambda command: command['name'])

        # Crear y enviar múltiples embeds si es necesario
        for i in range(0, len(commands), 25):
            # Crear embed
            embed = Embed(
                title="Comandos del bot",
                description="Los comandos disponibles son:",
                color=Color.orange(),
            )

            # Agregar hasta 25 comandos a este embed
            for command in commands[i:i+25]:
                embed.add_field(
                    name="/"+command['name'],
                    value=command['description'],
                    inline=False
                )

            # Si es la primera respuesta, usar interaction.response.send_message
            if i == 0:
                await interaction.response.send_message(embed=embed, ephemeral=True)
            # Para respuestas adicionales, usar interaction.followup.send
            else:
                await interaction.followup.send(embed=embed, ephemeral=True)

    except:
        traceback.print_exc()
        await interaction.response.send_message(
            f"Error al ejecutar el comando.",
            ephemeral=True,
        )