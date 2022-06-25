#!/usr/bin/env python3


"""Importing"""
from os import environ


class Config(object):
    API_ID = int(environ.get("API_ID", 7031536))
    API_HASH = environ.get("API_HASH", "fada850e5a6155f164c80e61d0ff0b82")
    BOT_TOKEN = environ.get("BOT_TOKEN", "5085164474:AAHQr8L12kO-yGX5Tb_6wo3md9o_LvwVqVI")
    MONGO_STR = environ.get("MONGO_STR", "mongodb+srv://dinukacreation:dinukacreation@cluster0.hnluk.mongodb.net/?retryWrites=true&w=majority")

