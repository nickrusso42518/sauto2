#!/usr/bin/env python

"""
Author: Nick Russo
Purpose: Create a mini-SDK around Cisco AMP Cloud
to simplify API interactions.
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
