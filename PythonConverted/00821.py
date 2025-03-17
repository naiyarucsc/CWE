from flask import Flask, request, make_response
import urllib.parse

app = Flask(__name__)

@app.route('/securecookie-00/BenchmarkTest00821', methods=['GET', 'POST'])
def benchmark():
    response = make_response()
    response.headers['Content-Type'] = 'text/html; charset=utf-8'

    query_string = request.query_string.decode('utf-8')
    param_name = "BenchmarkTest00821="
    param_loc = query_string.find(param_name)

    if param_loc == -1:
        return f"getQueryString() couldn't find expected parameter 'BenchmarkTest00821' in query string."

    ampersand_loc = query_string.find("&", param_loc)
    if ampersand_loc != -1:
        param = query_string[param_loc + len(param_name):ampersand_loc]
    else:
        param = query_string[param_loc + len(param_name):]

    param = urllib.parse.unquote(param)

    bar = param.split(" ")[0] if param else ""
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
