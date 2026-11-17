import json
D = '/tmp/claude-0/-home-claude/4a153826-8782-5b1f-a4c8-74dc680cb13e/scratchpad/guide_rp/'
I = json.load(open(D + 'imgs.json'))
BOOK = 'index.html'

def fig(k, cap, cls=''):
    src, w, h = I[k]
    return f'<figure class="shot {cls}"><img src="{src}" width="{w}" height="{h}" alt="{cap}" decoding="async"><figcaption>{cap} <span class="zoom">· 눌러서 크게 보기</span></figcaption></figure>'

FAV = "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='6' fill='%23f3efe6'/%3E%3Crect x='7' y='7' width='18' height='18' rx='2' fill='none' stroke='%23a0372b' stroke-width='3'/%3E%3Crect x='12' y='12' width='8' height='8' fill='%23a0372b'/%3E%3C/svg%3E"

TOC = [('start', '처음 펼칠 때'), ('routes', '다섯 갈래 읽는 길'), ('chapter', '한 장의 짜임'), ('views', '열 개의 화면'),
       ('tools', '읽기 도구'), ('mobile', '휴대폰에서'), ('keys', '단축키'), ('faq', '자주 묻는 것')]

html = f'''<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>읽는 법 · 공화국의 탄생</title>
<meta name="description" content="『공화국의 탄생』를 잘 읽는 방법: 다섯 갈래 읽는 길, 한 장의 짜임, 지도·무대 연표·연결망·인물·사람들의 변화·요소별 변천 화면, 밑줄과 책갈피와 이어 읽기.">
<meta name="theme-color" content="#f4f2ee" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#121417" media="(prefers-color-scheme: dark)">
<link rel="icon" href="{FAV}">
<meta property="og:type" content="article">
<meta property="og:site_name" content="공화국의 탄생">
<meta property="og:title" content="읽는 법 — 공화국의 탄생">
<meta property="og:description" content="다섯 갈래 읽는 길, 한 장의 짜임, 열 개의 화면과 밑줄·책갈피 같은 읽기 도구 안내.">
<meta property="og:image" content="thumbnail.png">
<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;700;800&family=Noto+Serif+KR:wght@700&display=swap">
<style>
:root{{--bg:#f4f2ee;--surface:#fffdf9;--ink:#1d1f24;--muted:#5f636b;--line:#dcd7cd;--soft:#ece7dd;--accent:#8a3b22;--accent-soft:#f3e6df;
  --c1:#9a6a1c;--c2:#2c6a5e;--c3:#8a3b22;--sans:"Noto Sans KR","Apple SD Gothic Neo","Malgun Gothic",system-ui,sans-serif;--serif:"Noto Serif KR","Nanum Myeongjo",serif;color-scheme:light}}
@media (prefers-color-scheme:dark){{:root{{--bg:#121417;--surface:#1a1d21;--ink:#e6e3dc;--muted:#a3a7ad;--line:#2e3238;--soft:#23272c;--accent:#e59a7b;--accent-soft:#33241f;--c1:#d9a650;--c2:#6cc2ad;--c3:#e59a7b;color-scheme:dark}}}}
*{{box-sizing:border-box}}
html{{scroll-behavior:smooth;-webkit-text-size-adjust:100%}}
@media (prefers-reduced-motion:reduce){{html{{scroll-behavior:auto}}}}
body{{margin:0;background:var(--bg);color:var(--ink);font-family:var(--sans);font-size:17px;line-height:1.8;word-break:keep-all;overflow-wrap:break-word}}
a{{color:var(--accent)}}
.top{{position:sticky;top:0;z-index:10;background:color-mix(in srgb,var(--bg) 90%,transparent);backdrop-filter:blur(8px);-webkit-backdrop-filter:blur(8px);border-bottom:1px solid var(--line)}}
.top .in{{max-width:1080px;margin:0 auto;display:flex;align-items:center;gap:.8rem;padding:.55rem 16px}}
.brand{{font-weight:800;color:var(--ink);text-decoration:none;line-height:1.25}}
.brand small{{display:block;font-weight:500;color:var(--muted);font-size:.72rem}}
.sp{{flex:1}}
.open{{display:inline-flex;align-items:center;gap:.4rem;padding:.4rem .95rem;border-radius:999px;background:var(--ink);color:var(--bg);text-decoration:none;font-weight:700;font-size:.88rem;white-space:nowrap}}
.chipnav{{display:flex;gap:.35rem;overflow-x:auto;scrollbar-width:none;padding:0 16px .5rem;max-width:1080px;margin:0 auto}}
.chipnav::-webkit-scrollbar{{display:none}}
.chipnav a{{flex:none;font-size:.82rem;color:var(--muted);text-decoration:none;border:1px solid var(--line);border-radius:999px;padding:.15rem .7rem;background:var(--surface)}}
.chipnav a.on{{background:var(--ink);color:var(--bg);border-color:var(--ink)}}
.wrap{{max-width:1080px;margin:0 auto;padding:0 16px 5rem;display:grid;grid-template-columns:13rem minmax(0,1fr);gap:2.5rem}}
.side{{position:sticky;top:5.2rem;align-self:start;padding-top:2.4rem}}
.side ol{{list-style:none;margin:0;padding:0;border-left:2px solid var(--line)}}
.side a{{display:block;padding:.28rem .8rem;margin-left:-2px;border-left:2px solid transparent;color:var(--muted);text-decoration:none;font-size:.9rem}}
.side a.on{{color:var(--accent);border-left-color:var(--accent);font-weight:700}}
.side .book{{margin-top:1.2rem;font-size:.85rem}}
@media (min-width:901px){{.chipnav{{display:none}}}}
@media (max-width:900px){{.wrap{{grid-template-columns:1fr;gap:0}}.side{{display:none}}}}
main{{min-width:0;max-width:46rem}}
.hero{{padding:2.4rem 0 1rem}}
.strata{{display:flex;flex-direction:column;gap:5px;width:56px;margin-bottom:1.1rem}}
.strata i{{display:block;height:9px;border-radius:2px}}
h1{{font-family:var(--serif);font-size:clamp(1.8rem,5.5vw,2.5rem);line-height:1.25;margin:0 0 .3rem;letter-spacing:-.01em}}
.sub{{color:var(--muted);margin:0 0 1rem}}
.lede{{font-size:1.04rem}}
h2{{font-size:1.35rem;margin:3.2rem 0 .8rem;padding-top:1.2rem;border-top:1px solid var(--line);scroll-margin-top:6rem;line-height:1.4}}
h2 .no{{display:inline-block;min-width:1.9rem;color:var(--accent);font-family:var(--serif)}}
h3{{font-size:1.05rem;margin:1.8rem 0 .4rem;line-height:1.45}}
p{{margin:.55rem 0}}
.box{{background:var(--surface);border:1px solid var(--line);border-radius:14px;padding:1rem 1.15rem;margin:1rem 0}}
.box .lbl{{font-size:.78rem;font-weight:700;color:var(--muted);letter-spacing:.04em;margin:0 0 .3rem}}
.routes{{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:.75rem;margin:1rem 0}}
@media (max-width:600px){{.routes{{grid-template-columns:1fr}}}}
.route:last-child:nth-child(odd){{grid-column:1/-1}}
.route{{background:var(--surface);border:1px solid var(--line);border-radius:14px;padding:.9rem 1rem;border-top:4px solid var(--c)}}
.route h3{{margin:.1rem 0 .3rem}}
.route p{{margin:.2rem 0;font-size:.92rem;color:var(--muted)}}
.route ol{{margin:.4rem 0 0;padding-left:1.2rem;font-size:.92rem}}
.who{{font-size:.78rem;font-weight:700;color:var(--c)}}
.steps{{counter-reset:s;list-style:none;padding:0;margin:.8rem 0}}
.steps>li{{counter-increment:s;position:relative;padding:.1rem 0 .7rem 2.4rem}}
.steps>li::before{{content:counter(s);position:absolute;left:0;top:.2rem;width:1.6rem;height:1.6rem;border-radius:50%;background:var(--accent-soft);color:var(--accent);font-weight:800;font-size:.85rem;display:grid;place-items:center}}
.parts{{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:.4rem;margin:.8rem 0}}
.parts div{{background:var(--surface);border:1px solid var(--line);border-radius:10px;padding:.5rem .55rem;font-size:.8rem;line-height:1.45}}
.parts b{{display:block;font-size:.85rem}}
.parts span{{color:var(--muted)}}
@media (max-width:600px){{.parts{{grid-template-columns:1fr 1fr}}}}
.anatomy{{display:grid;grid-template-columns:auto 1fr;gap:.35rem .9rem;margin:.6rem 0;font-size:.95rem}}
.anatomy dt{{font-weight:700;white-space:nowrap}}
.anatomy dd{{margin:0;color:var(--muted)}}
@media (max-width:520px){{.anatomy{{grid-template-columns:1fr;gap:0}}.anatomy dd{{margin-bottom:.5rem}}}}
.shot{{margin:1rem 0 1.4rem}}
.shot img{{display:block;width:auto;max-width:100%;height:auto;margin:0 auto;border:1px solid var(--line);border-radius:12px;background:var(--surface);box-shadow:0 2px 10px rgb(0 0 0/.06)}}
.shot figcaption{{font-size:.82rem;color:var(--muted);margin-top:.4rem;line-height:1.55}}
.pair{{display:grid;grid-template-columns:1fr 1fr;gap:.9rem;align-items:start}}
.pair .shot{{margin:.6rem 0;min-width:0}}
.pair.three{{grid-template-columns:repeat(3,minmax(0,1fr))}}
@media (max-width:760px){{.pair.three{{grid-template-columns:1fr 1fr}}}}
.phone img{{max-width:min(300px,100%)}}
.shot.wide{{margin-left:0;margin-right:0}}
@media (max-width:600px){{.pair{{grid-template-columns:1fr}}}}
.phone img{{max-width:min(300px,100%);margin:0 auto}}
.phone figcaption{{text-align:center}}
.views{{display:grid;gap:1.2rem}}
.view h3{{margin-top:.6rem}}
.tag{{display:inline-block;font-size:.72rem;font-weight:700;color:var(--muted);border:1px solid var(--line);border-radius:999px;padding:0 .5rem;margin-left:.3rem;vertical-align:2px}}
table{{width:100%;border-collapse:collapse;font-size:.92rem;margin:.6rem 0}}
th,td{{text-align:left;padding:.45rem .5rem;border-bottom:1px solid var(--line);vertical-align:top}}
th{{color:var(--muted);font-weight:600;font-size:.8rem}}
td:first-child{{white-space:nowrap;font-weight:700}}
kbd{{font-family:inherit;font-size:.82rem;border:1px solid var(--line);border-bottom-width:2px;border-radius:6px;padding:0 .4rem;background:var(--surface)}}
.tools{{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:.7rem}}
@media (max-width:600px){{.tools{{grid-template-columns:1fr}}}}
.tool{{background:var(--surface);border:1px solid var(--line);border-radius:12px;padding:.75rem .9rem}}
.tool b{{display:block;margin-bottom:.15rem}}
.tool p{{margin:0;font-size:.9rem;color:var(--muted)}}
details{{background:var(--surface);border:1px solid var(--line);border-radius:12px;padding:.6rem .9rem;margin:.5rem 0}}
summary{{cursor:pointer;font-weight:700}}
details p{{color:var(--muted);font-size:.93rem}}
.end{{margin-top:3rem;padding:1.2rem;border-radius:14px;background:var(--accent-soft);text-align:center}}
.end .open{{margin-top:.6rem}}
footer{{color:var(--muted);font-size:.8rem;text-align:center;padding:2rem 16px calc(2rem + env(safe-area-inset-bottom,0px))}}
.shot img{{cursor:zoom-in}}
.lb{{position:fixed;inset:0;z-index:50;background:rgb(0 0 0/.86);overflow:auto;-webkit-overflow-scrolling:touch;display:block;padding:52px 10px 20px;background:rgb(0 0 0/.92)}}
.lb[hidden]{{display:none}}
.lb img{{display:block;margin:0 auto;max-width:none;width:min(100%,var(--w));height:auto;border-radius:8px;background:#fff}}
@media (max-width:700px){{.lb img{{width:var(--mw)}}}}
.lb .x{{position:fixed;top:10px;right:12px;font:inherit;font-weight:700;color:#fff;background:rgb(255 255 255/.15);border:1px solid rgb(255 255 255/.35);border-radius:999px;padding:.3rem .9rem;cursor:pointer}}
.lb .hint{{position:fixed;top:14px;left:14px;color:#ddd;font-size:.8rem}}
.shot figcaption .zoom{{white-space:nowrap}}
@media print{{.top,.side,.chipnav{{display:none}}.wrap{{display:block}}body{{font-size:12pt}}}}
</style>
</head>
<body>
<header class="top">
 <div class="in"><a class="brand" href="#start">읽는 법<small>공화국의 탄생</small></a><span class="sp"></span><a class="open" href="{BOOK}">책 열기 →</a></div>
 <nav class="chipnav" aria-label="이 안내의 차례">{''.join(f'<a href="#{i}">{t}</a>' for i, t in TOC)}</nav>
</header>
<div class="wrap">
<aside class="side" aria-label="이 안내의 차례"><ol>{''.join(f'<li><a href="#{i}">{t}</a></li>' for i, t in TOC)}</ol>
<p class="book"><a class="open" href="{BOOK}">책 열기 →</a></p></aside>
<main>
<section class="hero" id="start">
 <div class="strata" aria-hidden="true"><i style="background:var(--c1)"></i><i style="background:var(--c2)"></i><i style="background:var(--c3)"></i></div>
 <h1>『공화국의 탄생』<br>읽는 법</h1>
 <p class="sub">계몽에서 제3공화정까지, 유럽이 왕을 없앤 길, 1640–1875</p>
 <p class="lede">이 책은 한 권의 웹 페이지입니다. 처음부터 끝까지 차례대로 읽어도 되고, 지도나 연표에서 궁금한 사건 하나를 골라 들어가도 됩니다. 이 안내는 읽는 길을 고르는 법, 한 장을 읽는 법, 편리한 도구를 쓰는 법을 화면 사진과 함께 보여 드립니다.</p>
 <div class="box"><p class="lbl">이 책을 한눈에</p>
 <p><b>물음</b> 나라는 왕의 것이 아니라 시민 모두의 공적인 것이라는 생각은 어떻게 책 속의 이상에서 유럽의 정치 체제가 되었는가.<br>
 <b>다섯 고리</b> 생각, 결사, 위기, 제도, 전파와 반동. 공화정이 구체화되는 길을 장마다 이 고리로 읽습니다.<br>
 <b>다섯 겹</b> 주권, 시민권, 헌정 구조, 자유와 권리, 민족과 교회. 사건마다 공화정의 어느 겹이 바뀌었는지 기록합니다.<br>
 <b>다섯 무대</b> 파리, 프랑스 지방, 대서양과 북서 유럽, 남유럽, 중부·동유럽.<br>
 <b>60장</b> 프랑스 혁명을 가운데 두고, 1640년대 잉글랜드 공화국부터 1875년 프랑스 제3공화정 헌법까지를 여섯 부로 나누었습니다. 프랑스와 유럽의 다른 나라가 절반씩입니다.</p></div>
 <div class="parts" aria-label="여섯 부">
  <div><b>제1부</b>공화주의의 씨앗과 계몽<br><span>1640–1788</span></div>
  <div><b>제2부</b>혁명과 제1공화정<br><span>1789–1799</span></div>
  <div><b>제3부</b>혁명의 수출과 나폴레옹<br><span>1791–1815</span></div>
  <div><b>제4부</b>복고와 저항<br><span>1815–1847</span></div>
  <div><b>제5부</b>1848년, 민족의 봄<br><span>1846–1852</span></div>
  <div><b>제6부</b>공화정의 정착<br><span>1852–1875</span></div>
 </div>
 <p>사상을 다룬 장과 사건을 다룬 장은 대략 2 대 8로 나뉩니다. 계몽사상(제1부)과 1848년(제5부)에 무게를 두었고, 나폴레옹이 유럽에 끼친 영향은 제3부의 다섯 장에 걸쳐 다룹니다. 마지막의 <b>맺음</b>은 다섯 겹과 다섯 고리를 따라 235년을 다시 정리합니다.</p>
</section>

<h2 id="routes"><span class="no">1</span>다섯 갈래 읽는 길</h2>
<p>어디서 시작해도 됩니다. 장과 장이 서로 이어져 있어서 어느 길로 들어와도 다른 길로 건너갈 수 있습니다.</p>
<div class="routes">
 <div class="route" style="--c:var(--c1)"><span class="who">처음부터 차례대로</span><h3>책처럼 읽기</h3>
  <ol><li><b>읽기</b> 탭의 차례에서 제1부 배경 장을 엽니다.</li><li>장 끝의 <b>다음</b>을 눌러 넘어갑니다.</li><li>부가 바뀌면 그 부의 배경 장이 먼저 나오고, 60장 다음에는 <b>맺음</b>이 이어집니다.</li></ol>
  <p>배경 장은 그 시대의 큰 그림과 다섯 고리가 어떻게 맞물렸는지를 먼저 보여 주므로 건너뛰지 않기를 권합니다.</p></div>
 <div class="route" style="--c:var(--c2)"><span class="who">한 지역에 관심이 있다면</span><h3>한 무대만 이어 읽기</h3>
  <ol><li><b>무대 연표</b>에서 무대(예: 남유럽)를 누릅니다.</li><li><b>○○의 장만 이어 읽기</b>를 누릅니다.</li><li>장 끝의 <b>다음</b>이 그 무대의 다음 장으로 이어집니다.</li></ol>
  <p>자매 공화국과 카디스, 카르보나리와 마치니, 로마 공화국과 통일로 이어지는 남유럽처럼 한 지역의 긴 흐름을 따라갈 수 있습니다.</p></div>
 <div class="route" style="--c:var(--c3)"><span class="who">궁금한 사건이 있다면</span><h3>한 사건에서 시작하기</h3>
  <ol><li>맨 위 검색창에 사건·인물·용어를 넣거나, <b>지도</b>에서 번호를 누릅니다.</li><li>장을 읽은 뒤 끝의 <b>고리</b>에서 원인과 결과를 따라갑니다.</li></ol>
  <p>고리마다 왜 이어지는지 한 문장이 붙어 있습니다.</p></div>
 <div class="route" style="--c:var(--muted)"><span class="who">한 사람이나 한 집단이 궁금하다면</span><h3>사람을 따라가기</h3>
  <ol><li><b>인물</b>에서 이름(예: 로베스피에르, 마치니)을 누르면 그 사람이 나오는 장과 행적, 관계가 모여 있습니다.</li><li><b>사람들의 변화</b>에서 집단(도시 민중, 노동자, 농민, 부르주아)을 고르면 공화정의 어느 겹이 그들의 삶을 언제 바꾸었는지 보입니다.</li></ol></div>
 <div class="route" style="--c:var(--c2)"><span class="who">한 개념·상징·도시가 궁금하다면</span><h3>하나만 골라 끝까지 따라가기</h3>
  <ol><li><b>요소별 변천</b>에서 갈래(개념과 제도·상징·인물·도시·사람들)를 고릅니다.</li><li>항목(예: 보통선거, 삼색기, 파리, 여성)을 열어 해설을 읽고, 붉은 장 번호로 본문에 들어갑니다.</li></ol>
  <p>본문은 시대순이라 한 요소의 변화가 여러 장에 흩어져 있습니다. 그것을 한 편의 글로 모은 길입니다.</p></div>
</div>

<h2 id="chapter"><span class="no">2</span>한 장의 짜임</h2>
<p>60개의 장은 모두 같은 틀로 쓰였습니다. 틀을 알면 필요한 부분만 골라 읽기 쉽습니다. 장의 무게에 따라 분량이 다릅니다(핵심 장 약 5천 자, 주요 장 약 2,500자, 보조 장 약 1,500자).</p>
{fig('chapter', '장 머리: 부와 장 번호, 연대와 장소, 무대와 중요도, 이 장이 속한 고리, 책갈피·링크 단추, 이 장이 던지는 물음, 핵심 요약.')}
<dl class="anatomy">
 <dt>고리</dt><dd>장 머리의 작은 표시. 이 사건이 생각·결사·위기·제도·전파와 반동 가운데 어느 고리에 걸쳐 있는지 보여 줍니다.</dd>
 <dt>물음과 핵심</dt><dd>이 장이 답하려는 물음 한 줄과 사건의 요약.</dd>
 <dt>먼저 알아 둘 것</dt><dd>처음 접하는 독자를 위해 낯선 말과 시대를 풀어 주는 상자. 배경지식이 있으면 건너뛰어도 됩니다.</dd>
 <dt>작은 지도</dt><dd>사건의 자리와 앞뒤로 이어지는 사건의 위치(파란 선은 원인, 붉은 선은 결과). 미국과 아이티의 사건은 지도 서쪽 끝에 기호로 놓았습니다.</dd>
 <dt>배경 · 원인 · 주체 · 전개</dt><dd>본문. 무슨 일이 왜, 누구에 의해, 어떤 순서로 일어났는지.</dd>
 <dt>영향</dt><dd>이 사건이 공화정의 어느 겹(주권, 시민권, 헌정 구조, 자유와 권리, 민족과 교회)을 바꾸었고, 어느 집단의 삶에 닿았는지.</dd>
 <dt>해석의 갈림 · 흔한 오해</dt><dd>학자들의 견해가 갈리는 곳과 널리 퍼진 잘못된 이해. 사실과 해석을 나누어 적었습니다.</dd>
 <dt>고리(장 끝)</dt><dd>앞선 사건(원인)과 다음 사건(결과). 각각 왜 이어지는지 한 문장 설명.</dd>
 <dt>근거 도서</dt><dd>이 장이 기댄 책과 그 책의 해당 부분.</dd>
</dl>
<p>본문에서 이름 아래 진영 색 밑줄이 그어진 사람을 누르면 그 사람의 생몰년과 역할이, 점선이 그어진 말을 누르면 용어 풀이가 뜹니다.</p>
<div class="seq">
 {fig('term', '이름을 누르면 그 사람의 원어 이름과 진영, 이 장에서의 행적이 바로 뜹니다. ‘(39장)’처럼 붉은 장 번호를 누르면 그 장으로 갑니다.')}
 {fig('links', '장 끝의 고리. 원인과 결과마다 연결의 이유가 한 문장씩 붙어 있습니다.')}
</div>
<h3>배경 장과 맺음</h3>
<p>여섯 부는 저마다 배경 장으로 시작합니다. 그 시대의 큰 그림, 다섯 무대의 모습, 그리고 다섯 고리가 그 시대에 어떤 얼굴로 나타나 어떻게 맞물렸는지를 먼저 보여 줍니다. 책의 끝에는 <b>맺음</b>이 있어, 235년을 공화정의 다섯 겹과 다섯 고리로 다시 정리하고 ‘질서의 공화국’과 ‘사회의 공화국’이라는 두 얼굴을 돌아봅니다.</p>
{fig('part', '제3부 배경 장: 이 시대의 큰 그림과 다섯 고리.')}

<h2 id="views"><span class="no">3</span>열 개의 화면</h2>
<p>맨 위 탭으로 오갑니다. 어느 화면에서든 사건을 누르면 그 장의 요약 카드가 나오고, <b>본문 읽기</b>로 들어갈 수 있습니다.</p>
<div class="views">
 <div class="view"><h3>지도 <span class="tag">어디서</span></h3>
  <p>시대(부)를 고르면 그 부의 사건만 남습니다. 번호를 누르면 원인과 결과가 화살표로 이어지고, 옆 목록에 연결 이유가 나옵니다. <b>겹쳐 보기</b>로 강과 오늘의 국경을 켜고 끌 수 있습니다. 대서양 건너의 미국 혁명과 아이티 혁명은 지도의 서쪽 끝에 놓았습니다.</p>
  {fig('map', '지도: 41장 2월 혁명을 고른 모습. 다른 시대의 연결 사건은 빈 원으로 표시됩니다.')}</div>
 <div class="view"><h3>무대 연표 <span class="tag">언제·어느 지역</span></h3>
  <p>다섯 무대를 가로줄로 놓은 연표입니다. 큰 점은 사건의 중심 무대, 작은 빈 점은 함께 걸린 무대입니다. 같은 해의 사건은 조금씩 비켜 놓았습니다. 무대 이름을 누르면 그 무대가 강조되고 <b>그 무대의 장만 이어 읽기</b> 단추가 나타납니다.</p>
  <div class="seq">{fig('lanes', '파리를 고른 무대 연표.')}{fig('trail', '무대별 이어 읽기 목록. 범위(걸린 모든 장 / 중심 장만)를 고를 수 있습니다.')}</div></div>
 <div class="view"><h3>사건 연결망 <span class="tag">왜</span></h3>
  <p>고른 사건을 가운데 두고 왼쪽에 원인의 사슬, 오른쪽에 결과의 사슬을 펼칩니다. 선을 누르면 두 사건이 왜 이어지는지 위 칸에 나옵니다. <b>범주로 고르기</b>에서 부·무대·줄기·겹·집단·중요도 가운데 하나를 고르면 그 범주의 장만 모아 보여 줍니다.</p>
  {fig('net', '사건 연결망: 41장 2월 혁명에서 42장으로 이어지는 선을 고른 모습.')}</div>
 <div class="view"><h3>인물 <span class="tag">누가</span></h3>
  <p>책에 나오는 305명을 진영별 색(사상가, 왕정, 입헌파, 온건·급진 공화파, 민중·사회주의, 보나파르트파, 민족 운동가 등)으로 모은 화면입니다. 띠는 생애를, 띠 위의 작은 원은 그 사람이 나오는 장의 연대를 나타냅니다. 이름을 누르면 장별 행적과 다른 인물과의 관계가 나옵니다.</p>
  <div class="seq">{fig('pplist', '인물 화면: 진영 고르기와 생애 띠.', 'wide')}{fig('person', '한 사람의 쪽: 원어 이름과 생몰년, 진영, 역할, 그리고 아래로 장별 행적과 관계가 이어집니다.')}</div></div>
 <div class="view"><h3>사람들의 변화 <span class="tag">누구의 삶이 바뀌었나</span></h3>
  <p>60개 사건이 네 집단, 곧 도시 민중과 노동자, 농민과 부르주아에게 공화정의 어느 겹을 바꾸었는지 모은 색인입니다. 집단을 따라가거나, 겹 하나를 골라 집단끼리 견주어 볼 수 있습니다.</p>
  {fig('id', '노동자 화면: 다섯 겹이 바뀐 때를 여섯 부 위에 장 번호로 표시합니다.')}</div>
 <div class="view"><h3>요소별 변천 <span class="tag">하나만 끝까지</span></h3>
  <p>개념과 제도, 상징, 인물, 도시, 사람들의 다섯 갈래 20개 항목이 거쳐 온 길을 한 편의 글로 이어 읽는 화면입니다. 목록의 카드에는 단계 이름이 화살표로 이어져 있어 펼치지 않고도 흐름이 보입니다.</p>
  <p>항목을 열면 물음과 핵심 요약이 먼저 나오고, 이어 절로 나뉜 해설이 그 요소의 일대기를 풀어 씁니다. 해설 속 붉은 장 번호를 누르면 근거가 된 본문으로 갑니다. 맨 아래에는 <b>한눈에 보기</b>와 <b>단계별 정리</b>가 있습니다.</p>
  <div class="seq">{fig('lnlist', '요소별 변천 목록: 갈래를 고르고, 카드에서 단계의 흐름을 봅니다.')}{fig('lineage', '파리 항목의 첫머리: 물음, 핵심, 그리고 해설의 첫 절.')}{fig('lnglance', '항목 맨 아래의 한눈에 보기와 단계별 정리.')}</div></div>
 <div class="view"><h3>줄기 · 서가 · 용어</h3>
  <p><b>줄기</b>는 인민 주권의 길, 투표하는 시민, 공화국의 수출과 모방, 혁명과 질서의 네 흐름을 부를 건너 시간순으로 모았습니다. <b>서가</b>는 근거가 된 79권의 책과 그 책이 쓰인 장을, <b>용어</b>는 350여 항목의 사전을 분야별로 보여 줍니다. 우리말로 읽을 수 있는 책은 서가에 출판사와 함께 적었습니다.</p></div>
</div>

<h2 id="tools"><span class="no">4</span>읽기 도구</h2>
<div class="tools">
 <div class="tool"><b>찾기</b><p>맨 위 검색창에 사건·인물·용어·책 이름을 넣으면 바로 결과가 뜹니다. <kbd>/</kbd> 키로 곧장 검색창으로 갈 수 있습니다.</p></div>
 <div class="tool"><b>차례 서랍</b><p>왼쪽 위 ☰ 단추. 60장 전체 차례가 열리고, 읽은 장에는 초록 점이 찍힙니다.</p></div>
 <div class="tool"><b>지금 읽는 절 띠</b><p>긴 글 위쪽에 따라다니는 띠. 지금 절 이름과 진행 막대가 보이고, 누르면 절 목록으로 바로 옮겨 갑니다.</p></div>
 <div class="tool"><b>직전 위치로</b><p>링크를 따라간 뒤에는 오른쪽 아래 「← 직전 위치로」가 나타납니다. 누르면 떠났던 화면의 그 스크롤 자리로 돌아갑니다. 브라우저의 뒤로가기도 똑같이 작동합니다.</p></div>
 <div class="tool"><b>책갈피 · 링크 복사</b><p>장 머리의 「☆ 책갈피」로 모아 둔 장은 첫 화면에 나타납니다. 「링크 복사」는 그 장의 주소를 복사합니다.</p></div>
 <div class="tool"><b>밑줄 긋기</b><p>본문에서 글을 고르면(PC는 끌어서, 휴대폰은 길게 눌러서) 「밑줄 긋기」 단추가 뜹니다. 그은 밑줄은 다시 열어도 그 자리에 남고, 누르면 지울 수 있습니다.</p></div>
 <div class="tool"><b>밑줄 모음</b><p>그은 밑줄을 장별로 모아 봅니다. 문장을 누르면 그 장의 그 자리로 가고, 「모두 글로 복사」로 다른 곳에 옮길 수 있습니다.</p></div>
 <div class="tool"><b>이어 읽기</b><p>마지막에 읽던 장과 자리를 기억해, 첫 화면의 「읽던 곳 이어 읽기」로 곧장 돌아갑니다.</p></div>
 <div class="tool"><b>글자 크기 · 어두운 화면</b><p>오른쪽 위 Aa 단추로 글자 크기를, 달 모양 단추로 밝은·어두운 화면을 바꿉니다. 설정은 기억됩니다.</p></div>
 <div class="tool"><b>지도 겹쳐 보기</b><p>지도 위쪽 단추로 강과 현재 국경을 켜고 끕니다.</p></div>
</div>
{fig('search', '‘바스티유’를 찾은 모습: 장, 용어, 책이 함께 나옵니다.')}
{fig('secbar', '지금 읽는 절 띠를 누르면 이 장의 절 목록이 펼쳐집니다.')}
{fig('ul', '밑줄: 위 문단에 그어 둔 밑줄, 아래 문단에서 새로 고른 글과 「밑줄 긋기」 단추.')}
{fig('ullist', '밑줄 모음: 장별로 모이고, 문장을 누르면 그 자리로 갑니다.')}

<h2 id="mobile"><span class="no">5</span>휴대폰에서</h2>
<div class="pair three">
 {fig('m_ul', '글을 길게 눌러 고르면 「밑줄 긋기」가 뜹니다.', 'phone')}
 {fig('m_home', '첫 화면의 「읽던 곳 이어 읽기」, 책갈피, 밑줄 모음.', 'phone')}
 {fig('m_read', '읽는 동안에는 절 띠가 위에 붙어 따라옵니다.', 'phone')}
</div>
<ol class="steps">
 <li>밑줄은 글을 <b>길게 눌러</b> 고른 뒤, 손잡이로 범위를 맞추고 <b>밑줄 긋기</b>를 누릅니다. 휴대폰 자체의 메뉴(복사 등)가 함께 떠도 상관없습니다.</li>
 <li><b>밀어서 뒤로가기</b>를 써도 직전 화면의 그 자리로 돌아옵니다.</li>
 <li>아래로 읽어 내려가는 동안 떠 있는 단추가 글을 가리지 않게 비켜 있습니다. 화면을 조금 위로 올리면 다시 나타납니다.</li>
 <li>지도와 연결망, 인물의 생애 띠는 손가락으로 끌어 옮깁니다. 지도는 + − 단추로 확대·축소합니다(PC에서는 마우스 휠도 됩니다).</li>
 <li>홈 화면에 추가해 두면 앱처럼 열 수 있습니다. Safari는 공유 단추 → <b>홈 화면에 추가</b>, Chrome은 메뉴 → <b>홈 화면에 추가</b>입니다.</li>
</ol>

<h2 id="keys"><span class="no">6</span>단축키 <span class="tag">PC</span></h2>
<table><thead><tr><th>키</th><th>하는 일</th></tr></thead><tbody>
 <tr><td><kbd>/</kbd></td><td>검색창으로 가기</td></tr>
 <tr><td><kbd>Esc</kbd></td><td>열린 풀이 상자·검색 결과·차례를 닫기. 열린 것이 없으면 직전 위치로.</td></tr>
 <tr><td><kbd>Backspace</kbd></td><td>직전 위치로(입력칸 밖에서)</td></tr>
 <tr><td><kbd>Alt</kbd> + <kbd>←</kbd></td><td>브라우저 뒤로가기. 스크롤 자리까지 돌아옵니다.</td></tr>
</tbody></table>

<h2 id="faq"><span class="no">7</span>자주 묻는 것</h2>
<details><summary>사람과 땅 이름은 어떻게 적었나요?</summary><p>국립국어원 외래어 표기법에 따라 원어 발음으로 적되, 우리말에 이미 굳은 이름은 그대로 썼습니다(나폴레옹, 빈, 로마). 그래서 프랑스 사람은 프랑스어 발음(로베스피에르, 강베타), 이탈리아 사람은 이탈리아어 발음(마치니, 카보우르), 네덜란드 사람은 네덜란드어 발음(빌럼 5세)으로 적힙니다. 이름을 누르면 원어 표기가 함께 나옵니다.</p></details>
<details><summary>날짜를 공화력으로 적지 않은 이유는 무엇인가요?</summary><p>날짜는 오늘의 달력으로 적었습니다. 다만 테르미도르, 브뤼메르처럼 사건의 이름이 된 공화력의 달 이름은 그대로 씁니다. 공화력 자체는 21장에서 다룹니다.</p></details>
<details><summary>프랑스 이야기가 많은데, 유럽의 다른 나라는요?</summary><p>60장 가운데 절반 정도가 프랑스 밖의 사건입니다. 잉글랜드와 네덜란드, 미국과 아이티, 이탈리아와 스페인, 독일과 오스트리아, 헝가리와 체코, 폴란드와 아일랜드, 그리스와 스위스의 공화주의가 각자의 장을 가집니다. 지도와 무대 연표에서 지역별로 골라 읽을 수 있습니다.</p></details>
<details><summary>읽은 표시, 책갈피, 밑줄, 이어 읽기 기록은 어디에 저장되나요?</summary><p>이 기기의 브라우저에만 저장됩니다. 다른 기기나 다른 브라우저에서는 보이지 않고, 브라우저의 사이트 데이터를 지우면 함께 지워집니다. 서버로 보내지는 것은 없습니다.</p></details>
<details><summary>그어 둔 밑줄이 보이지 않아요.</summary><p>밑줄은 그은 기기와 브라우저에만 남습니다. 사생활 보호(시크릿) 창이나 사이트 데이터를 지운 뒤에는 보이지 않습니다. 책 내용이 고쳐져 문장이 바뀌면 그 밑줄은 「밑줄 모음」에 ‘위치를 찾지 못함’으로 남습니다. 오래 간직할 문장은 「모두 글로 복사」로 따로 옮겨 두기를 권합니다.</p></details>
<details><summary>특정 장을 다른 사람에게 보내고 싶어요.</summary><p>장 머리의 「링크 복사」를 누르면 그 장으로 바로 열리는 주소가 복사됩니다. 지도·연표·연결망·인물 화면의 주소도 그대로 보내면 같은 화면이 열립니다.</p></details>
<details><summary>숫자와 해석이 다른 책과 다릅니다.</summary><p>공포정치나 파리 코뮌 ‘피의 일주일’의 사망자 수처럼 추정이 갈리는 숫자는 본문에 범위를 적고, 해석이 갈리는 문제는 각 장의 「해석의 갈림」에, 널리 퍼진 잘못된 이해는 「흔한 오해」에 모아 두었습니다.</p></details>

<div class="end"><b>이제 책을 펼쳐 보세요.</b><br><a class="open" href="{BOOK}">『공화국의 탄생』 열기 →</a></div>

</main>
</div>
<footer>『공화국의 탄생』 읽는 법</footer>
<script>
(function(){{
  const ids={json.dumps([i for i, _ in TOC])};
  const links=[...document.querySelectorAll('.side a, .chipnav a')];
  function sync(){{
    let cur=ids[0];
    for(const id of ids){{const el=document.getElementById(id);if(el&&el.getBoundingClientRect().top<140)cur=id;}}
    links.forEach(a=>a.classList.toggle('on',a.getAttribute('href')==='#'+cur));
    const on=document.querySelector('.chipnav a.on');
    if(on){{const n=on.parentElement,l=on.offsetLeft-n.clientWidth/2+on.offsetWidth/2;if(Math.abs(n.scrollLeft-l)>40)n.scrollTo({{left:l,behavior:'smooth'}});}}
  }}
  addEventListener('scroll',sync,{{passive:true}});sync();
}})();
</script>
<div class="lb" id="lb" hidden role="dialog" aria-label="화면 사진 크게 보기"><span class="hint">밀어서 둘러보기 · 바깥을 누르면 닫힘</span><button class="x" type="button">닫기 ✕</button><img alt=""></div>
<script>
(function(){{
  const lb=document.getElementById('lb'),im=lb.querySelector('img');
  document.querySelectorAll('.shot img').forEach(i=>{{
    i.tabIndex=0;
    const open=()=>{{im.src=i.src;im.alt=i.alt;const nw=i.naturalWidth/2||i.width;im.style.setProperty('--w',nw+'px');im.style.setProperty('--mw',Math.round(Math.min(nw,Math.max(innerWidth*1.6,innerWidth)))+'px');lb.hidden=false;lb.scrollTo(0,0);document.body.style.overflow='hidden';}};
    i.addEventListener('click',open);i.addEventListener('keydown',e=>{{if(e.key==='Enter')open();}});
  }});
  const close=()=>{{lb.hidden=true;document.body.style.overflow='';}};
  lb.addEventListener('click',e=>{{if(e.target!==im)close();}});
  addEventListener('keydown',e=>{{if(e.key==='Escape'&&!lb.hidden)close();}});
}})();
</script>
</body>
</html>
'''
open('/home/claude/republic/dist/guide.html', 'w').write(html)
print(len(html) // 1024, 'KB')
