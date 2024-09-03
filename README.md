# sysbench-graph-report
sysbench with graph reporting HTML

# Rapport de Benchmark - Analyse Automatisée des Fichiers de Log

Ce projet contient un script Python qui permet d'analyser des fichiers de log générés par des benchmarks, d'extraire des métriques clés, et de générer un rapport visuel sous forme de graphiques interactifs.

## Fonctionnalités

- **Extraction des Données** : Le script parcourt tous les fichiers `.log` dans un répertoire spécifié, identifie le type de charge (OLTP Read Only, OLTP Write Only, etc.), et extrait des métriques telles que le nombre total de requêtes, la latence moyenne, et le nombre d'événements par seconde.
- **Génération de Graphiques** : Pour chaque type de charge, le script génère des graphiques comparant les différentes métriques extraites pour chaque fichier de log.
- **Rapport HTML** : Le script compile les graphiques dans un rapport HTML interactif, prêt à être consulté dans un navigateur.

## Prérequis

Avant d'exécuter le script, assurez-vous d'avoir les éléments suivants installés sur votre machine :

- Python 3.x
- Bibliothèques Python :
  - `pandas` pour la manipulation des données
  - `plotly` pour la génération des graphiques

Vous pouvez installer les bibliothèques nécessaires en utilisant pip :

```bash
pip install pandas plotly
