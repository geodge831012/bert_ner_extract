# -*- coding: utf-8 -*-

import json
import urllib.parse
import urllib.request
import news_provider
import ner_extract


def ner_proc(id_str, title, content):

    news_list = []
    news_info = {}
    news_info["id"]         = id_str
    news_info["content"]    = content
    news_list.append(news_info)

    proc_news_list = news_provider.proc_all_news(news_list)

    rst_news_list = ner_extract.predict_online(proc_news_list)

    if(len(rst_news_list) > 0):
        return rst_news_list[0]
    else:
        return {}

def att_proc(id_str, title, content):

    return {}

    #headers = {'Content-Type': 'application/json'}
    #url = "http://localhost:8001/query"
    #req = urllib.request.Request(url, headers=headers, data=json.dumps(
    #    {'news_list': [{'content': content, 'news_id': id_str, 'title': title}]}).encode('utf-8'))
    #response = urllib.request.urlopen(req, timeout=5)
    #json_str = response.read()

    #att_list = eval(json_str.decode('utf-8'))

    #if(len(att_list) > 0):
    #    return att_list[0]
    #else:
    #    return {}


def label_proc(id_str, title, content):
    ner_dict = ner_proc(id_str, title, content)

    person_list = ner_dict["person"]
    new_person_list = []
    for i in range(len(person_list)):
        person = person_list[i]
        if(len(person) > 1):
            new_person_list.append(person)
    ner_dict["person"] = new_person_list

    att_dict = att_proc(id_str, title, content)

    merge_dict = ner_dict
    if "attitude" in att_dict:
        merge_dict["attitude"] = att_dict["attitude"]
    if "related_stocks" in att_dict:
        merge_dict["related_stocks"] = att_dict["related_stocks"]
    if "related_plates" in att_dict:
        merge_dict["related_plates"] = att_dict["related_plates"]
    if "related_districts" in att_dict:
        merge_dict["related_districts"] = att_dict["related_districts"]
    if "sensitive_words" in att_dict:
        merge_dict["sensitive_words"] = att_dict["sensitive_words"]

    if "sentence_list" in merge_dict:
        del merge_dict["sentence_list"]
    if "content" in merge_dict:
        del merge_dict["content"]

    return merge_dict

#########################################################################
## main 主函数 ##

if __name__ == '__main__':
    pass

