from flask import Flask, render_template, request
from pymongo import MongoClient
from pprint import pprint
app = Flask(__name__)
client = MongoClient()
db=client.restaurantsDB
storage = db.restaurants
data={}
@app.route('/',methods = [ 'GET'])
def fulllist():
      print("Into full list===========")
      global data
      tl=[' restaurant_id  ','  name  ','  cuisine  ',' borough  ']
      global db
      coll1 = db.restaurants #selecting the coll1 in myDatabase
      mod_dict={}
      for document in coll1.find({},{"name":1,"restaurant_id":1,"borough":1,"cuisine":1,"_id":0}):
            print('database',document)
            # print("split",document['restaurant_id'])
            dict1={
                  
                  'restaurant_id':document['restaurant_id'],
                  'name':document['name'],
                  'cuisine':document['cuisine'],
                  "borough":document['borough'],
                  
            }
            mod_dict[document['name']]=dict1
      return render_template('print.html',dict=mod_dict,headings=tl)
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)