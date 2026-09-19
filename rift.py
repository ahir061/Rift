"""Public Python interface for Rift.

The implementation remains in ``harness.py`` so existing integrations keep
working. New integrations should import ``Rift`` from this module.
"""

from harness import Harness, MODES, RETRY_LIMIT, console, fmt_args, normalize_base_url

Rift = Harness

__all__ = ["MODES", "RETRY_LIMIT", "Rift", "console", "fmt_args", "normalize_base_url"]
