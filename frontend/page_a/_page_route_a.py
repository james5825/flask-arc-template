from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

bp_page_a = Blueprint('bp_page_a', __name__,
                        template_folder='./')

@bp_page_a.route('/page1')
def page1():
    try:
        return render_template(f'page1.html')
    except TemplateNotFound:
        abort(404)

@bp_page_a.route('/page2')
def page2():
    try:
        return render_template(f'page2.html')
    except TemplateNotFound:
        abort(404)