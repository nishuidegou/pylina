from tornado import websocket, web, ioloop
import json
import speech_recognition as sr


r = sr.Recognizer()

def bingSR():
    # obtain audio from the microphone
    # r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    # recognize speech using Microsoft Bing Voice Recognition
    BING_KEY = ""  # Microsoft Bing Voice Recognition API keys 32-character lowercase hexadecimal strings
    try:
        return r.recognize_bing(audio, key=BING_KEY,language="zh-CN")
        # print("Microsoft Bing Voice Recognition thinks you said " + r.recognize_bing(audio, key=BING_KEY,language="zh-CN"))
    except sr.UnknownValueError:
        print("Microsoft Bing Voice Recognition could not understand audio")
        return 'error'
    except sr.RequestError as e:
        print("Could not request results from Microsoft Bing Voice Recognition service; {0}".format(e))
        return 'error'

sr_string = []

cl = []

class IndexHandler(web.RequestHandler):
    def get(self):
        self.render("index.html")

class SocketHandler(websocket.WebSocketHandler):
    def check_origin(self, origin):
        return True

    def open(self):
        if self not in cl:
            cl.append(self)

    def on_close(self):
        if self in cl:
            cl.remove(self)

class ApiHandler(web.RequestHandler):

    @web.asynchronous
    def get(self, *args):
        self.finish()
        id = self.get_argument("id")
        value = self.get_argument("value")
        # s = bingSR()
        # sr_string.append(s)
        data = {"id": id, "value" : value}

        data = json.dumps(data)
        for c in cl:
            c.write_message(data)
            print("message wrote")

    @web.asynchronous
    def post(self):
        pass

app = web.Application([
    (r'/', IndexHandler),
    (r'/ws', SocketHandler),
    (r'/api', ApiHandler),
    (r'/(favicon.ico)', web.StaticFileHandler, {'path': '../'}),
    (r'/(rest_api_example.png)', web.StaticFileHandler, {'path': './'}),
])

if __name__ == '__main__':
    app.listen(8888)
    ioloop.IOLoop.instance().start()