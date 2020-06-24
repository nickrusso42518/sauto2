#!/usr/bin/env python

"""
Author: Nick Russo
Purpose: Trivial Umbrella Enforcement regression test.
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
