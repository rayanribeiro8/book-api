from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class SimpleHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'message': 'API Online 🚀'}).encode())
        elif self.path == '/ping':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'message': 'pong-test'}).encode())
        else:
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'message': 'Not Found'}).encode())

def run():
    port = int(os.environ.get('PORT', 3000))
    server_address = ('', port)
    httpd = HTTPServer(server_address, SimpleHandler)
    print(f'Server running on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    import os
    run()