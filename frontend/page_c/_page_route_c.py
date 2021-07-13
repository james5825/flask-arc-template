from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

bp_page_c = Blueprint('bp_page_c', __name__,
                        template_folder='./')

@bp_page_c.route('/page5')
def page3():
    try:
        return render_template(f'page5.html')
    except TemplateNotFound:
        abort(404)

@bp_page_c.route('/page6')
def page4():
    try:
        return render_template(f'page6.html')
    except TemplateNotFound:
        abort(404)

# an auto mapping route to each page name, by default if no specified, it goes page5
# @bp_page_c.route('/', defaults={'page': 'page5'})
# @page_route_c.route('/<page_name>')
# def bp_page_c(page_name):
#     try:
#         return render_template(f'{page_name}')
#     except TemplateNotFound:
#         abort(404)