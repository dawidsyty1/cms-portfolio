from __future__ import unicode_literals
import graphene
from graphene_django import DjangoObjectType
from pages.models import PortfolioPage
from api import graphene_wagtail
from pages.snippet.seo import Seo


class SeoType(DjangoObjectType):
    class Meta:
        model = Seo


class PortfolioNode(DjangoObjectType):
    class Meta:
        model = PortfolioPage


class Query(graphene.ObjectType):
    portfolio = graphene.List(PortfolioNode)

    @graphene.resolve_only_args
    def resolve_portfolio(self):
        return PortfolioPage.objects.live()


schema = graphene.Schema(query=Query)
