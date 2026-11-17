p='template.html'; s=open(p,encoding='utf-8').read()
def R(a,b,cnt=1):
    global s
    n=s.count(a); assert n==cnt,(n,a[:90]); s=s.replace(a,b)
# base map layers
i=s.index("const base=(cls)=>"); j=s.index("\n",i)
s=s[:i]+"""const base=(cls)=>`<path d="${DATA.grat}" fill="none" stroke="var(--grat)" stroke-width=".6" vector-effect="non-scaling-stroke"/><path d="${DATA.land}" fill="var(--land)" stroke="var(--landline)" stroke-width=".7" stroke-linejoin="round" vector-effect="non-scaling-stroke"/><path class="pv" d="${DATA.prov}" fill="none" vector-effect="non-scaling-stroke"/><path class="lk" d="${DATA.lakes}" vector-effect="non-scaling-stroke"/><path class="rv" d="${DATA.rivers}" fill="none" vector-effect="non-scaling-stroke"/><path class="bd" d="${DATA.borders}" fill="none" vector-effect="non-scaling-stroke"/>`;"""+s[j:]
# CSS for new layers (after .noborders rule)
R(".noborders .bd{display:none}",""".noborders .bd{display:none}
.pv{stroke:var(--landline);stroke-width:.45;stroke-dasharray:2 2;opacity:.55}
.rv{stroke:var(--river);stroke-width:.8;opacity:.75;stroke-linecap:round;stroke-linejoin:round}
.lk{fill:var(--sea);stroke:var(--river);stroke-width:.4;opacity:.9}
.noprov .pv,.norivers .rv,.norivers .lk{display:none}
.lay-ports circle{fill:var(--surface);stroke:#8a3b22;stroke-width:1.4;vector-effect:non-scaling-stroke}
.lay-ports text,.lay-lease text,.lay-city text{fill:var(--ink);paint-order:stroke;stroke:var(--land);stroke-width:2.5px;stroke-linejoin:round;font-weight:600}
.lay-ports .yr{fill:#8a3b22;font-weight:700}
.lay-lease rect{fill:#7b3f78;opacity:.85;vector-effect:non-scaling-stroke}
.lay-city circle{fill:var(--ink);opacity:.6}
.noports .lay-ports,.nolease .lay-lease{display:none}
.mleg .sw2{display:inline-block;width:.7rem;height:.7rem;margin-right:.3rem;vertical-align:-1px}""")
# river colour var
R("--land:#ebe4d4;--landline:#b9ad94;--border:#b5a98f;--sea:#dfe8ec;--grat:#cdd8dd;","--land:#ebe4d4;--landline:#b9ad94;--border:#b5a98f;--sea:#dfe8ec;--grat:#cdd8dd;--river:#6f9cbf;")
R("--land:#262a2f;--landline:#4a4f56;--border:#565c64;--sea:#15191d;--grat:#22282e;","--land:#262a2f;--landline:#4a4f56;--border:#565c64;--sea:#15191d;--grat:#22282e;--river:#4f7896;",2)
# map view: header text, part buttons, wall group, legend, note
R("""<p class="note vsub">시대를 고르면 그 부의 사건만 남고 지도가 그 무대로 다가갑니다. 번호를 누르면 그 사건을 낳은 원인(파란 선)과 그 사건이 낳은 결과(붉은 선)가 이어지고, 지도 옆 목록에 연결의 이유가 나옵니다.</p>""",
"""<p class="note vsub">시대를 고르면 그 부의 사건만 남고 지도가 그 무대로 다가갑니다. 개항장과 조차지는 그 부가 끝나는 해까지 열린 것만 보입니다. 번호를 누르면 그 사건을 낳은 원인(파란 선)과 그 사건이 낳은 결과(붉은 선)가 이어지고, 지도 옆 목록에 연결의 이유가 나옵니다.</p>""")
R("""<button class="pill" data-pt="all">전체 120장</button></div>""","""<button class="pill" data-pt="all">전체 ${DATA.events.length}장</button></div>
  <div class="ctrl" role="group" aria-label="겹쳐 볼 것"><span class="lb">겹쳐 보기</span>${MAPLAY.map(([k,n])=>`<button class="pill" data-lay="${k}">${n}</button>`).join('')}</div>""")
