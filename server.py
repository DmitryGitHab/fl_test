# import requests
# from flask import request
from flask import Flask, jsonify, request
from flask.views import MethodView
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Integer, String, DateTime, func, create_engine

app = Flask('app')
# PG_DSN = 'postgresql://app:1234@127.0.0.1:5431/flask'
PG_DSN = 'postgresql://postgres:postgres@127.0.0.1/flask_test'

engine = create_engine(PG_DSN, pool_pre_ping=True)
Session = sessionmaker(bind=engine)

Base = declarative_base()


class User(Base):

    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String, index=True, unique=True, nullable=False)
    password = Column(String, nullable=False)
    created_at = Column(DateTime, server_default=func.now())

def get_user(session: Session, user_id: int):
    user = session.query(User).get(user_id)
    if user is None:
        pass
    return user

Base.metadata.create_all(engine)


class UserView(MethodView):

    def get(self, user_id: int):
        with Session() as session:
            user = get_user(session, user_id)
            return jsonify({'name': user.name, 'created_at': user.created_at.isoformat()})

    def post(self):
        json_data = request.json
        with Session() as session:
            user = User(name=json_data['name'], password=json_data['password'])
            session.add(user)
            session.commit()
            return {'id': user.id}

    def patch(self, user_id):
        json_data = request.json
        with Session() as session:
            user = get_user(session, user_id)
            if json_data.get('name'):
                user.name = json_data['name']
            if json_data.get('password'):
                user.password = json_data['password']
            session.add(user)
            session.commit()
            return {
                'id': user.id,
                'name': user.name,
                'status': "success",
            }


    def delete(self, user_id: int):
        with Session() as session:
            user = get_user(session, user_id)
            session.delete(user)
            session.commit()
            return {'status': "success"}


user_view = UserView.as_view('users')
app.add_url_rule('/users/', view_func=user_view, methods=['POST'])
app.add_url_rule('/users/<int:user_id>', view_func=user_view, methods=['GET', 'PATCH', 'DELETE'])


app.run()









