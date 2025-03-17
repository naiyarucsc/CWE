from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/securecookie-00/BenchmarkTest01134', methods=['GET', 'POST'])
def benchmark():
    response = make_response()
    response.headers['Content-Type'] = 'text/html; charset=utf-8'

    param = ""
    for name in request.headers:
        if name.lower() in ['host', 'connection', 'user-agent', 'accept', 'accept-encoding', 'accept-language']:
            continue
        param = name
        break

    def do_something(param):
        map9728 = {
            "keyA-9728": "a-Value",
            "keyB-9728": param,
            "keyC": "another-Value"
        }
        return map9728["keyB-9728"]

    bar = do_something(param)

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
