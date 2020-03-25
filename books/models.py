from django.db import models

# Create your models here.
class Author(models.Model):
    author_name = models.CharField('Author', max_length=40, primary_key=True)

    def __str__(self):
        return self.author_name

class Publisher(models.Model):
    publisher_name = models.CharField('Publisher', max_length=40, primary_key=True)

    def __str__(self):
        return self.publisher_name

class Genre(models.Model):
    """Model representing a book genre."""
    name = models.CharField(max_length=200, help_text='Enter a book genre (e.g. Science Fiction)', primary_key=True)

    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Language(models.Model):
    """Model representing a Language (e.g. English, French, Japanese, etc.)"""
    name = models.CharField(max_length=200,
                            help_text="Enter the book's natural language (e.g. English, French, Japanese etc.)",
                            primary_key=True)

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.name

class Book(models.Model):
    title = models.CharField('Title', max_length=40)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    isbn = models.CharField('ISBN', max_length=13)
    actual_price = models.DecimalField(max_digits=3,decimal_places=2)
    selling_price = models.DecimalField(max_digits=3,decimal_places=2)
    language = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True)
    genre = models.ManyToManyField(Genre, help_text='Select a genre for this book')
    image = models.ImageField(upload_to='book_images')

    def __str__(self):
        """String for representing the Model object."""
        return self.title
