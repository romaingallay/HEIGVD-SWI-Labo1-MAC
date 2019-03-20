# SWI - Labo1

## Question : quel type de trames sont nécessaires pour détecter les clients de manière passive ?
Il s'agit des probe requests, c'est à dire les trames de type 0 et de sous-type 4

## Question : pourquoi le suivi n'est-il plus possible sur iPhone depuis iOS 8 ?
Car IOS 8+ ajoute une adresse MAC aléatoire aux probe request envoyée pour ne pas divulguer sa véritable adresse MAC. Ainsi cette adresse change à chaque nouvelle probe request envoyée.