import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


MONGODB_URI = os.environ.get("MONGODB_URI")
MONGODB_NAME = os.environ.get("MONGODB_NAME")

app = Flask(__name__)

app.config["MONGO_DBNAME"] = MONGODB_NAME
app.config["MONGO_URI"] = MONGODB_URI

mongo = PyMongo(app)


@app.route('/')
def get_index():
    return render_template('login.html')
    
@app.route("/login", methods=['POST'])
def do_login():
    username = request.form['username']
    return redirect(username)

@app.route("/<username>") 
def get_userpage(username):
    return render_template("index.html", username=username)

@app.route("/<username>/get_collections")
def get_collections(username):
     user_collections = load_collections_by_username(username)
     return render_template('collections.html', username=username, user_collections=user_collections)  

@app.route("/<username>/create_new_collection", methods=["POST"]) 
def create_collection(username):
    collection_name= request.form['collection_name']
    create_collection_for_user(username,collection_name)
    return redirect(username + "/get_collections")

@app.route("/<username>/delete_collection/<collection_id>", methods=["POST"])
def delete_collection(username, collection_id):
    mongo.db[username].remove({'_id': ObjectId(collection_id)})
    return redirect(username + "/get_collections") 

@app.route("/<username>/edit_collection/<collection_id>")
def edit_collection(username, collection_id):
    collection=mongo.db[username].find_one({'_id': ObjectId(collection_id)})
    return render_template('edit_collection.html', username=username, collection=collection)

@app.route("/<username>/update_collection/<collection_id>", methods=['POST'])
def update_collection(username, collection_id):
    mongo.db[username].update({"_id":ObjectId(collection_id)}, {"$set": {"name": request.form['collection_name']}})
    return redirect(username + "/get_collections")

@app.route("/<username>/update_collection/<collection_id>/<item_id>", methods=['POST'])
def update_collection_item_name(username, collection_id, item_id):
    updated_text = request.form[item_id]
    mongo.db[username].update({"_id":ObjectId(collection_id), "collection_items": {"$elemMatch": {"item_id": int(item_id)}}}, {"$set": {"collection_items.$.collection_item_name":updated_text}})

    return redirect(username + "/get_collections")
  
  
@app.route("/<username>/<collection_name>") 
def view_collection_by_user(username, collection_name):
    collection_items = load_collection_items_from_mongo(username, collection_name)
    return render_template("collection_items.html", username=username, collection_name=collection_name, collection_items=collection_items)

    
@app.route("/<username>/<collection_name>/add_item", methods=["POST"]) 
def add_item_to_collection(username, collection_name):
    print ("here")
    print (collection_name)
    collection_item= request.form['collection_item_name']
    max_id = get_max_id(username, collection_name)
    try: 
        int(max_id)
        new_id = max_id
    except ValueError:
        new_id = 1
    
    collection_item_details = {"collection_item_name": collection_item, "item_id": new_id }
    save_collection_items_to_mongo(username, collection_name, collection_item_details)
    return redirect(username + "/" + collection_name)

#---------------------------------------functions--------------------------------------
def get_max_id(username, collection_name):
        collection = mongo.db[username].find_one({"name": collection_name})
        # Here we want to loop through the collection and get the highest id already in use, then add One to it
        max_id = 0
        for each in collection['collection_items']:
            if each['item_id'] > max_id:
                max_id = each['item_id']
        max_id = max_id + 1
        return max_id

def create_collection_for_user(username, collection_name):
        mongo.db[username].insert({'name': collection_name, 'collection_items': [] })


def load_collections_by_username(username):
        return mongo.db[username].find()

def save_collection_items_to_mongo(username, collection_name, new_collection_item):
        selected_collection = mongo.db[username].find_one({'name':collection_name})
        selected_collection['collection_items'].append(new_collection_item)
        mongo.db[username].save(selected_collection)

def load_collection_items_from_mongo(username, collection_name):
        return mongo.db[username].find({'name':collection_name})

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), port=int(os.environ.get('PORT')), debug=True)