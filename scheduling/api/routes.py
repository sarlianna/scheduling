from flask.views import MethodView
from scheduling import app


class UserAPI(MethodView):

    def get(self):
        pass

    def post(self):
        pass

app.add_url_rule('/api/users', view_func=UserAPI.as_view('users'))
