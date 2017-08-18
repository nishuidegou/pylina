from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
import hashlib
from lxml import etree
from django.utils.encoding import smart_str
from django.views.decorators.csrf import csrf_exempt

import xml.etree.ElementTree as ET
import time
import reply as reply
import receive as receive


# Create your views here.


@csrf_exempt
def weixin(request):
    if request.method == "GET":
        signature = request.GET.get("signature", '')
        timestamp = request.GET.get("timestamp", '')
        nonce = request.GET.get("nonce", '')

        echostr = request.GET.get("echostr", '')
        token = 'your token'

        tmp_list = [token, timestamp, nonce]
        tmp_list.sort()
        tmp_str = ''.join([s for s in tmp_list])
        tmp_str = hashlib.sha1(tmp_str.encode('utf-8')).hexdigest()

        if tmp_str == signature:
            return HttpResponse(echostr)
        else:
            return HttpResponseBadRequest("Verify Failed")

    elif request.method == "POST":
        # xml_str = smart_str(request.body)
        # request_xml = etree.fromstring(xml_str)
        # response_xml = auto_reply_main(request_xml) #
        # return HttpResponse(request_xml, content_type="application/xml")
        # return HttpResponse(response_xml)

        rawStr = smart_str(request.body)
        recMsg = receive.parse_xml(rawStr)
        
        if isinstance(recMsg, receive.Msg) and recMsg.MsgType == 'text':
            toUser = recMsg.FromUserName
            fromUser = recMsg.ToUserName
            if recMsg.Content == b'blog':
                content = "Hello world!"
            else:
                # content = "Hi, %s" % recMsg.Content # use str()
                # content = "欢迎"
                content = str(recMsg.Content, "utf-8")

            replyMsg = reply.TextMsg(toUser, fromUser, content)
            
            return HttpResponse(replyMsg.send())
        else:
            return HttpResponse("success")

