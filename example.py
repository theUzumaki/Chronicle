"""
Example demonstrating how to use Chronicle after installation.
"""

# After installing with: pip install git+https://github.com/theUzumaki/Chronicle.git
# You can use Chronicle like this:

from chronicle import (
    log,
    log_error,
    log_warning,
    log_success,
    log_info,
    log_section_header,
    log_step,
    Colors,
)

# Simple logging
log(0, 0, 0, Colors.GREEN, "Hello from Chronicle!")

# Semantic logging
log_section_header("Example Application")
log_info("Starting process...")
log_step(1, 3, "Initialize")
log_success("Initialization complete")
log_step(2, 3, "Processing")
log_warning("Low memory detected")
log_step(3, 3, "Finalize")
log_success("Process completed successfully!")

# Custom colored messages
log(1, 1, 0, Colors.BOLD + Colors.CYAN, "This is bold cyan text")
log(1, 0, 1, Colors.BG_BLUE + Colors.BRIGHT_WHITE, "White text on blue background")
