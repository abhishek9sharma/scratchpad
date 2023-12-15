import ray
from typing import Dict
import numpy as np
import ray

from sentence_transformers import SentenceTransformer

# #@ray.remote(num_cpus=2)
@ray.remote(num_gpus=0.3, num_cpus=2)
class EmbeddingActor:
    def __init__(self, model_path):
        self.transformer = SentenceTransformer(model_path)
        
    def get_embeddings(self, text_batch):
        #return len(text_batch)
        res =  self.transformer.encode(text_batch)
        res2 = [len(x) for x in text_batch]
        return res.tolist()
        #return res2


num_actors = 2
actor_pool = ray.util.ActorPool([EmbeddingActor.remote(model_path="/scratchpad/data/models/all-mpnet-base-v2/") for _ in range(num_actors)])

def process_batch(batch):
    print("CALL NAME")
    print(batch["text"], type(batch["text"]))
    print("CALL NAME END")
    x = actor_pool.map(lambda a, v:a.get_embeddings.remote(v), batch["text"])
    #res = list(x)
    #print("CALL x")
    batch["res"] =  list(x)
    return batch
    #return {"res":res}


ds = (
    ray.data.from_items([
        {"text": "My name is Donald Duck", },
        {"text": "I live in America", },
        {"text": "China is in Asia", },
         {"text": "France is in Europed"},
    ]).map_batches(process_batch, batch_size=2)
)
ds.show()



