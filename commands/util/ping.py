import os
from discord import Interaction, Member
import traceback
from dotenv import load_dotenv

from commands.functions.getDBFiles import getDotenv

load_dotenv(getDotenv())
PERMISO = int(os.getenv("PERMISO"))

async def ping(
    interaction: Interaction,
    bot,
):
    try:
        # Mostrar ping (ms)
        await interaction.response.send_message(
            f"Enlace de invitación: https://discord.com/api/oauth2/authorize?client_id={bot.user.id}&permissions={PERMISO}&scope=bot",
            ephemeral=True,
        )
    except:
        traceback.print_exc()
        await interaction.response.send_message(
            f"Error al ejecutar el comando.",
            ephemeral=True,
        )