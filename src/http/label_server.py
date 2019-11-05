# -*- coding: utf-8 -*-

from flask import Flask
from flask import request
from flask import json
from gevent import monkey
from gevent.pywsgi import WSGIServer
import label_processor


monkey.patch_all()
app = Flask(__name__)


@app.route('/label/', methods={"GET", "POST"})
def label_web():

    post_data = request.get_data().decode("utf8")
    post_data_dict = json.loads(post_data)
    print("post data:" + str(post_data_dict))

    id_str  = post_data_dict["id"]
    title   = post_data_dict["title"]
    content = post_data_dict["content"]

    rsp_dict = label_processor.label_proc(id_str, title, content)
    print("rsp_dict:")
    print(rsp_dict)

    return json.dumps(rsp_dict, ensure_ascii=False), 200, [('Content-Type', 'application/json;charset=utf-8')]


#########################################################################
## main 主函数 ##

if __name__ == '__main__':
    app.debug = True

    httpServer = WSGIServer(("0.0.0.0", 5000), app)
    print("label server started")
    httpServer.serve_forever()

