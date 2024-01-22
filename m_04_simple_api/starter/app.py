import json
import datetime
import json
import datetime
import pathlib
from urllib.parse import parse_qs, urlparse
import mimetypes
from http.server import HTTPServer, BaseHTTPRequestHandler

BASE_DIR = pathlib.Path()

class MyHttpRequestHandler(BaseHTTPRequestHandler):
    
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length).decode('utf-8')
        params = parse_qs(body)
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
                self.send_static('index.html')
            case "/contact":
                self.send_static('contact.html')
            case "/blog":
                self.send_static('blog.html')
            case _:
                file = BASE_DIR / route.path[1:]
                file = file if file.exists() else ('404.html', 404)
                self.send_static(file)
        
    def send_static(self, filename, status=200):
        self.send_response(status)
        mime_type, *rest = mimetypes.guess_type(filename)
        if mime_type:
            self.send_header('Content-Type', mime_type)
        else:
            self.send_header('Content-Type', 'text/plain')
        self.end_headers()
        with open(filename, 'rb') as f:
            html = f.read()
            self.wfile.write(html)

def run(server=HTTPServer, handler=MyHttpRequestHandler, port=3001):
    server_address = ('', port)
    server = server(server_address, handler)
    try:
        print(f"Starting server on port {port}")
        server.serve_forever()
    except KeyboardInterrupt:
        print("Shutting down the server")
        server.server_close()
    
if __name__ == '__main__':
    run()
    