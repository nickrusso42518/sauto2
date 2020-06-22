#!/usr/bin/env python

"""
Author: Nick Russo
Purpose: Abstract base class to encompass common logic for all
Cisco endpoint security products.
"""

import os
import requests


class CiscoEndpointBase:
    def __init__(self, base_url):

        # Retain the base URL and create a new, long-lived HTTP session
        self.base_url = base_url
        self.sess = requests.session()

        # Generally common headers can be re-used over and over.
        # Content-Type not supplied because it isn't always JSON, and
        # just by setting the "json" kwarg, requests sets the Content-Type.
        self.headers = {"Accept": "application/json"}

    def base_req(self, resource, method="get", **kwargs):
        resp = self.sess.request(
            url=f"{self.base_url}/{resource}",
            method=method,
            **kwargs,
        )
        resp.raise_for_status()

        return resp
        
    @staticmethod
    def load_env_vars(*args):
        ev_list = []
        for ev_name in args:
            ev_value = os.environ.get(ev_name)
            if not ev_value:
                raise ValueError(f"env var {ev_name} not defined")

            ev_list.append(ev_value)

        return ev_list

