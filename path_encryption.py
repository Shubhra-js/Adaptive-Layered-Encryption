import networkx as nx
import random

# ---------------- Noise Cipher ----------------
def noise_encrypt(text):
    shift = random.randint(1, 25)
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result, shift

def noise_decrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base - shift) % 26 + base)
        else:
            result += char
    return result

# ---------------- Caesar Cipher ----------------
def caesar_encrypt(text, shift=3):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def caesar_decrypt(text, shift=3):
    return caesar_encrypt(text, -shift)

# ---------------- Affine Cipher ----------------
def affine_encrypt(text, a=5, b=8):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            x = ord(char) - base
            result += chr(((a * x + b) % 26) + base)
        else:
            result += char
    return result

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

def affine_decrypt(text, a=5, b=8):
    result = ""
    a_inv = mod_inverse(a, 26)
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            y = ord(char) - base
            result += chr(((a_inv * (y - b)) % 26) + base)
        else:
            result += char
    return result

# ---------------- RSA ----------------
def generate_rsa_keys(p=61, q=53):
    n = p * q
    phi = (p-1) * (q-1)
    e = 17  # public exponent
    d = mod_inverse(e, phi)
    return ((e, n), (d, n))  # (public_key, private_key)

def rsa_encrypt(text, public_key):
    e, n = public_key
    return [pow(ord(char), e, n) for char in text]

def rsa_decrypt(cipher, private_key):
    d, n = private_key
    return "".join([chr(pow(c, d, n)) for c in cipher])

# ---------------- Graph Network ----------------
G = nx.Graph()
G.add_nodes_from(["Alice", "Bob", "R1", "R2", "R3", "R4", "R5", "R6", "R7"])
G.add_edges_from([
    ("Alice", "R1"), ("R1", "R2"), ("R2", "Bob"),         # Path 1 (3 hops)
    ("Alice", "R3"), ("R3", "Bob"),                       # Path 2 (2 hops)
    ("Alice", "R4"), ("R4", "R5"), ("R5", "R6"), ("R6", "Bob"), # Path 3 (4 hops)
    ("Alice", "R7"), ("R7", "Bob")                        # Path 4 (2 hops)
])

# Message should be defined BEFORE encryption
message = "HELLO"
print(f"Original Message: {message}")

public_key, private_key = generate_rsa_keys()

# Show all paths
all_paths = list(nx.all_simple_paths(G, source="Alice", target="Bob"))
print("All Paths:", all_paths)

# Find shortest path
shortest_path = nx.shortest_path(G, source="Alice", target="Bob")
print("Shortest Path:", shortest_path)

# ---------------- Encrypt Only Shortest Path ----------------
path = shortest_path
hops = len(path) - 1
encrypted = message
noise_key = None

print(f"\nEncrypting for Shortest Path -> {path}  (Hops: {hops})")

if hops == 2:
    encrypted = caesar_encrypt(encrypted)
    encrypted = affine_encrypt(encrypted)

elif hops == 3:
    encrypted = caesar_encrypt(encrypted)
    encrypted = affine_encrypt(encrypted)
    encrypted = rsa_encrypt(encrypted, public_key)
    encrypted = " ".join(map(str, encrypted))

elif hops >= 4:
    encrypted = caesar_encrypt(encrypted)
    encrypted = affine_encrypt(encrypted)
    encrypted = rsa_encrypt(encrypted, public_key)
    encrypted = " ".join(map(str, encrypted))
    encrypted, noise_key = noise_encrypt(encrypted)

print(f"Encrypted Message: {encrypted}")

# Decrypt
decrypted = encrypted
if hops == 2:
    decrypted = affine_decrypt(decrypted)
    decrypted = caesar_decrypt(decrypted)

elif hops == 3:
    decrypted = list(map(int, decrypted.split()))
    decrypted = rsa_decrypt(decrypted, private_key)
    decrypted = affine_decrypt(decrypted)
    decrypted = caesar_decrypt(decrypted)

elif hops >= 4:
    if noise_key:
        decrypted = noise_decrypt(decrypted, noise_key)
    decrypted = list(map(int, decrypted.split()))
    decrypted = rsa_decrypt(decrypted, private_key)
    decrypted = affine_decrypt(decrypted)
    decrypted = caesar_decrypt(decrypted)

print(f"Decrypted Message: {decrypted}")
