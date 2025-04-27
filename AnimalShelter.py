#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 30 15:55:04 2025

@author: georgeyockach_snhu
"""

from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """CRUD operations fro Animal collection in MongoDB"""
    
    def __init__(self, user, passwd, host, port, database, collection):
        #MongoDB connection variables
        USER = user
        PASS = passwd
        HOST = host
        PORT = port
        DB = database
        COL = collection
        
        self.client = MongoClient(f'mongodb://{USER}:{PASS}@{HOST}:{PORT}/?authSource={DB}')
        self.database = self.client[DB]
        self.collection = self.database[COL]
        
    def create(self, data):
        if data:
            try:
                result = self.collection.insert_one(data)
                return result.acknowledged
            except Exception as e:
                print(f"Insert error: {e}")
                return False
        else:
            raise ValueError("No data provided to insert.")
                    
    def read(self, query):
            
            try:
                documents = list(self.collection.find(query))
                return documents
            except Exception as e:
                print(f"Read error: {e}")
                return[]
    
    def update(self, query, new_values):
        """Updates documents based on the provided query and new vlaues"""
        try:
            result = self.collection.update_many(query, {'$set' : new_values})
            return result.modified_count
        except Exception as e:
            print(f"Update error: {e}")
            return 0
        
    def delete(self, query):
        """Delete documents based on the provided query"""
        try:
            result = self.collection.delete_many(query)
            return result.deleted_count
        except Exception as e:
            print(f"Delete error: {e}")
            return 0
        