import json
import datetime
import pathlib
from urllib.parse import parse_qs, unquote_plus, urlparse
import mimetypes
from http.server import HTTPServer, BaseHTTPRequestHandler

BASE_DIR = pathlib.Path()


class HTTPHandler(BaseHTTPRequestHandler):
    
    def do_POST(self):
        # self.send_html('contact.html')
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length).decode('utf-8')
        # body = unquote_plus(body.decode())
        print(body)
        # payload = {key: value for key, value in [el.split('=') for el in body.split('&')]}
        # with open(BASE_DIR.joinpath('data/data.json'), 'w', encoding='utf-8') as fd:
        #     json.dump(payload, fd, ensure_ascii=False)
        # print(payload)
        
        params = parse_qs(body)
        print(params)
        # name = params.get('name', [''])[0]
        # email = params.get('email', [''])[0]
        # text = params.get('text', [''])[0]
        current_datetime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        new_object = {key: value[0] for key, value in params.items()}
        new_object['current_datetime'] = current_datetime
        print(new_object)

        data_file_path = BASE_DIR.joinpath('data/data.json')
        
        with open(data_file_path, 'r', encoding='utf-8') as existing_file:
            try:
                existing_data = json.load(existing_file)
            except json.decoder.JSONDecodeError:
                existing_data = []

        existing_data.append(new_object)

        with open(data_file_path, 'w', encoding='utf-8') as updated_file:
            json.dump(existing_data, updated_file, ensure_ascii=False, indent=2)
            updated_file.write('\n') 
        
        self.send_response(302)
        self.send_header('Location', './blog')
        self.end_headers()
        
    def do_GET(self):
        route = urlparse(self.path)
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
            html = f.read()
            self.wfile.write(html)
        # print('html: **  ', html.decode('utf-8'))

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