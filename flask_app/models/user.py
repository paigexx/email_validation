from flask_app.config.mysqlconnection import connectToMySQL
import re
from flask import flash

email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User: 
    def __init__(self, data):
        self.usernme = data["username"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
    
    @classmethod
    def get_users(cls):
        query = "SELECT * FROM users;"
        return connectToMySQL("email_validation").query_db(query)

    @classmethod
    def get_user(cls, data):
        query = "SELECT * FROM users WHERE users.id = %(user_id)s;"
        results =  connectToMySQL("email_validation").query_db(query, data)
        return results[0]
    
        
    @classmethod
    def create_user(cls, data):
        query = "INSERT INTO users (user_name, email, created_at, updated_at) VALUES (%(user_name)s, %(email)s, NOW(), NOW());"
        return connectToMySQL("email_validation").query_db(query, data)
        
    @classmethod 
    def delete_user(cls, data):
        query = "DELETE FROM users WHERE users.id = %(user_id)s"
        return connectToMySQL("email_validation").query_db(query, data)


    @staticmethod
    def validate_data(data):
        is_valid = True

        if not email_regex.match(data["email"]):
            flash("Please enter a valid email")
            is_valid = False
        if len(data["user_name"]) < 6:
            flash("Username must be betweeen 6-8 characters.")
            is_valid = False
        if data["user_name"][0] == " " or data["email"][0] == " ":
            flash("Please don't add a space before your username.")
            is_valid = False
        
            
        return is_valid
