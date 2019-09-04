import chicobot
import json

fp = open("token.json")
jsonFile = json.load(fp)
fp.close()

bot = chicobot.ChicoBot(jsonFile["token"])
bot.run()
