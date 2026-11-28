# 사용: python3 app.py terms <file>  /  python3 app.py books <file>  /  python3 app.py bk <file>
import sys
kind,src=sys.argv[1],sys.argv[2]
new=open(src,encoding='utf8').read().strip().rstrip(',')
def ins(fn,marker,new,last=False):
    t=open(fn,encoding='utf8').read()
    i=t.rindex(marker) if last else t.index(marker)
    body=t[:i].rstrip()
    if not (body.endswith(',') or body.endswith('[') or body.endswith('{')): body+=','
    open(fn,'w',encoding='utf8').write(body+'\n'+new+'\n'+t[i:])
if kind=='terms': ins('terms.mjs','];',new,last=True)
elif kind=='books': ins('books.mjs','];\n\nexport const BK',new)
elif kind=='bk': ins('books.mjs','};',new,last=True)
print('ok')
