"""
translate the html file
"""
import os
from bs4 import BeautifulSoup
import random
from hashlib import md5
import requests
import json

# baidu translate api
appid = ''
salt = ''
key = ''
url = 'http://api.fanyi.baidu.com/api/trans/vip/translate?'

def get_sign(str4trans):
    salt = random.randint(1000000000,9999999999)
    tempstr = appid + str4trans + str(salt) + key
    sign = md5(tempstr.encode(encoding='utf-8')).hexdigest()
    # print(sign)
    return sign, str(salt)


def baidu_translate(str, from_language, to_language):
    sign, salt = get_sign(str)
    temp_url = url + 'q=' + str + '&from=' + from_language + '&to=' + to_language + '&appid=' + appid + '&salt=' + salt + '&sign=' + sign
    ret = requests.get(temp_url)
    # print(temp_url)
    # print(ret.status_code)

    if ret.text.find('error') == -1:
        trans_res = json.loads(ret.text)
        # print(trans_res['trans_result'][0]['dst'])
        trans_output = trans_res['trans_result'][0]['dst']
        # print(json_text.keys())
        # print(trans_res)
        return trans_output

    return -1


def process_translate(file):

    fopen_old = open(file, 'r')
    fopen_new = open(os.path.join('./templates-translated/' + os.path.basename(file)), 'w+')

    html_text = fopen_old.read()
    fopen_old.close()
    #

    soup = BeautifulSoup(html_text, "html.parser")
    # print(soup.get_text())
    # print(soup.strong)
    # print(soup.a)
    # print(soup.h3)
    for item in soup.stripped_strings:
        if item.find('{%') == -1 and item.find('{{') == -1 and item.find('{#') == -1:
            item_translated = baidu_translate(item, 'ru', 'en')

            print(item, item_translated)

            if item_translated != -1:
                html_text = html_text.replace(item, item_translated)    #

    fopen_new.write(html_text)
    fopen_new.close()


def translate(path):

    if os.path.isdir(path):

        # create new folder
        translate_folder = ('%s-translated' % os.path.dirname(path))
        print(translate_folder)
        if not os.path.exists(translate_folder):
            # print('create translated file...')
            os.mkdir(translate_folder)

        # get the files of the path
        # print(os.listdir(path))
        for file in os.listdir(path):
            child = os.path.join('%s%s' % (path, file))
            if os.path.isdir(child):
                for subfile in os.listdir(child):
                    print(subfile)
                    f = os.path.join('%s/%s' % (child, subfile))
                    process_translate(f)
                    print("----------------------")
            # print(os.path.join('%s%s' % (path, file)))
            # print(file)
            else:
                process_translate(child)
                print("----------------------")

    elif os.path.isfile(path):

        # read in the file and parse
        process_translate(path)



if __name__ == "__main__":

    # get_sign('проекте')
    # baidu_translate('проекте', 'ru', 'en')

    path = os.path.join(os.curdir, 'templates/')
    print(path)

    translate(path)




