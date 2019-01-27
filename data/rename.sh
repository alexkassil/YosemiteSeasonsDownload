for f in *.jpg;
do
	rename -f 's/^(.{19}).*(\..*)$/$1$2/' $f
done
