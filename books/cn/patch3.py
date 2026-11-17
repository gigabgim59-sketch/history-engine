p='template.html'; s=open(p,encoding='utf-8').read()
def R(a,b,cnt=1):
    global s
    n=s.count(a); assert n==cnt,(n,a[:90]); s=s.replace(a,b)
R("""   <section class="slot"><h2>영향: 무엇이 바뀌었나</h2>
   ${chs.length?`<table class="tbl"><thead><tr><th>집단</th><th>겹</th><th>변화</th></tr></thead><tbody>${chs.map(c=>`<tr><td><a href="#/id/${c.g}">${esc(G[c.g].n)}</a></td><td>${esc(AX[c.ax].n)}</td><td>${esc(c.t)}</td></tr>`).join('')}</tbody></table>`:''}
   ${BD('영향')?`<div class="rh">${rhHtml(BD('영향'))}</div>`:`<div class="todo" style="margin-top:.6rem"><b>집필 예정</b>정치·사회·경제에 남은 결과와, 위 표의 정체성 변화를 서술로 풀어 쓴다.</div>`}</section>""",
"""   <section class="slot"><h2>영향: 무엇이 바뀌었나</h2>
   ${BD('영향')?`<div class="rh">${rhHtml(BD('영향'))}</div>`:`<div class="todo" style="margin-top:.6rem"><b>집필 예정</b>정치·사회·경제에 남은 결과를 국가의 다섯 겹으로 나누어 풀어 쓴다.</div>`}
   ${e.axc&&e.axc.length?`<p class="lbl" style="margin-top:1rem">국가의 다섯 겹</p><table class="tbl"><tbody>${e.axc.map(([a,t])=>`<tr><th style="width:7rem"><span class="axt"><i class="ax-${a}"></i>${esc(AX[a].n)}</span></th><td>${esc(t)}</td></tr>`).join('')}</tbody></table>`:''}
   ${chs.length?`<p class="lbl" style="margin-top:1rem">사람들의 변화</p><table class="tbl"><thead><tr><th>집단</th><th>겹</th><th>변화</th></tr></thead><tbody>${chs.map(c=>`<tr><td><a href="#/id/${c.g}">${esc(G[c.g].n)}</a></td><td>${esc(AX[c.ax].n)}</td><td>${esc(c.t)}</td></tr>`).join('')}</tbody></table>`:''}</section>""")
R("""<section class="slot"><h2>근거 도서</h2><table class="tbl"><tbody>${e.bk.map(([b,ch])=>`<tr><td><a href="#/books/${b}">『${esc(B[b].t)}』</a></td><td>${esc(ch)}</td></tr>`).join('')}</tbody></table>
   ${e.ext?`<p class="note"><span class="flag">서가 밖 보충</span> 이 사건은 열두 권이 얇게 다루므로 외부 연구로 보충해 서술합니다.</p>`:''}</section>""",
"""<section class="slot"><h2>근거 도서</h2>${e.bk.length?`<table class="tbl"><tbody>${e.bk.map(([b,ch])=>`<tr><td><a href="#/books/${b}">${btitle(B[b])}</a></td><td>${esc(ch)}</td></tr>`).join('')}</tbody></table>`:`<div class="todo"><b>집필 예정</b>본문을 쓸 때 기댄 책과 그 부분을 적는다.</div>`}</section>""")
R("""`<a class="next" href="#/end"><small>다음</small>결론</a>`}</nav>`}</article>`;""","""`<a class="next" href="#/end"><small>다음</small>맺음</a>`}</nav>`}</article>`;""")
# btitle helper after evLink
R("const evLink=(id,extra)=>","const btitle=b=>b.lang==='en'?'<i>'+esc(b.t)+'</i>':'『'+esc(b.t)+'』';\nconst evLink=(id,extra)=>")
# viewEnd
i=s.index('function viewEnd(){'); j=s.index('// ── 지도 화면',i)
s=s[:i]+"""function viewEnd(){
  main.innerHTML=`<article class="col"><header class="chead"><p class="eyebrow">맺음</p><h1>천하에서 국가로</h1></header>
  <h2 class="sh">국가의 다섯 겹: 시대별 분포</h2>${heat()}
  <p class="note">수치는 이 책의 ‘사람들의 변화’ 표에 기록된 항목 수입니다.</p>
  ${DATA.concl?`<div class="rh">${rhHtml(DATA.concl)}</div>`:`<div class="todo"><b>집필 예정</b>여섯 부를 마친 뒤, 청 제국에서 오늘의 중국까지 버려진 것과 이어진 것을 국가의 다섯 겹으로 다시 정리한다.</div>`}</article>`;
}

"""+s[j:]
open(p,'w',encoding='utf-8').write(s); print('ok')
