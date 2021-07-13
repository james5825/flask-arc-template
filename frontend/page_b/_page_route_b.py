from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

bp_page_b = Blueprint('page_route_b', __name__,
                        template_folder='./')

@bp_page_b.route('/page3')
def page3():
    try:
        return render_template(f'page3.html')
    except TemplateNotFound:
        abort(404)

@bp_page_b.route('/page4')
def page4():
    try:
        return render_template(f'page4.html')
    except TemplateNotFound:
        abort(404)