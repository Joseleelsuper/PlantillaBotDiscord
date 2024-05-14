from discord import Color, Embed, Interaction

async def invite(interaction: Interaction):
    try:
        embed = Embed(
            title="Invitación del bot",
            description="Puedes invitar al bot a tu servidor con el siguiente [enlace](https://discord.com/api/oauth2/authorize?client_id=890066169474443048&permissions=8&scope=bot%20applications.commands).",
            color=Color.orange(),
        )

        await interaction.response.send_message(embed=embed, ephemeral=True)
    except:
        await interaction.response.send_message(
            f"Error al ejecutar el comando.",
            ephemeral=True,
        )