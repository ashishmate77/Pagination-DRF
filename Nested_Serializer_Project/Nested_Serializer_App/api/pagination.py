
from rest_framework import pagination

class UserPagination(pagination.PageNumberPagination):
    page_size = 6

    # page_size_query_param = 'number'

    # max_page_size = 4

    # page_query_param = 'mypage'

    # last_page_strings = ("endpage",)


# class UserPagination(pagination.LimitOffsetPagination):
#     default_limit = 3
#
#     limit_query_param = "mylimit"   # "limit"
#
#     offset_query_param = "myoffset"  # "offset"
#
#     max_limit = 5


# class UserPagination(pagination.CursorPagination):
#     page_size = 3
#     ordering = '-author_name'



