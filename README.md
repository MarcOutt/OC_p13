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

### Configuration requise:
- Un serveur compatible Docker (comme un serveur Linux) avec Docker installé.
- Base de données compatible avec Django configurée et accessible.
- Port réseau 8000 ouvert pour le trafic HTTP.

### Etapes pour effectuer le déploiment:

#### Configuration de l'environnement
- Configurez un serveur compatible Docker avec les mises à jour système.
- Installez Docker sur le serveur.

#### Créer une image
- S'identifier sur Docker `docker login`
- Créer l'image `docker build -t marcout/lettings-app .`
- Créer un tag `docker tag marcout/lettings-app:latest marcout/lettings-app:"$CIRCLE_SHA1"`
- Envoyer l'image dans docker `docker push marcout/lettings-app:"$SHA1`

#### Récupération de l'image Docker de l'application
- S'identifier sur Docker `docker login`
- Récupérer la version de l'image Docker que vous souhaitez utiliser : `docker pull marcout/lettings-app:latest`


#### Envoyer l'image dans le container Elastic Register
- S'identifier sur Amazon Web Application : `aws ecr-public get-login-password --region us-east-1 | docker login --username AWS --password-stdin public.ecr.aws/f9r8d7r0`
- Taguer l'image pour l'ECR`docker tag marcout/lettings-app:"$SHA1" public.ecr.aws/f9r8d7r0/lettings-app:"${SHA1}"`
- Envoyer l'image à ECR`docker push public.ecr.aws/f9r8d7r0/lettings-app:"${SHA1}"`

#### Déployer l'image ECR
- `aws apprunner update-service \
              -service-arn "arn:aws:apprunner:eu-west-1:935486624820:service/Lettings/e4e745a7cfc14b7bb3a647344759b057" \
              -source-configuration "ImageRepository=             {ImageIdentifier=$ECR_PUBLIC_ARN$SHA1,ImageRepositoryType="public.ecr.aws/f9r8d7r0/lettings-app:"}" \
              --region eu-west-1`

