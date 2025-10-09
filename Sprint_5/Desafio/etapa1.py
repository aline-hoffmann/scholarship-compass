import boto3

s3_client = boto3.client('s3')

bucket_name = 'desafio-final-aline'

file_movies = 'movies.csv'
file_series = 'series.csv'

s3_path_movies = 'Raw/Local/CSV/Movies/2025/10/09/movies.csv'
s3_path_series = 'Raw/Local/CSV/Series/2025/10/09/series.csv'

try:
    s3_client.upload_file(file_movies, bucket_name, s3_path_movies)
    print(f"✅ {file_movies} enviado para s3://{bucket_name}/{s3_path_movies}")

    s3_client.upload_file(file_series, bucket_name, s3_path_series)
    print(f"✅ {file_series} enviado para s3://{bucket_name}/{s3_path_series}")

except Exception as e:
    print("❌ Erro ao enviar arquivos:", e)