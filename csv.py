def load_users_from_csv(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            users = {}
            for line in lines[1:]: 
                email, name = line.strip().split(',')
                users[email] = name
            return users
    except FileNotFoundError:
        return {}

def save_users_to_csv(filename, users):
    with open(filename, 'a') as file:
        for email, name in users.items():
            file.write(f"{email},{name}\n")

