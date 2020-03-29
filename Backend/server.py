import torch

import transformers
from transformers import (WEIGHTS_NAME,BertConfig, BertForMaskedLM, BertTokenizer)

from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from flask_cors import CORS, cross_origin

import json
import pandas as pd
import numpy as np
import nmslib

from utils import *

# Create Flask app
app = Flask(__name__)
cors = CORS(app)

## Getting files from google drive:
functions = ["", "./data/functions.json"]
docstrings = ["", "./data/docstrings.csv"]
lineage = ["", "./data/lineage.csv"]
docstrings_vecs = ["", "./data/docstrings_avg_vec.npy"]
model_path = ["", "./model"]

download_file_from_google_drive(functions[0], functions[1])
download_file_from_google_drive(docstrings[0], docstrings[1])
download_file_from_google_drive(lineage[0], lineage[1])
download_file_from_google_drive(docstrings_vecs[0], docstrings_vecs[1])
download_file_from_google_drive(model_path[0], model_path[1])


## Import the data & model:
with open(functions[1]) as json_file:
    df_function = json.load(json_file)

df_docstring = pd.read_csv(docstrings[1],sep='\t', names=["docstring"])[:20000]
df_lineage = pd.read_csv(lineage[1],sep='\t', names=["Repo"])[:20000]


docstrings_avg_vec = np.load(docstrings_vecs[1],allow_pickle=True)

config = BertConfig.from_json_file(model_path[1]+'/config.json')
config.output_hidden_states = True


tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

model = BertForMaskedLM.from_pretrained("bert-base-uncased",config=config)
model.load_state_dict(torch.load(model_path[1]+"/pytorch_model.bin"))
model.eval()


# Initialize a new index, using a HNSW index on Cosine Similarity
index = nmslib.init(method='hnsw', space='cosinesimil')
index.addDataPointBatch(docstrings_avg_vec)
index.createIndex({'post': 2}, print_progress=True)


# Routes:
@app.route('/functions', methods=['POST'])
def post():
    posted_data = request.get_json()
    user_input = posted_data['input']

    input_ids = torch.tensor(tokenizer.encode(user_input, add_special_tokens=True)).unsqueeze(0)

    outputs = model(input_ids, masked_lm_labels=input_ids)

    embeddings = outputs[2][-1].detach().numpy()[0]

    size = embeddings.shape[0]
    sum_array = [sum(x) for x in zip(*embeddings)]
    avg_array = [sum_array[i]/size for i in range(len(sum_array))]

    ids, distances = index.knnQuery(avg_array, k=10)

    functions = []
    sources = []
    for elem in ids:
        functions.append(df_function[elem])
        sources.append(df_lineage[elem])

    response = jsonify({
        "Functions" : json.dumps(functions),
        "Sources" : json.dumps(sources)
    })

    return response


@app.route('/')
def hello_world():
    return 'Hello, From DiscoverCode engine!'

if __name__ == '__main__':
    app.run()