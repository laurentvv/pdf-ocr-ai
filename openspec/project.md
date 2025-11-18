# Project Context

## Purpose
Ce projet est un convertisseur PDF vers Markdown qui utilise des modèles d'intelligence artificielle pour effectuer de l'OCR avancé. Le système prend en entrée un fichier PDF et utilise un modèle d'IA (LM Studio avec qwen/qwen3-vl-30b) pour convertir chaque page. La sortie finale est un fichier Markdown. L'objectif principal est d'extraire les informations textuelles brutes et surtout les captures d'écran techniques informatiques d'interfaces utilisateur. La solution est particulièrement adaptée à l'extraction de contenu technique contenant des éléments visuels complexes.

## Tech Stack
- Python 3.13
- LM Studio avec le modèle qwen/qwen3-vl-30b pour l'OCR et l'analyse visuelle
- PyMuPDF (fitz) pour la manipulation des PDF
- openai pour les appels API vers LM Studio
- base64 pour l'encodage des images
- markdown pour la génération du Markdown
- pandas pour le traitement des données (si nécessaire)
- pytest pour les tests
- black pour le formatage du code
- flake8 pour le linting

## Project Conventions

### Code Style
- Utiliser Black pour le formatage du code (longueur de ligne : 88 caractères)
- Suivre les conventions de nommage PEP 8
- Utiliser des noms de variables et de fonctions descriptifs
- Rédiger des docstrings pour toutes les fonctions et classes publiques
- Utiliser les annotations de type pour les paramètres et valeurs de retour
- Utiliser les f-strings pour la mise en forme des chaînes de caractères
- Garder les fonctions focalisées sur une seule responsabilité

### Architecture Patterns
- Utiliser une architecture modulaire avec des modules distincts pour le traitement PDF, l'analyse IA et la génération Markdown
- Implémenter une approche pilotée par la configuration pour les options de traitement
- Utiliser l'injection de dépendances là où c'est approprié
- Suivre le principe de responsabilité unique
- Séparer les préoccupations entre extraction des données, traitement et génération de la sortie

### Testing Strategy
- Écrire des tests unitaires pour toutes les fonctions essentielles avec pytest
- Utiliser des tests paramétrés là où c'est approprié
- Inclure des tests pour les cas limites comme les pages voudes, les caractères spéciaux et les PDF mal formés
- Tester la mise en forme de la sortie et la préservation de la structure
- Maintenir au moins 80% de couverture de code
- Utiliser des fixtures de test pour les fichiers PDF d'exemple

### Git Workflow
- Utiliser des branches de fonctionnalités à partir de main pour les nouvelles fonctionnalités
- Suivre le modèle des commits conventionnels (ex. : feat:, fix:, refactor:, test:, docs:)
- Garder les commits atomiques et focalisés sur un seul changement
- Utiliser le rebasing pour maintenir un historique propre
- Créer des pull requests pour la revue de code avant la fusion

## Domain Context
- Les fichiers PDF peuvent contenir des structures internes complexes avec différents encodages de texte, polices intégrées et contenu image
- L'utilisation de modèles d'IA multimodaux permet une reconnaissance avancée des contenus visuels, y compris les captures d'écran techniques
- La conversion nécessite une compréhension du contexte visuel pour extraire correctement les textes et les éléments graphiques
- Les captures d'écran dans les PDFs nécessitent une analyse visuelle approfondie pour en extraire le texte et la structure
- Les modèles de vision/langage permettent de conserver la mise en forme visuelle dans la conversion Markdown
- L'analyse IA peut détecter automatiquement les hiérarchies de titres, les listes et autres structures de document
- Le modèle qwen/qwen3-vl-30b est particulièrement efficace pour l'OCR et la description d'éléments d'interface utilisateur

## Important Constraints
- Gérer les fichiers PDF de tailles variées jusqu'à 100Mo
- Préserver les caractères Unicode et les symboles spéciaux pendant la conversion
- Maintenir la structure et la hiérarchie du document dans le Markdown résultant
- Assurer la conformité en matière d'accessibilité dans le Markdown généré
- Gérer efficacement les appels API vers LM Studio pour éviter les dépassements de quota
- Traiter les fichiers de manière efficace sans usage excessif de la mémoire ou du GPU

## External Dependencies
- LM Studio avec le modèle qwen/qwen3-vl-30b pour l'OCR et l'analyse visuelle
- PyMuPDF (fitz) pour la manipulation des PDF
- openai pour les appels API
- base64 pour l'encodage des images
- PIL/Pillow pour le traitement des images
- python-magic pour la détection du type de fichier
