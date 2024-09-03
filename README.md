
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

   - placer vos fichier de log de sysbench sous ce format :
  
     ```bash
      oltp_update_non_index  ## attention changer par le oltp testé
      SQL statistics:
          queries performed:
              read:                            0
              write:                           68
              other:                           865
              total:                           933
          transactions:                        933    (15.55 per sec.)
          queries:                             933    (15.55 per sec.)
          ignored errors:                      0      (0.00 per sec.)
          reconnects:                          0      (0.00 per sec.)
      
      Throughput:
          events/s (eps):                      15.5477
          time elapsed:                        60.0088s
          total number of events:              933
      
      Latency (ms):
               min:                                   58.99
               avg:                                   64.31
               max:                                  223.48
               95th percentile:                       78.60
               sum:                                60000.52
      
      Threads fairness:
          events (avg/stddev):           933.0000/0.00
          execution time (avg/stddev):   60.0005/0.00
     ```

   - Lancez le script en utilisant la commande suivante :
     ```bash
     ./votre_script.py
     ```
   - Un fichier `data_extracted.csv` sera généré avec les données extraites.
  
     
4. **Génération du Rapport :**
   - Le script produit également un fichier `report.html` contenant un rapport interactif avec des graphiques. Vous pouvez l'ouvrir directement dans votre navigateur préféré.

![](https://i.imgur.com/T2ts60J.png)

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
