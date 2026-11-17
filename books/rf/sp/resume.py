import re,json,subprocess,sys
out=subprocess.run(['node','-e',"""import('./events.mjs').then(async m=>{const fs=await import('fs');const B={};for(const f of fs.readdirSync('.').filter(f=>/^body_p\\d[a-z]?\\.mjs$/.test(f))){const x=await import('./'+f);Object.assign(B,Object.values(x)[0]);}const o={};m.EVENTS.forEach(e=>{if(B[e.id])o[e.id]=Object.values(B[e.id]).flat().join('').length});console.log(JSON.stringify(o));})"""],capture_output=True,text=True).stdout
L=json.loads(out)
s=open('RESUME.md').read()
def rep(m):
    vid=m.group(1); rest=re.sub(r' · (작성 \d+자|미작성)$','',m.group(2))
    return f"- {vid}{rest} · "+(f"작성 {L[vid]}자" if vid in L else "미작성")
s=re.sub(r'^- (f\d\d)(.*)$',rep,s,flags=re.M)
if len(sys.argv)>1:
    s=re.sub(r'## 지금 상태.*?\n(?=\n## )','## 지금 상태 (2026-11-13)\n'+open(sys.argv[1]).read().strip()+'\n',s,flags=re.S)
open('RESUME.md','w').write(s)
