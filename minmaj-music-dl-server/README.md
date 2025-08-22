# MinMaj Music DL Server

Serveur Django pour télécharger des playlists et musiques depuis SoundCloud.

## 🚀 Installation et démarrage

### Prérequis

- Python 3.8+
- pip
- scdl (outil de téléchargement SoundCloud)

### 1. Cloner le projet

```bash
git clone <url-du-repo>
cd minmaj-music-dl-server
```

### 2. Créer un environnement virtuel

```bash
python -m venv .venv
source .venv/bin/activate  # Sur macOS/Linux
# ou
.venv\Scripts\activate  # Sur Windows
```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 4. Configurer la base de données

```bash
cd minmaj_music_dl
python manage.py migrate
```

### 5. Créer un superutilisateur (optionnel)

```bash
python manage.py createsuperuser
```

### 6. Démarrer le serveur

```bash
python manage.py runserver
```

Le serveur sera accessible sur `http://localhost:8000`

## 🔧 Configuration

### Configuration SoundCloud

1. Allez sur [SoundCloud for Developers](https://developers.soundcloud.com/)
2. Créez une nouvelle application
3. Récupérez votre `client_id` et `client_secret`

### Dossier de téléchargement

Modifiez la constante `DESTINATION_FOLDER` dans `minmaj_music_dl/app/constants.py` pour définir où seront téléchargés vos fichiers :

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

### Exemple d'utilisation

#### Télécharger une playlist

```bash
curl -X POST "http://localhost:8000/api/soundcloud/dl-playlist" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://soundcloud.com/lilefab/sets/tech"}'
```

**Réponse de succès :**
```json
{
  "success": true,
  "message": "Téléchargement terminé avec succès",
  "destination": "/Users/fabienfleisch/Music"
}
```

**Réponse d'erreur :**
```json
{
  "success": false,
  "message": "Erreur lors du téléchargement (code: 1)",
  "destination": "/Users/fabienfleisch/Music"
}
```

## 📚 Documentation et Administration

### Documentation de l'API

Django Ninja génère automatiquement une documentation interactive de votre API. Accédez-y sur :

```
http://localhost:8000/api/docs
```

Cette interface vous permet de :
- Tester tous les endpoints directement
- Voir les schémas de requête et réponse
- Comprendre la structure de l'API

### Interface d'Administration

Gérez toutes vos données via l'interface d'administration Django :

```
http://localhost:8000/admin
```

**Fonctionnalités disponibles :**
- **Credentials** : Configurez vos clés API SoundCloud
- **SoundcloudAuthInformations** : Gérez les tokens d'authentification

**Note :** Toutes les configurations sont stockées en base de données via cette interface.
