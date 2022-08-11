# import requests
# from flask import request
from flask import Flask, jsonify, request
from flask.views import MethodView
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Integer, String, DateTime, func, create_engine

app = Flask('app')
PG_DSN = 'postgresql://app:1234@127.0.0.1:5431/flask'
# PG_DSN = 'postgresql://postgres:postgres@127.0.0.1/flask_test'

engine = create_engine(PG_DSN, pool_pre_ping=True)
Session = sessionmaker(bind=engine)

Base = declarative_base()


class User(Base):

    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String, index=True, unique=True, nullable=False)
    password = Column(String, nullable=False)
    created_at = Column(DateTime, server_default=func.now())


Base.metadata.create_all(engine)

#
# @app.route('/test/', methods=['POST'])
# def test():
#     data = request
#     # print(requests)
#     uri_data = request.args
#     headers = request.headers
#     json_data = request.json
#
#     return jsonify({'status': 'ok',
#                     'qs': dict(uri_data),
#                     'headers': dict(headers),
#                     'json': json_data
#                     })


class UserView(MethodView):

    def get(self, user_id: int):
        with Session as session:
            user = session.query(User).get(user_id)
            if user is None:
                pass
            return jsonify({'name': user.name, 'created_at': user.created_at.isoformat()})

    def post(self):
        json_data = request.json
        with Session() as session:
            user = User(name=json_data['name'], password=json_data['password'])
            session.add(user)
            session.commit()
            return {'id': user.id}

    def patch(self):
        pass

    def delete(self):
        pass


user_view = UserView.as_view('users')
app.add_url_rule('/users/', view_func=user_view, methods=['POST'])
app.add_url_rule('/users/<int:user_id>', view_func=user_view, methods=['GET'])


app.run()









