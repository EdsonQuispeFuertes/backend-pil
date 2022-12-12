from flask import Blueprint, json, request, flash
from helpers.create_product import create_product
from helpers.pagination_helper import pagination
from models.product import Product
from routes.status_codes import StatusCode
from utils.db import db

import json as js

products = Blueprint("products", __name__)


@products.route('/')
def index():
    """This method returns all the data of the selected page,
    the data is always displayed in 10 increments."""
    products_list = Product.query.all()
    paginate = json.loads(request.data)
    result = [item.obj_to_dict() for item in products_list]
    result_paginated = pagination(result, paginate['page'])
    message = {
        'status': StatusCode.OK.value,
        'message': 'OK',
        'products': result_paginated
    }
    return message


@products.route('/new', methods=['POST'])
def add_product():
    """This method adds a product to the database"""
    if request.method == 'POST':

        # receive data from the form
        product = json.loads(request.data)
        new_product = create_product(product)

        # save the object into the database
        db.session.add(new_product)
        db.session.commit()

        flash('Product added successfully!')

        return {'status': StatusCode.OK.value, 'message': 'OK', 'product': product}


@products.route('/json', methods=['POST'])
def add_json_products():
    """This method adds all the products from a json file"""
    with open("json/MOCK_DATA.json") as data:
        products = js.load(data)
        for product in products:
            new_product = create_product(product)

            # save the object into the database
            db.session.add(new_product)
        db.session.commit()

        return {'status': StatusCode.OK.value, 'message': 'OK'}


@products.route("/update/<string:id>", methods=["GET", "POST"])
def update(id):
    """This method updates the stock quantity of a selected product"""
    product_db = Product.query.get(id)

    if request.method == "POST":
        product = json.loads(request.data)
        product_db.stock = product_db.stock - product['stock']

        db.session.commit()
    product_db = product_db.obj_to_dict()
    return {'status': StatusCode.OK.value, 'message': 'OK', 'product': product_db}
