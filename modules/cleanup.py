import os

def delete_files(target_dir):
    try:
        for filename in os.listdir(target_dir):
            file_path = os.path.join(target_dir, filename)
            if os.path.isfile(file_path):
                os.unlink(file_path)
        print(f"[+] Semua file di {target_dir} telah dihapus.")
    except Exception as e:
        print(f"[-] Error menghapus file: {e}")

def clear_logs():
    try:
        with open("attack.log", "w") as log_file:
            log_file.write("")
        print("[+] Log telah dibersihkan.")
    except Exception as e:
        print(f"[-] Error membersihkan log: {e}")
