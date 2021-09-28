from aiohttp import web, ClientSession

URL = "http://builds.hello.io:8080/job/System/job/UnitTests/buildWithParameters?token=vdsoifvhjlzkjdhalidushclziudfhgovjashfkuzydglvzjhdvkjhsdgfkdrgfoisdufhuid"
HEADER = {
    'Content-Type':
    'application/json',
    'Authorization':
    'Basic YS5tb2xvZHRzb3ZAaGVsbG8uaW86MTE2NTQyZWE0MWQ4OWMxMzgyYzI1MjdkYmZhMmMzMGIwNg=='
}

routes = web.RouteTableDef()


@routes.get('/')
async def hello(request):
    return web.Response(text="No one likes you, hon!")


@routes.post('/')
async def post(request):
    await jenkins(URL, HEADER)
    return web.Response(text="POSTED\n")


async def jenkins(url, headers):
    async with ClientSession(headers=headers) as session:
        await session.post(url, data='')


def main():
    app = web.Application()
    app.add_routes(routes)
    web.run_app(app)


if __name__ == "__main__":
    main()
