import requests
import json
import os
import time
import multiprocessing as mp

def _write(data, file):
    try:
        fappen = open(file, "w")
        fappen.write(data)
        fappen.close()
        return [True, 0]
    except Exception as e:
        return [False, e]

def _read(file):
    try:
        fappen = open(file)
        data = fappen.read()
        fappen.close()
        return data
    except Exception as e:
        raise e

def __parse_nhc(file):
    contents = _read(file)
    return contents.split("=UwU=")[0], contents.split("=UwU=")[1]

#------------------------------------------------------#
#             version 2 with a local queue             #
#------------------------------------------------------#

class Bot:
    def __init__(self, token):
        self.API = "https://api.telegram.org"
        self.base = f"{self.API}/bot{token}/"
        self.file_base = f"{self.API}/file/bot{token}/"
        self.commands = {}
        self.wait_queue = {}
        self.event_func = []
        self.cmd_info = []
        self.errors = []
        self.runner = None
        self.guid, self.gwid = __parse_nhc("env.nhc")
        self.attr = f"?offset={self.guid}"
        self.additional_attr = []

    def _guid_update(self):
        try:
            os.remove("env.nhc")
        except Exception as e:
            print(e)
            pass
        return _write(f"{self.guid}=UwU={self.gwid}", "env.nhc")[1]

    def _update(self):
        try:
            response = requests.get(f"{self.base}getUpdates{self.attr}")
            data = response.json()
        except Exception as e:
            self.errors.append(e)
            data = []
        return data

    def _context_object(self,upd):
        class context:
            def __init__(self, pself, upd):
                self.args = []
                self.user_name = ''
                self.user_id = ''
                self.user_fname = ''
                self.chat_name = ''
                self.chat_id = ''
                self.message_id = ''
                self.update_id = ''
                self.base = pself.base
                self.file_base = pself.file_base
                self.update = upd
                self.pself = pself

            def send(self, text, mention=False, reply=None):
                rep = ""
                if mention == True:
                    rep = f"&reply_to_message_id={self.message_id}"
                elif not reply == None:
                    rep = f"&reply_to_message_id={reply}"
                uri = f"{self.base}sendMessage?chat_id={self.chat_id}&text={text}" + rep
                response = requests.get(uri)
                data = response.json()
                return data

            def keyboard(self, text, buttons, resize=True, one_time=True):
                kb = []
                for key in buttons:
                    full_key = [{"text":key}]
                    kb.append(full_key)

                headers = {'Content-Type':'application/json'}
                rm = {"keyboard":kb, "resize_keyboard":resize, "one_time_keyboard":one_time}
                data = {"chat_id":str(self.chat_id), "text": text, "reply_markup":rm}
                data = json.dumps(data)
                uri = f"{self.base}sendMessage"
                response = requests.post(uri, headers=headers, data=data)
                return response.json()

            def upload(self, file, cap=None):
                cap = cap or file
                docFile = open(file, 'rb')
                uri = f"{self.base}sendDocument"
                response = requests.post(uri,data={'chat_id' : self.chat_id , 'caption' : cap}, files={'document' : docFile})
                data = response.json()
                docFile.close()
                return data

            def sendPhoto(self, file, cap=None):
                cap = cap or file
                docFile = open(file, 'rb')
                uri = f"{self.base}sendPhoto"
                res_d = {'chat_id':self.chat_id, 'caption':cap}
                response = requests.post(uri, data=res_d, files={'photo':docFile})
                data = response.json()
                docFile.close()
                return data

            def file(self):
                class fileContextObject:
                    def __init__(self):
                        self.file_name = 'null'
                        self.mime = 'none'
                        self.file_id = 'none'
                        self.file_u_id = 'none'
                        self.file_size = '0'

                if "document" in self.update["message"]:
                    doc = self.update["message"]["document"]
                    file_ctx = fileContextObject()
                    file_ctx.file_name = doc["file_name"]
                    file_ctx.mime = doc["mime_type"]
                    file_ctx.file_id = doc["file_id"]
                    file_ctx.file_u_id = doc["file_unique_id"]
                    file_ctx.file_size = doc["file_size"]
                    return file_ctx
                else:
                    return fileContextObject()

            def get_link(self, fid):
                if fid == 'none':
                    return "none"
                uri = f"{self.base}getFile?file_id={fid}"
                response = requests.get(uri)
                data = response.json()
                if not "result" in data:
                    if not "file_path" in data["result"]:
                        return 'none'
                    return 'none'
                return f'{self.file_base}{data["result"]["file_path"]}'

            def wait_for_response(self, func):
                param = {str(self.user_id) : func}
                self.pself.wait_queue.update(param)

            def got_response(self):
                self.pself.wait_queue.update({})

        ctx = context(self, upd)
        
        if "text" in upd["message"]:
            for arg in upd["message"]["text"].split(" "):
                if not arg.startswith("/"):
                    ctx.args.append(arg)

        elif "caption" in upd["message"]:
            for arg in upd["message"]["caption"].split(" "):
                if not arg.startswith("/"):
                    ctx.args.append(arg)

        #ctx.user_name = upd["message"]["from"]["username"]
        ctx.user_id = upd["message"]["from"]["id"]
        ctx.user_fname = upd["message"]["from"]["first_name"]
        #ctx.chat_name = upd["message"]["chat"]["title"]
        ctx.chat_id = upd["message"]["chat"]["id"]
        ctx.message_id = upd["message"]["message_id"]
        ctx.update_id = upd["update_id"]

        if "title" in upd["message"]["chat"]:
            ctx.chat_name = upd["message"]["chat"]["title"]
        else:
            ctx.chat_name = None

        if "username" in upd["message"]["from"]:
            ctx.user_name = upd["message"]["from"]["username"]
        else:
            ctx.user_name = None

        return ctx
    
    def _event_context_object(self, upd):
        class eventContextObject:
            def __init__(self, pself):
                self.chat_id = ''
                self.user_id = ''
                self.user_bot = False
                self.user_fname = ''
                self.user_name = None
                self.chat_title = ''
                self.event = ''
                self.base = pself.base

            def send(self, text):
                uri = f"{self.base}sendMessage?chat_id={self.chat_id}&text={text}"
                response = requests.get(uri)
                data = response.json()
                return data
            
        message = upd["message"]
        event_ctx = eventContextObject(self)

        event_ctx.chat_id = message["chat"]["id"]
        if "new_chat_participant" in message:
            ncp = message["new_chat_participant"]
            event_ctx.user_id = ncp["id"]
            if not ncp["is_bot"] == "false":
                event_ctx.user_bot = True
            event_ctx.user_fname = ncp["first_name"]
            if "username" in ncp:
                event_ctx.user_name = ncp["username"]
            event_ctx.chat_title = message["chat"]["title"]
            event_ctx.event = "new_chat_participant"

        return event_ctx

    def __event_loop(self):
        while True:
            time.sleep(0.5)
            opo = self._update()
            if "result" in opo:
                for upd in opo["result"]:
                    if "message" in upd:
                        uid = upd["update_id"]
                        if int(uid) > self.guid:
                            self.guid = int(uid)
                            self._guid_update()
                            if "text" in upd["message"]:
                                text = upd["message"]["text"]
                                text_old = text
                                if not text_old.startswith("/"):
                                    __user_id = upd["message"]["from"]["id"]
                                    __user_id = str(__user_id)
                                    if __user_id in self.wait_queue:
                                        self.wait_queue[__user_id](text_old)
                                else:
                                    text = text.split("/", 1)[1]
                                    text = text.split(" ", 1)[0]
                                    if text in self.commands:
                                        ctx = self._context_object(upd)
                                        self.commands[text](ctx)
                            if "caption" in upd["message"]:
                                text = upd["message"]["caption"]
                                text = text.split("/", 1)[1].split(" ", 1)[0]
                                if text in self.commands:
                                    ctx = self._context_object(upd)
                                    self.commands[text](ctx)
                            if "new_chat_participant" in upd["message"]:
                                event_ctx = self._event_context_object(upd)
                                for __event_handler in self.event_func:
                                    __event_handler(event_ctx)


    def Command(self, func):
        name = func.__name__
        name = name.split("_", 1)[1]
        self.commands[name] = func

        self.cmd_info.append(f"{name} has been added to the command queue")

    def Event(self, func):
        self.event_func.append(func)
        self.cmd_info.append(f"{func.__name__} has been added as an events handler")

    def run(self):
        if self.runner == None:
            self.runner = mp.Process(target = self.__event_loop)
            self.runner.start()
            line = ""
            for attr,value in self.additional_attr:
                line = line + f"&{attr}"
            return True
        else:
            return False

    def stop(self):
        if not self.runner == None:
            self.runner.terminate()
            self.runner = None
            return True
        else:
            return False
