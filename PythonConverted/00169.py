from flask import Flask, request, make_response
import base64
import urllib.parse

app = Flask(__name__)

@app.route('/securecookie-00/BenchmarkTest00169', methods=['GET', 'POST'])
def benchmark():
    response = make_response()
    response.headers['Content-Type'] = 'text/html; charset=utf-8'

    param = request.headers.get('BenchmarkTest00169', '')
    param = urllib.parse.unquote(param)

    bar = "alsosafe"
    if param:
        values_list = ["safe", param, "moresafe"]
        values_list.pop(0)  # remove the first safe value
        bar = values_list[1]  # get the last 'safe' value

    str_val = bar if bar else "No cookie value supplied"

    response.set_cookie(
        'SomeCookie',
        value=str_val,
        secure=False,
        httponly=True,
        path=request.path
    )

    # Escape for HTML (basic substitute for ESAPI)
    escaped_val = str_val.replace("<", "&lt;").replace(">", "&gt;")

    response.data = f"Created cookie: 'SomeCookie': with value: '{escaped_val}' and secure flag set to: false"
    return response

if __name__ == '__main__':
    app.run(debug=True)
