# Resumen del proyecto

Este proyecto es un bot de Discord desarrollado en Python. El bot tiene la capacidad de realizar diversas acciones y responder a comandos específicos en un servidor de Discord.

# Instalación de Python

Se debe de tener instalada la última versión de [Python](https://www.python.org/downloads/) para proceder a utilizar el bot localmente.
Instalarlo donde se quiera.

# Instalación de las dependencias

Para instalar las dependencias necesarias, puede utilizar el archivo `requirements.txt`. Ejecute el siguiente comando en tu consola de comandos:
```
pip install -r requirements.txt
``` 

# Configuración del bot

Para hacer que funcione, debe darle dos datos a través del fichero `variables.env`. Uno de ellos es el `token` y el otro el `guild_id`.

`token` es el token del bot de Discord. Para obtener el token, debe crear una aplicación de Discord en el [portal de desarrolladores](https://discord.com/developers/applications). Luego, debe dirigirte a la sección de bot y crear un bot. Finalmente, debe copiar el token y pegarlo en el archivo `.env`.

Sobre el `guild_id`, debe tener activado el modo desarrollador en discord. Puede activarlo desde las opciones. Cuando lo tenga, haga click derecho al servidor y después click a `Copiar ID del servidor`

# Ejecución del bot

Para ejecutar el bot, debes ejecutar el archivo `app.py`. Ejecuta el siguiente comando en tu consola de comandos:
```
python app.py
``` 

# Contribuciones

Si deseas contribuir, puedes abrir un issue o enviar un pull request. Si deseas realizar un cambio importante, te sugiero que abras un issue para discutirlo.

# Licencia

Este proyecto está licenciado bajo la licencia MIT. Para más información, puedes leer el archivo [LICENSE](LICENSE)