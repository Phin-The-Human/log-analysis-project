from collections import Counter

def count_status_codes(logs):
    status_counts = Counter(log["status"] for log in logs)
    return dict(status_counts) #converts the counted status in the log to a dictionary

def count_ip_address(logs):
    ip_counts = Counter(log["ip"] for log in logs)
    return dict(ip_counts) #converts the counted ip in the log to a dictionary

def Top_Traffic_Sources(logs):
    ip_counts = Counter(log["ip"] for log in logs)
    return f"Highest traffic source: {max(dict(ip_counts))},lowest traffic source: {min(dict(ip_counts))}"

def get_top_ips(logs,ip_counts,n =5,):
    """
    this function returns the top n ip address by request count.
    ip_counts (Counter): Counter object with IP addresses and their counts.
    n (int): Number of top IPs to return.
    """
    ip_counts = Counter(log["ip"] for log in logs)
    return ip_counts.most_common(n) 

