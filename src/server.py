from flask import Flask, render_template, request, abort, Response, redirect
import requests
from requests import JSONDecodeError

app = Flask(__name__)

PROXY_URL = "http://ec2-54-224-49-138.compute-1.amazonaws.com:8080/"


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>', methods=["GET", "PUT", "POST", "DELETE"])
def proxy_to_aws(path):
    print(f"Recieved Path:{path}")
    response = requests.request(
        method=request.method,
        url=request.url.replace(request.host_url, PROXY_URL),
        headers={key: value for (key, value) in request.headers if key != 'Host'},
        data=request.get_data(),
        cookies=request.cookies,
        allow_redirects=False,
        verify=False,
        stream=True)
    response.raise_for_status()
    try:
        json_response = response.json()
        return json_response
    except JSONDecodeError as e:
        print(f"Unable to decode json response, returning text instead: {response.text}")
        return response.text


app.run(host='0.0.0.0', port=8080)
