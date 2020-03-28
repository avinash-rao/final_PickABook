import os
import django
def populate():
    genre_list = ['Fantasy', 'Adventure', 'Romance', 'Contemporary',
    'Mystery', 'Horror', 'Thriller', 'Paranormal', 'Historical', 'fiction', 'Science', 'Fiction', 'Memoir',
    'Cooking', 'Art', 'Self-help', 'Personal', 'Development', 'Motivational', 'Health', 'History',
    'Travel', 'Guide', 'How-to', 'Families', 'Relationships', 'Humor', 'Children']

    for genre in genre_list:
        add_genre(genre)

def add_genre(name):
  g = Genre.objects.get_or_create(name=name)


if __name__ == '__main__':
  print ('GOING...')
  os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'final_PickABook.settings')
  django.setup()
  from books.models import Genre
  populate()
