from flask import Flask, request

app = Flask(__name__)
USERS = []

@app.get("/")
def index():
    return {'message': 'Hello World'}

@app.get("/aboutme")
def about_me():
    return get_users_by_id(1)

@app.get("/users")
def get_users():
    return {'users': USERS}

@app.get("/users/<int:user_id>")
def get_users_by_id(user_id):
    me = {}
    not_found = True
    if user_id == 1:
        me =  {
            'first_name': 'Rafael',
            'last_name': 'Chavez',
            'hobbies': 'games, programming and movies',
            'is_active': True,
        }
        not_found = False
    if not_found:
        return me, 404
    return me

@app.post("/users")
def create_user():
    user_data = request.json
    USERS.append(user_data)
    return 201, {'message': 'User created successfully'}

""" if __name__ == "__main__":
    app.run(debug=True) """