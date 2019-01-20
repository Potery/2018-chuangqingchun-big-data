python3 route.py ${1} > ${1}.route
python3 check_line.py ${1}.route > ${1}.line
python3 genansx.py ${1}.line > ${1}.sans
python3 aans.py ${1} ${1}.sans > ${1}.sub.csv