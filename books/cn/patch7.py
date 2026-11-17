p='template.html'; s=open(p,encoding='utf-8').read()
def R(a,b,cnt=1):
    global s
    n=s.count(a); assert n==cnt,(n,a[:90]); s=s.replace(a,b)
R("""  if(t){ev.preventDefault();const rs=t.getClientRects(),r=rs[rs.length-1]||t.getBoundingClientRect();pop.innerHTML=`<b>${esc(t.dataset.t)}</b>${esc(TDEF[t.dataset.t])}<div style="margin-top:.4rem"><a href="#/terms">용어 사전 →</a></div>`;
    pop.hidden=false;const pw=pop.offsetWidth;pop.style.left=Math.max(12,Math.min(innerWidth-pw-12,r.left))+'px';pop.style.top=(r.bottom+6)+'px';return;}""",
"""  if(t){ev.preventDefault();const rs=t.getClientRects(),r=rs[rs.length-1]||t.getBoundingClientRect();
    if(t.dataset.p){const q=PE[t.dataset.p],cid=(CUR.match(/^#\\/e\\/(\\w+)/)||[])[1],at=cid&&q.at&&q.at[cid];
      pop.innerHTML=`<b>${esc(q.n)} <small class="note" style="font-weight:400">${esc(q.hz||'')} · ${plife(q)}</small></b>${fchip(q)}<div>${esc(q.role)}</div>${at?`<div class="pat"><b style="display:inline">이 장에서</b> ${esc(at)}</div>`:''}${q.ch.length?`<div class="chips">${q.ch.slice(0,14).map(c=>`<a class="chip" href="#/e/${c}" title="${esc(E[c].t)}">${E[c].no}장</a>`).join('')}</div>`:''}<div style="margin-top:.4rem"><a href="#/pp/${q.id}">인물 사전에서 보기 →</a></div>`;}
    else pop.innerHTML=`<b>${esc(t.dataset.t)}</b>${esc(TDEF[t.dataset.t])}<div style="margin-top:.4rem"><a href="#/terms">용어 사전 →</a></div>`;
    pop.hidden=false;const pw=pop.offsetWidth,ph=pop.offsetHeight;pop.style.left=Math.max(12,Math.min(innerWidth-pw-12,r.left))+'px';pop.style.top=(r.bottom+6+ph>innerHeight-8?Math.max(8,r.top-ph-6):r.bottom+6)+'px';return;}""")
# chapter people box after guide
R("""   ${BD('안내')?`<section class="keys guide"><p class="lbl">먼저 알아 둘 것</p><div class="rh">${rhHtml(BD('안내'))}</div></section>`:''}""",
"""   ${BD('안내')?`<section class="keys guide"><p class="lbl">먼저 알아 둘 것</p><div class="rh">${rhHtml(BD('안내'))}</div></section>`:''}
   ${pbox(e)}""")
R("function viewEvent(id,rid){","""function pcard(q,cid){const at=cid&&q.at&&q.at[cid];return `<li><a href="#/pp/${q.id}" style="--pc:${pcol(q)}"><i class="fdot"></i><b>${esc(q.n)}<small>${plife(q)}</small></b><span class="pr">${esc(FC[q.f][1])} · ${esc(at||q.role)}</span></a></li>`;}
function pbox(e){const ps=e.pp.map(x=>PE[x]);if(!ps.length)return '';const main=ps.filter(q=>q.at&&q.at[e.id]),rest=ps.filter(q=>!(q.at&&q.at[e.id]));
  const top=main.length?main:ps,more=main.length?rest:[];
  return `<section class="pbox"><p class="lbl"><span>이 장의 인물</span><a href="#/pp" class="note">인물 사전 →</a></p><ul class="plist">${top.map(q=>pcard(q,e.id)).join('')}</ul>${more.length?`<details><summary>이 장에서 이름만 나오는 인물 ${more.length}명</summary><ul class="plist">${more.map(q=>pcard(q,e.id)).join('')}</ul></details>`:''}</section>`;}
function viewEvent(id,rid){""")
# part: main people
R("""  <h2 class="sh">이 부의 사건 ${p.ev.length}개</h2>""","""  ${(()=>{const cnt={};p.ev.forEach(e=>e.pp.forEach(x=>{if(PE[x].at&&PE[x].at[e.id])cnt[x]=(cnt[x]||0)+1;}));const ids=Object.keys(cnt).sort((a,b)=>cnt[b]-cnt[a]||(PE[a].life[0]||0)-(PE[b].life[0]||0)).slice(0,18);
    return ids.length?`<h2 class="sh">이 부의 주요 인물</h2><p class="note">이 부의 장에서 행적이 기록된 사람들입니다. 많이 나오는 순서이며, 이름을 누르면 장별 행적을 볼 수 있습니다.</p><ul class="plist">${ids.map(x=>{const q=PE[x];return `<li><a href="#/pp/${q.id}" style="--pc:${pcol(q)}"><i class="fdot"></i><b>${esc(q.n)}<small>${plife(q)}</small></b><span class="pr">${esc(FC[q.f][1])} · ${esc(q.role)} · ${cnt[x]}개 장</span></a></li>`;}).join('')}</ul>`:'';})()}
  <h2 class="sh">이 부의 사건 ${p.ev.length}개</h2>""")
