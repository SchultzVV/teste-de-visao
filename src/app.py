from flask import Flask, request, jsonify
from src import remove_salt_and_pepper, find_silo

app = Flask(__name__)

# Questão 1 - Rota para remoção parcial de ruído
@app.route('/questao1', methods=['POST'])
def questao1():
    image = request.files['image']
    # lógica para remover o ruído da imagem
    result_image = remove_salt_and_pepper(image)

    return jsonify({"result": result_image})

# Questão 2a - Rota para seleção de pixels associados ao objeto silo
@app.route('/questao2a', methods=['POST'])
def questao2a():
    # Receba a imagem RGB no corpo da requisição (exemplo: form-data com uma imagem)
    image = request.files['image']
    find_silo(image)
    # Implemente a lógica para selecionar os pixels do objeto silo

    # Substitua esta parte pelo seu código

    # Retorne os pixels associados ao objeto silo como resposta
    return jsonify({"result": "Conjunto de pixels do objeto silo"})

# Questão 2b - Rota para segmentação da vegetação nas imagens
@app.route('/questao2b', methods=['POST'])
def questao2b():
    # Receba a imagem com 8 canais espectrais no corpo da requisição (exemplo: form-data com uma imagem)
    image = request.files['image']

    # Implemente a lógica para segmentar a vegetação na imagem
    # Substitua esta parte pelo seu código

    # Retorne a imagem segmentada como resposta
    return jsonify({"result": "Imagem segmentada da vegetação"})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
