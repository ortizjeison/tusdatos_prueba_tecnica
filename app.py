from apiflask import APIFlask, Schema, abort, HTTPBasicAuth
from apiflask.fields import Integer, String
from apiflask.validators import Length, OneOf
from flask import request
from marshmallow import Schema, fields, post_load, validates, validate, ValidationError
import os
import json
import typing as t
from werkzeug.security import generate_password_hash, check_password_hash


app = APIFlask(__name__)
auth = HTTPBasicAuth()

users = {
    'userA': generate_password_hash('I_know_this_is_a_bad_practice'),
    'userB': generate_password_hash('So_I_Do'),
}



@auth.verify_password
def verify_password(username: str, password: str) -> t.Union[str, None]:
    if (
        username in users
        and check_password_hash(users[username], password)
    ):
        return username
    return None


            #Demandado
class queryDemandado(Schema):
    documento = fields.String(required=True)

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
        return f"consultando demandado {documento}"

        #Run query scripts
    
    except ValidationError as error:
        return error.messages
    finally:
        pass


            #Demandante
class queryDemandante(Schema):
    documento = fields.String(required=True)


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
        return f"consultando demandante {documento}"

        #Run query scripts
    
    except ValidationError as error:
        return error.messages
    finally:
        pass