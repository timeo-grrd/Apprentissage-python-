import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost", 4000))

print("Connexion établie. Début de la boucle...")

while True:
    
    reponse = s.recv(2048).decode('utf-8')
    
    
    if not reponse:
        break
        
    print(reponse.strip())

    
    if "FCSC{" in reponse:
        print("\n🏆 FLAG TROUVÉ ! 🏆")
        break

    
    if ">>> " in reponse:
       
        lignes = reponse.strip().split('\n')
        derniere_ligne = lignes[-1]  
        mot_a_inverser = derniere_ligne.replace(">>> ", "")
        
        mot_inverse = mot_a_inverser[::-1]
        
        s.sendall((mot_inverse + '\n').encode('utf-8'))