from email_validator import validate_email, EmailNotValidError

def validate_email_input(email):
    try:
        # Verifica el formato y la validez del correo electrónico
        v = validate_email(email)
        return True
    except EmailNotValidError as e:
        # El correo electrónico no es válido
        print(str(e))
        return False
