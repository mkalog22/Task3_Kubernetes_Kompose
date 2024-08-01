from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)

def get_data_from_mongodb():
    client = MongoClient("mongodb://mongo:27017/")
    db = client["testdb"]
    collection = db["testcollection"]
    data = collection.find()
    return [item["value"] for item in data]

@app.route('/')
def index():
    data = get_data_from_mongodb()
    total_sum = sum(data)
    return jsonify({"sum": total_sum})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
from pymongo import MongoClient

def get_data_from_mongodb():
    client = MongoClient("mongodb://mongo:27017/")
    db = client["testdb"]
    collection = db["testcollection"]
    data = collection.find()
    return [item["value"] for item in data]

def main():
    data = get_data_from_mongodb()
    total_sum = sum(data)
    print(f"The sum of the data is: {total_sum}")

if __name__ == "__main__":
    main()
