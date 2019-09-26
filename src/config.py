# -*- coding: utf-8 -*-

import pymysql

# 模型的路径
MODEL_DIR = '/home/mqq/geodge/github/bert_ner/output'

# google提供的BERT的预训练文件的路径
BERT_DIR = '/home/mqq/geodge/BERT/model/chinese_L-12_H-768_A-12'

#解析一篇文章的最大长度
DOC_MAX_LENGTH = 200

# 资讯新闻库
def get_connection_news():

    conn = pymysql.connect(
        host    = '',
        port    = 3306,
        user    = '',
        passwd  = '',
        db      = '',
        charset = 'utf8',
    )

    return conn
