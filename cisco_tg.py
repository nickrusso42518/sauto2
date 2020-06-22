#!/usr/bin/env python

"""
Author: Nick Russo
Purpose: Create a mini-SDK around Cisco ThreatGrid (TG) Cloud
to simplify API interactions.
"""

from cisco_endpoint_base import CiscoEndpointBase


class CiscoTG(CiscoEndpointBase):
    """
    Declaration of Cisco ThreatGrid (TG) SDK class.
    """

    def __init__(self, api_key):
        """
        Constructor to create a new object. TG uses a query parameter
        named api_key in each request for authentication.
        """

        # Call the base class constructor to pass in the base URL
        # and the basic auth kwarg
        super().__init__(
            base_url="https://panacea.threatgrid.com/api/v2",
        )

        self.auth_params = {"api_key": api_key}

    def req(self, resource, **kwargs):

        # If the user wants to query for some kwargs as well, we need
        # to update that argument with our base params dict which
        # is necessary for authentication. Yes, this is sloppy!
        if "params" in kwargs:
            kwargs["params"].update(self.auth_params)

        resp = super().base_req(resource, **kwargs)

        # If there is a body, it will be JSON; convert to Python objects
        if resp.text:
            return resp.json()

        # Body was not present; return empty dict for consistency
        return {}


    @staticmethod
    def build_from_env_vars():
        """
        Static class-level helper method to quickly create a new CiscoTG
        object using environment variables:
          1. TG_API_KEY: Your personal API key for ThreatGrid
        """



        api_key, = CiscoEndpointBase.load_env_vars("TG_API_KEY")
        return CiscoTG(api_key)
