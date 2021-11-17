# App run file

from app import app

if __name__ == "main":
    # silence flask warning
    app.run(debug=True) # !! change this to false for production deployment !!
