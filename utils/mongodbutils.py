from pymongo import MongoClient
from pymongo import errors
import pymongo
import datetime


def connect_to_db(dbserver, dbpassword, dbname, dbport=27017, dbuser="admin"):
    """
    :param dbserver: ip of mongodb server
    :param dbport:  port which mongod is running
    :param dbuser:  user to connect to mongod with
    :param dbpassword: password
    :param dbname:  database name to connect to
    :return:  a connection to mongodb
    """
    try:
        dbuser='admin'
        client = MongoClient(dbserver, int(dbport))
        database = client[dbname]
        database.authenticate(dbuser, dbpassword, source='admin')
        return database
    except Exception as e:
        print("Could not connect to MongoDB: ", e)
        assert False,"Could not connect to MongoDB"


def findone(dbconnection, collection, query):
    """
    :param dbconnection:
    :param collection:
    :param query:
    :return: Returns a single document, or None if no matching document is found.
    (as returned by find_one())
    """
    try:
        mycol = dbconnection[collection]
        return mycol.find_one(query)
    except Exception as e:
        print (type(e), e)


def find(dbconnection, collection, query):
    """
    :param dbconnection:
    :param collection:
    :param query:
    :return: Query the database.
    (filter=None, projection=None, skip=0, limit=0, no_cursor_timeout=False,
    cursor_type=CursorType.NON_TAILABLE, sort=None, allow_partial_results=False,
    oplog_replay=False, modifiers=None, manipulate=True)
    """
    try:
        mycol = dbconnection[collection]
        return mycol.find(query)
    except Exception as e:
        print (type(e), e)


def index_cursor_for_collection(dbconnection, collection):
    """
    :param dbconnection:
    :param collection:
    :return: return a cursor of connections for dbconnection, collection
    """
    try:
        mycol = dbconnection[collection]
        return mycol.list_indexes()
    except Exception as e:
        print (type(e), e)


def indexes_for_collection(dbconnection, collection):
    """
    :param dbconnection:
    :param collection:
    :return: Returns a dictionary where the keys are index names
    (as returned by create_index()) and the values are dictionaries containing information about each index
    """
    try:
        mycol = dbconnection[collection]
        return mycol.index_information()
    except Exception as e:
        print (type(e), e)


def list_collections(dbconnection):
    """
    :param dbconnection:
    :return: return a list of collections for dbconnection
    include_system_collections (optional): if False list will not include system collections (e.g system.indexes)
    """
    try:
        return dbconnection.collection_names(False)
    except Exception as e:
        print (type(e), e)


def list_databases(dbconnection):
    """
    :param dbconnection:
    :return: return a list of databases for dbconnection, must be run against admin database as an admin user
    """
    try:
        db_list = []
        db_names = dbconnection.command('listDatabases')
        for database in db_names['databases']:
            db_list.append(database['name'])
        return db_list
    except Exception as e:
        print (type(e), e)
