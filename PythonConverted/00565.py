from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/securecookie-00/BenchmarkTest00565', methods=['GET', 'POST'])
def benchmark():
    response = make_response()
    response.headers['Content-Type'] = 'text/html; charset=utf-8'

    param = ""
    for name in request.args:
        values = request.args.getlist(name)
        for value in values:
            if value == "BenchmarkTest00565":
                param = name
                break
        if param:
            break

    bar = param.replace("<", "&lt;").replace(">", "&gt;")

    str_val = param if param else "No cookie value supplied"

    response.set_cookie(
        'SomeCookie',
        value=str_val,
        secure=False,
        httponly=True,
        path=request.path
    )

    response.data = f"Created cookie: 'SomeCookie': with value: '{bar}' and secure flag set to: false"
    return response

if __name__ == '__main__':
    app.run(debug=True)
