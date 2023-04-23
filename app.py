from WebApp.app import create_app
from WebApp.app.core import core
import os

app = create_app()
app.register_blueprint(core)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
