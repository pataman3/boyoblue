import os
from googleapiclient.discovery import build

api_key = os.environ['GOOGLE_BOOKS_API_KEY']

service = build('books', 'v1', developerKey=api_key, cache_discovery=False)

class Book:
  def __init__(self, title, api_id, author, cover_art):
    self.title = title
    self.api_id = api_id
    self.author = author
    self.cover_art = cover_art


# converts the result of an API call to a Movie object
def parse_api_call(result):
  book = result['volumeInfo']
  cover_art = book['imageLinks']['thumbnail'] if 'imageLinks' in book else ''
  author = book['authors'][0] if 'authors' in book else 'Unknown Author'
  return Book(
    title=book['title'],
    api_id=result['id'],
    author=author,
    cover_art=cover_art
  )


def search(query, limit, page):
  request = service.volumes().list(source='public', q=query, maxResults=limit, startIndex=(page - 1) * limit)
  response = request.execute()
  books = []
  for result in response['items']:
    books.append(parse_api_call(result))
  return books


def get(api_key):
  request = service.volumes().get(source='public', volumeId=api_key)
  response = request.execute()
  return parse_api_call(response)
