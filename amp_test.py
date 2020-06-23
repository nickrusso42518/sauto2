#!/usr/bin/env python

"""
Author: Nick Russo
Purpose: Trivial AMP regression test.
"""

from cisco_amp import CiscoAMP


def main():
    """
    Execution starts here.
    """

    amp = CiscoAMP.build_from_env_vars()
    print(amp.req("computers"))


if __name__ == "__main__":
    main()
