 
class WebSocketMiddleware:
    def __init__(self, app):
        self.app = app

    async def __call__(self, scope ,receive, send):
        print(dict(scope["headers"]))
        print(dict(scope["headers"]).get(b"cookie").decode("utf-8"))
        return await self.app(scope, receive, send)