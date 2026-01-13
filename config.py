"""
Configuration, read from environment variables
"""

import os


LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
