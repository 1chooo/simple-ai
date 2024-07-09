from fastapi import APIRouter, status

mock_routes = APIRouter(tags=["mock"], prefix="/mock")

@mock_routes.get("/health", status_code=status.HTTP_200_OK)
async def health_check():
    return {"status": "ok"}

@mock_routes.get("/ping", status_code=status.HTTP_200_OK)
async def ping():
    return {"message": "pong"}

@mock_routes.get("/echo", status_code=status.HTTP_200_OK)
async def echo(message: str):
    return {"message": message}
