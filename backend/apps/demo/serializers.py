
from rest_framework import serializers
from .models import Post, Comment
from django.contrib.auth.models import User

class CommentSerializer(serializers.ModelSerializer):
	username = serializers.CharField(source='user.username', read_only=True)

	class Meta:
		model = Comment
		fields = ['id', 'text', 'timestamp', 'username']

class PostSerializer(serializers.ModelSerializer):
	username = serializers.CharField(source='user.username', read_only=True)
	comment_count = serializers.SerializerMethodField()
	comments = serializers.SerializerMethodField()

	class Meta:
		model = Post
		fields = ['id', 'text', 'timestamp', 'username', 'comment_count', 'comments']

	def get_comment_count(self, obj):
		return obj.comments.count()

	def get_comments(self, obj):
		comments = obj.comments.order_by('-timestamp')[:3]
		return CommentSerializer(comments, many=True).data
