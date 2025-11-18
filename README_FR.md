<div align="center">

# 📄 PDF to Markdown OCR

[![GitHub](https://img.shields.io/badge/GitHub-Repository-333333?logo=github)](https://github.com/laurentvv/pdf-to-md-ocr)
[![Python](https://img.shields.io/badge/Python-3.13+-blue?logo=python)](https://www.python.org/downloads/)
[![uv](https://img.shields.io/badge/uv-Modern%20package%20manager-00a8ff?logo=python)](https://github.com/astral-sh/uv)

**Convertit des documents PDF en Markdown en utilisant les capacités OCR alimentées par LM Studio**

*Alimenté par des modèles IA pour une extraction de texte précise et la reconnaissance d'éléments UI*

</div>

---

## ✨ Fonctionnalités

<div align="center">

| Fonctionnalité | Description |
|--------|-------------|
| 🧠 **OCR alimenté par IA** | Extrait le texte des documents PDF en utilisant des modèles IA avancés |
| 🔍 **Support multi-format** | Traite les PDF textuels et scannés |
| 💻 **Reconnaissance éléments UI** | Identifie et décrit les éléments d'interface dans les captures d'écran |
| 📝 **Sortie structurée** | Génère du Markdown structuré en préservant la hiérarchie du document |
| 📄 **Gestion multi-pages** | Gère les PDF multipages avec traitement individuel des pages |
| 📊 **Suivi de progression** | Suivi en temps réel avec pourcentage et ETA |
| ⚡ **Métriques de performance** | Calculs de temps et d'analyse de performance |

</div>

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

## 🚀 Installation

Pour la meilleure expérience, nous recommandons d'utiliser les méthodes basées sur uv. Ces approches offrent une meilleure gestion des dépendances et une utilisation plus simple :

### 🥇 Option 1 : Exécution directe avec uvx (Recommandée - Aucune Installation Requise)

Exécutez l'outil directement depuis le dépôt git sans aucune installation locale. C'est la façon la plus simple d'utiliser l'outil :

<div align="center">

```bash
uvx --from git+https://github.com/laurentvv/pdf-to-md-ocr pdf-ocr-lmstudio <input.pdf> <output.md>
```

</div>

<details>
<summary><b>Pourquoi cette approche ?</b></summary>

- ✅ Aucune installation locale requise
- ✅ Utilise toujours la dernière version
- ✅ Résolution automatique des dépendances
- ✅ Aucun conflit avec d'autres projets Python
- ✅ Parfait pour une utilisation ponctuelle

</details>

---

### 🥈 Option 2 : Installation en tant qu'outil avec uv (Recommandée pour une utilisation régulière)

Cette méthode installe définitivement l'outil dans votre environnement, le rendant disponible comme utilitaire en ligne de commande.

<div align="center">

```bash
uv tool install git+https://github.com/laurentvv/pdf-to-md-ocr
```

</div>

<details>
<summary><b>Avantages de cette approche</b></summary>

- ✅ La commande `pdf-ocr-lmstudio` devient disponible globalement
- ✅ uv gère automatiquement les dépendances dans un environnement isolé
- ✅ Pas besoin de réinstaller à chaque fois que vous utilisez l'outil
- ✅ Meilleure isolation des dépendances qu'avec pip traditionnel
- ✅ Facilité de mise à jour ou de suppression de l'outil
- ✅ Parfait pour une utilisation régulière

</details>

<div align="center">

**Utilisation après installation :**
```bash
pdf-ocr-lmstudio <input.pdf> <output.md>
```

</div>

#### Commandes de gestion de l'outil

<div align="center">

| Commande | Description |
|--------|-------------|
| `uv tool install git+https://github.com/laurentvv/pdf-to-md-ocr` | Installer l'outil |
| `uv tool install --force-reinstall git+https://github.com/laurentvv/pdf-to-md-ocr` | Mettre à jour l'outil |
| `uv tool uninstall pdf-ocr-lmstudio` | Supprimer l'outil |

</div>

---

### 🥉 Option 3 : Installation traditionnelle (Pour le développement)

Seulement recommandée si vous prévoyez de modifier le code ou de travailler avec un environnement virtuel :

1. Clonez le dépôt et installez les dépendances requises depuis pyproject.toml :
   ```bash
   pip install .
   ```
   OU avec uv :
   ```bash
   uv sync
   ```

2. Démarrez LM Studio localement et chargez le modèle `qwen/qwen3-vl-30b`

## 📋 Utilisation

<div align="center">

Pour la meilleure expérience, nous recommandons d'utiliser les méthodes basées sur uv :

### 🎯 Commande principale (uvx - Aucune Installation Requise)
```bash
uvx --from git+https://github.com/laurentvv/pdf-to-md-ocr pdf-ocr-lmstudio <input.pdf> <output.md> [options]
```

### 🧰 Outil installé (Après `uv tool install`)
```bash
pdf-ocr-lmstudio <input.pdf> <output.md> [options]
```

</div>

---

### ⚙️ Options de ligne de commande

<div align="center">

| Option | Description | Valeur par défaut |
|--------|-------------|------------------|
| `--model <nom_du_modele>` | Spécifier le modèle à utiliser dans LM Studio | `qwen/qwen3-vl-30b` |
| `--dpi <valeur>` | Définir le DPI pour la conversion d'image | `300` |

</div>

---

### 💡 Exemples

<div align="center">

#### Démarrage rapide
```bash
# Exécution directe avec uvx (pas d'installation nécessaire)
uvx --from git+https://github.com/laurentvv/pdf-to-md-ocr pdf-ocr-lmstudio document.pdf output.md
```

#### Utilisation avancée
```bash
# Avec modèle personnalisé en utilisant uvx
uvx --from git+https://github.com/laurentvv/pdf-to-md-ocr pdf-ocr-lmstudio document.pdf output.md --model "llama/llama3.2-vision"

# Avec DPI personnalisé en utilisant uvx
uvx --from git+https://github.com/laurentvv/pdf-to-md-ocr pdf-ocr-lmstudio document.pdf output.md --dpi 200

# Avec modèle et DPI personnalisés en utilisant uvx
uvx --from git+https://github.com/laurentvv/pdf-to-md-ocr pdf-ocr-lmstudio document.pdf output.md --model "llama/llama3.2-vision" --dpi 150
```

#### Avec l'outil installé
```bash
# Après installation via l'outil uv
pdf-ocr-lmstudio document.pdf output.md --model "llama/llama3.2-vision"
```

</div>

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

## 🔬 Fonctionnement

<div align="center">

| Étape | Description |
|------|-------------|
| 1️⃣ | Le script convertit chaque page PDF en une image haute résolution (300 DPI) |
| 2️⃣ | Chaque image est envoyée au modèle visuel LM Studio via l'API |
| 3️⃣ | Le modèle IA effectue un OCR et identifie les éléments d'interface dans les images |
| 4️⃣ | Les résultats sont formatés en Markdown structuré |
| 5️⃣ | Toutes les pages sont combinées en un seul fichier de sortie Markdown |
| 6️⃣ | La progression s'affiche en temps réel avec le temps restant estimé |
| 7️⃣ | Les métriques de performance sont calculées et affichées à l'achèvement |

</div>

## 📊 Suivi de progression

<div align="center">

| Fonctionnalité | Description |
|--------|-------------|
| 📈 **Barre de progression visuelle** | Affiche le pourcentage achevé en temps réel |
| ⏳ **ETA** | Estimation du temps restant |
| ⏱️ **Timing par page** | Temps de traitement de chaque page |
| 📉 **Timing moyen** | Temps moyen de traitement par page |
| 📋 **Résumé des performances** | Métriques globales à l'achèvement |

</div>

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

## 🛠️ Dépannage

<div align="center">

| Problème | Solution |
|-------|----------|
| 🔌 **Erreurs de connexion API** | Assurez-vous que LM Studio est en cours d'exécution et que le bon modèle est chargé |
| ❌ **Échec du traitement** | Vérifiez que le nom du modèle dans la commande correspond à celui dans LM Studio |
| 💾 **Problèmes de mémoire** | Pour les PDF volumineux, assurez-vous d'avoir au moins 1 Go de RAM par 50 pages |
| 🧠 **Modèle non trouvé** | Vérifiez que le nom du modèle correspond exactement à ce qui est disponible dans LM Studio |
| ⚠️ **Problèmes de performance** | Fermez d'autres applications avant de traiter des documents volumineux |
| 🚫 **Erreurs de mémoire** | Essayez de traiter des PDF plus petits ou augmentez les ressources système |
| 📊 **Barre de progression manquante** | Assurez-vous que tqdm est disponible dans votre environnement Python |
| 🐍 **Problèmes d'installation uv** | Assurez-vous que uv est correctement installé : `pip install uv` |

</div>

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