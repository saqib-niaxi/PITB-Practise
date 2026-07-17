def register_user(username, email, password):
    return {
        "message": "User registered successfully",
        "username": username,
        "email": email
    }


if __name__ == "__main__":
    user = register_user(
        "Hanzla",
        "hanzla@example.com",
        "123456"
    )
    print(user)