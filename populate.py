import os
import django


def populate():
    # genre_list = ['Fantasy', 'Adventure', 'Romance', 'Contemporary',
    # 'Mystery', 'Horror', 'Thriller', 'Paranormal', 'Historical', 'fiction', 'Science', 'Fiction', 'Memoir',
    # 'Cooking', 'Art', 'Self-help', 'Personal', 'Development', 'Motivational', 'Health', 'History',
    # 'Travel', 'Guide', 'How-to', 'Families', 'Relationships', 'Humor', 'Children']
    #
    # for genre in genre_list:
    #     add_genre(genre)

    # books = Book.objects.all()
    # for book in books:
    #     book.delete()

    # users = User.objects.all()
    # for user in users:
    #     user.delete()

    users = [
            {'mail':'rahulgeorge0009@gmail.com', 'first_name':'Rahul', 'last_name':'George'},
            {'mail':'rajnipriya1210@gmail.com', 'first_name':'RajniPriya', 'last_name':''},
            {'mail':'utpal38bpc@gmail.com', 'first_name':'Utpal', 'last_name':'Gaurav'},
            {'mail':'qureshiyusuff@gmail.com', 'first_name':'Yousuf', 'last_name':'Qureshi'},
            {'mail':'wahid786ali007@gmail.com', 'first_name':'Wahid', 'last_name':'Ali'},
          ]

    books = [
            {''}
            ]
    # for user in users:
    #     addUser(user)



def addUser(obj):
    u = User.objects.create_user(username=obj['mail'],
                                    password='Test1234',
                                    email=obj['mail'],
                                    first_name=obj['first_name'],
                                    last_name=obj['last_name'])

def add_genre(name):
  g = Genre.objects.get_or_create(name=name)


if __name__ == '__main__':
  print ('GOING...')
  os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'final_PickABook.settings')
  django.setup()
  from books.models import Genre
  from books.models import *
  from django.contrib.auth.models import User
  populate()
