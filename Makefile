
submission_$(target):aans.py $(target) pure_ans_$(target)
	python3 aans.py $(target) pure_ans_$(target) > submission_$(target).csv


datalist1: make_datalist.py
	python3 make_datalist.py d/user_4.txt datalist1

datalist2: make_datalist.py
	python3 make_datalist.py d/user_6.txt datalist2


station_$(target): station.py $(target)
	python3 station.py $(target) > station_$(target)

okid_$(target): direction.py direction2.py station_$(target) $(target)
	python3 direction.py station_$(target) > okid_tmp
	python3 direction2.py $(target) >> okid_tmp
	sort -u okid_tmp > okid_$(target)
	rm okid_tmp

pure_ans_$(target): genans.py station_$(target) okid_$(target)
	python3 genans.py station_$(target) > pure_ansx
	echo "positive count: "`wc -l pure_ansx`
	awk -F '|' 'ARGIND==1{ok[$$1]=1}ARGIND==2{if($$1 in ok){print}}' okid_$(target) pure_ansx > pure_ans_$(target)
	wc -l pure_ans_$(target)
	rm pure_ansx

.PHONY: clean
clean: 
	rm pure_ans_datalist? okid_datalist? station_datalist? submission_datalist?.csv

bad: $(target)
	awk -F '\t' '{if ($$3 < 2) {print}}' datalist1 > bad_$(target)
	
railway: railway.txt railway.py $(target)
	python railway.py $(target) >> railway_$(target)