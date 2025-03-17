from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/securecookie-00/BenchmarkTest00348', methods=['GET', 'POST'])
def benchmark():
    response = make_response()
    response.headers['Content-Type'] = 'text/html; charset=utf-8'

    input_data = request.get_data()
    str_val = input_data.decode('utf-8') if input_data else "No cookie value supplied"

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
