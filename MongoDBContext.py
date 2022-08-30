from pymongo import MongoClient


def connectToMongo(URI = 'mongodb://localhost:27017'):
    client = MongoClient(URI)
    return client

def insertOne(client, databaseName, collectionName, dataToInsert):
    db = client[databaseName]
    db[collectionName].insert_one(dataToInsert)

def insertMany(client, databaseName, collectionName, dataToInsert):
    db = client[databaseName]
    db[collectionName].insert_many(dataToInsert)

def updateOne(client, databaseName, collectionName, query, newValue):
    db = client[databaseName]
    db[collectionName].update_one(query, newValue)

def updateMany(client, databaseName, collectionName, query, newValues):
    db = client[databaseName]
    db[collectionName].update_many(query, newValues)

def deleteOne(client, databaseName, collectionName, query):
    db = client[databaseName]
    db[collectionName].delete_one(query)

def deleteMany(client, databaseName, collectionName, query):
    db = client[databaseName]
    return db[collectionName].delete_many(query)

def findOne(client, databaseName, collectionName):
    db = client[databaseName]
    return db[collectionName].find_one()

def findAll(client, databaseName, collectionName):
    db = client[databaseName]
    return db[collectionName].find()



