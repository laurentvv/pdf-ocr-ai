<div align="center">

# 📄 PDF to Markdown OCR

[![GitHub](https://img.shields.io/badge/GitHub-Repository-333333?logo=github)](https://github.com/laurentvv/pdf-to-md-ocr)
[![Python](https://img.shields.io/badge/Python-3.13+-blue?logo=python)](https://www.python.org/downloads/)
[![uv](https://img.shields.io/badge/uv-Modern%20package%20manager-00a8ff?logo=python)](https://github.com/astral-sh/uv)

**Convertit des documents PDF en Markdown en utilisant les capacités OCR alimentées par plusieurs fournisseurs d'IA**

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
| 🔄 **Support multi-fournisseur** | Fonctionne avec LM Studio, Ollama et llama.cpp |

</div>

## Prérequis

### Prérequis de base
- **Python 3.13+** (requis pour les méthodes d'installation traditionnelles)
- **Un des fournisseurs d'IA suivants** :
  - **LM Studio** exécuté localement avec un modèle de vision (ex. `qwen/qwen3-vl-30b`)
  - **Ollama** exécuté localement avec un modèle de vision (ex. `llava`)
  - **llama.cpp** exécuté localement avec un modèle de vision
- **Matériel** : RAM et VRAM suffisants pour le traitement des PDF (recommandé : 16 Go+ de RAM pour les documents volumineux)

### Prérequis spécifiques à l'installation

#### Pour les méthodes basées sur uv (recommandé) :
- **Gestionnaire de paquets uv** installé (installez avec : `pip install uv`)

#### Pour les méthodes traditionnelles :
- **Gestionnaire de paquets pip**
- Git pour cloner le dépôt (si vous clonez)

## 🚀 Installation

Pour la meilleure expérience, nous recommandons d'utiliser les méthodes basées sur uv. Ces approches offrent une meilleure gestion des dépendances et une utilisation plus simple :

### 🥇 Option 1 : Exécution directe avec uvx (Recommandée - Aucune Installation Requise)

Exécutez l'outil directement depuis le dépôt git sans aucune installation locale. C'est la façon la plus simple d'utiliser l'outil :

<div align="center">

```bash
uvx --from git+https://github.com/laurentvv/pdf-to-md-ocr pdf-ocr-ai <input.pdf> <output.md>
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

- ✅ La commande `pdf-ocr-ai` devient disponible globalement
- ✅ uv gère automatiquement les dépendances dans un environnement isolé
- ✅ Pas besoin de réinstaller à chaque fois que vous utilisez l'outil
- ✅ Meilleure isolation des dépendances qu'avec pip traditionnel
- ✅ Facilité de mise à jour ou de suppression de l'outil
- ✅ Parfait pour une utilisation régulière

</details>

<div align="center">

**Utilisation après installation :**
```bash
pdf-ocr-ai <input.pdf> <output.md>
```

</div>

#### Commandes de gestion de l'outil

<div align="center">

| Commande | Description |
|--------|-------------|
| `uv tool install git+https://github.com/laurentvv/pdf-to-md-ocr` | Installer l'outil |
| `uv tool install --force-reinstall git+https://github.com/laurentvv/pdf-to-md-ocr` | Mettre à jour l'outil |
| `uv tool uninstall pdf-ocr-ai` | Supprimer l'outil |

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

## 📋 Utilisation

<div align="center">

Pour la meilleure expérience, nous recommandons d'utiliser les méthodes basées sur uv :

### 🎯 Commande principale (uvx - Aucune Installation Requise)
```bash
uvx --from git+https://github.com/laurentvv/pdf-to-md-ocr pdf-ocr-ai <input.pdf> <output.md> [options]
```

### 🧰 Outil installé (Après `uv tool install`)
```bash
pdf-ocr-ai <input.pdf> <output.md> [options]
```

### 🔄 Compatibilité descendante
L'outil prend également en charge l'ancien nom de commande pour la compatibilité descendante :
```bash
pdf-ocr-lmstudio <input.pdf> <output.md> [options]
```

</div>

---

### ⚙️ Options de ligne de commande

<div align="center">

| Option | Description | Valeur par défaut |
|--------|-------------|------------------|
| `--provider` | Fournisseur d'IA à utiliser : lm-studio, ollama, llama.cpp | `lm-studio` |
| `--provider-url` | URL personnalisée du fournisseur (dépend du fournisseur) | Voir détails ci-dessous |
| `--model <nom_du_modele>` | Spécifier le modèle à utiliser avec le fournisseur | `qwen/qwen3-vl-30b` |
| `--dpi <valeur>` | Définir le DPI pour la conversion d'image | `300` |

</div>

---

### 💡 Exemples

<div align="center">

#### Démarrage rapide avec LM Studio
```bash
# Exécution directe avec uvx (pas d'installation nécessaire)
uvx --from git+https://github.com/laurentvv/pdf-to-md-ocr pdf-ocr-ai document.pdf output.md
```

#### Utilisation d'Ollama
```bash
# Avec le fournisseur Ollama
uvx --from git+https://github.com/laurentvv/pdf-to-md-ocr pdf-ocr-ai document.pdf output.md --provider ollama --model llava

# Avec une URL Ollama personnalisée
uvx --from git+https://github.com/laurentvv/pdf-to-md-ocr pdf-ocr-ai document.pdf output.md --provider ollama --provider-url http://localhost:11434/v1 --model llava
```

#### Utilisation de llama.cpp
```bash
# Avec le fournisseur llama.cpp
uvx --from git+https://github.com/laurentvv/pdf-to-md-ocr pdf-ocr-ai document.pdf output.md --provider "llama.cpp" --model qwen2-vl
```

#### Utilisation avancée
```bash
# Avec DPI personnalisé
uvx --from git+https://github.com/laurentvv/pdf-to-md-ocr pdf-ocr-ai document.pdf output.md --provider ollama --model llava --dpi 200

# Utilisation de l'ancien nom de commande (compatibilité descendante)
pdf-ocr-lmstudio document.pdf output.md --provider ollama --model llava
```

#### Avec l'outil installé
```bash
# Après installation via l'outil uv
pdf-ocr-ai document.pdf output.md --provider ollama --model llava
```

</div>

## Configuration des fournisseurs d'IA

### Configuration de LM Studio

1. Téléchargez et installez [LM Studio](https://lmstudio.ai/)
2. Dans LM Studio, téléchargez un modèle de vision (recommandé : `qwen/qwen3-vl-30b`)
3. Démarrez le serveur local avec le modèle chargé :
   - Ouvrez LM Studio
   - Sélectionnez votre modèle de vision dans la liste des modèles
   - Cliquez sur le bouton "Load" pour charger le modèle
   - Cliquez sur le bouton "Start Server" pour démarrer le serveur API local
4. Le script se connectera automatiquement à l'API à l'adresse `http://localhost:1234/v1`
5. Assurez-vous que l'option "Enable remote access (allows external connections)" est décochée pour une utilisation locale

### Configuration d'Ollama

1. Téléchargez et installez [Ollama](https://ollama.ai/)
2. Téléchargez un modèle de vision :
   ```bash
   ollama pull llava
   # ou
   ollama pull qwen2-vl
   ```
3. Démarrez Ollama (généralement exécuté automatiquement après installation) :
   ```bash
   ollama serve
   ```
4. Le script se connectera à l'API à l'adresse `http://localhost:11434/v1`

### Configuration de llama.cpp

1. Clonez et compilez [llama.cpp](https://github.com/ggerganov/llama.cpp)
2. Compilez avec le support serveur :
   ```bash
   make
   cd examples/server
   make server
   ```
3. Exécutez le serveur avec un modèle de vision :
   ```bash
   # Commande d'exemple (ajustez les chemins et paramètres selon vos besoins)
   ./server -m path/to/model.gguf --port 8080
   ```
4. Le script se connectera à l'API à l'adresse `http://localhost:8080/v1`

## 🔬 Fonctionnement

<div align="center">

| Étape | Description |
|------|-------------|
| 1️⃣ | Le script convertit chaque page PDF en une image haute résolution (300 DPI) |
| 2️⃣ | Chaque image est envoyée au modèle de vision du fournisseur d'IA sélectionné via l'API |
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
- Le temps de traitement varie considérablement selon le fournisseur d'IA et le modèle utilisé
- Pour les documents volumineux, envisagez de les traiter par lots ou d'utiliser une machine avec suffisamment de RAM
- La vitesse de traitement dépend de la complexité du document, du matériel et des performances du fournisseur d'IA
- Les images haute DPI (300 DPI) offrent une meilleure précision OCR mais prennent plus de temps
- La première exécution peut être plus lente car les modèles sont chargés en mémoire

## Configuration avancée

Le script utilise les paramètres par défaut suivants, qui peuvent être modifiés dans le code source :
- Fournisseur par défaut : lm-studio
- URL LM Studio : http://localhost:1234/v1
- URL Ollama : http://localhost:11434/v1
- URL llama.cpp : http://localhost:8080/v1
- DPI : 300 (pour la qualité de l'image)
- Modèle : qwen/qwen3-vl-30b (modifiable en ligne de commande)
- Tokens max : 2048
- Délai d'attente : 60 secondes
- Tentatives de réessai : 3

## 🛠️ Dépannage

<div align="center">

| Problème | Solution |
|-------|----------|
| 🔌 **Erreurs de connexion API** | Assurez-vous que votre fournisseur d'IA sélectionné (LM Studio/Ollama/llama.cpp) est en cours d'exécution et accessible |
| ❌ **Échec du traitement** | Vérifiez que le nom du modèle dans la commande correspond à ce qui est disponible dans votre fournisseur |
| 💾 **Problèmes de mémoire** | Pour les PDF volumineux, assurez-vous d'avoir au moins 1 Go de RAM par 50 pages |
| 🧠 **Modèle non trouvé** | Vérifiez que le nom du modèle correspond exactement à ce qui est disponible dans votre fournisseur |
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

- `openai` : Pour la communication API avec les fournisseurs d'IA
- `PyMuPDF` : Pour le traitement PDF et l'extraction d'images
- `tqdm` : Pour la visualisation de la barre de progression