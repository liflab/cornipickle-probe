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

Voilà, on est prêt à travailler avec django!

### Installer nodejs et npm

On installe ça pour grunt et bower; compilation automatique du scss et gestion des dépendances côté client (ex: bootstrap, jquery, etc)

#### sous OSX

    brew install nodejs

#### sous Ubuntu

    apt=get install nodejs

#### Installer les dépendances node

    npm install

procède par installer les dépendances mentionnés dans le fichier `package.json`

#### Installer bower en global (dépendances javascript, etc)

    npm install -g bower
    bower install

#### Installer Grunt en global

    npm install -g grunt-cli
    grunt

Il est peut-être nécessaire d'ajouter les apps de nodejs PATH

    export PATH="/usr/local/share/npm/bin:$PATH"

enjoy

## Traduction du site

    django-admin.py makemessages -l fr --ignore node_modules

Les fichiers `po` pour la traduction se trouvent dans `./conf/local/`. Après, c'est classique; on passe par PO Edit.
