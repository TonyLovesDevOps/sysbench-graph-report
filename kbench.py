#!/usr/bin/env python3

import pandas as pd
import plotly.graph_objects as go
import glob
import re
import os

# Répertoire contenant les fichiers .log
LOG_DIR = "./"

# Fonction pour nettoyer les noms de fichiers
def sanitize_filename(filename):
    # Remplacer les caractères non alphanumériques par des underscores
    return re.sub(r'[<>:"/\\|?*\x00-\x1F]', '_', filename)

# Initialiser une liste pour stocker les données extraites
data = []

# Lire tous les fichiers .log dans le répertoire spécifié
for file_path in glob.glob(f"{LOG_DIR}/*.log"):
    with open(file_path, 'r') as file:
        # Lire la première ligne pour déterminer le type de charge
        first_line = file.readline().strip()
        
        if 'oltp_read_only' in first_line:
            load_type = 'OLTP Read Only'
        elif 'oltp_read_write' in first_line:
            load_type = 'OLTP Read Write'
        elif 'oltp_update_index' in first_line:
            load_type = 'OLTP Update Index'
        elif 'oltp_update_non_index' in first_line:
            load_type = 'OLTP Update Non-Index'
        elif 'oltp_write_only' in first_line:
            load_type = 'OLTP Write Only'
        elif 'oltp_select_in_pk' in first_line:
            load_type = 'OLTP Select In PK'
        else:
            load_type = 'Unknown'

        content = file.read()

        # Extraire les valeurs nécessaires à l'aide de regex
        total_queries = re.search(r'total:\s+(\d+)', content)
        transactions = re.search(r'transactions:\s+(\d+)', content)
        queries_read = re.search(r'read:\s+(\d+)', content)
        events_per_sec = re.search(r'events/s \(eps\):\s+([\d.]+)', content)
        time_elapsed = re.search(r'time elapsed:\s+([\d.]+)s', content)
        total_events = re.search(r'total number of events:\s+(\d+)', content)
        min_latency = re.search(r'min:\s+([\d.]+)', content)
        avg_latency = re.search(r'avg:\s+([\d.]+)', content)
        max_latency = re.search(r'max:\s+([\d.]+)', content)
        percentile_95 = re.search(r'95th percentile:\s+([\d.]+)', content)
        sum_latency = re.search(r'sum:\s+([\d.]+)', content)

        # Stocker les données extraites dans une liste
        data.append({
            'Fichier': file_path.split('/')[-1],
            'Type de Charge': load_type,
            'Total Queries': float(total_queries.group(1)) if total_queries else float('nan'),
            'Transactions': float(transactions.group(1)) if transactions else float('nan'),
            'Queries Read': float(queries_read.group(1)) if queries_read else float('nan'),
            'Events/s': float(events_per_sec.group(1)) if events_per_sec else float('nan'),
            'Time Elapsed': float(time_elapsed.group(1)) if time_elapsed else float('nan'),
            'Total Events': float(total_events.group(1)) if total_events else float('nan'),
            'Min Latency': float(min_latency.group(1)) if min_latency else float('nan'),
            'Avg Latency': float(avg_latency.group(1)) if avg_latency else float('nan'),
            'Max Latency': float(max_latency.group(1)) if max_latency else float('nan'),
            '95th Percentile': float(percentile_95.group(1)) if percentile_95 else float('nan'),
            'Sum Latency': float(sum_latency.group(1)) if sum_latency else float('nan')
        })

# Convertir les données en DataFrame pandas
df = pd.DataFrame(data)

# Sauvegarder les données extraites dans un fichier CSV
df.to_csv('data_extracted.csv', index=False)

# Créer des graphiques pour chaque type de charge
types_of_load = df['Type de Charge'].unique()
graph_files = []

for load_type in types_of_load:
    df_load_type = df[df['Type de Charge'] == load_type]
    fig = go.Figure()

    metrics = [
        ('Total Queries', 'Total Queries'),
        ('Transactions', 'Transactions'),
        ('Queries Read', 'Queries Read'),
        ('Events/s', 'Events/s'),
        ('Min Latency', 'Min Latency'),
        ('Avg Latency', 'Avg Latency'),
        ('Max Latency', 'Max Latency'),
        ('95th Percentile', '95th Percentile')
    ]

    for metric, title in metrics:
        fig.add_trace(go.Bar(
            x=df_load_type['Fichier'],
            y=df_load_type[metric],
            name=title,
            text=df_load_type[metric],
            textposition='outside'
        ))

    fig.update_layout(
        title=f'Comparaison des Métriques pour {load_type}',
        xaxis_title='Fichier',
        yaxis_title='Valeur',
        barmode='group',
        bargap=0.1,
        xaxis_tickangle=-45,
        margin=dict(l=50, r=50, t=50, b=50)
    )

    # Sauvegarder chaque graphique en HTML
    graph_file = f'{sanitize_filename(load_type)}.html'
    fig.write_html(graph_file)
    graph_files.append(graph_file)

# Création du rapport HTML avec descriptions
html_content = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Rapport de Benchmark</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        h1 {
            color: #333;
        }
        .section {
            margin-bottom: 30px;
        }
        .chart-container {
            display: flex;
            justify-content: center;
            margin-bottom: 20px;
        }
        iframe {
            width: 100%;
            height: 600px;
            border: none;
        }
        .summary {
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 5px;
            background-color: #f9f9f9;
        }
    </style>
</head>
<body>
    <h1>Rapport de Benchmark</h1>
    <div class="summary">
        <h2>Résumé</h2>
        <p>Ce rapport présente les résultats des benchmarks extraits des fichiers de log, regroupés par type de charge. Les graphiques ci-dessous montrent la comparaison des différentes métriques pour chaque type de charge.</p>
    </div>
"""

# Ajouter des graphiques pour chaque type de charge
for graph_file in graph_files:
    html_content += f"""
    <div class="section">
        <h2>Graphique pour {sanitize_filename(graph_file).replace('.html', '')}</h2>
        <div class="chart-container">
            <iframe src="{graph_file}"></iframe>
        </div>
    </div>
    """

html_content += """
</body>
</html>
"""

# Sauvegarder le rapport HTML
with open('report.html', 'w') as f:
    f.write(html_content)

print("Rapport HTML généré : report.html")
