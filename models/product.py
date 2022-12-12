from utils.db import db


class Product(db.Model):
    """This class is the product's model object."""
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100))
    stock = db.Column(db.Integer)
    product_image = db.Column(db.String(250))

    def __init__(self, product_name, stock, product_image):
        self.product_name = product_name
        self.stock = stock
        self.product_image = product_image

    def obj_to_dict(self):
        return {
            "id": self.id,
            "product_name": self.product_name,
            "stock": self.stock,
            "product_image": self.product_image
        }

