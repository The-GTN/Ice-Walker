===========================
**Projet AP2 ,** Ice Walker
===========================

En fin de S3 de licence Info, s'impose la réalisation d'un projet parmi ceux suivants

- Algoritmes génétiques
- Ice walker

Notre choix s'est porté sur Ice-walker, qui  en plus d'être ludique, propose des perspectives d'améliorations assez intéressantes.

L'équipe se compose de 3 membres : Antoine, Bilal et Mathilde. Nous connaissant déjà et ayant déjà travaillé en équipe, la cohésion d'équipe est plutôt bonne et la répartition du travail se fait de aisément.
Voici donc le compte rendu suivant la progression du projet semaine après semaine.

Les outils utilisés
-------------------
- `Github <https://github.com/>`_
- `Atom Teletype <https://teletype.atom.io/>`_
- `Sphinx pour la doc <https://www.sphinx-doc.org/en/master/>`_
- `Beaucoup de café <https://www.youtube.com/watch?v=B2NYNEPC6VA>`_


Semaine 1 
---------
Différentes configurations s'offraient à nous pour gérer la grille. Nous avons tout d'abord pensé à soit la considérer comme un tableau de caractères, soit donner des attributs à des objets (joueurs, cellules) sans utiliser de tableau et les placer dans la grille au moment de l'impresssion à l'écran. Nous avons ensuite aptrès reflexion choisi de mélanger ces idées et de réaliser un tableau de ``Cell`` avec différents attributs listés plus bas.

Après avoir mis en place Atom Téletype, un outil permettant d'interagir à plusieurs sur un même document (une sorte de remote), il a fallu créer l'objet ``Grid``. Furent crées des méthodes permettant de récupérer ou d'écrire une valeur pour chaque attribut de la grille (taille, nombre de joueurs, murs, joueurs, case finale,..). Vient ensuite la construction de la grille qui se fait dans cet ordre :
 
1. créer une matrice aux dimensions de la grille avec un objet ``cell` en chaque élement
2. ajouter les joueurs dans les cell
3. poser les murs dans les cell
4. attribuer cette matrice à l'objet

La class ``Cell`` permet de gérer plus simplement less cases de la grille en lui attribuant un joueur, des murs et un prédicat de victoire et de jouer avec la méthode spéciale __repr__ pour l'afficher proprement dans la console.

La class ``Player``, dont le nom est assez explicite, facilite la gestion des joueurs en leur attribuant des coordonnées, un prédicat disant s'il sagit du joueur principalet encore le numéro du joueur.

Un fichier game.py contient les fonctions permettant au joueur d'intéragir avec le plateau notamment grâce aux différents mouvements disponibles.



Semaine 2
---------

Écriture de la documentation complète des fonctions.

Écriture du ``__str__`` de grid.

Correction de bugs dans la gestion du numéro des joueurs.

Semaine 3 
---------

Correctifs apportés aux différents bugs liés à la gestion des déplacements.

*Ice Walker* est jouable !!

Étant donné l'avancement dans le projet, nous avons décidé de mettre en place une interface graphique. Pour ce faire, nous disposons de différents outils. Notre choix s'est porté sur `Pygame <https://fr.wikipedia.org/wiki/Pygame>`_ , une biblothèque libre facilitant le développement de jeux en python.

Reste à créer l'algorithme perméttant de résoudre, travail déjà entammé par l'équipe de la Project_D.

Semaine 4 
---------

Ecriture de ``queue``. L'algorithme est fonctionnel mais a un petit bug si la grille n'est pas affichée avant. La source du bug est indéterminabe étant donné que l'affichage de la grille n'influence normalement en rien le bon déroulement du jeu ou de la resolution de la grille. Le problème : une fois la case victorieuse atteinte, les autres joueurs ont des comportements incompréhensibles et se déplacent inopinément. Quelle fut notre surprise lorsqu'on a découvert que la solution était d'afficher la grille en début d'algorithme.

Finition du Prezi pour la soutenance de projet.

On a un peu étoffé le thème : ajout d'un retour sur la musique précédente, lancement automatique de la musique suivante.

Ajout d'un petit bonus au lancement du jeu :)

A savoir 
---------

Il faut installer pygame pour pouvoir utiliser l'interface graphique. L'interface s'est bien lancée sur Windows depuis Thonny, mais a montré des problèmes sur Linux.

Pour pouvoir bénéficier du travail fait pour l'interface graphique, je vous invite à l'essayer sur Windows depuis thonny plutôt que sur une console Linux.

Dans src , il faut lancer le programme Pygame.py pour pouvoir jouer au jeu.

Pour quitter à tout moment, vous pouvez cliquer sur la croix de sortie ou taper la touche 'q' ('a' si votre clavier est en qwerti).

Vous devez cliquer sur un personnage pour pouvoir le déplacer avec les flèches directionnelles.

Pour annuler un coup, taper sur la touche back.

Pour retourner à l'état initial des personnages, cliquer sur la case finale.

Pour mettre la musique en pause/ en lecture, taper sur espace. 

Pour reprendre la musique précèdente, taper sur suppr. Et sur entrée pour la musique suivante.

Aussi, si vous avez un retour en particulier ou des questions à nous poser sur notre projet, n'hésitez à nous contacter par mail !

