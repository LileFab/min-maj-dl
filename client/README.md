# 🎵 MinMajDL - Client de Téléchargement Musical

Une application web moderne pour télécharger vos playlists SoundCloud et Spotify en local.

## 📋 Description

MinMajDL est une interface utilisateur intuitive construite avec **Nuxt.js 4** et **Tailwind CSS** qui permet de :
- Configurer vos credentials API SoundCloud et Spotify
- Lister et gérer vos playlists SoundCloud
- Télécharger des playlists complètes en local
- Interface responsive et moderne

## 🚀 Installation

### Prérequis
- **Node.js** (version 18+)
- **npm**, **yarn**, **pnpm** ou **bun**
- **API backend** MinMajDL en cours d'exécution sur `http://127.0.0.1:8000`

### Étapes d'installation

1. **Cloner le projet**
```bash
git clone <votre-repo>
cd minmaj-music-dl-client/client
```

2. **Installer les dépendances**
```bash
npm install
# ou
yarn install
# ou
pnpm install
# ou
bun install
```

3. **Lancer le serveur de développement**
```bash
npm run dev
# ou
yarn dev
# ou
pnpm dev
# ou
bun run dev
```

4. **Accéder à l'application**
Ouvrez votre navigateur sur `http://localhost:3000`

## 🎯 Utilisation

### Page d'accueil
- Vue d'ensemble de l'application
- Accès rapide aux fonctionnalités principales
- Navigation vers la configuration des credentials

### Page Credentials (`/credentials`)
- Configuration des clés API SoundCloud et Spotify
- Sauvegarde automatique des paramètres
- Validation des données avant envoi

### Page Playlists (`/playlists`)
- Liste complète de vos playlists SoundCloud
- Statistiques globales (nombre de playlists, durée totale, nombre de titres)
- Téléchargement individuel de chaque playlist
- Suivi en temps réel du statut des téléchargements