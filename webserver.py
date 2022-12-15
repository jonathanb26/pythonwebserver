from http.server import HTTPServer, BaseHTTPRequestHandler
class helloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("content-type","text/html")
        self.end_headers()
        self.wfile.write("Every journey has its bumps; I've gotten past the first.".encode())

def main():
    port = 8000
    server = HTTPServer(("", port), helloHandler)
    print("server online: port" + str(port))
    server.serve_forever()