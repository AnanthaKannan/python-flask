def authenticate(username, password):
    user = User.findby_username(username)
    if user and password == user.password
        return user
    
def identity(payload):
    user_id = payload['identity']
    return User.findby_id(user_id)