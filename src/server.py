from app import app
from os import getenv

app.run(host=getenv("HOST"),
        port=getenv("PORT", 8080),
        debug=getenv("DEBUG", False))
