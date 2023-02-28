from project import app,db
import os

with app.app_context():
    db.create_all()

if __name__=='__main__':
    app.run(debug=True,host="0.0.0.0",port=int(os.envion.get("PORT",8080)))