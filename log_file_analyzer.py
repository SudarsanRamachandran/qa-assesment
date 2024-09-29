import re
from collections import Counter

def analyze_log_file(log_file):
    with open(log_file, 'r') as file:
        logs = file.readlines()

    # Pattern for 404 errors
    error_pattern = re.compile(r'404')
    
    # Counter for page requests
    page_counter = Counter()

    for log in logs:
        # Count 404 errors
        if error_pattern.search(log):
            print(f"404 Error: {log.strip()}")
        
        # Extract page requested
        # Example log format: "127.0.0.1 - - [28/Sep/2024:00:00:00 +0000] \"GET /index.html HTTP/1.1\" 200 2326"
        match = re.search(r'\"GET (.*?) HTTP', log)
        if match:
            page = match.group(1)
            page_counter[page] += 1

    # Most requested pages
    most_common_pages = page_counter.most_common(5)
    print("\nMost Requested Pages:")
    for page, count in most_common_pages:
        print(f"{page}: {count} requests")

if __name__ == "__main__":
    analyze_log_file('access.log')  # Replace 'access.log' with your log file name
