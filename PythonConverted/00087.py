from flask import Flask, request, make_response, render_template_string
import base64
import urllib.parse

app = Flask(__name__)

@app.route('/securecookie-00/BenchmarkTest00087', methods=['GET'])
def benchmark_get():
    response = make_response(render_template_string('<html><body>Cookie Set</body></html>'))
    response.headers['Content-Type'] = 'text/html; charset=utf-8'

    cookie_value = 'whatever'
    response.set_cookie(
        'BenchmarkTest00087',
        value=cookie_value,
        max_age=60*3,  # 3 minutes
        secure=True,
        path=request.path,
        domain=request.host.split(':')[0]
    )

    return response

@app.route('/securecookie-00/BenchmarkTest00087', methods=['POST'])
def benchmark_post():
    response = make_response()
    response.headers['Content-Type'] = 'text/html; charset=utf-8'

    cookies = request.cookies
    param = cookies.get('BenchmarkTest00087', 'noCookieValueSupplied')

    # Base64 encode and decode
    encoded = base64.b64encode(param.encode('utf-8'))
    decoded = base64.b64decode(encoded).decode('utf-8')

    str_val = decoded

    if not str_val:
        str_val = "No cookie value supplied"

    # Create a new cookie
    response.set_cookie(
        'SomeCookie',
        value=str_val,
        secure=False,
        httponly=True,
        path=request.path
    )

    # Escape for HTML (basic version, replace with proper HTML encoder in prod)
    escaped_val = str_val.replace("<", "&lt;").replace(">", "&gt;")

    response.data = f"Created cookie: 'SomeCookie': with value: '{escaped_val}' and secure flag set to: false"
    return response

if __name__ == '__main__':
    app.run(debug=True)
