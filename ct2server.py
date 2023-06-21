import os
os.environ["CT2_CUDA_ALLOCATOR"] = "cuda_malloc_async"
os.environ["CT2_CUDA_ALLOW_FP16"] = "1"

import ctranslate2
import transformers
import warnings
from flask import Flask, request, jsonify
from gevent import pywsgi
import torch
import re

warnings.filterwarnings('ignore')

if torch.cuda.device_count() > 0:
    print("GPU Acc Enable")
else:
    print("GPU Acc Disable")
modelpath = input("Model Path To The Folder : ")
source = input("Source Language Type : ")
dest = input("Target Language Type : ")

try:
    translator = ctranslate2.Translator(model_path=modelpath,
                                        device="cuda", compute_type="float16")
    tokenizer = transformers.AutoTokenizer.from_pretrained("facebook/m2m100_418M")


    def resultarray(sourcelang, destlang, text):
        tokenizer.src_lang = sourcelang
        source = tokenizer.convert_ids_to_tokens(tokenizer.encode(text))
        target_prefix = [tokenizer.lang_code_to_token[destlang]]
        results = translator.translate_batch([source], target_prefix=[target_prefix])
        target = results[0].hypotheses[0][1:]
        translateresult = tokenizer.decode(tokenizer.convert_tokens_to_ids(target))
        return translateresult


    app = Flask(__name__)


    @app.route('/translater', methods=['POST'])
    def translate():
        print(request.json)
        text1 = request.json['text']
        print("Original Text: \n" + text1)

        if (source == 'zh') | (source == "ja"):
            text1.replace("。", "\n")
        else:
            text1.replace(".", "\n")
        textarray = re.split('\n', text1)
        for strs in textarray:
            if strs
        print(textarray)
        result1 = []
        print("Translated Text: \n")
        for str1 in textarray:
            str2 = resultarray(source, dest, str1)
            print(str2)
            result1.append(str2)
        r = {'text': text1, 'from': source, 'to': dest, 'result': result1, "errorMessage": "", "errorCode": "0"}
        return jsonify(r)


    print('Translate Service Is Started，Use This API Address：http://127.0.0.1:16888/translater')
    server = pywsgi.WSGIServer(('0.0.0.0', 16888), app)
    server.serve_forever()
except:
    print('Translate Service Error ... ...')
