# La séquence que vous avez extraite du fichier
encoded = "00110100110010011111100011111110010001001011000101000111111111100100100101011110100001001011000101000111111111100111110101000111110010101000111000001011011011111011100001010110011101001011111100001110011100110011100100101011000010100101001110111011000110100011010100100101011101110001010001001000101100010100010001010110011101111111110100000110101101001000100010001011110001110101011001110111111111100111110101110011001110010010011000111011100001101111100000011001011110100010101100001010101101001000100010001011111111100111000001000001011100110011100100100110001101011100111101110110001010110000011101010110011101111111111001000111000110010111011111000100111111100111110101111101010001001000100001010110010011010100011111001010100011100000100011000111100010000101011001110111000110100000001001110011001110101011011111000111010101100111010010001011110010010001111111001110010001111100011110001011110001110101011001110111001000111100111001000111110010101000111000001000110001001100101001100111011111111101111011111100"

# Les polynômes en hexadécimal
G0 = 0x19
G1 = 0x1B

# Fonction de parité (identique à celle du script Go)
def parity(b):
    b ^= (b >> 4)
    b ^= (b >> 2)
    b ^= (b >> 1)
    return b & 1

# Algorithme de Viterbi
# Initialisation : on commence à l'état 0 avec un coût de 0 et un chemin vide.
# Dictionnaire des états: {état_actuel: (coût_cumulé, "historique_bits")}
states = {0: (0, "")} 

print("Décodage en cours...")

# On lit les bits par paires (car le Go génère 2 bits de sortie par itération)
for i in range(0, len(encoded), 2):
    r0 = int(encoded[i])
    r1 = int(encoded[i+1])
    
    new_states = {}
    
    # On explore les branches pour chaque état existant
    for S, (metric, history) in states.items():
        # Pour chaque état, on peut recevoir soit un bit 0, soit un bit 1
        for bit in (0, 1):
            # Le nouveau registre R sur 5 bits
            R = (S << 1) | bit
            
            # Les sorties générées si ce bit avait été reçu
            out0 = parity(R & G0)
            out1 = parity(R & G1)
            
            # On calcule la pénalité (différence entre les bits simulés et ceux reçus)
            cost = (out0 != r0) + (out1 != r1)
            
            # Le prochain état (on ne garde que les 4 bits de poids faible)
            next_S = R & 0x0F
            new_metric = metric + cost
            
            # Viterbi : On conserve uniquement le chemin le moins coûteux pour atteindre cet état
            if next_S not in new_states or new_metric < new_states[next_S][0]:
                new_states[next_S] = (new_metric, history + str(bit))
                
    states = new_states

# Fin du décodage.
# Comme le script Go a fait un "flush" avec 4 bits à zéro à la fin, on SAIT
# avec certitude que l'état final attendu est 0. On prend donc le meilleur chemin menant à l'état 0.
best_metric, best_history = states[0]

# On supprime les 4 zéros qui ont servi au flush final
flag_bits = best_history[:-4]

# Conversion des bits retrouvés en caractères ASCII
flag = ""
for i in range(0, len(flag_bits), 8):
    byte = flag_bits[i:i+8]
    if len(byte) == 8:
        flag += chr(int(byte, 2))

print("Succès ! Voici le résultat :")
print(flag)