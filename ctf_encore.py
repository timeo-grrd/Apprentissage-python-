from Crypto.Cipher import AES
from Crypto.Util import Counter

# Les paramètres donnés dans l'énoncé
key_hex = "00112233445566778899aabbccddeeff"
# On transforme la chaîne hexadécimale en vrais octets compréhensibles par l'ordinateur
key = bytes.fromhex(key_hex)

# Un IV (Vecteur d'Initialisation) nul signifie que le compteur de l'AES démarre à 0.
# AES fonctionne toujours sur des blocs de 128 bits.
ctr = Counter.new(128, initial_value=0)

# Initialisation de la moulinette AES en mode CTR
cipher = AES.new(key, AES.MODE_CTR, counter=ctr)

print("[*] Lecture du fichier chiffré...")
with open("flag.jpg.enc", "rb") as f:
    encrypted_data = f.read()

print("[*] Déchiffrement en cours à la vitesse de la lumière...")
# En mode CTR, le déchiffrement est en fait identique au chiffrement
decrypted_data = cipher.decrypt(encrypted_data)

# Sauvegarde de l'image en clair
output_file = "flag_decrypted.jpg"
with open(output_file, "wb") as f:
    f.write(decrypted_data)

print(f"[+] BINGO ! L'image est sauvegardée sous : {output_file}")