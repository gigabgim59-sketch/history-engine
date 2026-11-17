import re
p='template.html'; s=open(p,encoding='utf-8').read()
def R(a,b,cnt=1):
    global s
    n=s.count(a); assert n==cnt,(n,a[:90]); s=s.replace(a,b)
def sub(pat,rep,cnt=1):
    global s
    s2,n=re.subn(pat,rep,s,flags=re.S); assert n==cnt,(n,pat[:60]); s=s2
# lanes
R("const ticks=[-4000,-3000,-2000,-1500,-1000,-700,-500,-300,0,200,400,600,800,1000,1100,1200,1300,1400,1500,1600,1700,1800,1850,1900,1950,2000];","const ticks=[1840,1850,1860,1870,1880,1890,1900,1910,1920,1930,1940,1950,1960,1970,1980,1990,2000,2010,2020];")
R("""<p class="eyebrow">지역 연표</p>
  <div class="ctrl"><span class="lb">지역만 보기</span>""","""<p class="eyebrow">무대 연표</p>
  <div class="ctrl"><span class="lb">무대만 보기</span>""")
R('aria-label="지역별 사건 연표"','aria-label="무대별 사건 연표"')
sub(r'<p class="note">큰 점은 사건의 중심 지역, 작은 빈 점은 함께 걸린 지역입니다\.','<p class="note">큰 점은 사건의 중심 무대, 작은 빈 점은 함께 걸린 무대입니다.')
R("lt.textContent=`${R[o].n}의 장만 이어 읽기","lt.textContent=`${R[o].n}의 장만 이어 읽기")
# regionMini: drop 통사 link
sub(r'<a class="pill" href="#/r/\$\{r\}">이 지역의 통사 읽기</a>','')
sub(r'이 지역의 장만 이어 읽기 \(\$\{n\}장\)','이 무대의 장만 이어 읽기 (${n}장)')
# trail
R("<small>지역별 이어 읽기</small>","<small>무대별 이어 읽기</small>")
R("""<p class="eyebrow"><a href="#/lanes">지역 연표</a> · 지역별 이어 읽기</p>""","""<p class="eyebrow"><a href="#/lanes">무대 연표</a> · 무대별 이어 읽기</p>""")
sub(r'<p>이 책은 다섯 지역을 시대순으로 번갈아 다룹니다\..*?</p>\n','<p>이 책은 다섯 무대를 시대순으로 번갈아 다룹니다. 여기서는 ${esc(r.n)}에 걸린 장만 골라 책의 순서대로 이어 읽습니다. 장을 열면 맨 아래의 ‘다음’이 이 무대의 다음 장으로 이어지고, 맨 위 띠에서 언제든 책 전체의 순서로 돌아갈 수 있습니다.</p>\n')
R("이 지역이 걸린 모든 장 ·","이 무대가 걸린 모든 장 ·")
R("이 지역이 중심인 장만 ·","이 무대가 중심인 장만 ·")
sub(r'<a class="pill" href="#/r/\$\{rid\}">\$\{esc\(r\.n\)\}의 지역 통사</a>','')
R("‘함께’ 표시는 이 지역이 중심 무대는 아니지만","‘함께’ 표시는 이 무대가 중심은 아니지만")
# NETCAT
R("{k:'region',n:'지역',d:'다섯 무대'","{k:'region',n:'무대',d:'다섯 무대'")
R("{k:'thread',n:'줄기',d:'지역을 건너는 흐름'","{k:'thread',n:'줄기',d:'시대를 건너는 흐름'")
R("{k:'axis',n:'정체성의 겹',d:'무엇이 바뀌었나'","{k:'axis',n:'겹',d:'무엇이 바뀌었나'")
R("// 연결망을 범주별로 고르기: 부·지역·줄기·정체성의 겹·집단·중요도","// 연결망을 범주별로 고르기: 부·무대·줄기·겹·집단·중요도")
# viewId texts
sub(r'<p class="eyebrow">정체성 변화</p><h1 class="vt">누가, 언제, 무엇이 바뀌었나</h1>\n  <p class="lede">.*?</p>\n  <p>.*?</p>\n',
 '<p class="eyebrow">사람들의 변화</p><h1 class="vt">누구의, 무엇이, 언제 바뀌었나</h1>\n  <p class="lede">국가가 바뀌면 사람들의 삶도 바뀝니다. 이 화면은 ${DATA.events.length}개 사건이 ${DATA.groups.length}개 집단의 무엇을 바꾸었는지를 국가의 다섯 겹(주권·영토, 정치 체제, 경제, 사회, 이념)으로 나누어 모은 색인입니다. 지금까지 ${tot}건을 기록했습니다. 본문을 쓴 장의 기록만 들어 있고, 집필이 이어지면 늘어납니다.</p>\n')
