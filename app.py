from flask import Flask, request

app = Flask(__name__)

from Controller.Product import ProductController


@app.route('/api/product', methods=["GET", "POST"])
def product_all_create():
    product_data = request.get_json()
    if request.method == "POST" and product_data:
        return ProductController.create(product_data)
    return ProductController.all()


@app.route('/api/product/<int:product_id>', methods=["GET", "PUT"])
def product_get_update(product_id):
    product_data = request.get_json()
    if request.method == "PUT":
        return ProductController.update(product_id, product_data)
    elif request.method == "DELETE":
        return ProductController.delete()
    return ProductController.get()


if __name__ == '__main__':
    app.run()
