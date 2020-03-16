#!/usr/bin/env python3
import flask
from flask import make_response
from flask import request
import sqlite3
import simplejson
#from sshtunnel import SSHTunnelForwarder

app = flask.Flask(__name__)
#CORS(app)
@app.route("/getData")
def getData():

    query = request.args.get('orderedBy')
    print("query--",query)
    conn = sqlite3.connect('gsoc.db')
    print("Opened database successfully")
    sqlQuery="SELECT * from bioinformatics"
    if query!=None and len(query)!=0:
        if(query=="count"):
            sqlQuery=sqlQuery+" ORDER BY ViewCount DESC;"
        elif query=="score":
            sqlQuery=sqlQuery+" ORDER BY Score DESC;"
    print("sqlQuery *************"+sqlQuery)
    cursor = conn.execute(sqlQuery)
    allDict = []

    for row in cursor:
        #print("ID = ", row[5])
        d = {
            'Id': row[0],
	        'PostTypeId':	row[1],
	        'AcceptedAnswerId':	row[2],
	        'ParentId':	row[3],
	        'CreationDate':	row[4],
	        'Score':	row[5],
	        'ViewCount':	row[6],
	        'Body':	row[7],
	        'OwnerUserId':	row[8],
	        'OwnerDisplayName':	row[9],
	        'LastEditorUserId':	row[10],
	        'LastEditDate': row[11],
	        'LastActivityDate':	row[12],
	        'Title':	row[13],
	        'Tags':	row[14],
	        'AnswerCount':	row[15],
	        'CommentCount':	row[16],
	        'ClosedDate':	row[17],
	        'FavoriteCount':	row[18]}
        allDict.append(d)
    res=simplejson.dumps(allDict)
    #print(res)
    
    response = make_response(res)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route("/searchData")
def searchData():
    query = request.args.get('searchBy')
    print("query--",query)
    conn = sqlite3.connect('gsoc.db')
    sqlQuery="SELECT * from bioinformatics"
    if query!=None and len(query)!=0:
        query="'%"+query+"%'"
        sqlQuery=sqlQuery +" where Body like "+query+" or Title like "+query+";"
    print("sqlQuery *************"+sqlQuery)
    cursor = conn.execute(sqlQuery)
    allDict = []

    for row in cursor:
        #print("ID = ", row[5])
        d = {
            'Id': row[0],
	        'PostTypeId':	row[1],
	        'AcceptedAnswerId':	row[2],
	        'ParentId':	row[3],
	        'CreationDate':	row[4],
	        'Score':	row[5],
	        'ViewCount':	row[6],
	        'Body':	row[7],
	        'OwnerUserId':	row[8],
	        'OwnerDisplayName':	row[9],
	        'LastEditorUserId':	row[10],
	        'LastEditDate': row[11],
	        'LastActivityDate':	row[12],
	        'Title':	row[13],
	        'Tags':	row[14],
	        'AnswerCount':	row[15],
	        'CommentCount':	row[16],
	        'ClosedDate':	row[17],
	        'FavoriteCount':	row[18]}
        allDict.append(d)
    res=simplejson.dumps(allDict)
    #print(res)
    
    response = make_response(res)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


#####################################################################################################################
if __name__ == '__main__':

    app.run(debug=True)