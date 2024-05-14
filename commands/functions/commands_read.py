import json
from commands.functions.getDBFiles import getCommands


def read_commands():
    with open(getCommands(), "r") as f:
        commands = json.load(f)
    return commands
