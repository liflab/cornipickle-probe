# Probe

Développement actuellement avec `Python 2.7.6`, Programmation en anglais (question de se pratiquer un peu :P)

## Dépendances

Il est préférable d'utiliser `virtualenv` avec l'aide de [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/) (Lire attentivement la documentation).

Voir `requirements.txt` pour les versions des dépendance.

    mkvirtualenv probe
    workon probe
    pip install -r requirements.txt

Si vous rencontrez des problèmes à l'installation des dépendances veuillez exécuter

    sudo apt-get install python2.7-dev

Pour rouler le serveur

    export DJANGO_SETTINGS_MODULE=probe_project.settings.local
    export PYTHONUNBUFFERED=1
    python manage.py runserver_plus

Voilà, on est prêt à travailler avec django!

### Installer nodejs et npm

On installe ça pour grunt et bower; compilation automatique du scss et gestion des dépendances côté client (ex: bootstrap, jquery, etc)

#### sous OSX

    brew install nodejs

#### sous Ubuntu

    sudo apt-get install nodejs

#### Installer les dépendances node

    npm install

procède par installer les dépendances mentionnés dans le fichier `package.json`

#### Installer bower en global (dépendances javascript, etc) *facultatif*

Note: n'est pas encore utilisé, on va peut-être s'en servir un jour ;)

    npm install -g bower
    bower install

#### Installer Grunt en global

    npm install -g grunt-cli
    grunt

Il est peut-être nécessaire d'ajouter les apps de nodejs PATH

    export PATH="/usr/local/share/npm/bin:$PATH"

enjoy

## Traduction du site

    django-admin.py makemessages -a -e py,jinja,jinja2,html -l fr --ignore node_modules

Les fichiers `po` pour la traduction se trouvent dans `./conf/local/`. Après, c'est classique; on passe par [Poedit](http://poedit.net/).

## Mise à jour des models

Dans ce projet, on utilise [South](http://south.aeracode.org/), présent dans la pluspart des projets django, ça permet de faire des migrations de la base de données.

### Commandes south

Le mieux, c'est de lire la [documentation de south](http://south.readthedocs.org/en/latest/tutorial/index.html), mais voici quand même les grandes lignes

Après la création d'un model, on execute habituellement `./manage.py syncdb`, Comme c'est le point initial du model, on cré donc un schema de migration;

    ./manage.py schemamigration nom_app --initial

On applique ensuite la migration

    ./manage.py migrate nom_app

Quand on modifie un model déjà existant, on s'assure qu'avant, il ait une migration initiale d'effectué (se trouve dans le dossier `migrations` à côté du dossier `mon_app`.

    ./manage.py schemamigration nom_app --auto

Puis on applique les migrations

    ./manage.py migrate mon_app

### Example

Disons que j'ajoute un champ `date` dans le model `Probe` de l'application `probe_dispatcher`, j'exécuterai ces commandes:

    ./manage.py schemamigration probe_dispatcher --auto
    ./manage.py migrate

## Installation et compilation de Cornipickle

Veuillez vous référer à l'installation de Cornipickle sur le [répertoire Cornipickle](https://bitbucket.org/sylvainhalle/cornipickle).
