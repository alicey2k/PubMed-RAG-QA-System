# PubMed-RAG QA System

A Retrieval-Augmented Generation (RAG) system for biomedical literature question answering using PubMed, S-PubMedBERT, FAISS, and FLAN-T5.

## Overview

This project retrieves biomedical papers from PubMed, converts abstracts into embeddings using S-PubMedBERT, performs semantic search with FAISS, and generates answers using FLAN-T5.

## Features

- Retrieve biomedical literature from PubMed
- Generate embeddings with S-PubMedBERT
- Semantic search using FAISS
- Retrieval-Augmented Generation (RAG)
- Question answering with FLAN-T5

## Project Structure

```text
.
├── search.py
├── embedding.py
├── rag.py
├── main.py
├── requirements.txt
└── README.md
```

## Workflow

```text
User Question
      │
      ▼
search_papers()
      │
      ▼
DataFrame
      │
      ▼
build_embeddings()
      │
      ▼
Embeddings
      │
      ▼
build_faiss_index()
      │
      ▼
FAISS Index
      │
      ▼
search_index()
      │
      ▼
Context
      │
      ▼
FLAN-T5
      │
      ▼
Answer
```

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
python main.py
```

## Technologies

- Python
- PubMed API
- Pandas
- NumPy
- BeautifulSoup
- Sentence Transformers
- S-PubMedBERT
- FAISS
- FLAN-T5
