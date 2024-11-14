import matplotlib.pyplot as plt
from collections import Counter


def count_ip_requests(logs,n=5):
    ip_counts = Counter(log["ip"] for log in logs if "ip" in log)
    
    
    return ip_counts.most_common(n)


def plot_ip_traffic(ip_data):
    """
    Plots a bar chart of IP traffic based on request counts.

    Args:
        ip_data (list): List of tuples (IP, request count).
    """
    ips, counts = zip(*ip_data)  # Separates IP addresses and their request counts for plotting

    plt.figure(figsize=(10, 6)) # size of the chart
    plt.bar(ips, counts, color='purple')  # Creates a bar chart
    plt.xlabel('IP Address')              # Sets label for the x-axis
    plt.ylabel('Number of Requests')      # Sets label for the y-axis
    plt.title('Top IP Addresses by Number of Requests')  # Adds a title to the chart
    plt.xticks(rotation=45, ha='right')   # Rotates x-axis labels for better readability
    plt.tight_layout()                    # Adjusts layout to fit all elements
    plt.show()                            # Displays the plot

    