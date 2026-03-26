import subprocess
result = subprocess.run(['git', 'ls-files', '--others', '--exclude-standard'], capture_output=True, text=True)
fichiers_restants = result.stdout.strip().split('\n')


if fichiers_restants and fichiers_restants[0] != '':
    
    fichier_a_push = fichiers_restants[0]
    
    print(f"Fichier sélectionné pour aujourd'hui : {fichier_a_push}")
    
    
    subprocess.run(['git', 'add', fichier_a_push])
    subprocess.run(['git', 'commit', '-m', f"Ajout quotidien : {fichier_a_push}"])
    subprocess.run(['git', 'push'])
    
    print("✅ Push réussi !")
else:
    print("❌ Plus aucun nouveau fichier à envoyer !")