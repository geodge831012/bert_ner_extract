# bert_ner_extract
利用bert对资讯新闻重的人名和机构名等做抽取

利用参考此项目，https://github.com/macanv/BERT-BiLSTM-CRF-NER

放在目录BERT-BiLSTM-CRF-NER/中


目录data_ner/中是训练及测试的样本


目录src/是自己开发的代码，其中src/ner_extract.py是基于BERT-BiLSTM-CRF-NER/terminal_predict.py做的定制化修改，是自己程序的入口


部分理解：
1.训练的命令如下

python3.6 /usr/local/bin/bert-base-ner-train \
    -data_dir /home/mqq/geodge/github/ChineseNER/data_ner \
    -output_dir /home/mqq/geodge/github/bert_ner/output \
    -init_checkpoint /home/mqq/geodge/BERT/model/chinese_L-12_H-768_A-12/bert_model.ckpt \
    -bert_config_file /home/mqq/geodge/BERT/model/chinese_L-12_H-768_A-12/bert_config.json \
    -vocab_file /home/mqq/geodge/BERT/model/chinese_L-12_H-768_A-12/vocab.txt


2.通过服务的方式启动ner服务

python3.6 /usr/local/bin/bert-base-serving-start \
    -bert_model_dir /home/mqq/geodge/BERT/model/chinese_L-12_H-768_A-12/ \
    -model_dir /home/mqq/geodge/github/bert_ner/output \
    -model_pb_dir /home/mqq/geodge/github/bert_ner/predict_optimizer \
    -num_worker 2 \
    -mode NER

其中-model_dir对应的就是1中的-output_dir

-model_pb_dir表示缓存的模型二进制文件，可以直接加载使用，以提高速度，此命令可以将-model_dir对应的模型加载到-model_pb_dir的位置，如果-model_pb_dir已经存在，则直接读取，如果没有，则在当前目录下的predict_optimizer目录中默认生成，对应的代码逻辑在BERT-BiLSTM-CRF-NER/bert_base/server/graph.py的函数optimize_ner_model中(if args.model_pb_dir is None:)

调用的客户端代码，可以将长语句切分为多段传入，其中每段不超过128

rst = bc.encode([list(str1), list(str2)], is_tokenized=True)


3.以下命令也可以启动，和2中一样，但有打印信息

需要修改run.py的main中的函数

python3.6 run.py \
    -bert_model_dir /home/mqq/geodge/BERT/model/chinese_L-12_H-768_A-12/ \
    -model_dir /home/mqq/geodge/github/bert_ner/output \
    -model_pb_dir /home/mqq/geodge/github/bert_ner/predict_optimizer2 \
    -num_worker 2 \
    -mode NER


4.使用terminal_predict.py也可以处理资讯

python3.6 terminal_predict.py

效果比run.py要好，句子长度不超过200

