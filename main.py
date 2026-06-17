from rag import rag_search
query = "What are the current treatments for diabetic nephropathy?"
search_query = "diabetic nephropathy treatment"
context = rag_search( "diabetic nephropathy treatment")
print(context[:500])

prompt = f"""
Based on the following papers, answer the question.

Do NOT copy the paper abstracts.

Summarize the main treatments mentioned.

Papers:
{context}

Answer:
"""
