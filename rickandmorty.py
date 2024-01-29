from flask import Flask
from flask_restful import Api, Resource
import requests

app = Flask(__name__)
api = Api(app)

class RickResponse(Resource):
    def get(self, page_number):
        url = f"https://rickandmortyapi.com/api/character/{page_number}"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                return {'data': data}, 200
            else:
                return {'message': 'Veri alınamadi', 'status_code': response.status_code}, 404
        except Exception as e:
            return {'message': 'Bir hata oluştu', 'error': str(e)}, 500

# Add URL endpoints
api.add_resource(RickResponse, '/character/<int:page_number>')  # <int:page_number> ile bir sayı beklediğimizi belirtiyoruz

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
