# This file  contains the code covering the google login workflow

from authlib.integrations.flask_client import OAuth
import os


def google_func(app):
    oauth = OAuth(app)
    google = oauth.register(
        name="google",
        client_id=os.getenv("GOOGLE_CLIENT_ID"),
        client_secret=os.getenv("GOOGLE_CLIENT_SECRET"),
        authorize_url="https://accounts.google.com/o/oauth2/auth",
        authorize_params=None,
        access_token_url="https://oauth2.googleapis.com/token",
        access_token_params=None,
        refresh_token_url=None,
        jwks_uri="https://www.googleapis.com/oauth2/v3/certs",
        client_kwargs={"scope": "openid email profile"},
    )
    return google