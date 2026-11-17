import re
p='template.html'; s=open(p,encoding='utf-8').read()
def R(a,b,cnt=1):
    global s
    n=s.count(a)
    assert n==cnt, (n,a[:80])
    s=s.replace(a,b)
# head: lines 6-22 replace
i=s.index('<title>'); j=s.index('<link rel="icon"')
s=s[:i]+'''<title>__TITLE__</title>
<meta name="description" content="__DESC__">
<meta property="og:type" content="website">
<meta property="og:site_name" content="__TITLE__">
<meta property="og:title" content="__TITLE__ — __SUB__">
<meta property="og:description" content="__DESC__">
<meta property="og:locale" content="ko_KR">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#f4f2ee" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#121417" media="(prefers-color-scheme: dark)">
'''+s[j:]
# favicon: red seal
s=re.sub(r'<link rel="icon" href="[^"]*">','<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns=\'http://www.w3.org/2000/svg\' viewBox=\'0 0 32 32\'%3E%3Crect width=\'32\' height=\'32\' rx=\'6\' fill=\'%23f3efe6\'/%3E%3Crect x=\'7\' y=\'7\' width=\'18\' height=\'18\' rx=\'2\' fill=\'none\' stroke=\'%23a0372b\' stroke-width=\'3\'/%3E%3Crect x=\'12\' y=\'12\' width=\'8\' height=\'8\' fill=\'%23a0372b\'/%3E%3C/svg%3E">',s,count=1)
# part colors: add p6
R("--p1:#9a6a1c;--p2:#7b3f78;--p3:#2c7062;--p4:#3a5a9c;--p5:#a0372b;","--p1:#9a6a1c;--p2:#7b3f78;--p3:#2c7062;--p4:#3a5a9c;--p5:#a0372b;--p6:#5d6b1f;")
R("--p1:#d9a650;--p2:#c98ac5;--p3:#6cc2ad;--p4:#8fa9e6;--p5:#ec8577;","--p1:#d9a650;--p2:#c98ac5;--p3:#6cc2ad;--p4:#8fa9e6;--p5:#ec8577;--p6:#b7c46a;",2)
# axis colour classes
for a,b in [('ax-lang','ax-sov'),('ax-rel','ax-pol'),('ax-legit','ax-eco'),('ax-name','ax-soc'),('ax-blood','ax-ide')]:
    s=s.replace(a,b)
# header
R('<a class="brand" href="#/">기원과 계승 그리고 재창조</a>','<a class="brand" href="#/">__TITLE__</a>')
R('placeholder="사건, 집단, 용어 찾기"','placeholder="장, 인물, 용어 찾기"')
i=s.index('<nav class="tabs" id="tabs"'); j=s.index('</nav>',i)
s=s[:i]+'''<nav class="tabs" id="tabs" aria-label="화면">
  <a href="#/" data-v="home">읽기</a><a href="#/map" data-v="map">지도</a><a href="#/lanes" data-v="lanes">무대 연표</a><a href="#/net" data-v="net">사건 연결망</a><a href="#/id" data-v="id">사람들의 변화</a><a href="#/ln" data-v="ln">요소별 변천</a><a href="#/t" data-v="t">줄기</a><a href="#/books" data-v="books">서가</a><a href="#/terms" data-v="terms">용어</a>
 '''+s[j:]
R("localStorage.getItem('eu-'+k)","localStorage.getItem('cn-'+k)")
R("localStorage.setItem('eu-'+k,","localStorage.setItem('cn-'+k,")
R("const regChips=e=>e.r.map(r=>`<a class=\"chip\" href=\"#/r/${r}\">${esc(R[r].n)}</a>`).join('')+(e.pe?`<span class=\"chip\" title=\"지중해·유럽·중국과 얽힌 사건\">주변</span>`:'');",
  "const regChips=e=>e.r.map(r=>`<a class=\"chip\" href=\"#/rr/${r}\">${esc(R[r].n)}</a>`).join('');")
# TERM_DENY reset
i=s.index('const TERM_DENY={'); j=s.index('};',i)+2
s=s[:i]+"""const TERM_DENY={
 '위원':[/(상무|중앙|정치국|군사)\\s*$/,/^(장|회)/],
 '신사':[null,/^(층의|층이|층은|층을|층)/]
};"""+s[j:]
# toc end
R("`<li class=\"tp\">결론과 부록</li><li><a href=\"#/end\"><span class=\"n\">結</span><span>결론: 다섯 겹의 정체성 다시 보기</span></a></li>`","`<li class=\"tp\">맺음과 부록</li><li><a href=\"#/end\"><span class=\"n\">結</span><span>맺음: 천하에서 국가로</span></a></li>`")
open(p,'w',encoding='utf-8').write(s); print('ok')
