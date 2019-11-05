# coding:utf-8

import re
from utils import log_util

DOC_MAX_LENGTH = 200

# 处理一篇资讯新闻原文
def proc_news(news_content):

    sentence_list = re.split('，|。|<p>|</p>', news_content)

    rst_sentence_list = []

    proc_sentence = ""

    for i in range(len(sentence_list)):

        sentence = sentence_list[i]

        if 0 == len(sentence):
            continue

        if len(proc_sentence) < DOC_MAX_LENGTH and len(proc_sentence+sentence) >= DOC_MAX_LENGTH:
            # proc sentence
            rst_sentence_list.append(proc_sentence)

            proc_sentence = ""

        proc_sentence += sentence

    # 最后一部分获取
    rst_sentence_list.append(proc_sentence)

    return rst_sentence_list



# 处理所有资讯新闻原文
def proc_all_news(news_list):

    rst_news_list = []

    for i in range(len(news_list)):

        news_info = news_list[i]

        news_content = news_info["content"]

        sentence_list = proc_news(news_content)

        news_info["sentence_list"] = sentence_list

        rst_news_list.append(news_info)

        #rst_news_list.append(rst_sentence_list)
        #rst_news_list += rst_sentence_list

    return rst_news_list



if __name__ == '__main__':

    rst_news_list = proc_all_news()

    print(rst_news_list[0])

