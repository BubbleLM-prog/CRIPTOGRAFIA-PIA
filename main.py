import base64
import binascii
from nacl.encoding import HexEncoder
from nacl.exceptions import BadSignatureError
from nacl.signing import SigningKey
from nacl.hash import blake2b
from random import randint

def encrypt(data: bytes, password: bytes):
    encrypted_array: list = []
    i=0
    for d in data:
        encrypted_array.append(((d + password[i]) % 256).to_bytes(1, "big"))
        i+=1
        if i >= len(password):
            i=0
    return b''.join(encrypted_array)

def decrypt(data: bytes, password: bytes):
    decrypted_array: list = []
    i=0
    for d in data:
        decrypted_array.append(((d - password[i]) % 256).to_bytes(1, "big"))
        i+=1
        if i >= len(password):
            i=0
    return b''.join(decrypted_array)

def write(data: bytes, path: str):
    with open(path, "wb") as file:
        file.write(data)

def read(path: bytes):
    with open(path, "rb") as file:
        return file.read()

def genKeyPair():
    kp = SigningKey.generate()
    pubKey= binascii.hexlify(kp.to_curve25519_private_key().public_key.__bytes__()).decode("utf-8")
    secKey= binascii.hexlify(kp.__bytes__())[0:64].decode("utf-8")
    return kp._seed


def bytesToString(data: bytes):
    return base64.encodebytes(data).decode("utf-8")

def stringToBytes(data: str):
    return base64.decodebytes(data.encode("utf-8"))

def sign(cer: str, seed: bytes):
    sign_key = SigningKey(seed)
    signed_raw = sign_key.sign(cer.encode("utf-8"))
    return signed_raw

def register(username: str, password: str):
    seed: bytes = genKeyPair()
    signed: dict = sign(username, seed)
    write(encrypt(seed, password.encode("utf-8")), username + ".key")
    write(signed, username + ".cer")

def login(namekey: str, namecer: str, password: str):
    seed: bytes = decrypt(read(namekey + ".key"), password.encode("utf-8"))
    signed_raw: bytes = read(namecer + ".cer")
    verify_key = SigningKey(seed).verify_key
    try:        
        verify_key.verify(signed_raw)
        return True
    except BadSignatureError:
        return False

