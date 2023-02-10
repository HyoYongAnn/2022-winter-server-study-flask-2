from flask import Flask, request
from flask_restx import Resource, Namespace
from database.database import Database

user = Namespace('user')
database = Database()

@user.route('')
class UserManagement(Resource):
    def get(self):
        # GET method 구현 부분
        return {'name' : 'hello world'}

    def post(self):
        # POST method 구현 부분
        #유저생성
        params = request.get_json()
        id = params['id']
        password = params['password']
        nickname = params['nickname']
        
        database.execute("INSERT INTO 'Hyoyong'.'user'")
        database.execute("VALUES ("+id+","+password+","+nickname+");")
        database.commit()
        
        return {"is_success" : True, "message" : "유저 생성 성공"}

    def put(self):
        # PUT method 구현 부분

        return {}
    
    def delete(self):
        # DELETE method 구현 부분
        return {}