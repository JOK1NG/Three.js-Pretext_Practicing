import http.server
import socketserver

class CORSHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Cross-Origin-Resource-Policy", "cross-origin")
        super().end_headers()

PORT = 8765
with socketserver.TCPServer(("", PORT), CORSHandler) as httpd:
    print(f"CORS server at http://localhost:{PORT}")
    httpd.serve_forever()
