# coding:utf-8

import config
import re
from utils import log_util

# 获取资讯新闻原文
def get_news():

    log_util.roll_log.info('Begin get_news()')

    # 获取配置信息的mysql库
    conn = config.get_connection_news()
    cur = conn.cursor()

    # 获得表中有多少条数据
    sql = "select content from news_page limit 100"

    log_util.roll_log.info("sql:" + sql)

    count = cur.execute(sql)

    log_util.roll_log.info('get news, count=%d' % count)

    # 股票名称集合 用于返回
    news_list = []

    # 获取股票名称
    row_info = cur.fetchall()
    for row in row_info:
        news_list.append(str(row[0]))

    cur.close()
    conn.close()

    return news_list


# 处理一篇资讯新闻原文
def proc_news(news_content):

    sentence_list = re.split('，|。|<p>|</p>', news_content)

    rst_sentence_list = []

    proc_sentence = ""

    for i in range(len(sentence_list)):

        sentence = sentence_list[i]

        if 0 == len(sentence):
            continue

        if len(proc_sentence) < 200 and len(proc_sentence+sentence) >= 200:
            # proc sentence
            rst_sentence_list.append(proc_sentence)

            proc_sentence = ""

        proc_sentence += sentence

    return rst_sentence_list



# 处理所有资讯新闻原文
def proc_all_news(news_list):

    rst_news_list = []

    for i in range(len(news_list)):

        news_content = news_list[i]

        rst_sentence_list = proc_news(news_content)

        #rst_news_list.append(rst_sentence_list)
        rst_news_list += rst_sentence_list

    return rst_news_list



if __name__ == '__main__':

    rst_news_list = proc_all_news(get_news())

    print(rst_news_list[0])

