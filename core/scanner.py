import socket
import requests

class Scanner:
    def __init__(self, target):
        self.target = target

    def scan_ports(self, ports):
        open_ports = []
        for port in ports:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                result = sock.connect_ex((self.target, port))
                if result == 0:
                    print(f"[+] Port {port} terbuka")
                    open_ports.append(port)
                sock.close()
            except:
                pass
        return open_ports

    def check_vulnerabilities(self):
        try:
            response = requests.get(f"http://{self.target}", timeout=3)
            if response.status_code == 200:
                print("[+] Website aktif, mencari kerentanan...")
                # Contoh sederhana: cek header server
                server_header = response.headers.get('Server')
                if server_header:
                    print(f"[+] Server header: {server_header}")
                    # Tambahkan logika untuk mencari kerentanan berdasarkan server header
                else:
                    print("[-] Tidak dapat menemukan server header.")
            else:
                print(f"[-] Website merespons dengan status code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"[-] Error: {e}")
