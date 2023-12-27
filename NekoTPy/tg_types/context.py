class Context:
    
    def __init__(self, pself) -> None:
        self.parent = pself
        self.ChatID: int = 0
        self.UserID: int = 0
        self.MessageID: int = 0
        self.UpdateID: int = 0
        self.UserName:str = ''
        self.ChatName:str = ''
        self.DetailedUserName: list = []
        self.Args: list[str] = []

        self.baseURL = self.parent.base
        self.fileBaseURL = self.parent.file_base
        self.offset = self.parent.offset

        def send(self, text, mention = False, reply = None):
            attr = ""
            reply = reply or self.MessageID
            if mention:
                attr = f"&reply_to_message_id={reply}"
            uri = f"{self.baseURL}sendMessage?chat_id={self.ChatID}&text={text}{attr}"
            payload = {'type':'get' , 'data':uri}
            self.parent.connectCable('send', payload)

        def renderButtons(self, layout):
            pass

        def keyboard(
            self, text, buttons, resize = True, one_time = True
            ):
            pass

        def upload(self, file, caption = None):
            pass

        def sendPhoto(self, file, caption = None):
            pass

        def sendVideo(self, file, caption = None):
            pass

        def sendGIF(self, file, caption = None):
            pass

        def files(self):
            pass

        def getFileLink(self, fileID):
            pass

        def waitForResponse(self, method):
            pass
