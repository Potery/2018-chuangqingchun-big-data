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

make target=${file}

cp submission_${file}.csv xdata/${timestr}_${file}_submission.csv
cp pure_ans_${file} xdata/${timestr}_${file}_pure_ans
cp station_${file} xdata/${timestr}_${file}_station
cp okid_${file} xdata/${timestr}_${file}_okid
cp pure_ans_${file} xdata/${timestr}_${file}_pure_ans

last_timestr=`tail -1 xdata/${file}.log`
echo ${timestr} >> xdata/${file}.log

sh diff.sh "xdata/${last_timestr}_${file}_pure_ans" "xdata/${timestr}_${file}_pure_ans" "xdata/${timestr}_${file}_pureans_inc" "xdata/${timestr}_${file}_pureans_rewind"


