from flask import Blueprint, request, jsonify
from users.models.product_model import Productos
from users.models.db import db

product_controller = Blueprint('product_controller', __name__)

@product_controller.route('/api/productos', methods=['GET'])
def get_products():
    print("listado de productos")
    productos = Productos.query.all()
    result = [{'id': producto.id, 'nombre': producto.nombre, 'descripcion': producto.descripcion, 'precio': producto.precio} for producto in productos]
    return jsonify(result)

@product_controller.route('/api/productos/<int:producto_id>', methods=['GET'])
def get_product(producto_id):
    print("obteniendo producto")
    producto = Productos.query.get_or_404(producto_id)
    return jsonify({'id': producto.id, 'nombre': producto.nombre, 'descripcion': producto.descripcion, 'precio': producto.precio})

@product_controller.route('/api/productos', methods=['POST'])
def create_product():
    print("creando producto")
    data = request.json
    new_product = Productos(nombre=data['nombre'], descripcion=data['descripcion'], precio=data['precio'])
    db.session.add(new_product)
    db.session.commit()
    return jsonify({'message': 'Product created successfully'}), 201

@product_controller.route('/api/productos/<int:producto_id>', methods=['PUT'])
def update_product(producto_id):
    print("actualizando producto")
    producto = Productos.query.get_or_404(producto_id)
    data = request.json
    producto.nombre = data['nombre']
    producto.descripcion = data['descripcion']
    producto.precio = data['precio']
    db.session.commit()
    return jsonify({'message': 'Product updated successfully'})

@product_controller.route('/api/productos/<int:producto_id>', methods=['DELETE'])
def delete_product(producto_id):
    print("eliminando producto")
    producto = Productos.query.get_or_404(producto_id)
    db.session.delete(producto)
    db.session.commit()
    return jsonify({'message': 'Product deleted successfully'})

