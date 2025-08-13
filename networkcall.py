# import requests

# # Example GET request
# url = "http://localhost:3333/"
# response = requests.get(url)

# if response.status_code == 200:
#     # data = response.text  
#     data = requests.json() # Parse JSON response
#     print(data)
# else:
#     print(f"Error: {response.status_code}")

from http.server import HTTPServer, BaseHTTPRequestHandler

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Hello from Python's built-in server!")

# Run server
server = HTTPServer(("localhost", 3333), MyHandler)
print("Serving on http://localhost:3333")
server.serve_forever()
