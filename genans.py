import sys
# UID|1|20180111080355|20180111093718

def station_v(station):
    if 'nanjing' in station:
        return 0
    if 'zhenjiang' in station:
        return 1
    if 'changzhou' in station:
        return 2
    if 'wuxi' in station:
        return 3
    if 'suzhou' in station:
        return 4
    if 'shanghai' in station or 'hongqiao' in station:
        return 5
    raise Exception('invalied station name')
    
with open(sys.argv[1], encoding='utf8') as f:
    for l in f:
        id, ss = l.split('\t')
        sss = ss.strip('\n').split(',')
        if len(sss) < 3:
            pass
            #print ('%s|1|%s|%s' %(id, sss[0].split('-')[1], sss[0].split('-')[1]))
        else:
            #print (sss)
            station = []
            cur_sv = station_v(sss[0].split('-')[0])
            first_index = 0
            i = 1
            while i < len(sss) - 1:
                xxx = sss[i].split('-')
                if len(xxx) == 2:
                    nsv = station_v(xxx[0])
                    if nsv > cur_sv:
                        first_index = i - 1
                        break
                    cur_sv = nsv
                i += 1
            
            last_index = -2
            i = first_index + 1
            cur_sv = station_v(sss[first_index].split('-')[0])
            while i < len(sss) - 1:
                xxx = sss[i].split('-')
                if len(xxx) == 2:
                    nsv = station_v(xxx[0])
                    if nsv not in station:
                        station.append(nsv)
                    if nsv < cur_sv:
                        last_index = i - 1
                        break
                    cur_sv = nsv
                i += 1
            if len(station) > 1: #last_index > 0:
                print ('%s|1|%s|%s' %(id, sss[first_index].split('-')[1], sss[last_index].split('-')[1]))
