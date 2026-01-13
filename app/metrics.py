"""
Prometheus custom metrics.
"""

from prometheus_client import Counter

hello_requests_total = Counter(
    "hello_requests_total", "Total number of /hello requests"
)
