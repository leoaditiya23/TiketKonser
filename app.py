import sys
import subprocess

if __name__ == "__main__":
    print("="*50)
    print("Memulai server KonserPass...")
    print("Untuk membuka di HP, pastikan HP dan PC/Laptop terhubung ke WiFi yang sama.")
    print("Silakan akses melalui URL 'Network URL' yang muncul di bawah ini.")
    print("="*50)
    
    # Menjalankan streamlit pada IP 0.0.0.0 agar bisa diakses di jaringan lokal (HP)
    sys.exit(subprocess.run([
        sys.executable, 
        "-m", 
        "streamlit", 
        "run", 
        "tiketkonser.py", 
        "--server.address", 
        "0.0.0.0"
    ]).returncode)
