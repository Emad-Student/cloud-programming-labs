# S1_MC_02.py
# Task: Command router using match/case

def run_command(cmd):
    """
    Route commands to appropriate handlers.
    Supported: "start", "stop", "status"
    Returns "UNKNOWN_COMMAND" for unsupported commands.
    """
    match cmd:
        case "start":
            return "Starting the system..."
        case "stop":
            return "Stopping the system..."
        case "status":
            return "System status: RUNNING"
        case _:
            return "UNKNOWN_COMMAND"

def main():
    print("Command Router Tests:")
    print("=" * 50)
    
    # Test various commands
    test_commands = [
        "start",
        "stop",
        "status",
        "restart",
        "help",
        "",
        None,
        "START",  # case-sensitive
    ]
    
    print(f"{'Command':<20} {'Response'}")
    print("-" * 50)
    
    for cmd in test_commands:
        result = run_command(cmd)
        cmd_str = repr(cmd)[:18]
        print(f"{cmd_str:<20} {result}")
    
    print("=" * 50)

if __name__ == "__main__":
    main()