# |---------------------------------------------------------------|#
# |   Nombre del programa: app.py                                 |#
# |   Descripción: Plantilla de Bot para Discord.                 |#
# |   @autor: José Gallardo Caballero                             |#
# |   @date: 07/03/2023                                           |#
# |   @version: v1.0.0                                            |#
# |   Versiones:                                                  |#
# |       v1.0.0 [07/03/2023]: Creación del programa.             |#
# |---------------------------------------------------------------|#

# Librerías
# Generales
import traceback  # Librería para el manejo de errores
from datetime import datetime  # Librería para el manejo de fechas y horas
from dotenv import load_dotenv  # Librería para el manejo de variables de entorno
import os  # Librería que permite el manejo de ficheros y directorios

# Discord
import discord  # Librería para el manejo de Discord
from discord import app_commands  # Librería para el manejo de comandos de Discord
from discord.ext import commands  # Librería para el manejo de comandos de Discord

# Comandos
from commands.functions import *  # Funciones de los comandos
from commands.other import *  # Otros comandos
from commands.util import *  # Comandos de utilidad

# Variables globales
load_dotenv(getDotenv())  # Carga las variables de entorno
# Generales
GUILD_ID = int(os.getenv("GUILD_ID"))  # ID del servidor
CREADOR_ID = int(os.getenv("CREADOR_ID"))  # ID del creador del bot
VERSION = str(os.getenv("VERSION"))  # Versión del bot
COMMAND = read_commands()  # Comandos del bot

# Discord
GUILD = discord.Object(id=GUILD_ID)  # Guild del servidor
INTENTS = discord.Intents.all()  # Permisos del bot
Color = discord.Color.orange()  # Color de la barra lateral de los embeds

# Bot
TOKEN = str(os.getenv("TOKEN"))  # Token del bot
commands_bot = commands.Bot(
    command_prefix="", intents=INTENTS
)  # Prefijo de los comandos del bot, en desuso
PERMISO = int(os.getenv("PERMISO"))  # Nivel de permisos del bot


# Definir la inicialización del bot
class abot(discord.Client):
    # Definir el estado del bot
    def __init__(self):
        super().__init__(
            intents=INTENTS, chunk_guilds_at_startup=True
        )  # Declara el bot como cliente de Discord
        self.token = TOKEN  # Declara el token del bot
        self.bot = commands_bot  # Declara el bot como cliente de Discord
        self.synced = True  # Declara que el bot está sincronizado
        self.activity = discord.Activity(
            type=discord.ActivityType.listening, name="/help"
        )  # Declara la actividad del bot
        self.status = discord.Status.online  # Declara el estado del bot

    # Mensaje de inicio
    async def on_ready(self):
        await tree.sync(
            guild=GUILD
        )  # Sincroniza los comandos del bot con los del servidor.
        print("Bot conectado y listo para usar")  # Mensaje de inicio
        print(
            f"Enlace de invitación: https://discord.com/api/oauth2/authorize?client_id={bot.user.id}&permissions={PERMISO}&scope=bot"
        )  # Enlace de invitación del bot


# Definir el árbol de comandos
bot = abot()
tree = app_commands.CommandTree(bot)

###################################################################
###################################################################
###################################################################


# Funciones
# Función que checkea el envío correcto de comandos
def check(interaction):
    try:
        if interaction.response.is_done():
            print("\n")
            print(
                f"El comando '{interaction.data['name']}' ha sido enviado a '{interaction.guild.name}' por '\
                  {interaction.user.name}' a la hora '{interaction.created_at}'"
            )
    except:
        print("\n\n")
        traceback.print_exc()
        print("\n\n")
        print(
            f"Error al enviar el comando '{interaction.data['name']}' a '{interaction.guild.name}' por '\
              {interaction.user.name}' a la hora '{interaction.created_at}'"
        )


###################################################################
###################################################################
###################################################################


# Eventos
# Evento del bot, da la bienvenida por privado a nuevos usuarios
@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f"Hola {member.name}, bienvenido al servidor {member.guild.name}."
    )


###################################################################
###################################################################
###################################################################


# Comandos
# Comando de ayuda
# Los comandos se ejecutan solamente en su servidor. Para que se ejecuten en cualquier servidor, quitar el parámetro 'guild = Guild'
@tree.command(
    name=COMMAND["help"]["name"], description=["help"]["description"], guild=GUILD
)
async def self(interaction):
    await help(interaction)
    check(interaction)


###################################################################
# Comando de ping
@tree.command(name=["ping"]["name"], description=["ping"]["description"], guild=GUILD)
async def self(interaction):
    await ping(interaction, bot)
    check(interaction)


###################################################################
# Comando de invitación
@tree.command(
    name=["invite"]["name"], description=["invite"]["description"], guild=GUILD
)
async def self(interaction):
    await invite(interaction, bot)
    check(interaction)


###################################################################
# Comando de uptime
@tree.command(
    name=["uptime"]["name"], description=["uptime"]["description"], guild=GUILD
)
async def self(interaction):
    await uptime(interaction, bot_start_time)
    check(interaction)


###################################################################
###################################################################
###################################################################
if __name__ == "__main__":
    bot_start_time = datetime.now()
    bot.run(TOKEN)
