# import requests
from flask import Flask, jsonify
from flask import request

app = Flask('app')

@app.route('/test/', methods=['POST'])
def test():
    data = request
    # print(requests)
    uri_data = request.args
    headers = request.headers
    json_data = request.json

    return jsonify({'status': 'ok',
                    'qs': dict(uri_data),
                    'headers': dict(headers),
                    'json': json_data
                    })


app.run()
