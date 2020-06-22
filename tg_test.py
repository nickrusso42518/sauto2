#!/usr/bin/env python

"""
Author: Nick Russo
Purpose: Create a mini-SDK around Cisco ThreatGrid (TG) Cloud
to simplify API interactions.
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
