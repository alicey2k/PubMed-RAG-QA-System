from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

#=================================
#function modularization（模組化）
#=================================
bio_model = SentenceTransformer("pritamdeka/S-PubMedBert-MS-MARCO")
def build_embeddings(df):
  documents=df['abstract'].fillna("").tolist()
  embeddings=bio_model.encode(documents,show_progress_bar=True)
  return embeddings

