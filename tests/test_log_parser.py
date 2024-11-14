# tests/test_log_parser.py
'''from src.log_parser import parse_log_line

def test_parse_log_line():
    sample_line = '192.168.1.1 - - [01/Jan/2024:00:00:01 +0000] "GET /index.html HTTP/1.1" 200 1234'
    expected_output = {
        'ip': '192.168.1.1',
        'timestamp': '01/Jan/2024:00:00:01 +0000',
        'method': 'GET',
        'url': '/index.html',
        'status': 200,
        'size': 1234
    }
    assert parse_log_line(sample_line) == expected_output
'''