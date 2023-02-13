from flask import Flask, request, make_response, jsonify
from flask_restx import Resource, Namespace
from database.database import Database

user = Namespace('user')


@user.route('')
class UserManagement(Resource):
    def get(self):
        database = Database()
        id = request.args.get('id')
        password = request.args.get('password')
        newSQL = "SELECT * FROM Hyoyong.user WHERE id = '" + id + "';"
        data = database.execute_one(newSQL)
        database.commit()
        if data is None:
            return make_response(jsonify({"messege": "해당 유저가 존재하지 않음"}),400)
        if data['pw'] != password:
            return make_response(jsonify({"messege": "아이디나 비밀번호 불일치"}),400)




        database.close()
        return {"nickname" : data['nickname']}

    def post(self):
        # POST method 구현 부분
        #유저생성
        database = Database()
        params = request.get_json()
        id = params['id']
        password = params['password']
        nickname = params['nickname']
        data = database.execute_one("SELECT * FROM Hyoyong.user WHERE id = '" + id +"';")
        if data is not None:
            return make_response(jsonify({"is_success" : False, "messege": "이미 있는 유저"}),400)
        newSQL = "INSERT INTO Hyoyong.user VALUES ('" + id + "','" + password + "','" + nickname +"');"
        database.execute(newSQL)
        database.commit()
        
        database.close()

        return {"is_success" : True, "message" : "유저 생성 성공"}

    def put(self):
        # PUT method 구현 부분
        database = Database()
        params = request.get_json()
        id = params['id']
        password = params['password']
        nickname = params['nickname']
        data = database.execute_one("SELECT * FROM Hyoyong.user WHERE id = '" + id +"' AND pw = '" + password + "';")
        if data is None:
            return make_response(jsonify({"is_success" : False,"messege": "아이디나 비밀번호 불일치"}),400)
        if data['nickname'] == nickname:
            return make_response(jsonify({"is_success" : False,"messege": "현재 닉네임과 같음"}),400)
        newSQL = "UPDATE Hyoyong.user SET nickname = '" + nickname + "' WHERE id = '" + id + "' AND pw = '" + password + "'"
        database.execute(newSQL)
        database.commit()

        database.close()
        return {"is_success" : True, "message" : "유저 닉네임 변경 성공"}
    
    def delete(self):
        # DELETE method 구현 부분
        database = Database()
        params = request.get_json()
        id = params['id']
        password = params['password']
        data = database.execute_one("SELECT * FROM Hyoyong.user WHERE id = '" + id +"' AND pw = '" + password + "';")
        if data is None:
            return make_response(jsonify({"is_success" : False,"messege": "아이디나 비밀번호 불일치"}),400)
        newSQL = "DELETE FROM Hyoyong.user WHERE id = '" + id +"' AND pw = '" + password + "';"
        database.execute(newSQL)
        database.commit()
        
        database.close()
        return {"is_success" : True, "message" : "유저 삭제 성공"}