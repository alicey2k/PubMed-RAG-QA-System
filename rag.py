
#=================================
#build_faiss_index🔥
#=================================
from search import search_papers
from embedding import build_embeddings, bio_model
import numpy as np
from sentence_transformers import SentenceTransformer
import faiss
from transformers import AutoTokenizer
from transformers import AutoModelForSeq2SeqLM
tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-base")
model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-base")

def build_faiss_index(embeddings):
  dimension=embeddings.shape[1]
  index = faiss.IndexFlatL2(dimension)
  index.add(np.array(embeddings).astype("float32"))
  return index

#=================================
#semantic search function🔥
#=================================
import pandas as pd
def search_index(query,model,index,df,top_k):
  top_abstracts = []
  query_embeddings=model.encode([query]).astype("float32")
  distance,indices=index.search(query_embeddings,top_k)
  for rank,idx in enumerate(indices[0]):
    #print("排名:", rank+1)
    #print("distance:",distance[0][rank])
    #print(df.iloc[idx]["title"])
    top_abstracts.append(df.iloc[idx]["abstract"][:300])
    #print("PMID:",df.iloc[idx]["pmid"])
    #print("-"*50)
  return top_abstracts

def rag_search(query,top_k=3):
  df=search_papers(query)
  doc_embeddings=build_embeddings(df)
  index=build_faiss_index(doc_embeddings)
  top_abstracts=search_index(
      query=query,
      model=bio_model,
      index=index,
      df=df,
      top_k=top_k
  )
  context = "\n\n".join(top_abstracts)
  return context
