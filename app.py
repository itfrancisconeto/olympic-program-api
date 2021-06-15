from flask import Flask
from flask_cors import CORS
from urllib.request import urlopen
from bs4 import BeautifulSoup
import json
import os

app = Flask(__name__)

URL_TO_READ = "https://olympics.com/tokyo-2020/en/schedule"
cors = CORS(app, resource={r"/*":{"origins": "*"}})

def pegaModalidadesJSON():
    html = urlopen(URL_TO_READ)
    listTagResult = []
    bs = BeautifulSoup(html, 'lxml')
    for item in bs.find_all('img', alt=True):
        if ('(' or ')') in str(item):
            listTagResult.append(str(item.get('alt')))
    modalidadesJSON = json.dumps(listTagResult, ensure_ascii=False).encode('utf8')
    return modalidadesJSON


#def pegaDetalhesModalidadeJSON():
#https://olympics.com/tokyo-2020/en/schedule/badminton-schedule


@app.route("/modalidades", methods=["GET"])
def enviaModalidadesJSON():
    modalidadesJSON = pegaModalidadesJSON()
    return modalidadesJSON


""" @app.route("/modalidade", methods=["POST"])
def enviaDetalhesModalidadeJSON():
    body = request.get_json()
    endereco = body["modalidade"]+'-schedule'
    modalidadeJSON = pegaDetalhesModalidadeJSON(endereco)
    return modalidadeJSON
 """

def main():
     port = int(os.environ.get("PORT", 5000))
     app.run(host = "0.0.0.0", port = port)

if __name__ == "__main__":
    main()