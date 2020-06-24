#!/usr/bin/env python

"""
Author: Nick Russo
Purpose: Block a specific application from executing on Windows hosts
by supplying a SHA-256 hash.
"""

import sys
from cisco_amp import CiscoAMP


def main(sha256):
    """
    Execution starts here.
    """

    # Instantiate a new AMP object from env vars and get the Windows
    # Protect policy which quarantines malicious files upon detection
    # and blocks execution of malware
    amp = CiscoAMP.build_from_env_vars()
    params = {"product": "windows", "name": "Protect"}
    policies = amp.req("policies", params=params)

    # Extract the GUID from the only response and perform another GET
    # to collect additional details about this policy
    wp_guid = policies["data"][0]["guid"]
    wp_policy = amp.req(f"policies/{wp_guid}")
    print(f"Found Windows Protect policy with GUID {wp_guid}")

    # Each policy has file lists to which it refers. Search for
    # the "execution blacklist" and store the GUID so we can add
    # our new executable
    for file_list in wp_policy["data"]["file_lists"]:
        if file_list["name"].lower() == "execution blacklist":
            exbl_guid = file_list["guid"]
            print(f"Found execution blacklist GUID of {exbl_guid}")
            break
    else:
        # Unlikely case, but if execution blacklist isn't found,
        # print an error message and exit with error code
        print(f"No execution blacklist in {wp_policy['data']['name']}")
        sys.exit(2)

    # Issue POST request to execution blacklist containing the app's SHA256,
    # which identifies this executable as malware. We don't need anything
    # from the response data
    body = {"description": "Windows Server calc.exe"}
    amp.req(f"file_lists/{exbl_guid}/files/{sha256}", method="post", json=body)
    print(f"Blocked executable {sha256} on Windows hosts")


if __name__ == "__main__":

    # User must supply a CLI argument of the SHA256 hash for the
    # application to blacklist. If not, print error message and exit
    # with error code
    if len(sys.argv) > 2:
        print("usage: python block_app.py <sha256_hash_of_app>")
        sys.exit(1)

    # Extract the CLI argument (SHA256 hash of app) and pass into main()
    # Example: calc.exe has a SHA256 hash of:
    #   3091E2ABFB55D05D6284B6C4B058B62C8C28AFC1D883B699E9A2B5482EC6FD51
    main(sys.argv[1])
