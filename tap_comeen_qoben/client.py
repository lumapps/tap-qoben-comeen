"""REST client handling, including ComeenQobenStream base class."""

from __future__ import annotations

import decimal
import sys
import typing as t

from tap_comeen_qoben.auth import ComeenQobenAuthenticator

from singer_sdk.helpers.jsonpath import extract_jsonpath
from singer_sdk.pagination import BaseHATEOASPaginator, PageNumberPaginator
from singer_sdk.streams import RESTStream

from urllib.parse import parse_qsl
from functools import cached_property

if sys.version_info >= (3, 12):
    from typing import override
else:
    from typing_extensions import override

if t.TYPE_CHECKING:
    from collections.abc import Iterable

    import requests
    from singer_sdk.helpers.types import Auth, Context


DEFAULT_PAGE_SIZE = 100


class ComeenQobenPaginator(BaseHATEOASPaginator):
    def get_next_url(self, response):
        data = response.json()
        return data.get("links", {}).get("next")
    
    def get_previous_url(self, response):
        data = response.json()
        return data.get("links", {}).get("previous")
    
    def has_more(self, response: requests.Response):
        data = response.json()
        next = data.get("links", {}).get("next")
        return next is not None


class ComeenQobenStream(RESTStream):
    """Base stream class for Comeen Qoben."""

    records_jsonpath = "$.data[*]"
    page_size = DEFAULT_PAGE_SIZE

    stream_params: dict = {}

    @override
    @property
    def url_base(self) -> str:
        return self.config["api_url"]

    @override
    @cached_property
    def authenticator(self) -> Auth:
        return ComeenQobenAuthenticator(
            client_id=self.config["client_id"],
            client_secret=self.config["client_secret"],
            auth_endpoint=self.config["auth_endpoint"],
        )

    @override
    def get_new_paginator(self) -> PageNumberPaginator:
        return ComeenQobenPaginator()

    @override
    def get_url_params(
        self,
        context: Context | None,
        next_page_token: t.Any | None,
    ) -> dict[str, t.Any]:
        """Return a dictionary of values to be used in URL parameterization.

        Args:
            context: The stream context.
            next_page_token: The next page index or value.

        Returns:
            A dictionary of URL query parameters.
        """
        params: dict = self.stream_params
        params["limit"] = self.page_size

        if next_page_token:
            return dict(parse_qsl(next_page_token.query))

        return params

    @override
    def parse_response(self, response: requests.Response) -> Iterable[dict]:
        yield from extract_jsonpath(
            self.records_jsonpath,
            input=response.json(parse_float=decimal.Decimal),
        )
