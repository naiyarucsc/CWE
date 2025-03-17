from flask import Flask, request, make_response
import urllib.parse

app = Flask(__name__)

@app.route('/securecookie-00/BenchmarkTest00977', methods=['GET'])
def benchmark_get():
    response = make_response("<html><body>Cookie Set</body></html>")
    response.headers['Content-Type'] = 'text/html; charset=utf-8'
    response.set_cookie(
        'BenchmarkTest00977',
        value='whatever',
        max_age=60 * 3,
        secure=True,
        path=request.path,
        domain=request.host.split(':')[0]
    )
    return response

@app.route('/securecookie-00/BenchmarkTest00977', methods=['POST'])
def benchmark_post():
    response = make_response()
    response.headers['Content-Type'] = 'text/html; charset=utf-8'

    param = request.cookies.get('BenchmarkTest00977', 'noCookieValueSupplied')
    param = urllib.parse.unquote(param)

    def do_something(param):
        num = 106
        return "This should never happen" if (7 * 42) - num > 200 else param

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
