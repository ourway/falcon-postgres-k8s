"""
general utilities
"""
import os
import secrets


def get_database_url() -> str:
    user = os.getenv("POSTGRES_USER", "postgres")
    password = os.getenv("POSTGRES_PASSWORD")
    server = os.getenv("POSTGRES_SERVER")
    port = os.getenv("POSTGRES_PORT")
    db = os.getenv("POSTGRES_DB")
    return f"postgresql://{user}:{password}@{server}:{port}/{db}"


def save_random_image() -> None:
    os.system(f"curl -L https://picsum.photos/200 --output /data/{secrets.token_urlsafe()}.jpg")
