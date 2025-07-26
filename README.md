ZENO VX - Multiverse Erasure
⚠️ EXTREMELY DANGEROUS TOOL ⚠️
ZENO VX is a powerful, multi-functional Denial-of-Service (DoS) tool designed to overwhelm target systems. This script combines various attack vectors inspired by notorious tools like LOIC, HOIC, XerXes, and Nano, along with previous iterations of the ZENO protocol (V1-V5).
⛔ DISCLAIMER: READ CAREFULLY BEFORE PROCEEDING ⛔
 * ILLEGAL USE: This tool is intended for EDUCATIONAL AND RESEARCH PURPOSES ONLY. Using ZENO VX to attack any network or system without explicit, written permission from the owner is ILLEGAL and can lead to severe legal penalties, including hefty fines and imprisonment.
 * YOUR RESPONSIBILITY: The developer, FrontMan, and the HDN Cyber Forces / ZENO Protocol group are NOT RESPONSIBLE for any misuse or damage caused by this software. You are solely responsible for your actions when using this tool.
 * ETHICAL HACKING ONLY: If you choose to use this, ensure it is within a controlled, legal environment (e.g., a personal test network, a capture-the-flag competition with explicit rules, or a penetration test with a signed engagement letter).
 * ANONYMITY IS NOT GUARANTEED: While this tool attempts to use IP spoofing, total anonymity online is never guaranteed. Your activities can still be traced.
Features
 * Multi-Method Attack: Integrates TCP, UDP, HTTP (HOIC-style), and SYN (XerXes-style) flood capabilities.
 * IP Stealth Mode: Attempts to spoof source IP addresses for HTTP requests.
 * Ubuntu Optimized: Specifically designed and tested for Ubuntu Linux environments.
 * Multi-threaded: Utilizes hundreds of threads for high-volume attack generation.
 * Custom User-Agents: Employs a variety of common browser user-agents for HTTP floods.
Requirements
 * Linux Operating System (Ubuntu recommended)
 * Python 3
 * socket module (built-in)
 * threading module (built-in)
 * random module (built-in)
 * time module (built-in)
 * os module (built-in)
 * platform module (built-in)
 * sys module (built-in)
Usage
 * Ensure Linux: This script is designed for Linux Ubuntu only. It will exit if run on other platforms.
 * Run the Script:
   git clone https://github.com/rifqi409/ZENO-VX.git # Assuming a repo
cd ZENO-VX
python3 zeno_vx.py

 * Enter Target: You will be prompted to enter the target IP address or hostname. The default port is 80 (HTTP).
 * Observe: The script will begin launching multi-threaded attacks, displaying messages for each packet/request sent.
Attack Modes Explained
 * TCP Flood: Establishes and sends random data over TCP connections.
 * UDP Flood: Sends large volumes of random UDP packets to the target.
 * HTTP Flood (HOIC Style): Floods the target with HTTP GET requests, including spoofed IP addresses and varied user-agents.
 * SYN Flood (XerXes Style): Rapidly initiates and drops TCP connections, aiming to exhaust the target's connection table.
Author & Group
 * Author: FrontMan
 * Group: HDN Cyber Forces | ZENO Protocol
🚫 STOP. THINK. ACT RESPONSIBLY. 🚫
Remember, with great power comes great responsibility. Use this tool ethically and legally.

