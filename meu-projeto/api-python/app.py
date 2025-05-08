from flask import Flask, request, jsonify
import mysql.connector
import os

app = Flask(__name__)

def conectar_banco():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )


@app.route('/criar_tabela', methods=['GET'])
def criar_tabela():
    try:
        conn = conectar_banco()
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS produtos (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(255) NOT NULL,
                preco DECIMAL(10,2) NOT NULL
            );
        """)
        conn.commit()
        conn.close()
        return " Tabela 'produtos' criada com sucesso!"
    except Exception as e:
        return f"Erro ao criar tabela: {str(e)}", 500

@app.route('/limpar', methods=['GET'])
def limpar_tabela():
    try:
        conn = conectar_banco()
        cursor = conn.cursor()
        cursor.execute("TRUNCATE TABLE produtos;")
        conn.commit()
        conn.close()
        return "Tabela 'produtos' limpa com sucesso!"
    except Exception as e:
        return f"Erro ao limpar tabela: {str(e)}", 500

@app.route('/getdados', methods=['GET']) 
def puxar_dados():
    try:
        conn = conectar_banco()
        cursor = conn.cursor(dictionary=True)  
        cursor.execute("SELECT * FROM produtos")
        resultados = cursor.fetchall()
        conn.close()
        return jsonify(resultados)
    except Exception as e:
        return jsonify({"erro": str(e)}), 500


@app.route('/formulario')
def formulario():
    return '''
    <h2>Cadastrar Produto</h2>
    <form method="POST" action="/salvar">
        <label>Nome:</label><br>
        <input type="text" name="nome" required><br><br>

        <label>Preço:</label><br>
        <input type="number" name="preco" step="0.01" required><br><br>

        <button type="submit">Salvar</button>
    </form>
    '''

@app.route('/salvar', methods=['POST'])
def salvar_produto():
    try:
        nome = request.form['nome']
        preco = request.form['preco']

        conn = conectar_banco()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO produtos (nome, preco) VALUES (%s, %s)", (nome, preco))
        conn.commit()
        conn.close()

        return f" Produto <strong>{nome}</strong> com preço <strong>R$ {preco}</strong> foi salvo com sucesso!"
    except Exception as e:
        return f" Erro ao salvar: {str(e)}", 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
