
FROMDIR=./autumn
TODIR=./autumn_sample

SAMPLE=100

N=$(ls -l $FROMDIR | wc -l)
#N/SAMPLE
S_N=$(expr $N / $SAMPLE)
for f in $FROMDIR/*.jpg
do
	A=$(shuf -i 1-$S_N -n 1)
	B=1
	if [ "$A" = "$B" ]; then
		cp "$f" $TODIR
	fi
done