# views: people
R("// ── 서가\n","""// ── 인물
let pfac=store.get('pfac','');
function viewPeople(id){
  const q=PE[id];if(q)return personPage(q);
  const Y0=1730,Y1=2030,LW=150,PX=3.2,RH=20;
  const list=()=>DATA.people.filter(x=>!pfac||x.f===pfac).slice().sort((a,b)=>(a.life[0]??(a.life[1]-50))-(b.life[0]??(b.life[1]-50)));
  const svg=()=>{const L=list(),W=LW+(Y1-Y0)*PX+20,H=30+L.length*RH+10,x=y=>LW+(y-Y0)*PX;
    const ticks=[1750,1800,1850,1900,1950,2000];const pb=DATA.parts.map(p=>[x(p.y0),x(p.y1),p]);
    return `<svg class="lf" width="${W}" height="${H}" viewBox="0 0 ${W} ${H}" role="img" aria-label="인물의 생몰 띠">
     ${pb.map(([a,b,p],i)=>`<rect x="${a}" y="18" width="${b-a}" height="${H-18}" fill="${pc(p.id)}" opacity="${i%2?.05:.09}"/><text x="${a+3}" y="13" class="yr" style="fill:${pc(p.id)};font-weight:700">${esc(p.no)}</text>`).join('')}
     ${ticks.map(t=>`<line x1="${x(t)}" x2="${x(t)}" y1="18" y2="${H}" stroke="var(--line)"/><text x="${x(t)+2}" y="${H-3}" class="yr">${t}</text>`).join('')}
     ${L.map((p,i)=>{const y=30+i*RH,b=p.life[0]??(p.life[1]-45),d=p.life[1]??2026,c=pcol(p);
       return `<a href="#/pp/${p.id}"><text x="${LW-8}" y="${y+4}" text-anchor="end">${esc(p.n)}</text><rect class="bar" x="${x(b)}" y="${y-5}" width="${Math.max(3,(d-b)*PX)}" height="10" rx="5" fill="${c}" opacity="${p.life[0]==null?.45:.8}"/>${p.ch.map(cid=>`<circle cx="${x(E[cid].yr)}" cy="${y}" r="3" fill="var(--surface)" stroke="${c}" stroke-width="1.5"><title>${E[cid].no}장 ${esc(E[cid].t)}</title></circle>`).join('')}<title>${esc(p.n)} ${plife(p)} · ${esc(p.role)}</title></a>`;}).join('')}</svg>`;};
  const draw=()=>{store.set('pfac',pfac);const L=list();
    document.querySelectorAll('[data-pf]').forEach(b=>b.classList.toggle('on',b.dataset.pf===pfac));
    $('#plife').innerHTML=svg();
    $('#pgroups').innerHTML=DATA.facts.filter(f=>!pfac||f[0]===pfac).map(f=>{const ps=L.filter(x=>x.f===f[0]);if(!ps.length)return '';
      return `<h2 class="sh"><span class="fchip" style="--pc:${f[2]}"><i class="fdot"></i>${esc(f[1])}</span><span class="shs">${esc(f[3])}</span></h2><ul class="plist">${ps.map(x=>`<li><a href="#/pp/${x.id}" style="--pc:${f[2]}"><i class="fdot"></i><b>${esc(x.n)}<small>${plife(x)}</small></b><span class="pr">${esc(x.role)}${x.ch.length?` · ${x.ch.length}개 장`:''}</span></a></li>`).join('')}</ul>`;}).join('');};
  main.innerHTML=`<div class="wide"><p class="eyebrow">인물</p><h1 class="vt">누가 이 역사를 움직였나</h1>
  <p class="note vsub">이 책에 나오는 ${DATA.people.length}명을 진영별로 모았습니다. 색은 진영을, 띠는 생애를, 띠 위의 작은 원은 그 사람이 나오는 장의 연대를 나타냅니다. 이름을 누르면 장별 행적과 관계를 볼 수 있습니다. 본문에서도 진영 색 밑줄이 그어진 이름을 누르면 같은 정보가 뜹니다.</p>
  <div class="ctrl"><span class="lb">진영</span><button class="pill" data-pf="">모두</button>${DATA.facts.map(f=>`<button class="pill" data-pf="${f[0]}"><i class="fdot" style="--pc:${f[2]};margin-right:.3rem"></i>${esc(f[1])}</button>`).join('')}</div>
  <div class="lifebox" id="plife"></div><p class="note">생몰년이 확실하지 않은 사람의 띠는 흐리게 그렸습니다. 좁은 화면에서는 옆으로 밀어 보세요.</p>
  <div id="pgroups"></div></div>`;
  document.querySelectorAll('[data-pf]').forEach(b=>b.onclick=()=>{pfac=b.dataset.pf;draw();});
  draw();
}
function personPage(q){
  const same=DATA.people.filter(x=>x.f===q.f&&x!==q).slice(0,24);
  const rel=(q.rel||[]).map(([r,t])=>[PE[r],t]).filter(x=>x[0]);
  const back=DATA.people.filter(x=>(x.rel||[]).some(r=>r[0]===q.id)&&!rel.some(y=>y[0]===x)).map(x=>[x,x.rel.find(r=>r[0]===q.id)[1]+'(상대 쪽에서)']);
  main.innerHTML=`<article class="col"><header class="chead"><p class="eyebrow"><a href="#/pp">인물</a> · ${esc(FC[q.f][1])}</p><h1>${esc(q.n)}</h1><p class="period">${esc(q.hz||'')}${q.hz?' · ':''}${plife(q)}</p><div class="chips">${fchip(q)}</div></header>
  <section class="keys"><p class="lbl">${esc(q.role)}</p><p>${linky(q.d)}</p></section>
  <section class="slot"><h2>장별 행적</h2>${q.ch.length?`<ol class="ptl">${q.ch.map(c=>{const e=E[c];return `<li style="--c:${ECOL(e)}"><span class="yr">${esc(e.y)} · ${esc(P[e.p].no)}</span><a href="#/e/${c}">${e.no}. ${esc(e.t)}</a>${q.at&&q.at[c]?`<p>${esc(q.at[c])}</p>`:`<p class="note">${DATA.body[c]?'이 장에서 이름이 나옵니다.':'이 장의 요약에 나옵니다. 본문은 집필 예정입니다.'}</p>`}</li>`;}).join('')}</ol>`:'<p class="note">아직 이 사람이 나오는 장의 본문이 쓰이지 않았습니다.</p>'}</section>
  ${rel.length||back.length?`<section class="slot"><h2>관계</h2><ul class="plist">${[...rel,...back].map(([x,t])=>`<li><a href="#/pp/${x.id}" style="--pc:${pcol(x)}"><i class="fdot"></i><b>${esc(x.n)}<small>${plife(x)}</small></b><span class="pr">${esc(t)}</span></a></li>`).join('')}</ul></section>`:''}
  <section class="slot"><h2>같은 진영의 인물</h2><div class="go">${same.map(x=>`<a class="pill" href="#/pp/${x.id}">${esc(x.n)}</a>`).join('')}</div></section></article>`;
}

// ── 서가
""")
# route
R("  else if(v==='id'){viewId(a);tab='id';}","  else if(v==='id'){viewId(a);tab='id';}\n  else if(v==='pp'){viewPeople(a);tab='pp';}")
# search
R(" ...DATA.regions.map(r=>({h:'#/rr/'+r.id,k:'무대',t:r.n,s:r.d}))];"," ...DATA.regions.map(r=>({h:'#/rr/'+r.id,k:'무대',t:r.n,s:r.d})),\n ...DATA.people.map(q=>({h:'#/pp/'+q.id,k:'인물',t:q.n,s:`${q.hz||''} ${plife(q)} · ${FC[q.f][1]} · ${q.role}`}))];")
# UL page key
R("if(['p','ln'].includes(v)&&h[1])return `#/${v}/${h[1]}`;","if(['p','ln','pp'].includes(v)&&h[1])return `#/${v}/${h[1]}`;")
R("if(v==='ln'&&LN[a])return `변천: ${LN[a].n}`;","if(v==='ln'&&LN[a])return `변천: ${LN[a].n}`;if(v==='pp'&&PE[a])return `인물: ${PE[a].n}`;")
open(p,'w',encoding='utf-8').write(s); print('ok')
