# src/main.py
import os
from log_parser import parse_log_line
from analysis import count_status_codes ,count_ip_address,Top_Traffic_Sources,get_top_ips
from visualization import plot_ip_traffic,count_ip_requests


def read_log_file(filepath):
    """
    Reads a log file line by line.
    
    Args:
        filepath (str): Path to the log file.

    Returns:
        list: Parsed lines from the log file.
    """
    parsed_logs = []
    with open(filepath, 'r') as file:
        for line in file:
            if line.strip() == "" or line.strip().startswith("#"):
                continue  # Skip blank lines or comments
            try:
                log_entry = parse_log_line(line)
                if log_entry:
                    parsed_logs.append(log_entry)
            except Exception as e:
                print(f"Error parsing line: {line.strip()} - {e}")
    return parsed_logs

def analyze_logs(filepath):
    """
    Calls the read_log_file function and prints the parsed log entries.
    
    Args:
        filepath (str): Path to the log file.
    """
    logs = read_log_file(filepath)
    print("Parsed Logs:", logs)

if __name__ == "__main__":
    # Set the path to the log file
    log_file_path = os.path.join("logs", "server_log.txt")
    logs = read_log_file(log_file_path) #function that reads the log file, stored in variable named "logs"
    print(f"Looking for log file at: {log_file_path}")
    analyze_logs(log_file_path)
    
     # Analyze log data
    status_counts = count_status_codes(logs)
    print("Status Code Counts:", status_counts)
    
    ip_counts = count_ip_address(logs) # calls the function that counts ip
    print("IP Address Traffic Analysis:",ip_counts)
    
    traffic_source = Top_Traffic_Sources(logs)
    print(traffic_source)
    
    # Get top 5 IPs by request count
    top_ips = get_top_ips(logs,ip_counts, n=10)
    print("Top IPs by Traffic:", top_ips)
    
    #plot the Top ip address by the number of request
    ip_data = count_ip_requests(logs)
    plot_ip_traffic(ip_data)




    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    