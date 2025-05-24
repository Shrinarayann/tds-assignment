import json
from http.server import BaseHTTPRequestHandler
from urllib.parse import parse_qs

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')  # Enable CORS
        self.end_headers()

        try:
            query = parse_qs(self.path[self.path.find('?')+1:])
            names = query.get('name', [])

            with open('q-vercel-python.json', 'r') as f:
                data = json.load(f)

            result = [data.get(name, None) for name in names]
            self.wfile.write(json.dumps({"marks": result}).encode())
        except Exception as e:
            self.wfile.write(json.dumps({"error": str(e)}).encode())
