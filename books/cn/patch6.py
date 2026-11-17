p='template.html'; s=open(p,encoding='utf-8').read()
def R(a,b,cnt=1):
    global s
    n=s.count(a); assert n==cnt,(n,a[:90]); s=s.replace(a,b)
# CSS
R("/* 밑줄 */","""/* 인물 */
.person{border-bottom-style:solid;border-bottom-color:color-mix(in srgb,var(--pc,var(--accent)) 70%,transparent)}
.fdot{display:inline-block;width:.55rem;height:.55rem;border-radius:50%;background:var(--pc);flex:none}
.fchip{display:inline-flex;align-items:center;gap:.3rem;font-size:.74rem;font-weight:700;color:var(--pc);border:1px solid color-mix(in srgb,var(--pc) 45%,transparent);border-radius:999px;padding:0 .5rem;white-space:nowrap;background:var(--surface)}
.plist{list-style:none;margin:.4rem 0 0;padding:0;display:grid;grid-template-columns:repeat(auto-fill,minmax(min(100%,17rem),1fr));gap:.45rem}
.plist a{display:grid;grid-template-columns:auto 1fr;gap:.1rem .55rem;align-items:baseline;padding:.45rem .65rem;border:1px solid var(--line);border-left:3px solid var(--pc);border-radius:9px;background:var(--surface);color:var(--ink);line-height:1.45}
.plist a:hover{text-decoration:none;border-color:var(--muted);border-left-color:var(--pc)}
.plist b{font-size:.92rem}.plist small{color:var(--muted);font-size:.74rem;font-weight:400;margin-left:.3rem}
.plist .pr{grid-column:1/-1;font-size:.82rem;color:var(--muted)}
.pbox{margin:1.4rem 0}.pbox>.lbl{display:flex;justify-content:space-between;align-items:baseline}
.pbox details summary{cursor:pointer;font-size:.82rem;color:var(--accent);margin-top:.4rem}
.pop .fchip{margin:.15rem 0 .3rem}.pop .pat{margin:.3rem 0;padding:.3rem .5rem;background:var(--soft);border-radius:6px;font-size:.84rem}
.pop .chips{margin-top:.35rem}.pop .chip{font-size:.72rem}
.lifebox{overflow-x:auto;border:1px solid var(--line);border-radius:12px;background:var(--surface);-webkit-overflow-scrolling:touch}
.lifebox svg{display:block}
.lf text{font-size:11px;fill:var(--ink)}.lf .yr{font-size:10px;fill:var(--muted)}
.lf a:hover rect.bar{opacity:1}
.ptl{list-style:none;margin:.6rem 0;padding:0 0 0 .4rem;border-left:2px solid var(--line)}
.ptl li{position:relative;padding:.35rem 0 .6rem 1rem}
.ptl li::before{content:"";position:absolute;left:-.5rem;top:.75rem;width:.7rem;height:.7rem;border-radius:50%;background:var(--c);border:2px solid var(--bg)}
.ptl a{color:var(--ink);font-weight:700}.ptl .yr{display:block;font-size:.78rem;color:var(--muted)}.ptl p{margin:.15rem 0 0}
/* 밑줄 */""")
# tabs
R('<a href="#/id" data-v="id">사람들의 변화</a>','<a href="#/pp" data-v="pp">인물</a><a href="#/id" data-v="id">사람들의 변화</a>')
# index people
R("DATA.regions.forEach(r=>R[r.id]=r);DATA.axes.forEach(a=>AX[a.id]=a);","""DATA.regions.forEach(r=>R[r.id]=r);DATA.axes.forEach(a=>AX[a.id]=a);
const PE={},PN={},FC={};DATA.people.forEach(p=>{PE[p.id]=p;[p.n,...(p.al||[])].forEach(n=>PN[n]=p.id);});DATA.facts.forEach(f=>FC[f[0]]=f);
const pcol=p=>FC[p.f][2];
const plife=p=>`${p.life[0]??'?'}–${p.life[1]??''}`;
const fchip=p=>`<span class="fchip" style="--pc:${pcol(p)}"><i class="fdot"></i>${esc(FC[p.f][1])}</span>`;""")
# term regex include people names
R("const TERM_RE=new RegExp('('+DATA.terms.map(t=>t[0]).filter(t=>!/[()]/.test(t))","const TERM_RE=new RegExp('('+[...DATA.terms.map(t=>t[0]),...Object.keys(PN)].filter(t=>!/[()]/.test(t))")
R("""const TERM_DENY={""","""const TERM_DENY={
 ...Object.fromEntries(Object.entries(DATA.pdeny).map(([k,[l,r]])=>[k,[l&&new RegExp(l),r&&new RegExp(r)]])),""")
R("""seen.add(m);return `<span class="term" role="button" tabindex="0" data-t="${esc(m)}">${m}</span>`;});}""",
"""seen.add(m);if(PN[m]){const p=PE[PN[m]];return `<span class="term person" style="--pc:${pcol(p)}" role="button" tabindex="0" data-p="${p.id}">${m}</span>`;}return `<span class="term" role="button" tabindex="0" data-t="${esc(m)}">${m}</span>`;});}""")
open(p,'w',encoding='utf-8').write(s); print('ok')
