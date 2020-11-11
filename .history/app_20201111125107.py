from flask import Flask

app= Flask(__name__)

@app.route('/store',methods=['POST'])
def create_store():
  pass


@app.route('/store/<string:name>')
def get_store(name):
  pass

@app.route('/store')
def get_all_store():
  pass

@app.route('/store/<string:name>/item',methods=['POST'])
def create_specific_store(name):
  pass


@app.route('/store/<string:name>/item')
def get_item_in_store(name):
  pass


app.run(port=3000)