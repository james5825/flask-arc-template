from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

bp_page_wildcard_a = Blueprint('bp_page_wildcard_a', __name__,
                        template_folder='./')

# an auto mapping route to each page name, by default if no specified, it goes page5
@bp_page_wildcard_a.route('/', defaults={'page': '../../index.html'})
@bp_page_wildcard_a.route('/<page_name>')
def show_page_wildcard_a(page_name):
    print(page_name)
    try:
        return render_template(f'{page_name}')
    except TemplateNotFound:
        abort(404)