sub(r'<p>칸의 숫자는 그 시대에 그 겹이 바뀐 기록의 수이고.*?</p>\n','<p>칸의 숫자는 그 시대에 그 겹이 바뀐 기록의 수이고, 색이 짙을수록 많습니다. 숫자를 누르면 그 칸의 변화가 아래에 펼쳐집니다.</p>\n')
sub(r'  <p class="note">혈통 겹은 고대 DNA 연구가.*?</p></div>`;','  <p class="note">이 분포는 맺음(<a href="#/end">천하에서 국가로</a>)에서 다시 읽습니다.</p></div>`;')
R("""<p class="eyebrow"><a href="#/id">정체성 변화</a> · 집단</p>""","""<p class="eyebrow"><a href="#/id">사람들의 변화</a> · 집단</p>""")
sub(r'<p class="note">가로는 시간\(다섯 부\), 세로는 겹입니다\..*?</p>','<p class="note">가로는 시간(여섯 부), 세로는 국가의 다섯 겹입니다. 점 하나가 그 겹을 바꾼 사건이고, 점 안의 숫자는 장 번호입니다.</p>')
R("""<p class="eyebrow"><a href="#/id">정체성 변화</a> · 겹별</p>""","""<p class="eyebrow"><a href="#/id">사람들의 변화</a> · 겹별</p>""")
R("<h2 class=\"sh\">다섯 겹이 바뀐 때</h2>","<h2 class=\"sh\">다섯 겹이 바뀐 때</h2>")
# thread / region
R("""<h1 style="font-family:var(--serif);font-size:1.7rem;margin:.2rem 0">다섯 줄기</h1>""","""<h1 style="font-family:var(--serif);font-size:1.7rem;margin:.2rem 0">네 줄기</h1>""")
R("부와 지역의 칸을 건너, 하나의 물음을 따라 사건을 시간 순으로 잇습니다.","부와 무대의 칸을 건너, 하나의 물음을 따라 사건을 시간 순으로 잇습니다.")
i=s.index('function viewRegion(rid){'); j=s.index('// ── 서가',i)
s=s[:i]+s[j:]
# lineage stage ref, notes
R("""<p class="note">각 단계는 그 일이 서술된 장으로 이어집니다. 띠 위의 점은 책 전체(제1부~제5부)에서 그 단계가 놓인 자리입니다.""","""<p class="note">각 단계는 그 일이 서술된 장으로 이어집니다. 띠 위의 점은 책 전체(제1부~제6부)에서 그 단계가 놓인 자리입니다.""")
sub(r'집단의 말·종교·정통성·이름·혈통이 언제 바뀌었는지 겹별로 나누어 보려면 <a href="#/id">정체성 변화</a>를 보세요\.','한 집단의 무엇이 언제 바뀌었는지 겹별로 보려면 <a href="#/id">사람들의 변화</a>를 보세요.')
sub(r'\$\{l\.g&&G\[l\.g\]\?`<p class="note">이 집단의 말·종교·정통성·이름·혈통이 각각 언제 바뀌었는지는 <a href="#/id/\$\{l\.g\}">정체성 변화: ','${l.g&&G[l.g]?`<p class="note">이 집단의 무엇이 언제 바뀌었는지는 <a href="#/id/${l.g}">사람들의 변화: ')
sub(r'본문은 시대순으로 흐르기 때문에, 한 집단이나 한 종교가 어떻게 바뀌어 왔는지는 여러 장에 흩어져 있습니다\. 이 화면은 그것을 하나씩 모았습니다\. 집단·종교·신화와 상징·언어와 문자·칭호와 제도·도시와 땅이름 가운데 하나를 고르면, 그것이 거쳐 온 모습들이 한 줄로 이어집니다\.','본문은 시대순으로 흐르기 때문에, 한 인물이나 정당이나 도시가 어떻게 바뀌어 왔는지는 여러 장에 흩어져 있습니다. 이 화면은 그것을 하나씩 모아 한 줄로 잇습니다.')
R("const LN=Object.fromEntries(DATA.lineage.map(l=>[l.id,l]))","const LN=Object.fromEntries(DATA.lineage.map(l=>[l.id,l]))")
R("""function viewLineage(id){
  const l=LN[id];if(l)return lineagePage(l);""","""function viewLineage(id){
  const l=LN[id];if(l)return lineagePage(l);
  if(!DATA.lineage.length){main.innerHTML=`<div class="col"><p class="eyebrow">요소별 변천</p><h1 class="vt">하나만 골라 끝까지 따라가기</h1><div class="todo"><b>집필 예정</b>인물(쑨원·장제스·마오쩌둥·덩샤오핑), 정당(국민당·공산당), 도시(상하이·홍콩·난징·충칭·선전), 개념(민족·혁명·민주), 조약과 제도, 변강(몽골·티베트·위구르·대만)의 일대기를 본문이 충분히 쓰인 뒤에 모읍니다.</div></div>`;return;}""")
