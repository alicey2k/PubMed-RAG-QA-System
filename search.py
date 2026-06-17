
import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup

def search_papers(query):

    # PubMed search API
    search_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"

    params = {
        "db":"pubmed",
        "term":query,
        "retmax":50,
        "retmode":"json"
    }

    response = requests.get(search_url,params=params)
    data = response.json()
    paper_ids = data["esearchresult"]["idlist"]

    rows = []

    # 一篇一篇抓詳細資料
    for pmid in paper_ids:

        fetch_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"

        fetch_params = {
            "db":"pubmed",
            "id":pmid,
            "retmode":"xml"
        }

        fetch_response = requests.get(
            fetch_url,
            params=fetch_params
        )

        soup = BeautifulSoup(
            fetch_response.text,
            "xml"
        )

        # title
        title_tag = soup.find("ArticleTitle")

        if title_tag:
            title = title_tag.text
        else:
            title = "N/A"

        # abstract
        abstract_tag = soup.find("AbstractText")

        if abstract_tag:
            abstract = abstract_tag.text
        else:
            abstract = "N/A"

        rows.append({
            "pmid":pmid,
            "title":title,
            "abstract":abstract
        })

    return pd.DataFrame(rows)
