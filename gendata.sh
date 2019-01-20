file=${1}
timestr=`date +%Y-%m-%d-%H-%M`

if [ "${file}" = 'datalist1' ]; then
    raw_file=d/user_4.txt
else
    if [ "${file}" = 'datalist2' ]; then
        raw_file=d/user_6.txt
    else
        echo 'ERROR'
        exit -1
    fi
fi

if [ ! -f ${file} ]; then
    echo "make ${file}"
    python3 make_datalist.py $raw_file $file
fi
echo "${file} is ok"
echo "test station"
python3 station.py ${file} > ${timestr}_station
echo "test driection 1"
python3 direction.py ${timestr}_station > ${timestr}_okid_tmp
echo "test driection 2"
python3 direction2.py $file >> ${timestr}_okid_tmp
sort -u ${timestr}_okid_tmp > ${timestr}_okid
python3 genans.py ${timestr}_station > ${timestr}_pure_ans
echo "positive count: "`wc -l ${timestr}_pure_ans`
python3 aans.py ${file} ${timestr}_pure_ans > ${timestr}_submission.csv

echo ${timestr} >> xlog