import pandas as pd
import jieba
import os

# Ce script construit un corpus équilibré pour l’analyse TXM,
# en se concentrant uniquement sur la catégorie "hôtel",
# avec deux polarités : positif et négatif.

# Configuration
INPUT_FILE = 'online_shopping_10_cats.csv'
TARGET_TOTAL_TOKENS = 250000

# On ne garde que la catégorie "酒店"
CATEGORY = '酒店'

# Labels : 0 = négatif, 1 = positif
LABELS = [0, 1]

# 125k tokens par sous-corpus (POS / NEG)
TOKENS_PER_BUCKET = TARGET_TOTAL_TOKENS // 2

# Mapping pour noms de fichiers
cat_map = {'酒店': 'hotel'}
label_map = {0: 'NEG', 1: 'POS'}

# Création des dossiers
folders = ['corpus_brut', 'corpus_tokenise']
for f in folders:
    if not os.path.exists(f):
        os.makedirs(f)

print("Chargement du corpus...")
df = pd.read_csv(INPUT_FILE).dropna(subset=['review'])

# Filtrer uniquement les hôtels
df = df[df['cat'] == CATEGORY]

# Construction des deux corpus (POS / NEG)
for label in LABELS:

    base_name = f"HUM_cat-{cat_map[CATEGORY]}_pol-{label_map[label]}.txt"

    subset = df[df['label'] == label]

    current_tokens = 0
    brut_lines = []
    tokenized_lines = []

    for _, row in subset.iterrows():
        review = str(row['review']).replace('\n', ' ').strip()
        if not review:
            continue

        words = jieba.lcut(review)
        current_tokens += len(words)

        brut_lines.append(review)
        tokenized_lines.append(" ".join(words))

        if current_tokens >= TOKENS_PER_BUCKET:
            break

    # Sauvegarde brut
    with open(f'corpus_brut/{base_name}', 'w', encoding='utf-8') as f:
        f.write("\n".join(brut_lines))

    # Sauvegarde tokenisé (TXM)
    with open(f'corpus_tokenise/{base_name}', 'w', encoding='utf-8') as f:
        f.write("\n".join(tokenized_lines))

    print(f"Fichier généré : {base_name} ({current_tokens} tokens)")

print("\nCorpus hôtel (POS/NEG) prêt pour TXM.")