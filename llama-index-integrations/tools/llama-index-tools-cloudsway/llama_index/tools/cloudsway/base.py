import os
import json
import asyncio
import urllib.request
import urllib.parse
from llama_index.core.tools.tool_spec.base import BaseToolSpec


class CloudswayToolSpec(BaseToolSpec):
    spec_functions = ["smartsearch"]

    def __init__(self, server_key: str = None):
        # Prefer explicit argument, fallback to environment variable
        self.server_key = server_key or os.getenv("CLOUDSWAY_SERVER_KEY")
        if not self.server_key:
            raise ValueError(
                "CLOUDSWAY_SERVER_KEY environment variable is not set and no key was provided."
            )

    async def smartsearch(
        self,
        query: str,
        count: int = 10,
        offset: int = 0,
        setLang: str = "en",
        safeSearch: str = "Strict",
    ) -> dict:
        """
        Performs a web search using the Cloudsway API.
        Returns a JSON object with the search results.
        """
        try:
            endpoint, api_key = self.server_key.split("-", 1)
        except ValueError:
            raise ValueError(
                "Invalid CLOUDSWAY_SERVER_KEY format. Expected 'endpoint-apikey'."
            )

        def sync_search():
            base_url = f"https://searchapi.xiaosuai.com/search/{endpoint}/smart"
            params = {
                "q": query,
                "count": count,
                "offset": offset,
                "mkt": setLang,
                "safeSearch": safeSearch,
            }
            url = f"{base_url}?{urllib.parse.urlencode(params)}"
            headers = {"Authorization": f"Bearer {api_key}"}
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=30) as response:
                if response.status != 200:
                    raise Exception(f"API Error: {response.status} {response.reason}")
                response_body = response.read()
                return json.loads(response_body)

        return await asyncio.to_thread(sync_search)
