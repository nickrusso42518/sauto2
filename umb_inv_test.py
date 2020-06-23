#!/usr/bin/env python

"""
Author: Nick Russo
Purpose: Trivial Umbrella Investigate regression test.
"""

from cisco_umbrella_investigate import CiscoUmbrellaInvestigate


def main():
    """
    Execution starts here.
    """

    umb_inv = CiscoUmbrellaInvestigate.build_from_env_vars()
    print(umb_inv.req("domains/categories"))


if __name__ == "__main__":
    main()
