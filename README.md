Dependency:

System Eviroment:

NVIDIA Discrete Graphics Card (Mine is RTX 3060 Laptop) with CUDA 11.8 and CUDNN 8.6

Windows 10 19045 x64

Anaconda Latest



Conda Enviroment:

Python 3.7

pytorch 1.13.0+cuda11.7

transformers

ctranslate2

flask

gevent




Prepare:

Method 1：

Download the test python file link: https://raw.githubusercontent.com/liuchuhan1/translateserver/main/test.py

In CMD,type follow command:

python test.py

Wait for a minute, the time will be long for download the model.

if show japanese result , it means the model is downloaded,then type follow command:

ct2-transformers-converter --model facebook/m2m100_418M --output_dir PATH_WHERE_YOU_WANT_TO_SAVE_THE_MODEL

Method 2：

Unzip the 7Z zipfile in folder model, the file in it is the already converted model file.

Method 3:

Download the already converted model from google driver : https://drive.google.com/file/d/1D7H4Qshc-uWcF_sLGQOy3pMaSNSemMhu/view?usp=sharing

Tips: Method 1 seems complex but can fit for other transformers model, you can change the model name in test.py and ct2server.py to the one which you want to use,
the model you can search in huggingface : https://www.huggingface.co/models
Otherwise, the Method 2 and 3 are simple but useful enough.




Download the server python file link: https://raw.githubusercontent.com/liuchuhan1/translateserver/main/ct2server.py

then you can type follow command to start the server:

python ct2server.py

Input the model path to the folder where your choose above.

Input your source language type and your target language type in short like follow

ru for Russian,zh for Chinese,ko for Korean,en for English,ja for japanese

more language should refer the ISO link: https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes

then the server will start.
