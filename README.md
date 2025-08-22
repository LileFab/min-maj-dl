# 🎵 MinMajDL - Application de Téléchargement Musical

Une application complète pour télécharger vos playlists SoundCloud et Spotify en local, composée d'un serveur Django et d'une interface web Nuxt.js.

## 📋 Description

MinMajDL est une solution complète qui permet de :
- **Serveur Backend** : API Django avec authentification SoundCloud et gestion des téléchargements
- **Interface Web** : Interface utilisateur moderne construite avec Nuxt.js 4 et Tailwind CSS
- **Téléchargement** : Récupération de playlists SoundCloud et Spotify en haute qualité
- **Gestion des Credentials** : Configuration sécurisée des clés API

## 🏗️ Architecture

```
min-maj-dl/
├── client/                 # Frontend Nuxt.js
│   ├── app/               # Pages et composants Vue
│   ├── assets/            # CSS et ressources
│   └── package.json       # Dépendances frontend
└── minmaj-music-dl-server/ # Backend Django
    ├── minmaj_music_dl/   # Application Django
    ├── requirements.txt    # Dépendances Python
    └── manage.py          # Gestionnaire Django
```

## 🚀 Installation Rapide

### Prérequis
- **Node.js** (version 18+)
- **Python** (version 3.8+)
- **Git**

### 1. Cloner le projet
```bash
git clone <votre-repo>
cd min-maj-dl
```

### 2. Installer et configurer le Backend
```bash
cd minmaj-music-dl-server
python -m venv .venv
source .venv/bin/activate  # Sur macOS/Linux
# ou
.venv\Scripts\activate     # Sur Windows

pip install -r requirements.txt
pip install scdl  # Outil de téléchargement SoundCloud

cd minmaj_music_dl
python manage.py migrate
python manage.py runserver
```

### 3. Installer et configurer le Frontend
```bash
cd client
npm install
npm run dev
```

### 4. Accéder à l'application
- **Interface Web** : http://localhost:3000
- **API Backend** : http://localhost:8000
- **Documentation API** : http://localhost:8000/api/docs
- **Admin Django** : http://localhost:8000/admin

## ⚙️ Configuration

### 1. Credentials SoundCloud
1. Allez sur [SoundCloud for Developers](https://developers.soundcloud.com/)
2. Créez une nouvelle application
3. Récupérez votre `client_id` et `client_secret`

### 2. Credentials Spotify
1. Allez sur [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
2. Créez une nouvelle application
3. Récupérez votre `client_id` et `client_secret`

### 3. Dossier de téléchargement
Modifiez la constante `DESTINATION_FOLDER` dans `minmaj-music-dl-server/minmaj_music_dl/app/constants.py` :

```python
DESTINATION_FOLDER = "/chemin/vers/votre/dossier/musique"
```

## 📡 API Endpoints

### Base URL
```
http://localhost:8000/api
```

### Endpoints disponibles

#### Credentials
- `GET /credentials/` - Récupérer les credentials
- `POST /credentials/create-or-update` - Créer ou mettre à jour les credentials

#### SoundCloud Auth
- `GET /sc_auth_infos/` - Récupérer les informations d'authentification
- `GET /sc_auth_infos/authentificate` - Authentifier et obtenir un token

#### SoundCloud
- `GET /soundcloud/playlists` - Récupérer les playlists
- `GET /soundcloud/liked` - Récupérer les musiques likées
- `GET /soundcloud/username` - Récupérer le nom d'utilisateur
- `POST /soundcloud/dl-playlist` - Télécharger une playlist

## 🎯 Utilisation

### 1. Configuration des Credentials
- Accédez à la page `/credentials`
- Renseignez vos clés API SoundCloud et Spotify
- Sauvegardez la configuration

### 2. Gestion des Playlists
- Accédez à la page `/playlists`
- Visualisez toutes vos playlists SoundCloud
- Téléchargez individuellement chaque playlist

### 3. Téléchargement
- Cliquez sur "Télécharger" pour une playlist
- Suivez le statut en temps réel
- Les fichiers sont sauvegardés dans le dossier configuré