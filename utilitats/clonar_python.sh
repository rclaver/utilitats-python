#!/bin/bash
# Rafael Claver

source ~/bin/colores 	#carga la definición de constantes de colores

dir_clone=~/Descargas 	#directori base
branca="master"

function clonar() {
   #$1: branca
   #$2: repositori
   #$3: directori destí
   echo -e ${CB_RED}repositori: $2 ${C_NONE}
   git clone -b $1 git@github.com:rclaver/$2.git $3
}

echo -e ${CB_BLU}Crea una còpia dels repositoris indicats, de la branca $branca, al directori de destí
echo -e El directori destí és un directori buit i temporal relatiu a: $dir_clone ${C_NONE}

cd $dir_clone

dir_desti=IA
repositori=IA
clonar $branca $repositori $dir_desti;

dir_desti=utilitats
repositori=utilitats
clonar $branca $repositori $dir_desti;
