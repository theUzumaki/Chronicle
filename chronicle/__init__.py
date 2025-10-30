"""
Chronicle - A flexible and colorized logging system for Python applications.
"""

from .logger import (
    Colors,
    log,
    log_newline,
    log_application_title,
    log_section_header,
    log_subsection,
    log_error,
    log_warning,
    log_success,
    log_info,
    log_debug,
    log_step,
    log_file_saved,
    log_detection_result,
    log_final_result,
)

__version__ = "0.1.0"

__all__ = [
    "Colors",
    "log",
    "log_newline",
    "log_application_title",
    "log_section_header",
    "log_subsection",
    "log_error",
    "log_warning",
    "log_success",
    "log_info",
    "log_debug",
    "log_step",
    "log_file_saved",
    "log_detection_result",
    "log_final_result",
]
