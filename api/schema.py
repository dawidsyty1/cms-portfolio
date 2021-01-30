from __future__ import unicode_literals
import graphene
from graphene_django import DjangoObjectType
from pages.models import PortfolioPage
from api import graphene_wagtail
from django.conf import settings
from pages.snippet.seo import Seo
from graphene.types.generic import GenericScalar
from wagtail.images.models import Image


class SeoType(DjangoObjectType):
    class Meta:
        model = Seo


class TitleBlock(graphene.ObjectType):
    title = GenericScalar()


class BodyBlock(graphene.ObjectType):
    body = GenericScalar()


class ImageNode(DjangoObjectType):

    class Meta:
        model = Image
        exclude_fields = ['tags']

    def resolve_file(self, info):
        return f'{settings.CMS_URL}{self.file.url}'


class ImageBlock(graphene.ObjectType):
    value = GenericScalar()
    image = graphene.Field(ImageNode)

    def resolve_image(self, info):
        return Image.objects.get(id=self.value)


class ItemsBlockNode(graphene.Union):
    class Meta:
        types = (ImageBlock, TitleBlock, BodyBlock)


class PortfolioNode(DjangoObjectType):
    items = graphene.List(ItemsBlockNode)

    class Meta:
        model = PortfolioPage

    def resolve_items(self, info):
        repr_body = []
        for block in self.items.stream_data:
            block_type = block.get('type')
            value = block.get('value')
            if block_type == 'image':
                repr_body.append(ImageBlock(value=value))
            elif block_type == 'title':
                repr_body.append(TitleBlock(title=value))
            elif block_type == 'body':
                repr_body.append(BodyBlock(body=value))
        return repr_body


class Query(graphene.ObjectType):
    portfolio = graphene.List(PortfolioNode)

    @graphene.resolve_only_args
    def resolve_portfolio(self):
        return PortfolioPage.objects.live()


schema = graphene.Schema(query=Query)
