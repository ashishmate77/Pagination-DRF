
from rest_framework import serializers
from Nested_Serializer_App.models import Author,Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"

class AuthorSerializer(serializers.ModelSerializer):
    # books_by_author = BookSerializer(many=True,read_only=True)
    class Meta:
        model = Author
        fields = "__all__"







