import os
import json
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
    return render_template('edit_collection.html', username=username, collection=collection, collection_id=collection_id)

@app.route("/<username>/update_collection/<collection_id>", methods=['POST'])
def update_collection(username, collection_id):
    mongo.db[username].update({"_id":ObjectId(collection_id)}, {"$set": {"name": request.form['collection_name']}})
    return redirect(username + "/get_collections")

  
@app.route("/<username>/<collection_name>/<collection_id>") 
def view_collection_by_user(username, collection_name, collection_id):
    collection_items = load_collection_items_from_mongo(username, collection_id)
    return render_template("collection_items.html", username=username, collection_name=collection_name, collection_items=collection_items, collection_id=collection_id)


@app.route("/<username>/add_collection_item/<collection_name>/<collection_id>")
def add_collection_item(username, collection_name, collection_id):
    collection=mongo.db[username].find_one({'_id': ObjectId(collection_id)})
    return render_template('add_collection_item.html', username=username, collection_name=collection_name, collection=collection, collection_id=collection_id)    
    
@app.route("/<username>/<collection_name>/<collection_id>/add_item", methods=["POST"]) 
def add_item_to_collection(username, collection_name, collection_id):
    collection_item= request.form['collection_item_name']
    description = request.form['collection_item_description']
    item_bullet = request.form['bullet']
    future_log = request.form['future_log']
    due_date = request.form['due_date']
    max_id = get_max_id(username, collection_name, collection_id)
    try: 
        int(max_id)
        new_id = max_id
    except ValueError:
        new_id = 1
    collection_item_details = {"collection_item_name": collection_item, "description": description, "item_id": new_id, "item_bullet": item_bullet, "future_log":future_log, "due_date":due_date }
    save_collection_items_to_mongo(username, collection_name, collection_id, collection_item_details)
    return redirect(username + "/" + collection_name + "/" + collection_id)
    
    
@app.route("/<username>/edit_collection_item/<collection_name>/<collection_id>/<item_id>")
def edit_collection_item_name(username, collection_name, collection_id, item_id):
    collection=mongo.db[username].find_one({'_id': ObjectId(collection_id)})
    return render_template('edit_collection_item.html', username=username, collection_name=collection_name, collection=collection, collection_id=collection_id, item_id=item_id)

@app.route("/<username>/update_collection_item/<collection_name>/<collection_id>/<item_id>", methods=['POST'])
def update_collection_item_name(username, collection_name, collection_id, item_id):
    updated_text = request.form[item_id]
    print(updated_text)
    updated_description = request.form['collection_item_description']
    updated_bullet = request.form['item_bullet']
    updated_due_date = request.form['due_date']
    print(updated_bullet)
    updated_future_log = request.form['future_log']
    mongo.db[username].update({"_id":ObjectId(collection_id), "collection_items": {"$elemMatch": {"item_id": int(item_id)}}}, {"$set": {"collection_items.$.collection_item_name":updated_text}})
    mongo.db[username].update({"_id":ObjectId(collection_id), "collection_items": {"$elemMatch": {"item_id": int(item_id)}}}, {"$set": {"collection_items.$.description":updated_description}})
    mongo.db[username].update({"_id":ObjectId(collection_id), "collection_items": {"$elemMatch": {"item_id": int(item_id)}}}, {"$set": {"collection_items.$.item_bullet":updated_bullet}})
    mongo.db[username].update({"_id":ObjectId(collection_id), "collection_items": {"$elemMatch": {"item_id": int(item_id)}}}, {"$set": {"collection_items.$.due_date":updated_due_date}})
    mongo.db[username].update({"_id":ObjectId(collection_id), "collection_items": {"$elemMatch": {"item_id": int(item_id)}}}, {"$set": {"collection_items.$.future_log":updated_future_log}})
    collection_items = load_collection_items_from_mongo(username, collection_id)
    return render_template("collection_items.html", username=username, collection_name=collection_name, collection_items=collection_items, collection_id=collection_id)

@app.route("/<username>/collection_item_done/<collection_name>/<collection_id>/<item_id>", methods=['POST'])
def collection_item_done(username, collection_name, collection_id, item_id):
    mongo.db[username].update({"_id":ObjectId(collection_id), "collection_items": {"$elemMatch": {"item_id": int(item_id)}}}, {"$set": {"collection_items.$.status":"58"}})
    
    user_collections = load_collections_by_username(username)
    user_collections = list(user_collections)
    return render_template('future_log.html', username=username, user_collections=user_collections) 

@app.route("/<username>/collection_item_push/<collection_name>/<collection_id>/<item_id>", methods=['POST'])
def collection_item_push(username, collection_name, collection_id, item_id):
    
    updated_month = request.form['month']
    print(updated_month)
    print(item_id)
    mongo.db[username].update({"_id":ObjectId(collection_id), "collection_items": {"$elemMatch": {"item_id": int(item_id)}}}, {"$set": {"collection_items.$.future_log":updated_month}})
    
    user_collections = load_collections_by_username(username)
    user_collections = list(user_collections)
    return render_template('future_log.html', username=username, user_collections=user_collections) 



@app.route("/<username>/delete_collection_item/<collection_name>/<collection_id>/<item_id>", methods=['POST'])
def delete_collection_item_name(username, collection_name, collection_id, item_id):
    collection=mongo.db[username].find_one({'_id': ObjectId(collection_id)})
    deleted_id = request.form[item_id]
    mongo.db[username].update({"_id":ObjectId(collection_id)}, {"$pull":{"collection_items": {"item_id": int(deleted_id)}}})
    collection_items = load_collection_items_from_mongo(username, collection_id)
    return render_template("collection_items.html", username=username, collection=collection, collection_name=collection_name, collection_items=collection_items, collection_id=collection_id)
  

# Future Log

@app.route("/<username>/add_future_log", methods=["POST"]) 
def assign_item_to_future_log(username):
    future_month= request.form.get("month")
    both = request.form.get("futuremonthitem")
    words = both.split()
    collection_id = words[0]
    item_id = words[1]
    item = words[2]
    add_future_month_to_task(username, collection_id, future_month, item_id)
    user_collections = load_collections_by_username(username)
    user_collections = list(user_collections)
    return render_template('future_log.html', username=username, user_collections=user_collections)  


@app.route("/<username>/show_future_log")
def show_future_log(username):
     user_collections = load_collections_by_username(username)
     user_collections = list(user_collections)
     return render_template('future_log.html', username=username, user_collections=user_collections) 




#---------------------------------------functions--------------------------------------
def get_max_id(username, collection_name, collection_id):
        collection = mongo.db[username].find_one({"_id":ObjectId(collection_id)})
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

def save_collection_items_to_mongo(username, collection_name, collection_id, new_collection_item):
        selected_collection = mongo.db[username].find_one({"_id":ObjectId(collection_id)})
        selected_collection['collection_items'].append(new_collection_item)
        mongo.db[username].save(selected_collection)

def load_collection_items_from_mongo(username, collection_id):
        return mongo.db[username].find({"_id":ObjectId(collection_id)})
        
def add_future_month_to_task(username, collection_id, future_month, item_id):
       return mongo.db[username].update({"_id":ObjectId(collection_id), "collection_items": {"$elemMatch": {"item_id":int(item_id)}}}, {"$set": {"collection_items.$.future_log":future_month}})

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), port=int(os.environ.get('PORT')), debug=True)