# Ce script réalise une analyse quantitative préliminaire du corpus CSV original contenant 10 cats .
# L'objectif est de calculer le nombre total de commentaires et de tokens,
# ainsi que leur distribution selon les catégories de produits et les labels (avis positifs / négatifs).

import pandas as pd
import jieba

# 1. Chargement du fichier CSV
file_path = 'online_shopping_10_cats.csv'
print(f"Chargement du corpus : {file_path} ...")
df = pd.read_csv(file_path)

# Suppression des lignes sans texte (valeurs manquantes)
df = df.dropna(subset=['review'])

# 2. Fonction de tokenisation et comptage
def tokenize_and_count(text):
    # Segmentation du texte chinois en utilisant jieba (mode précis)
    tokens = jieba.lcut(str(text))
    # Retourne le nombre de tokens dans chaque commentaire
    return len(tokens)

print("Tokenisation en cours avec jieba (cela peut prendre un certain temps)...")

# Application de la tokenisation à chaque commentaire
df['token_count'] = df['review'].apply(tokenize_and_count)

# 3. Statistiques globales du corpus
total_reviews = len(df)
total_tokens = df['token_count'].sum()

print("\n" + "="*50)
print("Aperçu global du corpus :")
print(f"Nombre total de commentaires : {total_reviews}")
print(f"Nombre total de tokens : {total_tokens}")
print("="*50 + "\n")

# 4. Analyse par catégorie et par label
print("Répartition des tokens par catégorie (label 1 = positif, label 0 = négatif) :")
print("-" * 65)
print(f"{'Catégorie':<12} | {'Tokens totaux':<12} | {'Tokens négatifs (0)':<20} | {'Tokens positifs (1)':<20}")
print("-" * 65)

categories = df['cat'].unique()

for cat in categories:
    cat_df = df[df['cat'] == cat]
    
    cat_total_tokens = cat_df['token_count'].sum()
    cat_label_0_tokens = cat_df[cat_df['label'] == 0]['token_count'].sum()
    cat_label_1_tokens = cat_df[cat_df['label'] == 1]['token_count'].sum()
    
    print(f"{cat:<10} | {cat_total_tokens:<14} | {cat_label_0_tokens:<19} | {cat_label_1_tokens:<19}")

print("-" * 65)
print("Analyse terminée.")