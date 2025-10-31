"""example.py
Runnable demonstration of Chronicle's public API.

This script is intentionally small and dependency-free. It shows a short
pipeline using the functions exported by the package. Run it with:

    python example.py

The demo is safe to run in CI or a local terminal; it simply prints to stdout
using the library's color and formatting helpers.
"""

from time import sleep

from chronicle import (
    Colors,
    log,
    log_application_title,
    log_section_header,
    log_subsection,
    log_step,
    log_file_saved,
    log_error,
    log_warning,
    log_success,
    log_info,
    log_debug,
    log_final_result,
    log_newline,
)


def main() -> None:
    # Application title
    log_application_title("CHRONICLE DEMO", width=50)

    # High-level section
    log_section_header("SHORT DEMO")

    # Info and steps
    log_info("Starting demo...")

    for i, step_name in enumerate(("Initialize", "Process", "Finalize"), start=1):
        log_step(i, 3, step_name)
        # simulate some work
        log_debug(f"Running internal work for {step_name}")
        sleep(0.12)

        if i == 1:
            log_success("Initialization complete")
        elif i == 2:
            log_warning("Low memory detected — continuing")
        else:
            log_success("All steps finished")

    # File operation example
    log_subsection("File operations")
    log_file_saved("output/results.json")
    log(1, 0, 1, Colors.BOLD + Colors.CYAN, "Custom-styled message: demo complete")

    # Final boxed result
    log_final_result(True, "Demo completed successfully")


if __name__ == "__main__":
    main()
