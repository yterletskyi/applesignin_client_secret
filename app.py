import jwt
import time
import configparser

config = configparser.ConfigParser()
config.read_file(open('defaults.cfg'))

key_id = config['DEFAULT']['key_id']
key_path = config['DEFAULT']['key_path']
team_id = config['DEFAULT']['team_id']
client_id = config['DEFAULT']['client_id']

now = int(time.time())
exp = now + 86400 * 180

headers = {
    'kid': key_id
}

payload = {
    'iss': team_id,
    'iat': now,
    'exp': exp,
    'aud': 'https://appleid.apple.com',
    'sub': client_id
}

private_key = open(key_path, 'r').read()

secret = jwt.encode(payload, private_key, 'ES256', headers)
print(secret.decode('utf-8'))
