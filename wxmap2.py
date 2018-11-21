#-*-coding:utf-8-*-
import itchat,json
from itchat.content import *
@itchat.msg_register(itchat.content.TEXT,TEXT,isGroupChat=True)
def text_reply(msg):
    print(msg)
    with open("test.json", 'r',encoding="utf-8") as f:
        myjson = json.load(f)
    if "branch" in msg["Text"]:
        name_emb = list(json.loads(msg["Text"]))#把字符串转为字典,再转为列表
        with open("test.json", "w",encoding="utf-8") as fc:
            myjson += name_emb
            json.dump(myjson, fc, ensure_ascii=False,indent=4)
            fc.close()
        return "[+1]Success"

    elif "ls" in msg["Text"]:
       return str(myjson)
    elif 'rm' in msg["Text"]:
        re = msg["Text"].find('m')
        with open("test.json", "w",encoding="utf-8") as fc:
            myjson.pop(msg["Text"][re + 1:len(msg["Text"])])
            json.dump(myjson, fc, ensure_ascii=False,indent=4)
            fc.close()
        return "[-1]Delete"

    f.close()
itchat.auto_login(hotReload=True)
itchat.run()