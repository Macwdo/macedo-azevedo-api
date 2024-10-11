from ninja import NinjaAPI

from api.lawyers.routes import lawyer_router

api = NinjaAPI()

api.add_router("lawyers", lawyer_router)
