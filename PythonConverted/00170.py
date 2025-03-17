from flask import Flask, request, make_response
import base64
import urllib.parse

app = Flask(__name__)

@app.route('/securecookie-00/BenchmarkTest00170', methods=['GET', 'POST'])
def benchmark():
    response = make_response()
    response.headers['Content-Type'] = 'text/html; charset=utf-8'

    param = request.headers.get('BenchmarkTest00170', '')
    param = urllib.parse.unquote(param)

    # Propagation chain
    a9823 = param
    b9823 = a9823 + " SafeStuff"
    b9823 = b9823[:-len("Chars")] + "Chars"
    map9823 = {"key9823": b9823}
    c9823 = map9823["key9823"]
    d9823 = c9823[:-1]
    e9823 = base64.b64decode(base64.b64encode(d9823.encode())).decode()
    f9823 = e9823.split(" ")[0]
    g9823 = "barbarians_at_the_gate"
    bar = g9823  # hardcoded reflection equivalent

    str_val = param if param else "No cookie value supplied"

    response.set_cookie(
        'SomeCookie',
        value=str_val,
        secure=False,
        httponly=True,
        path=request.path
    )

    escaped_val = str_val.replace("<", "&lt;").replace(">", "&gt;")

    response.data = f"Created cookie: 'SomeCookie': with value: '{escaped_val}' and secure flag set to: false"
    return response

if __name__ == '__main__':
    app.run(debug=True)