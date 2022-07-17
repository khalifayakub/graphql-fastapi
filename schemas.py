import graphene

class ProductType(graphene.ObjectType):
    id = graphene.Int(required=True)
    name = graphene.String(required=True)
    price = graphene.Int(required=True)
    category = graphene.Int(required=True)


class AllProductType(graphene.ObjectType):
    products = graphene.Field(graphene.List(ProductType))
    total_products = graphene.Int()
    total_price = graphene.Int()
    

