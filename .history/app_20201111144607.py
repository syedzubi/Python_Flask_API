from flask import Flask,jsonify,request

app= Flask(__name__)

#Normally we would store this in Database

stores = [
    {
      'name' : 'My First Store',
      'items' : [
        {
          'name':'Shampoo',
          'price': 15.99
        }
      ]
    }
]

@app.route('/store',methods=['POST'])
def create_store():
  request_data = request.get_json()
  new_store = {
    'name': request_data['name'],
    'items' : []
  }
  stores.append(new_store)
  return jsonify(new_store)


@app.route('/store/<string:name>')
def get_store(name):
  for store in stores:
    if store['name'] == name:
      return jsonify(store)
  return jsonify({"message":"store not found"})

@app.route('/store')
def get_all_store():
  return jsonify({'stores': stores})

@app.route('/store/<string:name>/item',methods=['POST'])
def create_item_in_store(name):
  pass


@app.route('/store/<string:name>/item')
def get_item_in_store(name):
  for store in stores:
    if store['name'] == name:
      return jsonify({"item" : store['items']})
  return jsonify({"Error":"item not found"})


@app.route("/")
def hello():
  return "Hello World"

app.run(port=3000)