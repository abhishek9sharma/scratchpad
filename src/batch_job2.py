# import ray
# import psutil
# from typing import Dict
import pandas as pd
# from sentence_transformers import SentenceTransformer

# @ray.remote
# class TextEmbedder:
#  def __init__(self, model_name):
#     self.model = SentenceTransformer(model_name)

#  def compute_embedding(self, row: pd.Series, column_name: str) -> Dict[str, float]:
#     text = row[column_name]
#     embedding = self.model.encode([text])[0]
#     return embedding

# # Assume df is your dataframe and "text_column" is the column you want to compute the embedding of
df = pd.DataFrame({
 "text_column": ["Hello", "World", "Ray", "Actor"]
})

column_name = "text_column"

# # Create a pool of actors
# num_cpus = 2
# actors = [TextEmbedder.remote("/scratchpad/data/models/all-mpnet-base-v2/") for _ in range(num_cpus)]
# actor_pool = ray.util.ActorPool(actors)

# # Use the actor pool throughout your program
# result_embeddings = []
# for _, row in df.iterrows():
#  embeddings = actor_pool.map(lambda a, v: a.compute_embedding.remote(v, column_name), [row])
#  for embedding in embeddings:
#    result_embeddings.append(ray.get(embedding))

# print(result_embeddings)


import ray
from ray.util.actor_pool import ActorPool
import pandas as pd

df = pd.DataFrame({
 "text_column": ["Hello", "World", "Ray", "Actor"]
})

column_name = "text_column"


@ray.remote
class Actor:
    def compute_len(self, v):
      return len(v)

a1, a2 = Actor.remote(), Actor.remote()
pool = ActorPool([a1, a2])
final_result = []
for _, row in df.iterrows():
   row_result = pool.map(lambda a, v: a.compute_len.remote(v),[row["text_column"]])
   final_result.append(list(row_result)[0])

print(final_result)
