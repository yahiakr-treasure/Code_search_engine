import torch

import transformers
from transformers import (WEIGHTS_NAME,BertConfig, BertForMaskedLM, BertTokenizer)

import json
import pandas as pd
import numpy as np
import nmslib

## Getting files from google drive:

with open('/content/data/test_original_function.json') as json_file:
    function_data = json.load(json_file)

df_docstring = pd.read_csv("./data/test.docstring",sep='\t', names=["docstring"])[:20000]
df_lineage = pd.read_csv("./data/test.lineage",sep='\t', names=["Repo"])[:20000]


docstrings_avg_vec = np.load('/content/drive/My Drive/Colab Notebooks/Code_search_engine/docstrings_avg_vecs.npy',allow_pickle=True)


model_path = "./output/pytorch_model.bin"

config = BertConfig.from_json_file('./output/config.json')
config.output_hidden_states = True


tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

model = BertForMaskedLM.from_pretrained("bert-base-uncased",config=config)
model.load_state_dict(torch.load(model_path))
model.eval()


import numpy

# create a random matrix to index
data = docstrings_avg_vec

# initialize a new index, using a HNSW index on Cosine Similarity
index = nmslib.init(method='hnsw', space='cosinesimil')
index.addDataPointBatch(data)
index.createIndex({'post': 2}, print_progress=True)