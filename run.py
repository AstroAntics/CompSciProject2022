# App run file

from app import app
from waitress import serve

if __name__ == "main":
    # silence flask warning
    # serve(app, host='0.0.0.0', port=5000)
    app.run(debug=True) # !! change this to false for production deployment !!
