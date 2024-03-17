from apiflask import APIFlask, Schema, HTTPBasicAuth
from flask import request
from marshmallow import Schema, fields, validate, ValidationError
import typing as t
from werkzeug.security import generate_password_hash, check_password_hash
from pysondb import db

from apis.api_handler import query_demandado
from apis.api_handler import query_demandante

app = APIFlask(__name__)
auth = HTTPBasicAuth()
app.config['JSON_SORT_KEYS'] = False

users = {
    'userA': generate_password_hash('I_know_this_is_a_bad_practice'),
    'userB': generate_password_hash('So_I_Do'),
}


#Username/Password validation logic
@auth.verify_password
def verify_password(username: str, password: str) -> t.Union[str, None]:
    if (
        username in users
        and check_password_hash(users[username], password)
    ):
        return username
    return None


#Schema creation

            #Demandado
class queryDemandado(Schema):
    
    #define input field and validation
    documento = fields.String(required=True, validate=validate.Length(min=13,max=13))

class getResults(Schema):
    
    #define input field and validation
    documento = fields.String(required=True, validate=validate.Length(min=13,max=13))

@app.get('/consultarDemandado')
@app.auth_required(auth)
def queryByDocDemandado():

    documento = request.args.get("documento")
    
    #Load Schema
    schema = queryDemandado()

    #Set input data
    inputData = {"documento": documento}
    
    try:
        schema.load(inputData)
        print(f"consultando demandado {documento}")

        #Run query scripts
        causas_demandado = query_demandado(documento)
        return causas_demandado
    
    except ValidationError as error:
        return error.messages
    finally:
        pass


            #Demandante
class queryDemandante(Schema):
    #define input field and validation
    documento = fields.String(required=True, validate=validate.Length(min=13,max=13))


@app.get('/consultarDemandante')
@app.auth_required(auth)
def queryByDocDemandante():

    documento = request.args.get("documento")
    
    #Load Schema
    schema = queryDemandado()

    #Set input data
    inputData = {"documento": documento}
    
    try:
        schema.load(inputData)
        print(f"consultando demandante {documento}")

        #Run query scripts
        causas_demandante = query_demandante(documento)
        return causas_demandante
    
    except ValidationError as error:
        return error.messages
    finally:
        pass



class queryResults(Schema):
    
    #define input field and validation
    id = fields.Integer(required=True)


@app.get('/consultarResultados')
@app.auth_required(auth)
def queryByIdResults():

    id = request.args.get("id")
    
    #Load Schema
    schema = queryResults()

    #Set input data
    inputData = {"id": id}
    
    try:
        schema.load(inputData)
        print(f"consultando resultados {id}")

        #Run query scripts
        database = db.getDb('database.json')
        results = database.find(id)
        return results
    
    except ValidationError as error:
        return error.messages
    finally:
        pass