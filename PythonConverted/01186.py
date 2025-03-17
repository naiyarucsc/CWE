from flask import Flask, request, make_response
import urllib.parse
import html

app = Flask(__name__)

@app.route('/securecookie-00/BenchmarkTest01186', methods=['GET', 'POST'])
def benchmark():
    response = make_response()
    response.headers['Content-Type'] = 'text/html; charset=utf-8'

    param = request.headers.get('BenchmarkTest01186', '')
    param = urllib.parse.unquote(param)

    def do_something(param):
        return html.escape(param)

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
