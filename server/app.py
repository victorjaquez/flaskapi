import uuid
from flask import Flask, jsonify, request
from flask_cors import CORS

# create globals
app = Flask(__name__)
app.config.from_object(__name__)


# enable CORS
CORS(app)


# initial list of customers to fetch with axios
CUSTOMERS = [
    {
        'id': uuid.uuid4().hex,
        'name': 'vic',
        'email': 'vic@vic.me',
        'phone': '6023434484',
        'contacted': True
    },
    {
        'id': uuid.uuid4().hex,
        'name': 'pod',
        'email': 'pod@pod.me',
        'phone': '6023005000',
        'contacted': False
    },
    {
        'id': uuid.uuid4().hex,
        'name': 'Jaz',
        'email': 'jaz@jaz.me',
        'phone': '6025550000',
        'contacted': True
    }
]

# test


@app.route('/test', methods=['GET'])
def ping_pong():
    return jsonify('nice!')

# get and post routes


@app.route('/customers', methods=['GET', 'POST'])
def all_customers():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        CUSTOMERS.append({
            'id': uuid.uuid4().hex,
            'name': post_data.get('name'),
            'email': post_data.get('email'),
            'phone': post_data.get('phone'),
            'contacted': post_data.get('contacted')
        })
        response_object['message'] = 'Customer added!'
    else:
        response_object['customers'] = CUSTOMERS
    return jsonify(response_object)


# helper function


def remove_customer(customer_id):
    for customer in CUSTOMERS:
        if customer['id'] == customer_id:
            CUSTOMERS.remove(customer)
            return True
    return False


if __name__ == '__main__':
    app.run(debug=True)
