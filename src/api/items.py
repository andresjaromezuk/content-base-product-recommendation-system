import sys
import os
project_root = os.path.abspath(os.path.join(os.getcwd(), '..'))
if project_root not in sys.path:
    sys.path.append(project_root)

from flask_restful import Resource
from flask import request, jsonify

import pandas as pd
import numpy as np

from src.services.database.vector_db_service import VectorDbService
from src.services.database.models import Item

vdbs = VectorDbService()
client = vdbs.client
client.cluster.health()

class ItemResource(Resource):
  def __init__(self) :
    self.db_service = ""

  
  def post(self,action=None):
    print(action)
    if action == 'recommendation':

      return self.item_recommendation()
  
  
  def item_recommendation(self):
    data = request.get_json() 
    item_to_search = data.get('item')
    vector = np.array(item_to_search)
    
    query = {
        "size": 5,
        "query": {
            "knn": {
            "text_vector": {
                "vector": vector,
                "k" : 10
            }
            }
        }
    }

    response = client.search(index='items', body=query)
          
    return response['hits']['hits']   

  # def all_embeddings(self):
  #   query_all = {
  #       "size": 1000,  # Definir el número de resultados que quieres obtener, si es muy grande puedes usar un scroll
  #       "query": {
  #       "match_all": {}
  #     }
  #   }
  #   response = client.search(index='movie', body=query_all)
  #   response_list = []
  #   for idx, h in enumerate(response['hits']['hits']):
  #     id= h['_source']['movie_id']
  #     print(h)
  #     movie = self.db_service.readOne(Movie, Movie.id == id)
  #     if movie:
  #         movie_dict= movie.__dict__
  #         response_list.append({
  #             'name':h['_source']['name'], 
  #             'vector': h['_source']['vector'],
  #             'year':movie_dict['release_date'], 
  #             'url':h['_source']['url'], 
  #             'genres':movie_dict['genres'],
  #             'ranking':idx +1
  #         })
  #   return response_list   