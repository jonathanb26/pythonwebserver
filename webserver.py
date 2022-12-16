from http.server import HTTPServer, BaseHTTPRequestHandler
class HelloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("content-type","text/html")
        self.end_headers()
        self.wfile.write("Every journey has its bumps; I've gotten past the first.".encode())

def main():
    port = 8000
    server = HTTPServer(('', port), HelloHandler)
    print("server online: port %s" % port)
    server.serve_forever()
    
if __name__ == "__main__":
    main()