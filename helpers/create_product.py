from models.product import Product


def create_product(product):
    product_name = product['product_name']
    stock = product['stock']
    product_image = product['product_image']

    # create a new Contact object
    return Product(product_name, stock, product_image)
