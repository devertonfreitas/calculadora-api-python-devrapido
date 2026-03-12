from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/calcular', methods=['POST'])
def calcular():

    dados = request.get_json()

    a = dados.get("a")
    b = dados.get("b")
    operacao = dados.get("operacao")

    if operacao == "soma":
        resultado = a + b
    elif operacao == "subtracao":
        resultado = a - b
    elif operacao == "multiplicacao":
        resultado = a * b
    elif operacao == "divisao":
        if b == 0:
            return jsonify({"Erro": "Nao e possivel fazer divisao por zero."})
        resultado = a / b

    else:
        return jsonify({"Erro": "Operacao Invalida."})
    
    return jsonify({
        "a": a,
        "b": b,
        "operacao": operacao,
        "resultado": resultado
    })

if __name__ == '__main__':
    app.run(debug=True)