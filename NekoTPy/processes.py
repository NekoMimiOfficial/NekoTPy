import cables

def RequestHandler(requestQueue):
    while True:
        if len(requestQueue) > 0:
            currentRequest = requestQueue[0]
            requestQueue.pop(0)

            requestType = currentRequest['type']
            payload = currentRequest['contents']

            if requestType == "halt":
                break
            elif requestType == "get":
                cables.getUpdates(payload)
            elif requestType == "send":
                cables.sendPayload(payload)
            
            del(currentRequest)
            del(requestType)
            del(payload)
