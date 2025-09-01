
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from .models import Post
from .serializers import PostSerializer


from rest_framework.pagination import CursorPagination

class PostCursorPagination(CursorPagination):
	page_size = 10
	page_size_query_param = 'page_size'
	ordering = '-timestamp'
	cursor_query_param = 'cursor'


class PostListView(APIView):
	def get(self, request):
		posts = Post.objects.all()
		paginator = PostCursorPagination()
		result_page = paginator.paginate_queryset(posts, request)
		serializer = PostSerializer(result_page, many=True)
		return paginator.get_paginated_response(serializer.data)

# ---
# Follow-up Q: How to fetch 3 random comments for a post?
# Instead of: comments = obj.comments.order_by('-timestamp')[:3]
# Use: comments = obj.comments.order_by('?')[:3]
# This will return 3 random comments for each post.
