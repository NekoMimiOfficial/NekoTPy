import requests
import json
import os
import time
import guid as _db
import multiprocessing as mp

def _write(data, file):
    try:
        fappen = open(file, "w")
        fappen.write(data)
        fappen.close()
        return [True, 0]
    except Exception as e:
        return [False, e]

class Bot:
    def __init__(self, token):
        self.API = "https://api.telegram.org"
        self.base = f"{self.API}/bot{token}/"
        self.guid = _db.guid
        self.safe = 1
        self.commands = []
        self.loops = []

    def update_guid(self):
        try:
            os.remove("guid.py")
        except:
            pass
        return str(_write(f"guid = {self.guid}", "guid.py")[1])

    def updater(self):
        try:
            response = requests.get(f"{self.base}getUpdates?offset={self.guid}")
            data = response.json()
        except Exception as e:
            data = []
        return data

    def send(self, message, id):
        uri = f"{self.base}sendMessage?chat_id={id}&text={message}"
        response = requests.get(uri)
        data = response.json()
        return data
    
    def get_context(self,upd):
        class context:
            response = ''
            args = []
            user_id = ''
            username = ''
            chat_id = ''
            update_id = ''
            message_id = ''
            chat_name = ''

        ctx = context()
        ctx.response = ''
        ctx.args = []

        for arg in upd["message"]["text"].split(" "):
            if not arg.startswith("/"):
                ctx.args.append(arg)

        ctx.user_id = upd["message"]["from"]["id"]
        ctx.username = upd["message"]["from"]["username"]
        ctx.chat_id = upd["message"]["chat"]["id"]
        ctx.update_id = upd["update_id"]
        ctx.message_id = upd["message"]["message_id"]

        if "title" in upd["message"]["chat"]:
            ctx.chat_name = upd["message"]["chat"]["title"]
        else:
            ctx.chat_name = ctx.username
        return ctx

    def command(self, func):
        def wrapper():
            name = func.__name__
            name = name.split("_")[1]
            name = f"/{name}"
            while self.safe == 1:
                for upd in self.updater()["result"]:
                    if "message" in upd:
                        uid = upd["update_id"]
                        if int(uid) > self.guid:
                            self.guid = int(uid)
                            self.update_guid()
                            if "text" in upd["message"]:
                                if name in upd["message"]["text"]:
                                    cid = upd["message"]["chat"]["id"]
                                    ctx = self.get_context(upd)
                                    ctx = func(ctx)
                                    self.send(ctx.response, ctx.chat_id)
        self.commands.append(wrapper)
        return wrapper

    def loop(self):
        for com in self.commands:
            loop = mp.Process(target=com)
            self.loops.append(loop)
        for _loop in self.loops:
            _loop.start()

    def halt(self):
        for _loop in self.loops:
            _loop.terminate()
        self.loops = []

