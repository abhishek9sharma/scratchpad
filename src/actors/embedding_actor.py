import ray
from sentence_transformers import SentenceTransformer

# #@ray.remote(num_cpus=2)
@ray.remote(num_gpus=0.2, num_cpus=1)
class EmbeddingActor:
    def __init__(self, model_path):
        self.transformer = SentenceTransformer(model_path)
        
    def get_embeddings(self, text_batch):
        #return len(text_batch)
        return self.transformer.encode(text_batch)

# @ray.remote(num_gpus=0.2, num_cpus=1)
# class Embed:
#     def __init__(self, model_path):
#         # Specify "cuda" to move the model to GPU.
#         self.transformer = SentenceTransformer(model_path, device="cuda")

#     def __call__(self, text_batch):
#         # We manually encode using sentence_transformer since LangChain
#         # HuggingfaceEmbeddings does not support specifying a batch size yet.
#         embeddings = self.transformer.encode(
#             text_batch,
#             batch_size=100,  # Large batch size to maximize GPU utilization.
#             device="cuda",
#         ).tolist()

#         return list(zip(text_batch, embeddings))