p='template.html'; s=open(p,encoding='utf-8').read()
def between(start,end):
    i=s.index(start); j=s.index(end,i); return i,j
def R(a,b,cnt=1):
    global s
    n=s.count(a); assert n==cnt,(n,a[:90]); s=s.replace(a,b)

# ── viewHome
i,j=between('function viewHome(){','function viewPart(id){')
s=s[:i]+r'''function viewHome(){
  const n=DATA.events.length,M=DATA.meta,done=DATA.events.filter(e=>DATA.body[e.id]).length;
  main.innerHTML=`<div class="col hero"><p class="eyebrow">분기점 사건으로 읽는 중국 근현대사 · ${esc(M.span)}</p>
  <h1>${esc(M.title)}</h1><p class="sub">${esc(M.sub)}</p>
  <p class="note"><a href="guide.html" target="_blank" rel="noopener">처음이라면 「읽는 법」부터 →</a> 읽는 길과 화면·도구 사용법을 사진과 함께 안내합니다.</p>
  ${done<n?`<div class="keys"><p class="lbl">집필 중</p><p>${n}장 가운데 ${done}장의 본문이 쓰였습니다. 나머지 장은 물음과 핵심 요약, 연결과 근거 도서가 먼저 채워져 있고 본문은 부 단위로 이어서 씁니다.</p><div class="meter"><i style="width:${done/n*100}%"></i></div></div>`:''}
  ${M.intro.map(x=>`<p class="lede">${x}</p>`).join('')}
  <h2 class="sh">세 힘</h2>
  <p class="lede">${M.engines}</p>
  <div class="f3">${DATA.engines.map(([k,nm,d])=>`<div class="card"><h3>${esc(nm)}</h3><p>${esc(d)}</p></div>`).join('')}</div>
  <h2 class="sh">이 책을 읽는 여덟 가지 길</h2>
  <div class="grid">
   <a class="card" href="#/p/p1"><h3>읽기</h3><p>부마다 배경 장으로 시대의 다섯 무대를 훑고, 사건 장을 차례로 읽습니다.</p></a>
   <a class="card" href="#/map"><h3>지도</h3><p>사건이 일어난 자리, 개항장과 조차지, 원인과 결과가 무대를 넘나드는 길을 봅니다.</p></a>
   <a class="card" href="#/lanes"><h3>무대 연표</h3><p>다섯 무대를 가로 레인으로 놓고 사건 사이의 화살표를 따라갑니다. 무대를 고르면 그 무대의 장만 이어 읽을 수 있습니다.</p></a>
   <a class="card" href="#/net/c01"><h3>사건 연결망</h3><p>한 장씩, 그 사건을 낳은 원인과 그 사건이 낳은 결과를 이유와 함께 따라갑니다.</p></a>
   <a class="card" href="#/id"><h3>사람들의 변화</h3><p>농민, 신사와 지식인, 여성, 티베트인, 대만 사람들 같은 집단의 무엇이 어느 사건에서 바뀌었는지 모아 봅니다.</p></a>
   <a class="card" href="#/ln"><h3>요소별 변천</h3><p>인물·정당·도시·개념 하나를 골라 그것이 거쳐 온 모습을 한 줄로 봅니다.</p></a>
   <a class="card" href="#/t"><h3>줄기</h3><p>주권, 혁명, 근대화, 변강의 네 줄기를 시대를 건너 따라갑니다.</p></a>
   <a class="card" href="#/books"><h3>서가</h3><p>이 책이 기댄 책들과, 각 책이 받치는 장을 봅니다.</p></a>
  </div>
  <h2 class="sh">국가의 다섯 겹</h2>
  <p>장마다 ‘영향’에서 무엇이 바뀌었는지를 다섯 겹으로 나누어 적습니다.</p>
  <table class="tbl"><tbody>${DATA.axes.map(a=>`<tr><th style="width:7rem"><span class="axt"><i class="ax-${a.id}"></i>${esc(a.n)}</span></th><td>${esc(a.d)}</td></tr>`).join('')}</tbody></table>
  <h2 class="sh">다섯 무대</h2>
  <table class="tbl"><tbody>${DATA.regions.map(r=>`<tr><th style="width:7rem"><a href="#/rr/${r.id}">${esc(r.n)}</a></th><td>${esc(r.d)}</td></tr>`).join('')}</tbody></table>
  <h2 class="sh">중요도와 분량</h2>
  <p class="lede">모든 사건에 같은 지면을 나누지 않습니다. 국가의 여러 겹을 한꺼번에 바꾸었거나 뒤의 사건을 여럿 낳은 사건을 핵심으로 두고 가장 길게 씁니다.</p>
  <table class="tbl"><tbody><tr><th style="width:7rem"><span class="wt w1">핵심</span></th><td>본문 약 5천 자 · ${DATA.events.filter(e=>e.w===1).length}개</td></tr><tr><th><span class="wt w2">주요</span></th><td>본문 약 2,500자 · ${DATA.events.filter(e=>e.w===2).length}개</td></tr><tr><th><span class="wt w3">보조</span></th><td>본문 약 1,500자 · ${DATA.events.filter(e=>e.w===3).length}개</td></tr></tbody></table>
  <h2 class="sh">차례</h2>
  ${DATA.parts.map(p=>`<section class="part"><h3><span class="pbar" style="background:${pc(p.id)}"></span>${esc(p.no)} ${esc(p.t)}<em>${esc(p.y)}</em></h3>
   <ol class="clist"><li><a href="#/p/${p.id}"><span class="n">序</span><span class="t">배경: 이 시대의 다섯 무대</span></a></li>
   ${p.ev.map(e=>`<li><a href="#/e/${e.id}" class="w${e.w}"><span class="n">${e.no}</span><span class="t">${esc(e.t)}${e.w===1?'<span class="wt w1">핵심</span>':''}${DATA.body[e.id]?'':'<span class="tg">집필 예정</span>'}</span><small>${esc(e.y)}</small><span class="rd ${READ[e.id]?'on':''}"></span></a></li>`).join('')}</ol></section>`).join('')}
  <section class="part"><h3>맺음</h3><ol class="clist"><li><a href="#/end"><span class="n">結</span><span class="t">천하에서 국가로</span></a></li></ol></section></div>`;
}

'''+s[j:]

