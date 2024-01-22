import json
import pathlib
import urllib.parse
from urllib.parse import parse_qs 
import mimetypes
from http.server import HTTPServer, BaseHTTPRequestHandler

BASE_DIR = pathlib.Path()


class HTTPHandler(BaseHTTPRequestHandler):
    
    def do_POST(self):
        # self.send_html('contact.html')
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length).decode('utf-8')
        # body = urllib.parse.unquote_plus(body.decode())
        print(body)
        payload = {key: value for key, value in [el.split('=') for el in body.split('&')]}
        with open(BASE_DIR.joinpath('data/data.json'), 'w', encoding='utf-8') as fd:
            json.dump(payload, fd, ensure_ascii=False)
        print(payload)
        
        params = parse_qs(body)
        print(params)
        name = params.get('name', [''])[0]
        email = params.get('email', [''])[0]
        text = params.get('text', [''])[0]
        print(f"Name = {name}, email = {email}, text = {text}")
        
        self.send_response(302)
        self.send_header('Location', './blog')
        self.end_headers()

    def do_GET(self):
        route = urllib.parse.urlparse(self.path)
        match route.path:
            case "/":
                self.send_html('index.html')
            case "/contact":
                self.send_html('contact.html')
            case "/blog":
                self.send_html('blog.html')
            case _:
                file = BASE_DIR / route.path[1:]
                if file.exists():
                    self.send_static(file)
                else:
                    self.send_html('404.html', 404)

    def send_html(self, filename, status_code=200):
        self.send_response(status_code)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()
        with open(filename, 'rb') as f:
            self.wfile.write(f.read())

    def send_static(self, filename):
        self.send_response(200)
        mime_type, *rest = mimetypes.guess_type(filename)
        if mime_type:
            self.send_header('Content-Type', mime_type)
        else:
            self.send_header('Content-Type', 'text/plain')
        self.end_headers()
        with open(filename, 'rb') as f:
            self.wfile.write(f.read())


def run(server=HTTPServer, handler=HTTPHandler, port=3000):
    address = ('', port)
    http_server = server(address, handler)
    try:
        print(f"Starting server on port {port}")
        http_server.serve_forever()
    except KeyboardInterrupt:
        print("Shutting down the server")
        http_server.server_close()


if __name__ == '__main__':
    run()
