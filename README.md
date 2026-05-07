# AI-vs-human-hotel-reviews-txm
Ce projet, réalisé dans le cadre du cours Analyse Statistique des données textuelles (Master 1 TAL, 2025-2026), mobilise la fouille de textes et les statistiques pour comparer les caractéristiques linguistiques d'avis hôteliers réels (JD.com) avec celles de textes générés par IA (GPT et DeepSeek). 


## Structure du dépôt

```text
├── corpus_brut/                # Corpus hôteliers non segmenté
├── corpus_tokenise/            # Corpus hôteliers originaux segmentés avec Jieba (prêts pour TXM)
├── resultats_txm/              # Exports des analyses statistiques et graphiques
├── compter.py                  # Script de statistiques descriptives du corpus initial online_shopping_10_cats.csv
├── online_shopping_10_cats.csv # Jeu de données initial (62k+ commentaires)
├── tokeniser_compter_ai.py     # Script de segmentation et comptage pour l'IA
├── traitement_corpus.py        # Script pour extraire les textes hôteliers (bruts et segmentés)
├── README.md 
└── rapport.pdf                  
```

## Outils et Technologies
* **Langage :** Python (Jieba pour la segmentation lexicale).
* **Analyse textométrique :** Logiciel TXM.
* **Données :** Avis clients issus du site JD.com (2016) https://github.com/jamosnet/JD-comments-sentiment-analysis/blob/main/online_shopping_10_cats.csv  et générations LLM.

## Équipe 
* **Membres :** Emmy Lebail, Mengge Liu, Peng Chen, Ting Zheng, Shiyi Yao.
* **Encadrant :** Mathieu Valette.

---
*Projet universitaire - Master 1 PluriTAL*
