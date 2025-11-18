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

### Prérequis de base
- **Python 3.13+** (requis pour les méthodes d'installation traditionnelles)
- **LM Studio** exécuté localement avec le modèle `qwen/qwen3-vl-30b` chargé
- **Matériel** : RAM et VRAM suffisants pour le traitement des PDF (recommandé : 16 Go+ de RAM pour les documents volumineux)

### Prérequis spécifiques à l'installation

#### Pour les méthodes basées sur uv (recommandé) :
- **Gestionnaire de paquets uv** installé (installez avec : `pip install uv`)
- LM Studio avec le modèle `qwen/qwen3-vl-30b` chargé

#### Pour les méthodes traditionnelles :
- **Gestionnaire de paquets pip**
- Git pour cloner le dépôt (si vous clonez)
- LM Studio avec le modèle `qwen/qwen3-vl-30b` chargé

### Configuration de LM Studio
Avant d'utiliser l'outil, vous devez configurer LM Studio :
1. Téléchargez et installez [LM Studio](https://lmstudio.ai/)
2. Dans LM Studio, téléchargez le modèle `qwen/qwen3-vl-30b` (c'est le modèle recommandé pour des résultats optimaux)
3. Démarrez le serveur local avec le modèle chargé :
   - Ouvrez LM Studio
   - Sélectionnez le modèle `qwen/qwen3-vl-30b` dans votre liste de modèles
   - Cliquez sur le bouton "Load" pour charger le modèle
   - Cliquez sur le bouton "Start Server" pour démarrer le serveur API local
4. Le script se connectera automatiquement à l'API à l'adresse `http://localhost:1234/v1`
5. Assurez-vous que l'option "Enable remote access (allows external connections)" est décochée pour une utilisation locale
6. Pour de meilleurs résultats, assurez-vous d'avoir suffisamment de VRAM allouée au modèle dans LM Studio

## Installation

Vous pouvez utiliser cet outil de plusieurs manières :

### Option 1 : Exécution directe avec uvx (pas d'installation nécessaire)
```bash
uvx --from git+https://github.com/laurentvv/pdf-to-md-ocr pdf-ocr-lmstudio <input.pdf> <output.md>
```

### Option 2 : Installation en tant qu'outil avec uv
Cette méthode installe définitivement l'outil dans votre environnement, le rendant disponible comme utilitaire en ligne de commande. L'outil est installé dans un environnement isolé géré par uv, ce qui empêche les conflits de dépendances avec d'autres projets Python sur votre système.

Avantages de cette approche :
- La commande `pdf-ocr-lmstudio` devient disponible globalement dans votre terminal
- uv gère automatiquement les dépendances dans un environnement isolé
- Pas besoin de réinstaller à chaque fois que vous voulez utiliser l'outil
- Meilleure isolation des dépendances qu'avec l'installation pip traditionnelle
- Facilité de mise à jour ou de suppression de l'outil ultérieurement

Pour installer et utiliser :
```bash
uv tool install git+https://github.com/laurentvv/pdf-to-md-ocr
# Puis utilisez : pdf-ocr-lmstudio <input.pdf> <output.md>
```

Pour mettre à jour l'outil ultérieurement :
```bash
uv tool install --force-reinstall git+https://github.com/laurentvv/pdf-to-md-ocr
```

Pour supprimer l'outil :
```bash
uv tool uninstall pdf-ocr-lmstudio
```

### Option 3 : Installation traditionnelle
1. Clonez le dépôt et installez les dépendances requises :
   ```bash
   pip install -r requirements.txt
   ```
   OU avec uv :
   ```bash
   uv sync
   ```

2. Démarrez LM Studio localement et chargez le modèle `qwen/qwen3-vl-30b`

### Note sur requirements.txt et pyproject.toml
Ce projet utilise maintenant `pyproject.toml` comme source principale pour les dépendances et les métadonnées du projet. Le fichier `requirements.txt` est maintenu pour des raisons de compatibilité avec les anciennes versions de pip. Pour les nouvelles installations, le fichier `pyproject.toml` sera utilisé automatiquement par des outils modernes comme uv.

## Utilisation

Après installation traditionnelle :
```bash
python pdf_ocr_lmstudio.py <input.pdf> <output.md>
```

Après installation avec l'outil uv :
```bash
pdf-ocr-lmstudio <input.pdf> <output.md>
```

### Exemple :
```bash
# Installation traditionnelle
python pdf_ocr_lmstudio.py document.pdf output.md

# Ou exécuté directement via uvx
uvx --from git+https://github.com/laurentvv/pdf-to-md-ocr pdf-ocr-lmstudio document.pdf output.md

# Ou si installé via l'outil uv
pdf-ocr-lmstudio document.pdf output.md
```

## Prérequis

- Python 3.13+ (pour l'installation traditionnelle)
- uv (pour les méthodes d'installation uv)
- LM Studio exécuté localement avec le modèle qwen/qwen3-vl-30b chargé
- Le modèle qwen/qwen3-vl-30b doit être disponible dans LM Studio (voir la section Configuration de LM Studio ci-dessous)
- Serveur LM Studio local en cours d'exécution avec le modèle chargé (point de terminaison API par défaut : http://localhost:1234/v1)

## Configuration du développement

### Configuration de l'environnement virtuel (Méthode traditionnelle)
1. Créez un environnement virtuel :
   ```bash
   python -m venv .venv
   ```
2. Activez l'environnement :
   - Windows : `.venv\Scripts\activate`
   - macOS/Linux : `source .venv/bin/activate`
3. Installez les dépendances :
   ```bash
   pip install -e .
   ```

### Configuration de l'environnement virtuel (Méthode uv)
1. Créez un environnement virtuel avec uv :
   ```bash
   uv venv
   ```
2. Activez l'environnement (uv utilisera sa propre gestion d'environnement virtuel)
3. Installez les dépendances :
   ```bash
   uv sync
   ```

### Utilisateurs de VSCode sur Windows
Lorsque vous utilisez des environnements virtuels uv, vous devrez peut-être sélectionner manuellement l'interpréteur Python dans VSCode :
1. Ouvrez VSCode dans le répertoire du projet
2. Appuyez sur `Ctrl+Maj+P` pour ouvrir la palette de commandes
3. Tapez "Python: Sélectionner l'interpréteur" et sélectionnez-le
4. Choisissez l'interpréteur de votre environnement virtuel uv
   - Vous pouvez le localiser en exécutant `uv venv --path` pour voir l'emplacement de l'environnement
   - L'interpréteur Python se trouve généralement dans `.venv\Scripts\python.exe` (lors de l'utilisation de `uv venv .venv`) ou dans un chemin comme `%USERPROFILE%\AppData\Local\uv\...` lors de l'utilisation d'environnements uv globaux (Windows)
   - Pour macOS/Linux, l'interpréteur Python se trouve dans `bin/python`

## Configuration de LM Studio

1. Téléchargez et installez [LM Studio](https://lmstudio.ai/)
2. Dans LM Studio, téléchargez le modèle `qwen/qwen3-vl-30b` (c'est le modèle recommandé pour des résultats optimaux)
3. Démarrez le serveur local avec le modèle chargé :
   - Ouvrez LM Studio
   - Sélectionnez le modèle `qwen/qwen3-vl-30b` dans votre liste de modèles
   - Cliquez sur le bouton "Load" pour charger le modèle
   - Cliquez sur le bouton "Start Server" pour démarrer le serveur API local
4. Le script se connectera automatiquement à l'API à l'adresse `http://localhost:1234/v1`
5. Assurez-vous que l'option "Enable remote access (allows external connections)" est décochée pour une utilisation locale
6. Pour de meilleurs résultats, assurez-vous d'avoir suffisamment de VRAM allouée au modèle dans LM Studio

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

## Considérations de performance

- Les PDF volumineux (>100 pages) peuvent nécessiter une quantité substantielle de mémoire (plusieurs Go)
- Le temps de traitement est d'environ 10-30 secondes par page selon la complexité
- Pour les documents volumineux, envisagez de les traiter par lots ou d'utiliser une machine avec suffisamment de RAM
- La vitesse de traitement dépend de la complexité du document et du matériel
- Les images haute DPI (300 DPI) offrent une meilleure précision OCR mais prennent plus de temps
- La première exécution peut être plus lente car les modèles sont chargés en mémoire

## Configuration avancée

Le script utilise les paramètres par défaut suivants, qui peuvent être modifiés dans le code source :
- DPI : 300 (pour la qualité de l'image)
- Modèle : qwen/qwen3-vl-30b (modifiable dans le code source)
- Tokens max : 2048
- Délai d'attente : 60 secondes
- Tentatives de réessai : 3

## Dépannage

- Si vous obtenez des erreurs de connexion à l'API, assurez-vous que LM Studio est en cours d'exécution et que le bon modèle est chargé
- Si le traitement échoue, vérifiez que le nom du modèle dans le script correspond à celui dans LM Studio
- Pour les PDF volumineux, assurez-vous d'avoir au moins 1 Go de RAM par 50 pages
- Envisagez de fermer d'autres applications avant de traiter des documents volumineux
- Si vous rencontrez des erreurs de mémoire, essayez de traiter des PDF plus petits
- Les PDF très volumineux peuvent nécessiter plus de mémoire et de temps de traitement
- Assurez-vous que tqdm est installé pour la fonctionnalité de suivi de progression
- Lors de l'utilisation de uv, assurez-vous que uv est correctement installé : `pip install uv`

## Migration depuis le .venv traditionnel vers uv

Si vous avez un répertoire `.venv` existant et que vous souhaitez passer à la gestion d'environnement basée sur uv :

1. Sauvegardez votre configuration actuelle si nécessaire
2. Conservez votre `.venv` existant si vous souhaitez y revenir plus tard
3. Utilisez plutôt les commandes uv :
   ```bash
   uv venv  # Crée un nouvel environnement géré par uv
   uv sync  # Installe les dépendances avec uv
   ```
4. Lors de l'activation des environnements, utilisez les commandes uv ou sélectionnez manuellement l'interpréteur dans votre IDE

## Dépendances

- `openai` : Pour la communication API avec LM Studio
- `PyMuPDF` : Pour le traitement PDF et l'extraction d'images
- `tqdm` : Pour la visualisation de la barre de progression