from collections import defaultdict
mydict = defaultdict(list)

for line in open('datafile'):
    names, loc1, loc2 = line.strip().split()
    names = names.split(',')
    for name in names:
        mydict[loc1 + ' ' + loc2].append(name)

for prefix in ('CS', 'NA'):
    for key in mydict:
        templist = [name for name in mydict[key]
			if name.startswith(prefix)]
        print(','.join(templist), end='')
        if len(templist):
            print(' ', key, sep='')
    