i=s.index('   <g class="wall">'); j=s.index('\n',i)
s=s[:i]+"""   <g id="mlay"></g>"""+s[j:]
R("""<div class="mleg"><label class="bdt"><input type="checkbox" id="bdt"> 현재 국경</label><span><i class="ln in"></i>원인</span><span><i class="ln out"></i>결과</span><span><i class="ring"></i>다른 시대의 연결 사건</span></div></div>""",
"""<div class="mleg"><span><i class="ln in"></i>원인</span><span><i class="ln out"></i>결과</span><span><i class="ring"></i>다른 시대의 연결 사건</span><span><svg class="sw2" viewBox="0 0 10 10"><circle cx="5" cy="5" r="3.6" fill="var(--surface)" stroke="#8a3b22" stroke-width="1.4"/></svg>개항장</span><span><svg class="sw2" viewBox="0 0 10 10"><rect x="1.5" y="1.5" width="7" height="7" fill="#7b3f78"/></svg>조차지·할양지</span></div></div>""")
R("""<p class="note">갈색 굵은 선은 명대 장성의 대략적 노선, 점선은 실크로드 간선입니다. 가는 회색 선은 오늘의 국경으로, 위치를 가늠하라고 희미하게 넣었습니다(크림은 국제적으로 인정된 경계를 따르고, 카슈미르는 실효 지배선입니다). 같은 곳에 몰린 번호는 서로 비켜 놓았고, 가는 선이 실제 위치를 가리킵니다. 지도는 끌어서 옮기고, 휠이나 단추로 확대합니다.</p></div>`;""",
"""<p class="note">바탕은 Natural Earth 자료로 그렸습니다. 회색 선은 오늘의 국경, 점선은 오늘의 성 경계로, 위치를 가늠하라고 희미하게 넣었습니다(분쟁 지역은 실효 지배선을 따릅니다). 투영은 『중국 역사 지도』와 같은 등장방형(표준 위선 북위 33도)입니다. 같은 곳에 몰린 번호는 서로 비켜 놓았고, 가는 선이 실제 위치를 가리킵니다. 지도는 끌어서 옮기고, 휠이나 단추로 확대합니다.</p></div>`;""")
R("""  const bdOn=store.get('borders',true);$('#bdt').checked=bdOn;stage.classList.toggle('noborders',!bdOn);$('#bdt').onchange=ev=>{store.set('borders',ev.target.checked);stage.classList.toggle('noborders',!ev.target.checked);};""",
"""  let lay=store.get('maplay',{bd:true,prov:true,rivers:true,ports:true,lease:true});
  const paintLay=()=>{MAPLAY.forEach(([k])=>{stage.classList.toggle('no'+(k==='bd'?'borders':k),!lay[k]);});document.querySelectorAll('[data-lay]').forEach(b=>b.classList.toggle('on',!!lay[b.dataset.lay]));};
  document.querySelectorAll('[data-lay]').forEach(b=>b.onclick=()=>{lay[b.dataset.lay]=!lay[b.dataset.lay];store.set('maplay',lay);paintLay();});
  paintLay();""")
# overlays drawn in drawMarks depending on part
R("""    const kz=mapState.vb[2]/W;document.querySelectorAll('#mlab .lbl-reg').forEach(t=>t.style.fontSize=Math.max(15*kz,5)+'px');document.querySelectorAll('#mlab .lbl-sea').forEach(t=>t.style.fontSize=Math.max(12*kz,4)+'px');document.querySelectorAll('.wall text').forEach(t=>t.style.fontSize=Math.max(9*kz,3)+'px');""",
"""    const kz=mapState.vb[2]/W;document.querySelectorAll('#mlab .lbl-reg').forEach(t=>t.style.fontSize=Math.max(15*kz,5)+'px');document.querySelectorAll('#mlab .lbl-sea').forEach(t=>t.style.fontSize=Math.max(12*kz,4)+'px');
    const yEnd=mapState.part==='all'?9999:P[mapState.part].y1,yBeg=mapState.part==='all'?0:P[mapState.part].y0;
    const pr=DATA.ports.filter(q=>q.y<=yEnd),ls=DATA.leases.filter(q=>q.y<=yEnd&&q.until>=yBeg);
    $('#mlay').innerHTML=`<g class="lay-ports">${pr.map(q=>`<circle cx="${q.xy[0]}" cy="${q.xy[1]}" r="${3.2*kz}"><title>${esc(q.n)} · ${q.y}년 개항${q.d?' · '+esc(q.d):''}</title></circle><text x="${q.xy[0]+5*kz}" y="${q.xy[1]+3.5*kz}" style="font-size:${8.5*kz}px">${esc(q.n)} <tspan class="yr">${q.y}</tspan></text>`).join('')}</g>
     <g class="lay-lease">${ls.map(q=>`<rect x="${q.xy[0]-3.6*kz}" y="${q.xy[1]-3.6*kz}" width="${7.2*kz}" height="${7.2*kz}"><title>${esc(q.n)} · ${esc(q.who)} · ${q.y}–${q.until>2100?'':q.until}</title></rect><text x="${q.xy[0]+6*kz}" y="${q.xy[1]-5*kz}" style="font-size:${8.5*kz}px">${esc(q.n)}(${esc(q.who)})</text>`).join('')}</g>`;""")
# map layer list constant near mapState
R("let mapState={part:null,sel:null,vb:null};","let mapState={part:null,sel:null,vb:null};\nconst MAPLAY=[['ports','개항장'],['lease','조차지·할양지'],['rivers','강'],['prov','성 경계'],['bd','현재 국경']];")
R("""$('#mside').innerHTML=`${p?`<p class="lbl">${esc(p.no)} · ${esc(p.y)}</p><h3 class="st">${esc(p.t)}</h3>`:`<h3 class="st">전체 120장</h3>`}""","""$('#mside').innerHTML=`${p?`<p class="lbl">${esc(p.no)} · ${esc(p.y)}</p><h3 class="st">${esc(p.t)}</h3>`:`<h3 class="st">전체 ${DATA.events.length}장</h3>`}""")
open(p,'w',encoding='utf-8').write(s); print('ok')
