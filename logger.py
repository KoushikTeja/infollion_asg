from datetime import datetime


def log_request(ip, node):

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(f"[{current_time}] Incoming IP: {ip} -> Routed to: {node}")