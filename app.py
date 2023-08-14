from flask import Flask, jsonify, request
#se importa el modulo flask y jsonify que nos permite convertir un objeto en json

app = Flask(__name__)
#lo ejecuto
from products import products

#se crea una ruta de prueba para testiar si el servidor esta funcionando cuando alguien visite esta ruta, me responde con un pong
@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({'response': 'pong!'})

# se crea la ruta y cuando alguien la visite me va a traer la lista de mis productos
@app.route('/products')
def getProducts():
    # return jsonify(products)
    return jsonify({'products': products})

#se crea la ruta en la cuan se tendra que especificar el nombre del producto y asi solo se mostrara solo ese producto
@app.route('/products/<string:product_name>')
def getProduct(product_name):
    productsFound = [
        product for product in products if product['name'] == product_name.lower()]
    if (len(productsFound) > 0):
        return jsonify({'product': productsFound[0]})
    return jsonify({'message': 'Product Not found'})

# en esta ruta llega la informacion atraves de insomnia para agregar un nuevo producto
@app.route('/products', methods=['POST'])
def addProduct():
    new_product = {
        'name': request.json['name'],
        'price': request.json['price'],
        'quantity': request.json['quantity']
    }
    products.append(new_product)
    return jsonify({'message':'producto agregado','products': products})

# en esta ruta se edita la informacion de un producto y se retorna la informacion ya editada
@app.route('/products/<string:product_name>', methods=['PUT'])
def editProduct(product_name):
    productsFound = [product for product in products if product['name'] == product_name]
    if (len(productsFound) > 0):
        productsFound[0]['name'] = request.json['name']
        productsFound[0]['price'] = request.json['price']
        productsFound[0]['quantity'] = request.json['quantity']
        return jsonify({
            'message': 'Product Updated',
            'product': productsFound[0]
        })
    return jsonify({'message': 'Product Not found'})

# con esta ruta vamos a eliminar un producto y retorna la lista de productos 
@app.route('/products/<string:product_name>', methods=['DELETE'])
def deleteProduct(product_name):
    productsFound = [product for product in products if product['name'] == product_name]
    if len(productsFound) > 0:
        products.remove(productsFound[0])
        return jsonify({
            'message': 'Product Deleted',
            'products': products
        })

if __name__ == '__main__':
    app.run(debug=True, port=5000)