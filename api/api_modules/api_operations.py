import re

def is_email_valid(email):
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    if re.fullmatch(regex, email):
      return True
    else:
      return False

def is_username_valid(username):
    regex = re.compile(r'([a-zA-Z0-9]{4,16})')
    if re.fullmatch(regex, username):
      return True
    else:
      return False

