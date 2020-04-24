from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination,
    )


# number of posts per page
class PostLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 10


class PostPageNumberPagination(PageNumberPagination):
    page_size = 20
    