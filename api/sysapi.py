# sysapi.py
import json
import psutil
from http.server import HTTPServer, BaseHTTPRequestHandler

def bytes_to_MB(bytes_value):
    return bytes_value / (1024 * 1024)

class SysApiHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/sysinfo':
            try:
                cpu = psutil.cpu_percent(interval=1)
                ram = psutil.virtual_memory().percent
                disk = psutil.disk_usage('/').percent
                net = psutil.net_io_counters()
                data = {
                    "cpu": cpu,
                    "ram": ram,
                    "disk": disk,
                    "net_sent": bytes_to_MB(net.bytes_sent),
                    "net_recv": bytes_to_MB(net.bytes_recv)
                }
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(data, indent=2).encode())
            except Exception as e:
                self.send_response(500)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"error": str(e)}).encode())
        else:
            self.send_response(404)
            self.end_headers()

if __name__ == "__main__":
    server = HTTPServer(('0.0.0.0', 8080), SysApiHandler)
    print("API running: http://localhost:8080/sysinfo")
    server.serve_forever()