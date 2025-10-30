import json

def load_user_agents(file_path="user_agents.json"):
    try:
        with open(file_path, 'r') as f:
            user_agents = json.load(f)
            return user_agents
    except FileNotFoundError:
        print("[-] File user_agents.json tidak ditemukan.")
        return ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"]
    except json.JSONDecodeError:
        print("[-] Error decoding user_agents.json. Memuat daftar default.")
        return ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"]

def read_config(file_path="config.json"):
    try:
        with open(file_path, 'r') as f:
            config = json.load(f)
            return config
    except FileNotFoundError:
        print("[-] File config.json tidak ditemukan. Menggunakan default.")
        return {}
    except json.JSONDecodeError:
        print("[-] Error decoding config.json. Menggunakan default.")
        return {}
