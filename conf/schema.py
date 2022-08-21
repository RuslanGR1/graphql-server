import graphene

import apps.blog.schema


class Query(apps.blog.schema.Query, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)
