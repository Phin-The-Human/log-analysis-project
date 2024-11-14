
from src.visualization import plot_ip_traffic, count_ip_requests

parsed_logs = [
    {'ip': '192.168.1.1', 'timestamp': '01/Jan/2024:00:05:00 +0000', 'method': 'GET', 'url': '/index.html', 'status': 200, 'size': 1234},
    {'ip': '192.168.1.2', 'timestamp': '01/Jan/2024:00:15:00 +0000', 'method': 'POST', 'url': '/submit', 'status': 404, 'size': 567},
    {'ip': '192.168.1.1', 'timestamp': '01/Jan/2024:01:00:00 +0000', 'method': 'GET', 'url': '/contact', 'status': 200, 'size': 890},
    {'ip': '192.168.1.3', 'timestamp': '01/Jan/2024:02:10:00 +0000', 'method': 'GET', 'url': '/home', 'status': 200, 'size': 1500},
    {'ip': '192.168.1.1', 'timestamp': '01/Jan/2024:03:25:00 +0000', 'method': 'GET', 'url': '/about', 'status': 200, 'size': 750},
    # Add more log entries as needed
]

# Generate data and plot
top_ips = count_ip_requests(parsed_logs)
plot_ip_traffic(top_ips)