# books
sub(r'<h1 style="font-family:var\(--serif\);font-size:1\.7rem;margin:\.2rem 0">\$\{DATA\.books\.length\}권과 그 역할</h1>.*?</div>`;\n  if\(bid\)',
 '''<h1 style="font-family:var(--serif);font-size:1.7rem;margin:.2rem 0">${DATA.books.length}권과 그 역할</h1>
  <p class="note">장마다 기댄 책과 그 부분을 적었습니다. 각 책이 어떤 장을 받치는지 아래에서 볼 수 있습니다. 본문을 쓰면서 서가가 늘어납니다.</p>
  <h2 class="sh">우리말 번역본 · ${ko.length}권</h2>${ko.map(card).join('')}
  <h2 class="sh">원서 · ${en.length}권</h2><p class="note">우리말 번역본이 확인되지 않은 책은 원서 제목으로 적었습니다.</p>${en.map(card).join('')}</div>`;
  if(bid)''')
R("const ext=DATA.events.filter(e=>e.ext);\n","")
R("""   <p style="color:var(--ink);margin-top:.4rem">${esc(b.role)}</p><p style="margin-top:.2rem"><b style="color:var(--warn)">읽을 때 주의</b> ${esc(b.warn)}</p>""","""   <p style="color:var(--ink);margin-top:.4rem">${esc(b.role)}</p>${b.warn&&b.warn!=='—'?`<p style="margin-top:.2rem"><b style="color:var(--warn)">읽을 때 주의</b> ${esc(b.warn)}</p>`:''}""")
R("""<p>${esc(b.a)}${b.tr?' · '+esc(b.tr):''}${b.pub?' · '+esc(b.pub):''}</p>""","""<p>${esc(b.a)}${b.tr?' · '+esc(b.tr):''}${b.pub?' · '+esc(b.pub):''}${b.o?' · '+esc(b.o):''}</p>""")
# terms
R("const CATS=['개념·제도','종교·사상','언어·문자','민족·집단','왕조·국가','땅이름','인물','문헌'];","const CATS=DATA.tcats;")
# search index
R("const IDX=[...DATA.events.map(e=>({h:'#/e/'+e.id,k:'사건',","const IDX=[...DATA.events.map(e=>({h:'#/e/'+e.id,k:'장',")
R(" ...DATA.regions.map(r=>({h:'#/r/'+r.id,k:'지역',t:r.n,s:r.d}))];"," ...DATA.regions.map(r=>({h:'#/rr/'+r.id,k:'무대',t:r.n,s:r.d}))];")
# route
R("  else if(v==='r'){viewRegion(a);tab='r';}","  else if(v==='r'){viewTrail(a);tab='lanes';}")
sub(r"document\.title=\(t\?t\+' · ':''\)\+'기원과 계승 그리고 [^']*';","document.title=(t?t+' · ':'')+DATA.meta.title;")
R("if(['p','r','ln'].includes(v)&&h[1])","if(['p','ln'].includes(v)&&h[1])")
R("if(v==='r'&&R[a])return `${R[a].n} 통사`;","")
R("if(!['e','p','end','r','ln'].includes(v))return;","if(!['e','p','end','ln'].includes(v))return;")
open(p,'w',encoding='utf-8').write(s); print('ok')
