# Log Analysis Project

A Python-based tool for parsing, analyzing, and visualizing server log data.

# 📖 Overview
This project aims to provide insights into server traffic by analyzing server logs. It can identify the most active IPs, visualize traffic trends, and help understand how the server is being accessed. The current functionality focuses on IP traffic analysis with a clear, graphical output.

# 🔑 Features
- Log Parsing: Extracts relevant details from each server log entry (IP address, request method, status code, etc.).
- IP Traffic Analysis: Identifies and counts how often each IP address appears in the logs.
- Data Visualization: Generates bar charts to visualize IP traffic patterns.
- Extensibility: The project is designed to be easily extended with more sophisticated analysis features (e.g., traffic by time).

# 🛠️ Installation & Setup
Prerequisites
Before you begin, ensure that you have the following installed on your system:

- Python 3.x (preferably Python 3.7 or newer)
- pip (Python's package installer)
- matplotlib
- pytest (for running test)
# Steps to Install
1. Clone the repository
```bash
git clone https://github.com/yourusername/log_analysis_project.git
```
2. Navigate to the project directory
```bash
cd log_analysis_project
```
3. Install the required packages
```bash
pip install -r requirements.txt
```

# 📄 Usage
To use the log analysis tool:

1. Place a log file (e.g., server_log.txt) in the logs/ directory.
2. Run the main script
```bash
python src/main.py
```
3. Expected Output
- The script parses and analyzes the log file.
- A bar chart will display the top IP addresses by request count.

# 🔍 Analysis Breakdown
Data Points Analyzed
The log_parser.py module extracts the following data from each log line:

- IP Address: Identifies the origin of the request.
- Timestamp: Captures the date and time of access.
- Request Method: Indicates the HTTP method (GET, POST, etc.).
- URL: Points to the requested resource.
- Status Code: HTTP response status (200, 404, etc.).
- Size: The size of the server’s response.

Code Example:
Here’s a breakdown of how each part of the code functions:

```python
parsed_logs = []  # List to store parsed log entries
with open(filepath, 'r') as file:
    for line in file:
        # Skips blank lines or commented lines
        if line.strip() == "" or line.strip().startswith("#"):
            continue  
        # Try parsing each line, appending results to parsed_logs
        log_entry = parse_log_line(line)
        if log_entry:
            parsed_logs.append(log_entry)
```
# 📊 Visualizations
The visualization feature uses a bar chart to display the top IPs by request frequency. This chart helps quickly identify the most active IPs accessing the server.

Example:

- Top IP Addresses: The chart displays the top 10 IPs by default, though this can be adjusted in the code.


# 🧪 Testing
Running Tests
1. Install pytest
```bash
pip install pytest
```
2. Run the Tests
```bash
pytest
```
These tests validate that the log parsing functionality works as expected, ensuring that log entries are parsed correctly and that edge cases (e.g., malformed lines) are handled.

# 🛠️ Error Handling and Troubleshooting
- Parsing Errors: If a line fails to match the expected pattern, it is logged, and the script continues with other lines.
- Skipping Blank/Comment Lines: The code ignores blank lines and lines starting with # to prevent issues with invalid data.
# Future Enhancements
- Additional Filters: Add filtering options by date, status code, or URL.
- Time-based Analysis: Analyze request patterns over time for a clearer view of server traffic.

🤝 Contributing
If you’d like to contribute:

1. Fork the repository.
2. Create a new branch (git checkout -b feature/YourFeature).
3. Make your changes and commit them (git commit -m 'Add some feature').
4. Push to the branch (git push origin feature/YourFeature).
5. Open a Pull Request.

# 📄 License
This project is licensed under the MIT License.
















