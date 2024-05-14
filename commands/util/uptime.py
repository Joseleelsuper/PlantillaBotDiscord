from datetime import datetime
from discord import Interaction

async def uptime(
    interaction: Interaction,
    bot_start_time: datetime,
):
    try:
        # Mostrar tiempo de actividad
        now = datetime.now()
        uptime = now - bot_start_time
        await interaction.response.send_message(f"Bot uptime: {uptime}", ephemeral=True)
    except:
        await interaction.response.send_message(
            f"Error al ejecutar el comando.",
            ephemeral=True,
        )