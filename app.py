from flask import Flask, jsonify, request
from config import Config
from models import db, Professor
import logging

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

@app.route('/get_professores', methods=['GET'])
def get_professores():
    try:
       
        professores = Professor.query.all()
        professores_json = []

        for professor in professores:
            professor_data = {
                'id_professor': professor.id_professor,
                'nome_completo': professor.nome_completo,
                'data_nascimento': professor.data_nascimento,
                'celular': professor.celular,
                'endereco': professor.endereco,
                'cpf': professor.cpf,
                'bio': professor.bio,
                'foto_perfil': professor.foto_perfil,
                'email': professor.email,
                'senha': professor.senha,
                'data_cadastro': professor.data_cadastro
            }

            professores_json.append(professor_data)

        if len(professores_json) > 0:
            return jsonify({'Professor': True, 'Mensagem': professores_json})
    
        return jsonify({'Professor': False, 'Mensagem': 'Nenhum professor encontrado!'}), 404

    except Exception as e:
        logging.error(f"Erro no get_cursos: {e}")
        db.session.rollback()
        return jsonify({'Professor': False, 'Mensagem': str(e)}), 500
    
@app.route('/get_professores_id', methods=['GET'])
def get_professores_id():
    try:

        id_professor_entry = request.args.get('id_professor')

        if not id_professor_entry:
            return jsonify({'Erro': 'id nao digitado'}), 400
        
        professor = Professor.query.filter_by(id_professor=id_professor_entry).first()

        if professor:
            return jsonify({'Professor': True, 'Mensagem': {
                'id_professor': professor.id_professor,
                'nome_completo': professor.nome_completo,
                'data_nascimento': professor.data_nascimento,
                'celular': professor.celular,
                'endereco': professor.endereco,
                'cpf': professor.cpf,
                'bio': professor.bio,
                'foto_perfil': professor.foto_perfil,
                'email': professor.email,
                'senha': professor.senha,
                'data_cadastro': professor.data_cadastro}})
        
        return jsonify({'Professor': False, 'Mensagem': 'Nenhum professor encontrado!'}), 404

    except Exception as e:
        logging.error(f"Erro no get_cursos: {e}")
        db.session.rollback()
        return jsonify({'Professor': False, 'Mensagem': str(e)}), 500
 
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5000)
