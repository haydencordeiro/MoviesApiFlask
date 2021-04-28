from pymongo import MongoClient
import flask
import json
from flask import request
from flask import jsonify
client = MongoClient(
    "mongodb+srv://test:test@cluster0.vsegj.mongodb.net/<Cluster0>?retryWrites=true&w=majority")
db = client.get_database('dbname')#database name here
records = db.collname#table name here

print(records.count_documents({}))


def insertMovie(name, img, summary):
    new_movie = {
        'name': name,
        'img': img,
        'summary': summary
    }

    records.insert_one(new_movie)


def showMovies():
    return (list(records.find()))


app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET', 'POST'])
def getMovies():
    if request.method == 'GET':
        data = showMovies()
        return json.dumps(data, default=str)
    else:
        try:
            data = request.form.to_dict(flat=False)
            insertMovie(data['name'][0], data['img'][0], data['summary'][0])
            resp = jsonify(success=True)
            return resp
        except:
            resp = jsonify(success=True)
            return resp


app.run()
