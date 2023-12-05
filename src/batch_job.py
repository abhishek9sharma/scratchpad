import pandas as pd
import ray
from actors.embedding_actor import EmbeddingActor
from ray.util.actor_pool import ActorPool

df = pd.read_csv(
    "/scratchpad/data/dummy_data.csv", nrows=100
)  # Replace with your DataFrame
print(df)

num_actors = 2
embedding_actors = [EmbeddingActor.remote("/scratchpad/data/models/all-mpnet-base-v2") for _ in range(num_actors)]
# #actors = [EmbeddingActor.remote() for _ in range(num_actors)]
embedding_actor_pool = ActorPool(embedding_actors)


embeddings = []


# act = embedding_actors[0]
# print(ray.get(act.get_embeddings.remote(["Delhi is the capital of India"])))

for _, row in df.iterrows():
    row_result = embedding_actor_pool.map(lambda act, v: ray.get(act.get_embeddings.remote(v)), [row["text"]])
    embeddings.append(list(row_result)[0])
         

print(len(embeddings))
#print(embeddings[0])
#print(ray.get(embeddings[0]))


# while 1:
#     time.sleep(100)
#     print("looping")


# # actor = EmbeddingActor.remote("all-MiniLM-L6-v2")
# # embeddings = ray.get(actor.get_embeddings.remote(["Hello, world!", "Ray is great!"]))
# # print(embeddings)


# # # actor = EmbeddingActor.remote("all-MiniLM-L6-v2") # Replace with your model name
# # # embeddings = []
# # # for batch in dataset.iter_batches(batch_format="pandas"):
# # #    batch_embeddings = ray.get(actor.get_embeddings.remote(batch['text'])) # Replace 'text' with your text column name
# # #    embeddings.append(batch_embeddings)