# ── viewPart forces & regions
R("""${p.f?`<h2 class="sh">이 시대의 세 힘</h2><div class="f3">${[['mono','고대근동의 유일신'],['ie','인도유럽어 사람들'],['tm','투르크·몽골 유목민']].map(([k,n])=>`<div class="card"><h3>${n}</h3><p>${linky(p.f[k])}</p></div>`).join('')}</div><div class="keys"><p class="lbl">세 힘이 만나는 곳</p><p>${linky(p.f.meet)}</p></div>`:''}""",
  """${p.f?`<h2 class="sh">이 시대의 세 힘</h2><div class="f3">${DATA.engines.map(([k,n])=>`<div class="card"><h3>${esc(n)}</h3><p>${linky(p.f[k])}</p></div>`).join('')}</div><div class="keys"><p class="lbl">세 힘이 만나는 곳</p><p>${linky(p.f.meet)}</p></div>`:''}""")
R("""<h2 class="sh">이 시대의 다섯 지역</h2>
  <div class="bg5">${DATA.regions.map(r=>`<a class="card" href="#/r/${r.id}"><h3>${esc(r.n)}</h3><p>${linky(p.bg[r.id])}</p></a>`).join('')}
   <div class="card pe"><h3>주변 <span class="note">지중해·유럽·중국</span></h3><p>${linky(p.bg.pe)}</p></div></div>""",
  """${p.bg?`<h2 class="sh">이 시대의 다섯 무대</h2>
  <div class="bg5">${DATA.regions.map(r=>`<a class="card" href="#/rr/${r.id}"><h3>${esc(r.n)}</h3><p>${linky(p.bg[r.id])}</p></a>`).join('')}
   <div class="card pe"><h3>세계 <span class="note">중국 밖에서는</span></h3><p>${linky(p.bg.pe)}</p></div></div>`:''}""")
R("""<div class="slot"><h2>기초 배경 서술</h2>${p.bgx?`<div class="rh">${rhHtml(p.bgx)}</div>`:`<div class="todo"><b>집필 예정</b>이 시대의 지리·생활양식·언어·종교의 바탕을 지역별로 풀어 쓴다.</div>`}</div>
  ${p.sum?`<section class="slot"><h2>이 부에서 쌓인 이름들</h2><div class="rh">${rhHtml(p.sum)}</div></section>`:''}""",
  """<div class="slot"><h2>기초 배경 서술</h2>${p.bgx?`<div class="rh">${rhHtml(p.bgx)}</div>`:`<div class="todo"><b>집필 예정</b>이 시대를 읽는 데 필요한 국가와 사회의 바탕을 풀어 쓴다.</div>`}</div>
  ${p.sum?`<section class="slot"><h2>이 부에서 바뀐 것</h2><div class="rh">${rhHtml(p.sum)}</div></section>`:''}""")

# ── SLOTS: skip empty slots when body exists; 영향 table by axes
R("""   ${SLOTS.map(([h,d])=>`<section class="slot"><h2>${h}</h2>${BD(h)?`<div class="rh">${rhHtml(BD(h))}</div>`:`<div class="todo"><b>집필 예정</b>${esc(d)}</div>`}</section>`).join('')}""",
  """   ${SLOTS.filter(([h])=>BD(h)||!DATA.body[id]).map(([h,d])=>`<section class="slot"><h2>${h}</h2>${BD(h)?`<div class="rh">${rhHtml(BD(h))}</div>`:`<div class="todo"><b>집필 예정</b>${esc(d)}</div>`}</section>`).join('')}""")
open(p,'w',encoding='utf-8').write(s); print('ok')
