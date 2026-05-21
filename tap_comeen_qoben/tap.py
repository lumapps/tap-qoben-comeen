"""Comeen Qoben tap class."""

from __future__ import annotations

import sys

from singer_sdk import Tap
from singer_sdk import typing as th

from tap_comeen_qoben import streams

if sys.version_info >= (3, 12):
    from typing import override
else:
    from typing_extensions import override


class TapComeenQoben(Tap):
    """Singer tap for Comeen Qoben."""

    name = "tap-comeen-qoben"

    config_jsonschema = th.PropertiesList(
        th.Property(
            "client_id",
            th.StringType(nullable=False),
            required=True,
            secret=True,
            title="Client ID",
            description="The client ID from the Qoben portal administration menu",
        ),
        th.Property(
            "client_secret",
            th.StringType(nullable=False),
            required=True,
            secret=True,
            title="Client Secret",
            description="The API key (secret) from the Qoben portal administration menu",
        ),
        th.Property(
            "api_url",
            th.StringType(nullable=False),
            title="API URL",
            default="https://api.qoben.co",
            description="The base URL for the Qoben API",
        ),
        th.Property(
            "auth_endpoint",
            th.StringType(nullable=False),
            title="Auth Endpoint",
            default="https://auth.dotsha.com/identity/resources/auth/v1/api-token",
            description="The authentication endpoint for obtaining API tokens",
        ),
    ).to_dict()

    @override
    def discover_streams(self) -> list[streams.SubscriptionsStream]:
        return [
            streams.ContactsStream(self),
            streams.CouponsStream(self),
            streams.CustomersStream(self),
            streams.DiscountsStream(self),
            streams.HierarchiesStream(self),
            streams.PricesStream(self),
            streams.ProductsStream(self),
            streams.SubscriptionsStream(self),
        ]


if __name__ == "__main__":
    TapComeenQoben.cli()
