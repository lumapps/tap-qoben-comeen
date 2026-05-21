"""Comeen Qoben Authentication."""

from __future__ import annotations

import sys
import typing as t
import requests

from singer_sdk.authenticators import OAuthAuthenticator, SingletonMeta, requests
from singer_sdk.helpers._util import utc_now


if sys.version_info >= (3, 12):
    from typing import override
else:
    from typing_extensions import override

class ComeenQobenAuthenticator(OAuthAuthenticator, metaclass=SingletonMeta):
    """Authenticator for the Comeen Qoben API.

    Exchanges clientId + secret for a JWT bearer token.
    """

    @override
    @property
    def oauth_request_body(self) -> dict[str, t.Any]:
        return {
            "clientId": self.client_id,
            "secret": self.client_secret,
        }
    
    @override
    def update_access_token(self) -> None:
        """Update `access_token` along with: `last_refreshed` and `expires_in`.

        Raises:
            RuntimeError: When OAuth login fails.
        """
        self.logger.info("Requesting new access token")
        request_time = utc_now()
        auth_request_payload = self.oauth_request_payload
        token_response = self._session.post(
            self.auth_endpoint,
            headers=self._oauth_headers,
            data=auth_request_payload,
            timeout=60,
        )
        try:
            token_response.raise_for_status()
        except requests.HTTPError as ex:
            text, status_code = (
                (ex.response.text, ex.response.status_code)
                if ex.response is not None
                else ("Error", None)
            )
            self.handle_error(
                content=text,
                status_code=status_code,
            )
            msg = f"Failed to update access token (status={status_code or 'Unknown'})"
            raise RuntimeError(msg) from ex
        

        self.logger.debug("OAuth authorization attempt was successful")

        token_json = token_response.json()
        self.access_token = token_json["accessToken"] # Need to replace "access_token" with "accessToken" to work with Comeen Qoben API
        self.refresh_token = token_json["refreshToken"]
        expiration = token_json.get("expiresIn", self._default_expiration)
        self.expires_in = int(expiration) if expiration else None
        if self.expires_in is None:
            self.logger.debug(
                "No expires_in received in OAuth response and no "
                "default_expiration set. Token will be treated as if it never "
                "expires.",
            )
        self.last_refreshed = request_time

