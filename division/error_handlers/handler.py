from flask import Blueprint, render_template

error_handler_bp = Blueprint('httperror', __name__)

@error_handler_bp.app_errorhandler(404)
def error404(e):
    return render_template('error_pages/404.html')

@error_handler_bp.app_errorhandler(500)
def error500(e):
    return render_template('error_pages/500.html')

