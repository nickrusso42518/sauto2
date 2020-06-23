#!/usr/bin/env python

"""
Author: Nick Russo
Purpose: Trivial Umbrella Reporting regression test.
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
