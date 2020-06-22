#!/usr/bin/env python

"""
Author: Nick Russo
Purpose: Create a mini-SDK around Cisco AMP Cloud
to simplify API interactions.
"""

from cisco_umbrella_reporting import CiscoUmbrellaReporting


def main():
    """
    Execution starts here.
    """

    umb_rep = CiscoUmbrellaReporting.build_from_env_vars()
    print(umb_rep.req("security-activity"))


if __name__ == "__main__":
    main()
