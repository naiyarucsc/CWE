from flask import Flask, request, make_response
import urllib.parse

app = Flask(__name__)

@app.route('/securecookie-00/BenchmarkTest01061', methods=['GET', 'POST'])
def benchmark():
    response = make_response()
    response.headers['Content-Type'] = 'text/html; charset=utf-8'

    param = request.headers.get("BenchmarkTest01061", "")
    param = urllib.parse.unquote(param)

    def do_something(param):
        if param and len(param) > 1:
            return param[:-1] + "Z"
        return param

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
