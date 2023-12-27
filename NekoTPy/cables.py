import requests

def getUpdates(PAYLOAD):
    request = requests.get(
        PAYLOAD
    )
    return request

def sendPayload(PAYLOAD):
    type = PAYLOAD['type']
    request = False
    if type == 'get':
        request = requests.get(
            PAYLOAD['uri']
        )
    elif type == 'post':
        headers = PAYLOAD['headers']
        data = PAYLOAD['data']
        uri = PAYLOAD['uri']
        request = requests.post(
            uri, data=data, headers=headers
        )
        del(headers)
        del(data)
        del(uri)
    if request:
        return request
    return
