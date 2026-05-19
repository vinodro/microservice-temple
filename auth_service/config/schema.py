import graphene
from graphene_django import DjangoObjectType

from apps.users.models import User


class UserType(DjangoObjectType):

    class Meta:
        model = User
        fields = '__all__'


class Query(graphene.ObjectType):
    users = graphene.List(UserType)

    def resolve_users(root, info):
        return User.objects.all()


schema = graphene.Schema(query=Query)