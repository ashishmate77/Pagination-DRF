
from Nested_Serializer_App.models import Author,Book
from Nested_Serializer_App.api.serializers import AuthorSerializer,BookSerializer
from rest_framework import generics
from Nested_Serializer_App.api.pagination import UserPagination

class AuthorListView(generics.ListCreateAPIView):
    queryset = Author.objects.all()

    serializer_class = AuthorSerializer

    pagination_class = UserPagination





class AuthorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer