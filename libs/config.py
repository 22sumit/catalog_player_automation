import configparser
import logging.config


#log config

logging.config.fileConfig("../resources/logging.ini")
log = logging.getLogger(__name__)

# app config

config= configparser.ConfigParser()
config.read("../resources/app.ini")
print(config.get("DEFAULT", "url"))

def get_default(key):
    value=config.get("DEFAULT",key)
    return value