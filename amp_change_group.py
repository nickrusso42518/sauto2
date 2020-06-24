#!/usr/bin/env python

"""
Author: Nick Russo
Purpose: Change the group membership of a specific computer.
"""

from cisco_amp import CiscoAMP


# Quick and dirty alternative to environment variables or CLI args
CONNECTOR_GUID = "6eb002f2-3574-4fe7-a9e8-f028c618e69d"
GROUP_NAME = "Audit"


def main():
    """
    Execution starts here.
    """

    # Instantiate a new AMP object from env vars and get specific computer
    amp = CiscoAMP.build_from_env_vars()
    computer = amp.req(f"computers/{CONNECTOR_GUID}")

    # Issue another GET request to get the name of the group by GUID
    cur_group = amp.req(f"groups/{computer['data']['group_guid']}")

    # Check if the computer is already in the correct group
    if cur_group["data"]["name"].lower() == GROUP_NAME.lower():

        # No action needed; just report that the computer is up to date
        print(f"Group {GROUP_NAME} already applied to GUID {CONNECTOR_GUID}")
        return

    # Group does not match; GET the new group
    print(f"Applying group {GROUP_NAME} to GUID {CONNECTOR_GUID}")
    new_group = amp.req("groups", params={"name": GROUP_NAME})

    # Build HTTP body and issue PATCH request to update the computer
    body = {"group_guid": new_group["data"][0]["guid"]}
    amp.req(f"computers/{CONNECTOR_GUID}", method="patch", json=body)

    # Print final status message
    print(f"Group {GROUP_NAME} successfully applied")


if __name__ == "__main__":
    main()
