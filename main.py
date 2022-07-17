import asyncio
from unicodedata import category
from fastapi import FastAPI
from graphene import ObjectType, List, Int, String, Schema, Field, Mutation
from starlette_graphene3 import GraphQLApp, make_graphiql_handler
from schemas import ProductType, AllProductType
import json

class Query(ObjectType):
    product_list = None
    product_details = Field(ProductType, id=Int())
    product_overview = Field(AllProductType)
    products_by_category = Field(List(ProductType), id=Int())

    async def resolve_product_details(self, info, id=None):
        with open("./products.json") as products:
            product_list = json.load(products)
        print(product_list)
        if (id):
            for product in product_list:
                if product['id'] == id: return product
        else:
            raise Exception('This route needs an Id')


    async def resolve_product_overview(self, info):
        with open("./products.json") as products:
            product_list = json.load(products)

        return {
            "products": product_list,
            "total_products": len(product_list),
            "total_price": sum([x['price'] for x in product_list])
        }

    def resolve_products_by_category(self, info, id=None):
        with open("./products.json") as products:
            product_list = json.load(products)
        return list(filter(lambda x: x['category'] == id, product_list))



app = FastAPI()
app.add_route("/graphql", GraphQLApp(
    schema=Schema(query=Query),
    on_get=make_graphiql_handler()
))

