from flask import Flask,jsonify

app= Flask(__name__)

#Normally we would store this in Database

stores = [
    {
      'name' : 'My_First_Store',
      'item' : [
        {
          'name':'Shampoo',
          'price': 15.99
        }
      ]
    }
]

@app.route('/store',methods=['POST'])
def create_store():
  pass


@app.route('/store/<string:name>')
def get_store(name):
  return jsonify({'stores': stores['item']})

@app.route('/store')
def get_all_store():
  return jsonify({'stores': stores})

@app.route('/store/<string:name>/item',methods=['POST'])
def create_item_in_store(name):
  pass


@app.route('/store/<string:name>/item')
def get_item_in_store(name):
  pass


@app.route("/")
def hello():
  return "Hello World"

app.run(port=3000)