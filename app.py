from flask import Flask, render_template

app = Flask(__name__)

################################################################
# config backend blueprint
################################################################
url_prefix_apis = '/apis'

# INSTRUCTION: import each backend py file
# INSTRUCTION: register each under app with '/api' prefix

from backend.api_a._route_api_a import bp_api_a
app.register_blueprint(bp_api_a, url_prefix=url_prefix_apis)

from backend.api_b._route_api_b import bp_api_b
app.register_blueprint(bp_api_b, url_prefix=url_prefix_apis)

################################################################
# frontend view model tempalte
################################################################
url_prefix_pages = '/pages'

# INSTRUCTION: import each front route and page file
# INSTRUCTION: register each under app with '/page' prefix

from frontend.page_a._page_route_a import bp_page_a
app.register_blueprint(bp_page_a, url_prefix=url_prefix_pages)

from frontend.page_b._page_route_b import bp_page_b
app.register_blueprint(bp_page_b, url_prefix=url_prefix_pages)

from frontend.page_c._page_route_c import bp_page_c
app.register_blueprint(bp_page_c, url_prefix=url_prefix_pages)

from frontend.page_wildcard_a._page_route_wildcard_a import bp_page_wildcard_a
app.register_blueprint(bp_page_wildcard_a, url_prefix=url_prefix_pages)


################################################################
# index page
################################################################
@app.route("/")
def index():
    return render_template("index.html", url_prefix_apis=url_prefix_apis, url_prefix_pages=url_prefix_pages)

################################################################
# app run
################################################################
if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
