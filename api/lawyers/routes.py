from ninja import Router

lawyer_router = Router()


@lawyer_router.get("/")
def get_lawyers(request):
    return {"message": "Get all lawyers"}
