from models.product import Product


def get_ordered_products_by_price(products: list[Product]) -> list[Product]:
    return sorted(products, key=lambda prod: prod.get_price(), reverse=True)
