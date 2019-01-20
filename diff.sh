awk -F '|' -v inc=$3 -v rewind=$4 'ARGIND==1{
	c[$1] = 1
}ARGIND==2{
	if ($1 in c) {c[$1] = 0;} else {
		print > inc;
	}
}END{
	for (k in c) {
		if (c[k] == 1) {
			print k > rewind;
		}
	}
}' $1 $2 