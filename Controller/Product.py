from flask import jsonify
from Model.Product import Product


class ProductController:

    def __init__(self, product_id):
        self.product_id = product_id

    @staticmethod
    def all():
        return jsonify({Product.get_all()})

    @staticmethod
    def create(product):
        return

    def get(self, product_id):
        return

    def update(self, data):
        return

    def remove(self):
        return


