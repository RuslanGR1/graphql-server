import graphene
from graphene_django import DjangoObjectType

from ..models import Category, Post, Comment

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = "__all__"

class PostType(DjangoObjectType):
    class Meta:
        model = Post
        fields = ("id", "text", "title")

class CommentType(DjangoObjectType):
    class Meta:
        model = Comment
        fields = "__all__"


class Query(graphene.ObjectType):
    posts = graphene.List(PostType)
    post_by_id = graphene.Field(PostType, id=graphene.String())

    def resolve_posts(root, info, **kwargs):
        return Post.objects.all()

    def resolve_posts_by_id(root, info, id):
        return Post.objects.get(pk=id)
