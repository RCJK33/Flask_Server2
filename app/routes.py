from flask import Flask, request

app = Flask(__name__)
USERS = []

@app.get("/users/<int:user_id>")
@app.get("/")
def index(user_id):
    me = {}
    not_found = True
    if user_id == 1:
        me =  {
            'first_name': 'Rafael',
            'last_name': 'Chavez',
            'hobbies': ['games', 'programming', 'movies'],
            'is_programmer': True,
            'age': 19,
        }
        not_found = False
    if not_found:
        return me, 404
    return me

@app.get("/users")
def get_users():
    return {'users': USERS}

@app.post("/users")
def create_user():
    user_data = request.json
    USERS.append(user_data)
    return 201, {'message': 'User created successfully'}

""" if __name__ == "__main__":
    app.run(debug=True) """