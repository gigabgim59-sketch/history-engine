# python3 tools/genp.py N rows.txt at.txt  -> people_pN.mjs
import sys,json
n=sys.argv[1]; rows=open(sys.argv[2]).read(); ats=open(sys.argv[3]).read() if len(sys.argv)>3 else ''
deny=open(sys.argv[4]).read().strip() if len(sys.argv)>4 else '{}'
L=[]
for r in rows.strip().split('\n'):
    if not r.strip() or r.startswith('#'): continue
    id,nm,al,hz,a,b,fa,role,d,at=r.split('|')
    alj='null' if not al else json.dumps(al.split(','),ensure_ascii=False)
    atd={}
    for x in at.split(';'):
        if x.strip(): k,v=x.split(':',1); atd[k.strip()]=v
    L.append(f"P({json.dumps(id)},{json.dumps(nm,ensure_ascii=False)},{alj},{json.dumps(hz,ensure_ascii=False)},[{a},{b}],{json.dumps(fa)},{json.dumps(role,ensure_ascii=False)},{json.dumps(d,ensure_ascii=False)},{json.dumps(atd,ensure_ascii=False)})")
A={}
for r in ats.strip().split('\n'):
    if not r.strip(): continue
    id,rest=r.split('|',1)
    for x in rest.split(';'):
        if x.strip(): k,v=x.split(':',1); A.setdefault(id,{})[k.strip()]=v
out=f"// 제{n}부 인물\nconst P=(id,n,al,hz,life,f,role,d,at)=>({{id,n,...(al?{{al}}:{{}}),hz,life,f,role,d,at}});\nexport const PEOPLE{n} = [\n"+",\n".join(L)+f"\n];\nexport const AT{n} = {json.dumps(A,ensure_ascii=False,indent=0)};\nexport const REL{n} = {{}};\nexport const PDENY{n} = {deny};\n"
open(f'people_p{n}.mjs','w').write(out); print('ok',len(L))
