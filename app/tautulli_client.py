import httpx

class TautulliClient:
    """
    Minimal Tautulli API client.

    API structure:
      http://IP:PORT[/HTTP_ROOT]/api/v2?apikey=...&cmd=...
    """
    def __init__(self, base_url: str, apikey: str, timeout: float = 30.0) -> None:
        self.base_url = base_url.rstrip("/")
        self.apikey = apikey
        self.timeout = timeout

    async def _get(self, cmd: str, **params):
        url = f"{self.base_url}/api/v2"
        q = {"apikey": self.apikey, "cmd": cmd}
        q.update({k: v for k, v in params.items() if v is not None})
        async with httpx.AsyncClient(timeout=self.timeout) as client:
            r = await client.get(url, params=q)
            r.raise_for_status()
            data = r.json()
        # Tautulli returns: {"response": {"result": "success", "data": ...}}
        resp = data.get("response", {})
        if resp.get("result") != "success":
            raise RuntimeError(f"Tautulli API error for cmd={cmd}: {resp.get('message')}")
        return resp.get("data")

    async def get_users(self):
        return await self._get("get_users")

    async def get_history(self, start: int = 0, length: int = 1000):
        # get_history supports paging with start/length
        return await self._get("get_history", start=start, length=length, order_dir="desc")