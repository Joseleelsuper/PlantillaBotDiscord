# Resumen del proyecto

Este proyecto es un bot de Discord desarrollado en Python. El bot tiene la capacidad de realizar diversas acciones y responder a comandos específicos en un servidor de Discord.

## Instalación de las dependencias

Para instalar las dependencias necesarias, puedes utilizar el archivo `requirements.txt`. Ejecuta el siguiente comando en tu consola de comandos:
```
pip install -r requirements.txt
``` 

## Configuración del bot

Para hacer que funcione, debes darle dos datos a través del fichero `variables.env`. Uno de ellos es el `token` y el otro el `guild_id`.

`token` es el token del bot de Discord. Para obtener el token, debes crear una aplicación de Discord en el [portal de desarrolladores](https://discord.com/developers/applications). Luego, debes dirigirte a la sección de bot y crear un bot. Finalmente, debes copiar el token y pegarlo en el archivo `.env`.

Sobre el `guild_id`, debes tener activado el modo desarrollador en discord. Puedes activarlo desde las opciones. Cuando lo tengas, dele click derecho al servidor y haga click a `Copiar ID del servidor`

## Ejecución del bot

Para ejecutar el bot, debes ejecutar el archivo `app.py`. Ejecuta el siguiente comando en tu consola de comandos:
```
python app.py
``` 

## Contribuciones

Si deseas contribuir, puedes abrir un issue o enviar un pull request. Si deseas realizar un cambio importante, te sugiero que abras un issue para discutirlo.

## Licencia

Este proyecto está licenciado bajo la licencia MIT. Para más información, puedes leer el archivo [`LICENSE`](LICENSE)