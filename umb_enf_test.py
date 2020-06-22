#!/usr/bin/env python

"""
Author: Nick Russo
Purpose: Create a mini-SDK around Cisco ThreatGrid (TG) Cloud
to simplify API interactions.
"""

from cisco_umbrella_enforcement import CiscoUmbrellaEnforcement


def main():
    """
    Execution starts here.
    """

    umb_enf = CiscoUmbrellaEnforcement.build_from_env_vars()
    print(umb_enf.req("domains"))


if __name__ == "__main__":
    main()
