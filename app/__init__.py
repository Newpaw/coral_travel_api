from fastapi import FastAPI


def create_app() -> FastAPI:
    """
    Application factory function. This function creates and configures
    an instance of the FastAPI application.
    """

    app = FastAPI(
        title="Webhooks API",
        version="0.0.2",
        description="A FastAPI application"
    )

    from .routes import setup_routes
    setup_routes(app)

    return app
