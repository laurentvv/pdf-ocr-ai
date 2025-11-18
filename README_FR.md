# PDF to Markdown OCR

[![GitHub](https://img.shields.io/badge/GitHub-Repository-333333?logo=github)](https://github.com/laurentvv/pdf-to-md-ocr)

Ce projet convertit des documents PDF en Markdown en utilisant les capacités OCR alimentées par LM Studio avec le modèle qwen/qwen3-vl-30b.

## Fonctionnalités

- Extrait le texte des documents PDF en utilisant un OCR alimenté par l'IA
- Traite les PDF textuels et scannés
- Identifie et décrit les éléments d'interface dans les captures d'écran
- Génère une sortie Markdown structurée en préservant la hiérarchie du document
- Gère les PDF multipages avec traitement individuel des pages
- Suivi de progression en temps réel avec pourcentage et ETA
- Calcul du temps pour les pages individuelles et le traitement global
- Métriques de performance incluant les pages par seconde et le temps moyen de traitement

## Prérequis

- Python 3.13+
- LM Studio exécuté localement avec le modèle qwen/qwen3-vl-30b chargé
- Le modèle qwen/qwen3-vl-30b doit être disponible dans LM Studio

## Installation

1. Installez les dépendances requises :
   ```bash
   pip install -r requirements.txt
   ```

2. Démarrer LM Studio localement et charger le modèle `qwen/qwen3-vl-30b`

## Utilisation

```bash
python pdf_ocr_lmstudio.py <input.pdf> <output.md>
```

### Exemple :
```bash
python pdf_ocr_lmstudio.py document.pdf output.md
```

## Configuration de LM Studio

1. Téléchargez et installez [LM Studio](https://lmstudio.ai/)
2. Dans LM Studio, téléchargez le modèle `qwen/qwen3-vl-30b`
3. Démarrez le serveur local avec le modèle chargé
4. Le script se connectera automatiquement à l'API à l'adresse `http://localhost:1234/v1`

## Fonctionnement

1. Le script convertit chaque page PDF en une image haute résolution (300 DPI)
2. Chaque image est envoyée au modèle visuel LM Studio via l'API
3. Le modèle IA effectue un OCR et identifie les éléments d'interface dans les images
4. Les résultats sont formatés en Markdown structuré
5. Toutes les pages sont combinées en un seul fichier de sortie Markdown
6. La progression s'affiche en temps réel avec le temps restant estimé
7. Les métriques de performance sont calculées et affichées à l'achèvement

## Suivi de progression

Le script inclut un suivi de progression complet :
- Barre de progression visuelle montrant le pourcentage achevé
- Estimation du temps restant (ETA)
- Temps de traitement de chaque page
- Temps moyen de traitement par page
- Métriques de performance globales à l'achèvement

## Dépannage

- Si vous obtenez des erreurs de connexion à l'API, assurez-vous que LM Studio est en cours d'exécution et que le bon modèle est chargé
- Si le traitement échoue, vérifiez que le nom du modèle dans le script correspond à celui dans LM Studio
- Les PDF très volumineux peuvent nécessiter plus de mémoire et de temps de traitement
- Assurez-vous que tqdm est installé pour la fonctionnalité de suivi de progression

## Dépendances

- `openai` : Pour la communication API avec LM Studio
- `PyMuPDF` : Pour le traitement PDF et l'extraction d'images
- `tqdm` : Pour la visualisation de la barre de progression