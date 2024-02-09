from flask import Blueprint

comparar_bp = Blueprint('comparar', __name__)

from . import comparar_routes