from tg_types import context
import processes

__internal_errors = []
__TG_BOT_API = "https://api.telegram.org/"


def write(data: str, file: str):
    try:
        buffer = open(file, 'w')
        buffer.write(data)
        buffer.close()
    except Exception as e:
        __internal_errors.append(e)
        print(str(e))


def read(file: str):
    try:
        buffer = open(file, 'r')
        data = buffer.read()
        buffer.close()
    except Exception as e:
        __internal_errors.append(e)
        print(str(e))
        data = ""

    return data


class Command:
    def __init__(self, token):
        self.token = token
        self.base = f"{__TG_BOT_API}bot{self.token}/"
        self.file_base = f"{__TG_BOT_API}file/bot{self.token}/"
        self.offset = f"?offset={self.getOffset()}"
        self.queue = []

    def getOffset(self):
        pass

    def setOffset(self):
        pass

    def connectCable(self, operation, data):
        if operation == 'send':
            self.queue.append({'type':'send', 'contents':data})
        elif operation == 'get':
            self.queue.append({'type':'get', 'contents':data})

    def createContext(self, update):
        ctx = context.Context(self)
        
        if "message" in update:
            if "text" in update["message"]:
                for arg in update["message"]["text"].split(" "):
                    if not arg.startswith("/"):
                        ctx.Args.append(arg)
            elif "caption" in update["message"]:
                for arg in update["message"]["caption"].split(" "):
                    if not arg.startswith("/"):
                        ctx.Args.append(arg)

            if "from" in update["message"]:
                ctx.UserID = int(update["message"]["from"]["id"])
                if "username" in update["message"]["from"]:
                    ctx.UserName = update["message"]["from"]["username"]
                if "first_name" in update["message"]["from"]:
                    ctx.DetailedUserName.append(update["message"]["from"]["first_name"])
            
            ctx.MessageID = int(update["message"]["message_id"])
            ctx.UpdateID = int(update["update_id"])

            if "chat" in update["message"]:
                ctx.ChatID = int(update["message"]["chat"]["id"])
                if "title" in update["message"]["chat"]:
                    ctx.ChatName = update["message"]["chat"]["title"]

        return ctx
