import pymysql
import config
from app import app
from config import mysql
from flask import jsonify
from flask import flash, request

		
@app.route('/user', methods=['POST'])
def add_emp():
	try:
		_json = request.json
		_id = _json['id']
		_name = _json['name']
		_age =_json['age']
		_department = _json['department']
		_subject = _json['subject']
        
		if _id and _name and _age and _department and _subject and request.method == 'POST':			
			sqlQuery = "INSERT INTO user(id, name, age, department, subject) VALUES(%s, %s, %s, %s, %s)"
			bindData = (_id, _name, _age, _department, _subject)
			conn = mysql.connect()
			cursor = conn.cursor()
			cursor.execute(sqlQuery, bindData)
			conn.commit()
			respone = jsonify('User added successfully!')
			respone.status_code = 200
			return respone
		else:
			return not_found()
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()


@app.route('/user', methods=['GET'])
def emp1():
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)		
		cursor.execute("SELECT * FROM user")
		empRows = cursor.fetchall()
		respone = jsonify(empRows)
		respone.status_code = 200
		return respone
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

		
@app.route('/user/<int:id>', methods=['GET'])
def emp(id):
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT id, name, age, department, subject FROM user WHERE id =%s", (id,))
		empRow = cursor.fetchone()
		respone = jsonify(empRow)
		respone.status_code = 200
		return respone
	except Exception as e:
		print("User Not Exist")
	finally:
		cursor.close() 
		conn.close()


@app.route('/user/<int:id>', methods=['DELETE'])
def delete_emp(id):
	try:
		conn = mysql.connect()
		cursor = conn.cursor()
		cursor.execute("DELETE FROM user WHERE id =%s", (id,))
		conn.commit()
		respone = jsonify('User deleted successfully!')
		respone.status_code = 200
		return respone
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()


@app.route('/user/<int:id>', methods=['PUT'])
def update_emp(id):
	try:
		_json = request.json
		_id = _json['id']
		_name = _json['name']
		_age = _json['age']
		_department = _json['department']
		_subject = _json['subject']

		if _id and _name and _age and _department and _subject and request.method == 'PUT':
			sqlQuery = "UPDATE user SET name=%s, age=%s, department=%s, subject=%s WHERE id=%s"
			bindData = (_name, _age, _department, _subject, _id)
			conn = mysql.connect()
			cursor = conn.cursor()
			cursor.execute(sqlQuery, bindData)
			conn.commit()
			respone = jsonify('User updated successfully!')
			respone.status_code = 200
			return respone
		else:
			return not_found()	
	except Exception as e:
	 	print(e)
	finally:
	 	cursor.close() 
	 	conn.close()

		
@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Please Enter valid user id ',
    }
    respone = jsonify(message)
    respone.status_code = 404
    return respone

if __name__ == "__main__":
	app.run(host='0.0.0.0',port=8080,debug=True)

