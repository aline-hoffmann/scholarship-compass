import os
import requests
import json
import time

# Chave API
TMDB_API_KEY = "4e9572f883f351f99ca1729dfa04e22e"

# Principais definições 
GENRE_NAME = "Comédia"
GENRE_ID = 35
PAGES = 50
RECORDS_PER_FILE = 100

# Criando a pasta para armazenar os jsons
OUT_DIR = "raw_zone"
MOVIES_DIR = os.path.join(OUT_DIR, "movies")
os.makedirs(MOVIES_DIR, exist_ok=True)

# Função para buscar os filmes
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
            print(f"⚠️ Erro {response.status_code} ao buscar {content_type} página {page}")
            continue

        for item in response.json().get("results", []):
            if item["id"] not in seen:
                seen.add(item["id"])
                # removendo campos desnecessários
                item.pop("overview", None)
                item.pop("backdrop_path", None)
                item.pop("poster_path", None)
                items.append(item)
    return items

# Buscando orçamento e bilheteria dos filmes
def fetch_movie_details(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    params = {"api_key": TMDB_API_KEY, "language": "pt-BR"}
    try:
        r = requests.get(url, params=params, timeout=10)
        if r.status_code == 200:
            data = r.json()
            return {"budget": data.get("budget"), "revenue": data.get("revenue")}
    except Exception as e:
        print(f"Erro ao buscar detalhes do filme {movie_id}: {e}")
    return {"budget": None, "revenue": None}

# Função pra dividir os json com no máximo 100 registros
def save_json_chunks(data_list, target_dir, prefix):
    for i in range(0, len(data_list), RECORDS_PER_FILE):
        chunk = data_list[i:i+RECORDS_PER_FILE]
        file_name = os.path.join(target_dir, f"{prefix}_{i//RECORDS_PER_FILE + 1:03d}.json")
        with open(file_name, "w", encoding="utf-8") as f:
            json.dump(chunk, f, ensure_ascii=False, indent=2)
        print(f"💾 Arquivo salvo: {file_name} ({len(chunk)} registros)")


# Executando a coleta
print(f"\n Buscando FILMES de {GENRE_NAME}...")
movies = fetch_tmdb("movie", GENRE_ID)
for m in movies:
    m["genero"] = GENRE_NAME
    m["tipo"] = "Filme"
    detalhes = fetch_movie_details(m["id"])
    m.update(detalhes)
    time.sleep(0.2)

# Salvando os resultados
save_json_chunks(movies, MOVIES_DIR, "movies")

print(f"\n✅ Concluído!")
print(f"Filmes coletados: {len(movies)}")
print("Arquivos salvos em:")
print(f"  → {MOVIES_DIR}")