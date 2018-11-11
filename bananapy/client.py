import aiohttp 
from box import Box

class Error(Exception):
    """
    Error that is caused when the client returns a status code other than 200 (success).
    """
    pass


class Client:
    """
    Main Client of BananAPI.

    Params:
    token (str): The BananAPI token.
    """
    def __init__(self, token, session=None):
        self.session = session or aiohttp.ClientSession()
        self.token = token
        self.base_url = "https://bananapi.ml/api/"

    async def _get(self, endpoint, params):
        """
        Private function to request from the API.

        This should not be called directly.
        """
        headers = { "Authorization": self.token }
        res = await self.session.get(self.base_url + endpoint, headers=headers, params=params)
        msg = ""
        if res.status != 200:
            try:
                resp = await res.json()
                msg = resp.get("message", "No message found.")
            except:
                msg = await res.text()
            raise Error("{}: {}".format(res.status, resp))
        else:
            return res
        
    async def abandon(self, text):
        res = await self._get("abandon", { "text": text })
        res = await res.read()
        return res
        



