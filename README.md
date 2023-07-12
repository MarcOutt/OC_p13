## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/MarcOutt/OC_p13.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- Créer un fichier .env
- Récupérer la clef 
- Ajouter la variable d'environnement API_KEY=DEMANDER_LA_CLEF
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

## Deploiement

### Fonctionnement du déploiement
Le déploiement de l'application est effectué à l'aide de Docker et AWS EC2. Docker est utilisé pour créer une image conteneurisée de l'application, puis l'image est envoyée à EC2 et on lance l'image sur le serveur.

### Configuration requise

Avant de procéder au déploiement, assurez-vous d'avoir les éléments suivants :
- Un serveur compatible Docker (comme un serveur Linux) avec Docker installé.
- Une base de données compatible avec Django configurée et accessible.
- Le port réseau 8000 doit être ouvert pour le trafic HTTP.
- Un compte AWS avec les autorisations nécessaires pour créer et gérer des ressources.

### Étapes de déploiement
1. Configurez un serveur compatible Docker avec les mises à jour système.
2. Installez Docker sur le serveur.
3. Créez une image Docker de l'application en utilisant la commande `docker build -t marcout/lettings-app .`.
4. Envoyez l'image Docker vers Docker Hub en utilisant la commande `docker push marcout/lettings-app:"$SHA1"`.
5. Récupérez l'image Docker de l'application en utilisant la commande `docker pull marcout/lettings-app:latest`.
6. ******

### Circle CI/CD

- Pour chaque modification au niveau de la branche master, circle ci/cd permettra le déclenchement de la conteneurisation et le déploiment du site automatiquement. Le déploimenent se déclenche si seulement si la compilation et les tests sont réussies
- Concernant les modifications d'une branche secondaire, circle ci/cd lancera les tests pour vérifier si les fonctionnalitées du site sont fonctionnelles.

Pour avoir plus d'informations concernant le processus, aller dans le dossier .cirlceci et ouvrir le fichier config.yml

### Configuration de la journalisation avec Sentry

Pour configurer la journalisation avec Sentry dans votre déploiement, suivez les étapes ci-dessous :

1. Créez un compte sur [Sentry](https://sentry.io/) si vous n'en avez pas déjà un.
2. Une fois que vous avez créé le projet, vous recevrez une clé d'authentification (DSN). Cette clé sera utilisée pour configurer la journalisation de votre application.
3. **Ne stockez pas la clé d'authentification Sentry ou d'autres données sensibles dans le code source**. Utilisez plutôt des variables d'environnement pour configurer ces informations en toute sécurité.
4. Allez dans le fichier .env et ajouter la variable d'environnement `SENTRY_DSN=VOTRE_CLEF`
5. Dans votre fichier de configuration Django (`settings.py`), ajoutez les lignes suivantes pour configurer la journalisation avec Sentry :

```python
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

sentry_sdk.init(
    dsn=os.environ.get('SENTRY_DSN'),  # Utilisez la variable d'environnement pour configurer la clé d'authentification Sentry
    integrations=[DjangoIntegration()],
    traces_sample_rate=1.0,  # Pour activer la journalisation des traces de performances
    send_default_pii=True  # Pour inclure les informations d'identification de l'utilisateur dans les rapports d'erreur
)
```
