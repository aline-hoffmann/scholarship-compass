import os
import json
import time
import boto3
import requests
from datetime import datetime

TMDB_API_KEY = os.getenv("TMDB_API_KEY")
BUCKET_NAME = os.getenv("BUCKET_NAME")

GENRE_NAME = "Comédia"
GENRE_ID = 35
PAGES = 50
RECORDS_PER_FILE = 100

s3 = boto3.client("s3")

def fetch_tmdb(content_type, genre_id):
    items = []
    seen = set()
    url = f"https://api.themoviedb.org/3/discover/{content_type}"

    for page in range(1, PAGES + 1):
        params = {
            "api_key": TMDB_API_KEY,
            "with_genres": genre_id,
            "language": "pt-BR",
            "sort_by": "popularity.desc",
            "page": page
        }
        response = requests.get(url, params=params, timeout=10)
        if response.status_code != 200:
            print(f"Erro {response.status_code} página {page}")
            continue

        for item in response.json().get("results", []):
            if item["id"] not in seen:
                seen.add(item["id"])
                item.pop("overview", None)
                item.pop("poster_path", None)
                item.pop("backdrop_path", None)
                items.append(item)
    return items

def save_to_s3(data_list, prefix):
    now = datetime.utcnow()
    for i in range(0, len(data_list), RECORDS_PER_FILE):
        chunk = data_list[i:i + RECORDS_PER_FILE]
        file_number = i // RECORDS_PER_FILE + 1
        path = (
            f"Raw/TMDB/JSON/{now.year}/{now.month:02d}/{now.day:02d}/"
            f"{prefix}_{file_number}.json"
        )
        s3.put_object(
            Bucket=BUCKET_NAME,
            Key=path,
            Body=json.dumps(chunk, ensure_ascii=False, indent=2),
            ContentType="application/json"
        )
        print(f"Arquivo salvo em: s3://{BUCKET_NAME}/{path}")
    print(f"Total de {len(data_list)} registros enviados em múltiplos arquivos.")

def lambda_handler(event, context):
    print(f"Coletando filmes de {GENRE_NAME}")
    movies = fetch_tmdb("movie", GENRE_ID)
    for m in movies:
        m["genero"] = GENRE_NAME
        m["tipo"] = "Filme"
        time.sleep(0.2)
    save_to_s3(movies, "filmes_comedia")
    return {"status": "ok", "filmes": len(movies)}