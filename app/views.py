from app import app
from flask_restful import Api
from utilities.const import prefix_api
from resources.session import Session, SessionNew
from resources.users import Users, UsersPassword
from resources.pages import App, Account
from resources.account import AccountPassword
from resources.company import AllCompany, Company


api = Api(app)

#API:
api.add_resource(Session, f'/{prefix_api}/session')
api.add_resource(SessionNew, f'/{prefix_api}/session/new')
api.add_resource(Users, f'/{prefix_api}/users')
api.add_resource(UsersPassword, f'/{prefix_api}/users/password')
api.add_resource(
    AccountPassword,
    f'/{prefix_api}/users/<int:user_id>/account/password'
)
api.add_resource(AllCompany, f'/{prefix_api}/company')
api.add_resource(Company, f'/{prefix_api}/company/<int:company_id>')

#PAGES:
api.add_resource(App, '/app')
api.add_resource(Account, '/app/account')
