from apiflask import APIFlask, Schema, abort
from apiflask.fields import Integer, String
from apiflask.validators import Length, OneOf
from flask import request
from marshmallow import Schema, fields, post_load, validates, validate, ValidationError
import os
import json


app = APIFlask(__name__)


            #Demandado
class queryDemandado(Schema):
    documento = fields.String(required=True)

@app.get('/consultarDemandado')
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
def queryByDocDemandante():

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