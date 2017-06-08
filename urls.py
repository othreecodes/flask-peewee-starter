from app import app
from views import *

app.add_url_rule(
    '/',view_func=index,methods=['GET']
)
