def authenticateUser():
    print("test code search")

def authenticateUser(username: str, password: str) -> bool:
    print(f"Authenticating user: {username}")
    return username == "admin" and password == "secure123"