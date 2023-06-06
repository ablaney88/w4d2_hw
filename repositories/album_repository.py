import pdb
from db.run_sql import run_sql

from models.album import Album

def select_all():
    albums = []

    sql = "SELECT * FROM albums"
    results = run_sql

    for row in results:
        album = Album(row["album_name"],
                        row["id"])
        albums.append(album)

    return albums

def select(id):
    album = None
    sql = "SELECT * FROM albums WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:

        album = album(
            result["album_name"],
            result["id"]
        )

    return album

def save(album):
    sql = "INSERT INTO albums (album_name) VALUES (%s) RETURNING *"
    values = [album.album_name]

    result = run_sql(sql, values)
    id = result[0]["id"]
    album.id = id
    return album

def delete_all():
    sql = "DELETE FROM albums"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM albums WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(album):
    sql = "UPDATE albums SET (album_name) = (%s) WHERE id = %s"
    values = [album.album_name, album.id]
    run_sql(sql, values)
        
def tasks_for_user(artist):
    albums = []

    sql = 'SELECT * FROM albums WHERE user_id = %s'
    values = [artist.id]
    results = run_sql(sql, values)

    for row in results:
        album = Album(row["album_name"],
                    artist,
                    row["id"]
                    )
        albums.append(album)
    return albums