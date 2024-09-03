
# 📊 Rapport de Benchmark - Analyse Automatisée des Fichiers de Log

Ce projet propose un script Python permettant d'analyser automatiquement des fichiers de log issus de benchmarks, d'en extraire des métriques essentielles, et de générer un rapport interactif en HTML avec des graphiques.

## 🚀 Fonctionnalités

- **Extraction des Données :** 
  - Parcourt tous les fichiers `.log` dans un répertoire donné.
  - Identifie automatiquement le type de charge (OLTP Read Only, OLTP Write Only, etc.).
  - Extrait des métriques clés : nombre total de requêtes, transactions, latences (min, moy, max), événements par seconde, etc.

- **Génération de Graphiques :**
  - Crée des graphiques interactifs pour chaque type de charge.
  - Compare les différentes métriques extraites pour chaque fichier de log.

- **Rapport HTML :**
  - Compile tous les graphiques dans un rapport HTML prêt à être consulté dans un navigateur.

## 🛠️ Prérequis

Avant d'exécuter le script, assurez-vous d'avoir installé :

- **Python 3.x**
- **Bibliothèques Python :**
  - `pandas` pour la manipulation des données.
  - `plotly` pour la génération des graphiques interactifs.

```bash
pip3 install pandas plotly
```

## 📂 Structure du Répertoire

- `votre_script.py` : Le script principal pour l'extraction et l'analyse.
- `data_extracted.csv` : Fichier CSV généré contenant les données extraites.
- `report.html` : Rapport HTML interactif avec les graphiques pour chaque type de charge.

## 📝 Instructions d'Utilisation

1. **Préparation :**
   - Placez vos fichiers `.log` dans le même répertoire que le script ou modifiez la variable `LOG_DIR` pour spécifier un autre répertoire.

2. **Exécution du Script :**
   - Lancez le script en utilisant la commande suivante :
     ```bash
     ./votre_script.py
     ```
   - Un fichier `data_extracted.csv` sera généré avec les données extraites.

3. **Génération du Rapport :**
   - Le script produit également un fichier `report.html` contenant un rapport interactif avec des graphiques. Vous pouvez l'ouvrir directement dans votre navigateur préféré.

## ⚙️ Personnalisation

- **Répertoire des Logs :**
  - Modifiez la variable `LOG_DIR` dans le script pour changer le répertoire contenant les fichiers logs.

- **Types de Charges :**
  - Le script détecte plusieurs types de charges (OLTP Read Only, OLTP Write Only, etc.). Si vos logs contiennent des types de charges différents, ajustez les conditions dans la section correspondante du script.

## 🤝 Contributions

Les contributions sont les bienvenues ! Si vous avez des idées d'amélioration, n'hésitez pas à ouvrir une issue ou à soumettre une pull request.

## 📄 Licence

Ce projet est sous licence MIT. Vous êtes libre de l'utiliser, de le modifier et de le distribuer comme bon vous semble.

---

*Merci d'utiliser cet outil pour vos analyses de benchmarks !* 🎉
