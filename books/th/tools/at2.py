# python3 tools/at2.py sp/atA.txt ... -> sp/p1at.txt (lNN|id:text|id:text 형식을 id|lNN:text;... 로)
import sys,collections
A=collections.OrderedDict()
for f in sys.argv[1:]:
    for r in open(f).read().strip().split('\n'):
        if not r.strip() or r.startswith('#'):continue
        c,*xs=r.split('|')
        for x in xs:
            if not x.strip():continue
            i,t=x.split(':',1);A.setdefault(i.strip(),[]).append(c.strip()+':'+t.strip().replace(';',','))
open('sp/p1at.txt','w').write('\n'.join(i+'|'+';'.join(v) for i,v in A.items())+'\n');print('at',sum(len(v) for v in A.values()))
