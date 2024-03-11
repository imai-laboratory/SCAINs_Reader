import os
import datetime
import time
import csv
import tiktoken
import logging
import extractor

from importlib.machinery import OPTIMIZED_BYTECODE_SUFFIXES
from natsort import natsorted
from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

logging.basicConfig(format = '%(asctime)s - %(levelname)s - %(name)s -   %(message)s',
                    datefmt = '%m/%d/%Y %H:%M:%S',
                    level = logging.INFO)
logger = logging.getLogger(__name__)

class Params:
    GPT_MODEL_COMPLETION = "gpt-3.5-turbo"
    #GPT_MODEL_COMPLETION = "text-davinci-003"
    GPT_MODEL_EMBEDDING = "text-embedding-ada-002"
    DIALOGUE_PATH = "./dat/"
    DIALOGUE_FILENAME = "PP"
    FILENAME = "PP1.txt"
    FILEPATH = DIALOGUE_PATH + FILENAME
    SPEAKERS = ["A: ", "B: "]
    DIALOGUE_START = 0
    DIALOGUE_END = 1
    MAX_TOKENS = 200
    TEMPERATURE = 0
    STOP_WORDS = "\n"
    USE_DUMMY = 0
    RESULTS_PATH = "./results/"

dialogue = []
filename = ""
flag = 1

@app.route("/")
def index():
    global dialogue, filename, flag
    if flag:
        filename = Params().FILENAME  # 初回のリクエスト時にファイル名をセッションに保存
        dialogue = read_file(filename)
        flag = 0
    return render_template("index.html", filename=filename, dialogue=dialogue)

@app.route("/select-txt", methods=['POST'])
def select_text():
    global dialogue, filename
    if request.method == 'POST':
        selected_filename = request.form['filename']
        if selected_filename != "unselected":
            dialogue = read_file(selected_filename)  # ファイルの内容を読み取る
            filename = selected_filename
#         return render_template("index.html", filename=filename, dialogue=dialogue)
        return redirect(url_for('index'))
    else:
        return "Method not allowed"

def read_file(filename):
    with open(Params().DIALOGUE_PATH + filename) as f:
        lines = [s.rstrip() for s in f.readlines()]
    dialogue = []
    for line in lines:
        parts = line.strip().split(':', 1)
        if len(parts) == 2:
            speaker = parts[0].strip() + ":"
            statement = parts[1].strip()
            dialogue.append({"speaker": speaker, "statement": statement})
    return dialogue

if __name__ == '__main__':
    app.run(debug=True)
#     start = time.time()
    params = Params()

    # Encoder
    encoding = tiktoken.encoding_for_model(params.GPT_MODEL_COMPLETION)

    #html表示
    app.run(debug=True)

#     # Get list of dialogues
#     file_list = natsorted(os.listdir(params.DIALOGUE_PATH))
#     # file_list = os.listdir(params.DIALOGUE_PATH)
#     # logger.debug(file_list)
#     file_list = [f for f in file_list if f.startswith(params.DIALOGUE_FILENAME)]
#     # logger.debug(file_list)
#     file_list = file_list[params.DIALOGUE_START:params.DIALOGUE_END]
#     logger.debug(file_list)
#
#     # Loop
#     n_tokens = []
#     results = []
#     for filename in file_list:
#         logger.info("------ dialogue: {}".format(filename))
#         with open(params.DIALOGUE_PATH + filename) as f:
#             dialogue = [s.rstrip() for s in f.readlines()]
#
#         ex = extractor.SCAINExtractor(params, encoding, dialogue, filename)
#         #ex = extractor.ImportantExtractor(params, encoding, dialogue, filename)
#         # n_token = ex.extract()
#         n_token = ex.distance_extract()
#         logger.info("------ number of tokens: {}".format(n_token))
#         n_tokens.append(n_token)
#         results.extend(ex.results)
#
#         # Wait to avoid overloading
#         time.sleep(3)
#
#         # Save results for each dialogue
#         dt_now = datetime.datetime.now()
#         results_filename = params.RESULTS_PATH + dt_now.strftime("%Y%m%d_%H%M%S") + ".csv"
#         with open(results_filename, "w") as f:
#             writer = csv.writer(f)
#             writer.writerows(ex.results)
#
#         logger.info("------ number of total tokens: {}".format(sum(n_tokens)))
#     end = time.time()
#     time_diff = end - start  # 処理完了後の時刻から処理開始前の時刻を減算する
#     print(time_diff)
