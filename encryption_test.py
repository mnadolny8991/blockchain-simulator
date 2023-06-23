from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from transaction_utils import *

private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

public_key = private_key.public_key()

message = b"encrypted data"
ciphertext = public_key.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

plaintext = private_key.decrypt(
    ciphertext,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)


wallet_t = generate_rsa_key_pair()
wallet_r = generate_rsa_key_pair()
tx = wallet_t[1]
rx = wallet_r[1]
trans = Transaction(tx, rx, 100.99, 200.00)
trans_dict = trans.to_dict()

print(trans_dict)

trans_copy = Transaction()
trans_copy.from_dict(trans_dict)

print("-------------------------------")
print(trans_copy.to_dict())



    

