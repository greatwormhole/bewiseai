import uvicorn
from app.app import app
from app.conf import host, port

if __name__ == "__main__":
    uvicorn.run(
        app,
        host=host,
        port=port,
    )