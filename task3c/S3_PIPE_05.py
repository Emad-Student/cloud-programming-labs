# S3_PIPE_05.py
# Task: Log line pipeline (parse → filter → extract)

import re

def parse_log_line(line):
    """
    Parse a log line like "INFO: user=42 action=login"
    Returns dict or None if parsing fails.
    """
    match = re.match(r'(\w+):\s+user=(\d+)\s+action=(\w+)', line)
    if match:
        level, user_id, action = match.groups()
        return {
            "level": level,
            "user": int(user_id),
            "action": action
        }
    return None

def process_logs(lines):
    """
    Process log lines to extract user IDs from INFO entries.
    Pipeline: parse → filter INFO → extract user ids
    """
    user_ids = []
    
    for line in lines:
        # Parse
        parsed = parse_log_line(line)
        if parsed is None:
            continue
        
        # Filter: only INFO entries
        if parsed["level"] != "INFO":
            continue
        
        # Extract user ID
        user_ids.append(parsed["user"])
    
    return user_ids

def main():
    print("Log Line Pipeline:")
    print("=" * 60)
    
    # Sample log data
    logs = [
        "INFO: user=42 action=login",
        "ERROR: user=15 action=failed_login",
        "INFO: user=100 action=logout",
        "DEBUG: user=99 action=debug",
        "INFO: user=42 action=view_profile",
        "WARN: user=50 action=warning",
        "INFO: user=200 action=purchase",
        "invalid log line",
        "INFO: user=42 action=logout",
    ]
    
    print("Input logs:")
    for log in logs:
        print(f"  {log}")
    print("-" * 60)
    
    # Process logs
    result = process_logs(logs)
    
    print(f"\nExtracted user IDs from INFO entries:")
    print(f"  {result}")
    print("-" * 60)
    
    # Show detailed processing
    print("\nDetailed processing:")
    for line in logs:
        parsed = parse_log_line(line)
        if parsed:
            status = "✓ Included" if parsed["level"] == "INFO" else "✗ Filtered out"
            print(f"  {line}")
            print(f"    → Parsed: {parsed}")
            print(f"    → {status}")
        else:
            print(f"  {line}")
            print(f"    → Failed to parse")
    
    print("=" * 60)

if __name__ == "__main__":
    main()
    