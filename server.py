

from flask import Flask
from mock_data import catalog
import json

app = Flask("Main")
me = {
        "name": "Miguel",
        "last": "Renteria",
        "age": 28,
        "hobbies": [],
        "address": {
            "street": "Evergreen",
            "number": 118,
            "city": "Springfield"
        }
    }

@app.route("/", methods=['GET'])
def home():
    return "Hello from Python"


@app.route("/test")
def any_name():
    return "I'm a test function"


@app.route("/about")
def about():
    return me["name"] + " " + me["last"]




#*******************************************************
#************************** API Endpoints **************
#*******************************************************

@app.route("/api/catalog")
def get_catalog():
    # TODO: Read the catalog from the database
    return json.dumps(catalog)





@app.route("/api/cheapest")
def get_cheapest():

    cheap = catalog[0]
    for product in catalog:
        if product["price"] < cheap["price"]:
            cheap = product
    

    return json.dumps(cheap)


@app.route("/api/product/<id>")
def get_product(id):
    for product in catalog:
        if product["_id"] == id:
            return json.dumps(product)
    

    return "NOT FOUND"


app.run(debug=True)
