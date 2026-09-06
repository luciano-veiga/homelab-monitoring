from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from datetime import datetime, timezone


class WebhookHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(length)

        try:
            payload = json.loads(body)
        except json.JSONDecodeError:
            payload = {"raw": body.decode(errors="replace")}

        timestamp = datetime.now(timezone.utc).isoformat()
        log_line = f"[{timestamp}] Alerta recebido:\n{json.dumps(payload, indent=2, ensure_ascii=False)}\n"

        print(log_line, flush=True)
        with open("/app/alerts.log", "a") as f:
            f.write(log_line + "\n")

        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"OK")

    def log_message(self, format, *args):
        pass


if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 5001), WebhookHandler)
    print("Webhook receiver ouvindo na porta 5001...")
    server.serve_forever()
