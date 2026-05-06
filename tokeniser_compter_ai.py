import jieba
import os
import argparse

def segmenter_texte(texte):
    """Effectue la segmentation jieba et retourne le texte avec espaces."""
    tokens = jieba.lcut(texte.strip())
    return " ".join(tokens), len(tokens)

def traiter_fichier(chemin_entree, chemin_sortie):
    """Traite un fichier unique : segmente et compte les tokens."""
    nb_tokens_fichier = 0
    lignes_segmentees = []
    
    with open(chemin_entree, 'r', encoding='utf-8') as f:
        for ligne in f:
            if not ligne.strip():
                continue
            texte_seg, count = segmenter_texte(ligne)
            lignes_segmentees.append(texte_seg)
            nb_tokens_fichier += count
            
    with open(chemin_sortie, 'w', encoding='utf-8') as f_out:
        f_out.write("\n".join(lignes_segmentees))
    
    return nb_tokens_fichier

def main():
    # Configuration de l'analyseur d'arguments
    parser = argparse.ArgumentParser(description="Outil de segmentation Jieba pour TXM (Fichier ou Dossier)")
    parser.add_argument("-i", "--input", required=True, help="Chemin vers le fichier .txt ou le dossier d'entrée")
    parser.add_argument("-o", "--output", required=True, help="Chemin vers le fichier de sortie ou le dossier de sortie")
    
    args = parser.parse_args()

    total_tokens_general = 0

    # CAS 1 : L'entrée est un DOSSIER
    if os.path.isdir(args.input):
        if not os.path.exists(args.output):
            os.makedirs(args.output)
            print(f"Dossier de sortie créé : {args.output}")

        fichiers = [f for f in os.listdir(args.input) if f.endswith('.txt')]
        print(f"--- Début du traitement du dossier : {len(fichiers)} fichiers trouvés ---")
        
        for nom_f in fichiers:
            chemin_f_entree = os.path.join(args.input, nom_f)
            chemin_f_sortie = os.path.join(args.output, f"TOKENIZED_{nom_f}")
            
            nb = traiter_fichier(chemin_f_entree, chemin_f_sortie)
            total_tokens_general += nb
            print(f"Traité : {nom_f} | Tokens : {nb}")

    # CAS 2 : L'entrée est un FICHIER unique
    elif os.path.isfile(args.input):
        print(f"--- Traitement du fichier unique : {args.input} ---")
        nb = traiter_fichier(args.input, args.output)
        total_tokens_general = nb
        print(f"Terminé. Fichier enregistré sous : {args.output}")

    else:
        print("Erreur : Le chemin d'entrée n'est ni un fichier ni un dossier valide.")
        return

    print("-" * 40)
    print(f"NB TOTAL DE TOKENS : {total_tokens_general}")
    print("-" * 40)

if __name__ == "__main__":
    main()