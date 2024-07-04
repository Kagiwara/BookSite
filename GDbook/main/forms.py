from .models import Book
from django.forms import ModelForm, TextInput, FileInput


class BookForm(ModelForm):

    class Meta:
        # Название модели на основе
        # которой создается форма
        model = Book
        # Включаем все поля с модели в форму
        fields = ['name_book', 'description_book', 'author_book', 'file', 'photo']

        widgets = {
            "name_book": TextInput(attrs={
                'class': 'create-form-input create-input-name',
                'type': "text",
                'name': "bookName",
                'value': "name book"
            }),
            "description_book": TextInput(attrs={
                'class': 'create-form-input create-input-description',
                'type': "text",
                'name': "bookDescription",
                'value': "description book"
            }), "author_book": TextInput(attrs={
                'class': 'create-form-input create-input-author',
                'type': "text",
                'name': "bookAuthor",
                'value': "author book"
            }), "file": FileInput(attrs={
                'class': 'form-control',
                'type': "file",
                'name': "file",
            }), "photo": FileInput(attrs={
                'class': 'form-control',
                'type': "file",
                'name': "photo"
            })

        }