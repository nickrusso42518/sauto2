#!/usr/bin/env python

"""
Author: Nick Russo
Purpose: Trivial ThreatGrid regression test.
"""

from cisco_tg import CiscoTG


def main():
    """
    Execution starts here.
    """

    tg = CiscoTG.build_from_env_vars()
    print(tg.req("samples", params={"limit": 10}))


if __name__ == "__main__":
    main()
