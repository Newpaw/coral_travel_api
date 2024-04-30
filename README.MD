FastAPI Webhook Handler for Mluvii API
======================================

Overview
--------

This application serves as an intermediary to handle webhooks, fetch data from the Mluvii API, and forward that data to a specified destination URL. It authenticates, retrieves session data from Mluvii, and forwards the data as JSON.

Requirements
------------

-   Python 3.10+
-   FastAPI
-   HTTPX
-   asyncio

Setup
-----

1.  Clone the repository.

2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3.  Set up environment variables by creating a `.env` file with the following structure:

    ```bash
    API_USERNAME=<your_api_username>
    API_PASSWORD=<your_api_password>
    AUTH_URL=<your_auth_url>
    SESSIONS_URL=<your_sessions_url>
    DESTINATION_URL=<your_destination_url>
    ACCESS_TOKEN_EXPIRY=<token_expiry_time_in_seconds>
    LOG_LEVEL=<desired_log_level>`
    ```

Running the Application
-----------------------

Use Docker to build and run the application:

```bash
docker build -t fastapi-webhook-handler .
docker run -p 8000:8000 fastapi-webhook-handler`
```
Usage
-----

1.  Register the Webhook:

    -   Register a webhook in Mluvii for the "SessionEnded" event for the relevant company. This webhook will trigger notifications to your FastAPI application when a session ends.
2.  Receive JSON Payload:

    -   Your application will receive a JSON payload at the `/webhook/` endpoint whenever the registered session ends. This payload includes the `sessionID`.
3.  Process and Forward Session Data:

    -   The application parses the received JSON to extract the `sessionID`.
    -   It then authenticates and queries the Mluvii API using the URL pattern defined in `SESSIONS_URL` to fetch all details about the session.
    -   Finally, the complete session data retrieved from the Mluvii API is forwarded as JSON to the destination URL defined in `DESTINATION_URL` in the `.env` file.

This setup ensures that each time a session ends, all relevant data is automatically fetched and passed on to another system or service for further processing or analysis.

Docker
------

The Dockerfile is set up to use Python 3.10, install dependencies, expose port 8000, and start the FastAPI application using Gunicorn with Uvicorn workers.

Notes
-----

-   Ensure all necessary environment variables are set in your `.env` file.
-   The application logs all significant events, aiding in debugging and monitoring.