# Myges Grades Notification 🎓

## Description

Ce projet codé en Python, permet d'envoyer des notifications des nouvelles notes via Telegram en utilisant l'API Skolae.
## Prérequis

- Python 3.x
- pip
- Docker

## Installation

1. Clonez le dépôt :
    ```sh
    git clone https://github.com/Enzo-Qlns/myges-grades-notifications.git
    cd myges-grades-notification
    ```

2. Créez un environnement virtuel et activez-le :
    ```sh
    python -m venv .venv
    source .venv/bin/activate  # Sur Windows, utilisez .venv\Scripts\activate
    ```

3. Installez les dépendances :
    ```sh
    pip install -r requirements.txt
    ```

4. Copiez le fichier `.env.example` en `.env` et remplissez les valeurs nécessaires :
    ```sh
    cp .env.example .env
    ```

5. Créez un bot Telegram et récupérez le token :
    1. Ouvrez Telegram et recherchez le bot `@BotFather`
    2. Créez un nouveau bot en envoyant la commande `/newbot`
    3. Copiez le token du bot
    4. Ouvrez `https://api.telegram.org/bot<TOKEN>/getUpdates` dans votre navigateur
    5. Récupérez l'ID du canal

6. Créez les fichiers `grades.csv` et `app.log` :
    ```sh
    touch grades.csv
    touch app.log
    ```

## Configuration

Modifiez le fichier `.env` :

```dotenv
#############
# MYGES ENV #
#############
MYGES_LOGIN=VotreLogin
MYGES_PASSWORD=VotreMotDePasse

################
# TELEGRAM ENV #
################
TELEGRAM_BOT_TOKEN=VotreBotToken
TELEGRAM_CHANNEL_ID=VotreChannelID
```

## Déploiement

1. Modifiez le fichier .env comme indiqué dans la section [Configuration](#configuration):
2. Exécutez le script :
    ```sh
    chmod +x start_docker.sh
    ```
3. Lancez le script :
    ```sh
    ./start_docker.sh
    ```

## Auteur

[Enzo QUELENIS](www.enzoquelenis.fr)

## License

[MIT](https://choosealicense.com/licenses/mit/)
