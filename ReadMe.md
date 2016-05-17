# Probe

Développement actuellement avec `Python 2.7.6`, Programmation en anglais (question de se pratiquer un peu :P)
IDE recommandé: PyCharm Community Edition de JetBrains](https://www.jetbrains.com/pycharm/download/)

Il est recommandé de lire [Getting started](https://docs.djangoproject.com/en/1.8/intro/) dans la doc de django
avant de débuter à travailler sur ce projet, ça sera beaucoup plus simple par la suite.

## Installation

### Dépendances

Il est préférable d'utiliser `virtualenv` avec l'aide de 
[virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/) 
(Lire attentivement la documentation).

Voir `requirements.txt` pour les dépendances.

    mkvirtualenv probe
    workon probe
    pip install -r requirements.txt

Sous Ubuntu, si vous rencontrez des problèmes à l'installation des dépendances, exécuter

    sudo apt-get install python2.7-dev

### Base de données

Vous devrez exécuter les migrations pour initialiser la base de données

    ./manage.py migrate

Se créer un utilisateur superuser

    python manage.py createsuperuser --username=joe --email=joe@example.com

### Exécution du serveur

Pour démarer le serveur en mode dev:

    export DJANGO_SETTINGS_MODULE=probe_project.settings.local
    export PYTHONUNBUFFERED=1
    python manage.py runserver_plus

Voilà, on est prêt à travailler avec django!


## Traduction du site

Documentation django](https://docs.djangoproject.com/en/1.8/topics/i18n/translation/)

    django-admin.py makemessages -a -e py,jinja,jinja2,html -l fr --ignore node_modules

Les fichiers `po` pour la traduction se trouvent dans `./conf/locale/<lang_code>/LC_MESSAGES/django.po`. 
Après, c'est classique; on passe par [Poedit](http://poedit.net/).
[Weblate](https://weblate.org/en/) peut être une bonne idée une fois en production ;)

## Développement et outils

### Installer nodejs](https://nodejs.org/) et [npm](https://www.npmjs.com/)

On installe ça pour grunt](http://gruntjs.com/) et [bower](http://bower.io/) 
compilation automatique du [scss](http://sass-lang.com/) et 
gestion des dépendances (js) côté client (ex: bootstrap, jquery, etc)

#### sous OSX

    brew install nodejs

#### sous Ubuntu


    # Node
    sudo apt-get install nodejs

    # NPM
    sudo apt-get install -y npm

    ln -s /usr/bin/nodejs /usr/bin/node

#### Installer les dépendances node

    npm install

Cette commande va installer les dépendances mentionnées dans le fichier `package.json`

### Installer bower (outil de gestion de dépendances javascript, etc)

    npm install -g bower
    bower install

    # Récupération des fichiers statiques pour Django
    sudo python manage.py collectstatic --noinput

### Installer Grunt

[grunt](http://gruntjs.com/)

    npm install -g grunt-cli
    grunt

Il est peut-être nécessaire d'ajouter le dossier d'installation des applications npm dans 
la variable d'environnement `$PATH` pour exécuter les apps installées avec npm.

    export PATH="/usr/local/share/npm/bin:$PATH"
    
    
## Installation et compilation de Cornipickle

Veuillez vous référer à l'installation de Cornipickle sur le [répertoire Cornipickle](https://bitbucket.org/sylvainhalle/cornipickle).
