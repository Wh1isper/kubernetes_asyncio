# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1.27.6
    Generated by: https://openapi-generator.tech
"""


import io
import json
import logging
import re
import ssl

import aiohttp
# python 2 and python 3 compatibility library
from six.moves.urllib.parse import urlencode

from kubernetes_asyncio.client.exceptions import ApiException, ApiValueError

logger = logging.getLogger(__name__)


class RESTResponse(io.IOBase):

    def __init__(self, resp, data):
        self.aiohttp_response = resp
        self.status = resp.status
        self.reason = resp.reason
        self.data = data

    def getheaders(self):
        """Returns a CIMultiDictProxy of the response headers."""
        return self.aiohttp_response.headers

    def getheader(self, name, default=None):
        """Returns a given response header."""
        return self.aiohttp_response.headers.get(name, default)


class RESTClientObject(object):

    def __init__(self, configuration, pools_size=4, maxsize=None):

        # maxsize is number of requests to host that are allowed in parallel
        if maxsize is None:
            maxsize = configuration.connection_pool_maxsize

        ssl_context = ssl.create_default_context(cafile=configuration.ssl_ca_cert)
        if configuration.cert_file:
            ssl_context.load_cert_chain(
                configuration.cert_file, keyfile=configuration.key_file
            )

        if not configuration.verify_ssl:
            ssl_context.check_hostname = False
            ssl_context.verify_mode = ssl.CERT_NONE

        connector = aiohttp.TCPConnector(
            limit=maxsize,
            ssl=ssl_context
        )

        self.proxy = configuration.proxy
        self.proxy_headers = configuration.proxy_headers

        # https pool manager
        self.pool_manager = aiohttp.ClientSession(
            connector=connector,
            trust_env=True,
            # Watch events containing large resource objects can exceed
            # aiohttp's default read buffer size.
            #
            # There is no hard-limit defined by k8s, but the etcd default
            # maximum request size is 1.5MiB.
            # https://github.com/kubernetes/kubernetes/issues/19781
            read_bufsize=2**21
        )

    async def close(self):
        await self.pool_manager.close()

    async def request(self, method, url, query_params=None, headers=None,
                      body=None, post_params=None, _preload_content=True,
                      _request_timeout=None):
        """Execute request

        :param method: http request method
        :param url: http request url
        :param query_params: query parameters in the url
        :param headers: http request headers
        :param body: request json body, for `application/json`
        :param post_params: request post parameters,
                            `application/x-www-form-urlencoded`
                            and `multipart/form-data`
        :param _preload_content: this is a non-applicable field for
                                 the AiohttpClient.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        """
        method = method.upper()
        assert method in ['GET', 'HEAD', 'DELETE', 'POST', 'PUT',
                          'PATCH', 'OPTIONS']

        if post_params and body:
            raise ApiValueError(
                "body parameter cannot be used with post_params parameter."
            )

        post_params = post_params or {}
        headers = headers or {}
        timeout = _request_timeout or 5 * 60

        if 'Content-Type' not in headers:
            headers['Content-Type'] = 'application/json'

        args = {
            "method": method,
            "url": url,
            "timeout": timeout,
            "headers": headers
        }

        if self.proxy:
            args["proxy"] = self.proxy
        if self.proxy_headers:
            args["proxy_headers"] = self.proxy_headers

        if query_params:
            args["url"] += '?' + urlencode(query_params)

        # For `POST`, `PUT`, `PATCH`, `OPTIONS`, `DELETE`
        if method in ['POST', 'PUT', 'PATCH', 'OPTIONS', 'DELETE']:
            if (
                re.search("json", headers["Content-Type"], re.IGNORECASE)
                or headers["Content-Type"] == "application/apply-patch+yaml"
            ):
                if headers['Content-Type'] == 'application/json-patch+json':
                    if not isinstance(body, list):
                        headers['Content-Type'] = 'application/strategic-merge-patch+json'
                if body is not None:
                    body = json.dumps(body)
                args["data"] = body
            elif headers['Content-Type'] == 'application/x-www-form-urlencoded':  # noqa: E501
                args["data"] = aiohttp.FormData(post_params)
            elif headers['Content-Type'] == 'multipart/form-data':
                # must del headers['Content-Type'], or the correct
                # Content-Type which generated by aiohttp
                del headers['Content-Type']
                data = aiohttp.FormData()
                for param in post_params:
                    k, v = param
                    if isinstance(v, tuple) and len(v) == 3:
                        data.add_field(k,
                                       value=v[1],
                                       filename=v[0],
                                       content_type=v[2])
                    else:
                        data.add_field(k, v)
                args["data"] = data

            # Pass a `bytes` parameter directly in the body to support
            # other content types than Json when `body` argument is provided
            # in serialized form
            elif isinstance(body, bytes):
                args["data"] = body
            else:
                # Cannot generate the request from given parameters
                msg = """Cannot prepare a request message for provided
                         arguments. Please check that your arguments match
                         declared content type."""
                raise ApiException(status=0, reason=msg)

        r = await self.pool_manager.request(**args)
        if _preload_content:

            data = await r.read()
            r = RESTResponse(r, data)

            # log response body
            logger.debug("response body: %s", r.data)

            if not 200 <= r.status <= 299:
                raise ApiException(http_resp=r)

        return r

    async def GET(self, url, headers=None, query_params=None,
                  _preload_content=True, _request_timeout=None):
        return (await self.request("GET", url,
                                   headers=headers,
                                   _preload_content=_preload_content,
                                   _request_timeout=_request_timeout,
                                   query_params=query_params))

    async def HEAD(self, url, headers=None, query_params=None,
                   _preload_content=True, _request_timeout=None):
        return (await self.request("HEAD", url,
                                   headers=headers,
                                   _preload_content=_preload_content,
                                   _request_timeout=_request_timeout,
                                   query_params=query_params))

    async def OPTIONS(self, url, headers=None, query_params=None,
                      post_params=None, body=None, _preload_content=True,
                      _request_timeout=None):
        return (await self.request("OPTIONS", url,
                                   headers=headers,
                                   query_params=query_params,
                                   post_params=post_params,
                                   _preload_content=_preload_content,
                                   _request_timeout=_request_timeout,
                                   body=body))

    async def DELETE(self, url, headers=None, query_params=None, body=None,
                     _preload_content=True, _request_timeout=None):
        return (await self.request("DELETE", url,
                                   headers=headers,
                                   query_params=query_params,
                                   _preload_content=_preload_content,
                                   _request_timeout=_request_timeout,
                                   body=body))

    async def POST(self, url, headers=None, query_params=None,
                   post_params=None, body=None, _preload_content=True,
                   _request_timeout=None):
        return (await self.request("POST", url,
                                   headers=headers,
                                   query_params=query_params,
                                   post_params=post_params,
                                   _preload_content=_preload_content,
                                   _request_timeout=_request_timeout,
                                   body=body))

    async def PUT(self, url, headers=None, query_params=None, post_params=None,
                  body=None, _preload_content=True, _request_timeout=None):
        return (await self.request("PUT", url,
                                   headers=headers,
                                   query_params=query_params,
                                   post_params=post_params,
                                   _preload_content=_preload_content,
                                   _request_timeout=_request_timeout,
                                   body=body))

    async def PATCH(self, url, headers=None, query_params=None,
                    post_params=None, body=None, _preload_content=True,
                    _request_timeout=None):
        return (await self.request("PATCH", url,
                                   headers=headers,
                                   query_params=query_params,
                                   post_params=post_params,
                                   _preload_content=_preload_content,
                                   _request_timeout=_request_timeout,
                                   body=body))
