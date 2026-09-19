from dotenv import load_dotenv
import os
from flask_cors import CORS

# FORCE python to read the .env file BEFORE doing anything else
load_dotenv()

from app import create_app

app = create_app()

if name == 'main':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
