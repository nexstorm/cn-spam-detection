import ijson
import re

file = open("./text.txt","a+",encoding='utf-8')
with open("./result.json", "r",encoding='utf-8') as f:
    for rec in ijson.items(f, "messages.item"):
        if rec['type'] == "message":
            text = rec['text']
            if type(text) == str:
                id_ = rec['id']
                print(id_)
                text = text.replace('\n','').replace('/','')
                text = re.sub('[^\u4e00-\u9fa5]+', '',text)
            elif type(text) == list:
                if type(text[0]) == str:
                    id_ = rec['id']
                    print(id_)
                    text = text[0].replace('\n','').replace('/','')
                    text = re.sub('[^\u4e00-\u9fa5]+', '',text)
                else:
                    text = ""
            else:
                    text = ""
            if text != "":
                file.write("n   "+text+"\n")