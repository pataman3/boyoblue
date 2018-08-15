from . import movies, television, songs, albums, artists, books

def get(media_type, api_key):
  if media_type == 'movie':
    return movies.get(api_key)
  elif media_type == 'television':
    return television.get(api_key)
  elif media_type == 'song':
    return songs.get(api_key)
  elif media_type == 'album':
    return albums.get(api_key)
  elif media_type == 'artist':
    return artists.get(api_key)
  elif media_type == 'book':
    return books.get(api_key)
  else:
    return None

def search(media_type, query):
  if media_type == 'movies':
    return movies.search(query, limit=20)
  elif media_type == 'television':
    return television.search(query, limit=20)
  elif media_type == 'songs':
    return songs.search(query, limit=15)
  elif media_type == 'albums':
    return albums.search(query, limit=15)
  elif media_type == 'artists':
    return artists.search(query, limit=15)
  elif media_type == 'books':
    return books.search(query, limit=20)
  else:
    return None
