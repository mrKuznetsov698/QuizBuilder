import tornado.web
import tornado.ioloop
from ModelsUI import *


class LibraryRender(tornado.web.RequestHandler):
    def get(self):
        self.render('templates/index.html', library=get_all_info())


def create_app() -> tornado.web.Application:
    return tornado.web.Application([
        (r"/", LibraryRender),
        (r"/static/(.*)", tornado.web.StaticFileHandler, {'path': 'static'})
    ])


if __name__ == '__main__':
    app = create_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
