# Import necessary modules
from http.server import HTTPServer, BaseHTTPRequestHandler

# Define the HTML content to be served by the server
# html = """
# <!doctype html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport"
#           content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
#     <meta http-equiv="X-UA-Compatible" content="ie=edge">
#     <title>Document</title>
# </head>
# <body>
# <h1>Hello world</h1>
# <div class="test">Test</div>
# </body>
# </html>
# """


# Custom request handler class
class MyHTTPRequestHandler(BaseHTTPRequestHandler):
    
    file = "test.html"
    with open(file, 'r') as f:
        content = f.read()
        # print(content)
     # Handler for GET requests
    def do_GET(self):
        # Send a 200 OK response status
        self.send_response(200)
        # Specify the content type as HTML
        self.send_header('Content-Type', 'text/css')
        self.send_header('Content-Type', 'application/javascript')
        self.send_header('Content-Type', 'text/html')

        # End HTTP headers
        self.end_headers()

        # Write the HTML content to the response stream
        self.wfile.write(self.content.encode())

# Function to run the HTTP server
def run(server=HTTPServer, handler=MyHTTPRequestHandler):
    # Define the server address and port
    address = ('', 5000)
    # Create an instance of the HTTP server
    http_server = server(address, handler)
    try:
        # Start serving requests indefinitely
        http_server.serve_forever()
    except KeyboardInterrupt:
        # Handle keyboard interrupt (Ctrl+C) to gracefully stop the server
        http_server.server_close()

# Entry point for the script
if __name__ == '__main__':
    # Run the HTTP server
    run()

