import re

# regular expression pattern to parse log lines
log_pattern = r'(\d+\.\d+\.\d+\.\d+) - - \[(.*?)\] "(GET|POST|PUT|DELETE|HEAD|OPTIONS) (.*?) HTTP/1\.\d" (\d{3}) (\d+)'

def parse_log_line(line):
    """
    Parses a single log line and extracts key components.
    Returns a dictionary with IP, timestamp, method, URL, status code, and size.
    """
    match = re.match(log_pattern, line)
    if match:
        ip, timestamp, method, url, status, size = match.groups()
        return {
            'ip': ip,
            'timestamp': timestamp,
            'method': method,
            'url': url,
            'status': int(status),
            'size': int(size)
        }
    else:
        print(f"No match found for line: {line.strip()}")
    return None


sample_line = '192.168.1.1 - - [01/Jan/2024:00:00:01 +0000] "GET /index.html HTTP/1.1" 200 1234'
parsed_entry = parse_log_line(sample_line)
print(parsed_entry)


