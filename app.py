import json
from apiflask import APIFlask, Schema, HTTPBasicAuth, abort
from flask import request
from marshmallow import Schema, fields, validate, ValidationError
from flask import render_template
import typing as t
from werkzeug.security import generate_password_hash, check_password_hash
from pysondb import db
from json2html import *

from apis.api_handler import query_demandado
from apis.api_handler import query_demandante

app = APIFlask(__name__, docs_path=None)
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

@app.post('/consultarDemandado')
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


@app.post('/consultarDemandante')
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

class queryView(Schema):
    documento = fields.String(required=True, validate=validate.Length(min=13,max=13))
    tipo_consulta = fields.String(required=True, validate=validate.OneOf({'demandado','demandante'}))

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
        try:
            database = db.getDb('database.json')
            results = database.find(id)
            return results
        except:
            abort(404,message=f'Request was not found by ID')
    
    except ValidationError as error:
        return error.messages
    finally:
        pass


@app.route('/apiDoc')
def docsView():
    return render_template('docs.html')

@app.route('/verResultados')
def resultsView():

    documento = request.args.get("documento")
    tipo_consulta = request.args.get("tipo_consulta")

    #Load Schema
    schema = queryView()

    #Set input data
    inputData = {"documento":documento,"tipo_consulta":tipo_consulta}
    try:
        schema.load(inputData)
        #Run query scripts
        try:

            
            if tipo_consulta == 'demandado':
                result = query_demandado(documento)
            else:
                result = query_demandante(documento)
  
            fecha_de_consulta = result['fecha_de_consulta']
            id = result['id']

            causas = result['causas']
            num_registros=len(causas)
            table = json2html.convert(json = json.dumps(causas))
            return render_template(template_name_or_list='/resultados.html',
                                   table=table,tipo_consulta=tipo_consulta,documento=documento,fecha_de_consulta=fecha_de_consulta,id=id,num_registros=num_registros)
            
        except Exception as e:
            print(f'Error rendering view: {e}')
            abort(404,message=f'Request was not found by ID')
    except ValidationError as error:
        return error.messages
    finally:
        pass