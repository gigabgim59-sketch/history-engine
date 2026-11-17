import json
D = '/tmp/claude-0/-home-claude/4a153826-8782-5b1f-a4c8-74dc680cb13e/scratchpad/guide/'
I = json.load(open(D + 'imgs.json'))
BOOK = 'index.html'

def fig(k, cap, cls=''):
    src, w, h = I[k]
    return f'<figure class="shot {cls}"><img src="{src}" width="{w}" height="{h}" alt="{cap}" decoding="async"><figcaption>{cap} <span class="zoom">· 눌러서 크게 보기</span></figcaption></figure>'

FAV = "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='6' fill='%23f3efe6'/%3E%3Crect x='6' y='7' width='20' height='5' rx='1.5' fill='%239a6a1c'/%3E%3Crect x='6' y='14' width='20' height='5' rx='1.5' fill='%232c6a5e'/%3E%3Crect x='6' y='21' width='20' height='5' rx='1.5' fill='%238a3b22'/%3E%3C/svg%3E"

TOC = [('start', '처음 펼칠 때'), ('routes', '네 갈래 읽는 길'), ('chapter', '한 장의 짜임'), ('views', '여덟 개의 화면'),
       ('tools', '읽기 도구'), ('mobile', '휴대폰에서'), ('keys', '단축키'), ('faq', '자주 묻는 것')]

html = f'''<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>읽는 법 · 기원과 계승 그리고 재창조</title>
<meta name="description" content="『기원과 계승 그리고 재창조』를 잘 읽는 방법: 네 갈래 읽는 길, 한 장의 짜임, 지도·연표·연결망·정체성 변화 화면, 책갈피와 이어 읽기 같은 읽기 도구.">
<meta name="theme-color" content="#f4f2ee" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#121417" media="(prefers-color-scheme: dark)">
<link rel="icon" href="{FAV}">
<meta property="og:type" content="article">
<meta property="og:site_name" content="기원과 계승 그리고 재창조">
<meta property="og:title" content="읽는 법 — 기원과 계승 그리고 재창조">
<meta property="og:description" content="네 갈래 읽는 길, 한 장의 짜임, 지도·연표·연결망·정체성 변화 화면과 읽기 도구 안내.">
<meta property="og:image" content="https://gigabgim59-sketch.github.io/WORLD/thumbnail.png">
<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta property="og:url" content="https://gigabgim59-sketch.github.io/WORLD/guide.html">
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
.route{{background:var(--surface);border:1px solid var(--line);border-radius:14px;padding:.9rem 1rem;border-top:4px solid var(--c)}}
.route h3{{margin:.1rem 0 .3rem}}
.route p{{margin:.2rem 0;font-size:.92rem;color:var(--muted)}}
.route ol{{margin:.4rem 0 0;padding-left:1.2rem;font-size:.92rem}}
.who{{font-size:.78rem;font-weight:700;color:var(--c)}}
.steps{{counter-reset:s;list-style:none;padding:0;margin:.8rem 0}}
.steps>li{{counter-increment:s;position:relative;padding:.1rem 0 .7rem 2.4rem}}
.steps>li::before{{content:counter(s);position:absolute;left:0;top:.2rem;width:1.6rem;height:1.6rem;border-radius:50%;background:var(--accent-soft);color:var(--accent);font-weight:800;font-size:.85rem;display:grid;place-items:center}}
.parts{{display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:.4rem;margin:.8rem 0}}
.parts div{{background:var(--surface);border:1px solid var(--line);border-radius:10px;padding:.5rem .55rem;font-size:.8rem;line-height:1.45}}
.parts b{{display:block;font-size:.85rem}}
.parts span{{color:var(--muted)}}
@media (max-width:600px){{.parts{{grid-template-columns:1fr 1fr}}.parts div:last-child{{grid-column:1/-1}}}}
.anatomy{{display:grid;grid-template-columns:auto 1fr;gap:.35rem .9rem;margin:.6rem 0;font-size:.95rem}}
.anatomy dt{{font-weight:700;white-space:nowrap}}
.anatomy dd{{margin:0;color:var(--muted)}}
@media (max-width:520px){{.anatomy{{grid-template-columns:1fr;gap:0}}.anatomy dd{{margin-bottom:.5rem}}}}
.shot{{margin:1rem 0 1.4rem}}
.shot img{{display:block;width:auto;max-width:100%;height:auto;margin:0 auto;border:1px solid var(--line);border-radius:12px;background:var(--surface);box-shadow:0 2px 10px rgb(0 0 0/.06)}}
.shot figcaption{{font-size:.82rem;color:var(--muted);margin-top:.4rem;line-height:1.55}}
.pair{{display:grid;grid-template-columns:1fr 1fr;gap:.9rem;align-items:start}}
.pair .shot{{margin:.6rem 0}}
.phone img{{max-width:300px}}
.shot.wide{{margin-left:0;margin-right:0}}
@media (max-width:600px){{.pair{{grid-template-columns:1fr}}}}
.phone img{{max-width:300px;margin:0 auto}}
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
 <div class="in"><a class="brand" href="#start">읽는 법<small>기원과 계승 그리고 재창조</small></a><span class="sp"></span><a class="open" href="{BOOK}">책 열기 →</a></div>
 <nav class="chipnav" aria-label="이 안내의 차례">{''.join(f'<a href="#{i}">{t}</a>' for i, t in TOC)}</nav>
</header>
<div class="wrap">
<aside class="side" aria-label="이 안내의 차례"><ol>{''.join(f'<li><a href="#{i}">{t}</a></li>' for i, t in TOC)}</ol>
<p class="book"><a class="open" href="{BOOK}">책 열기 →</a></p></aside>
<main>
<section class="hero" id="start">
 <div class="strata" aria-hidden="true"><i style="background:var(--c1)"></i><i style="background:var(--c2)"></i><i style="background:var(--c3)"></i></div>
 <h1>『기원과 계승 그리고 재창조』<br>읽는 법</h1>
 <p class="sub">근동·이란·인도·중앙유라시아·러시아, 6천 년 정체성의 역사</p>
 <p class="lede">이 책은 한 권의 웹 페이지입니다. 처음부터 끝까지 차례대로 읽을 수도 있고, 지도나 연표에서 궁금한 사건 하나를 골라 들어갈 수도 있습니다. 이 안내는 그 여러 길을 어떻게 고르고, 한 장을 어떻게 읽고, 어떤 도구를 쓰면 편한지를 화면 사진과 함께 보여 드립니다.</p>
 <div class="box"><p class="lbl">이 책을 한눈에</p>
 <p><b>다섯 무대</b> 근동·중동, 이란, 인도, 중앙유라시아, 러시아·동유럽.<br>
 <b>세 힘</b> 유일신 신앙, 인도유럽어 사람들, 투르크·몽골 유목민. 이야기를 움직이는 엔진입니다.<br>
 <b>다섯 겹</b> 언어, 종교, 정통성, 이름, 혈통. 정체성을 나누어 보는 틀입니다.<br>
 <b>120장</b> 기원전 4천년기부터 2026년까지의 분기점 사건을 다섯 부로 나누었습니다.</p></div>
 <div class="parts" aria-label="다섯 부">
  <div><b>제1부</b>문명과 신들의 기원<br><span>~ 기원전 5세기</span></div>
  <div><b>제2부</b>경전과 제국<br><span>~ 8세기 중엽</span></div>
  <div><b>제3부</b>초원과 이슬람의 만남<br><span>~ 13세기</span></div>
  <div><b>제4부</b>몽골 이후의 세계<br><span>~ 18세기</span></div>
  <div><b>제5부</b>제국의 해체와 민족의 탄생<br><span>~ 2026</span></div>
 </div>
 <p>제목의 세 낱말은 이 책이 따라가는 세 움직임입니다. 말과 신과 이름이 처음 생겨난 <b>기원</b>, 누가 정통을 잇는가를 다툰 <b>계승</b>, 근대의 민족과 국가가 옛 이름 가운데 하나를 골라 새로 지어낸 <b>재창조</b>입니다.</p>
</section>

<h2 id="routes"><span class="no">1</span>네 갈래 읽는 길</h2>
<p>어디서 시작해도 됩니다. 장과 장은 서로 이어져 있어서, 어느 길로 들어와도 다른 길로 건너갈 수 있습니다.</p>
<div class="routes">
 <div class="route" style="--c:var(--c1)"><span class="who">처음부터 차례대로</span><h3>책처럼 읽기</h3>
  <ol><li>맨 위 <b>읽기</b> 탭의 차례에서 제1부 배경 장을 엽니다.</li><li>장 끝의 <b>다음</b>을 눌러 넘어갑니다.</li><li>부가 바뀌면 그 부의 배경 장이 먼저 나옵니다.</li></ol>
  <p>배경 장은 그 시대 다섯 지역의 모습을 먼저 보여 주므로 건너뛰지 않기를 권합니다.</p></div>
 <div class="route" style="--c:var(--c2)"><span class="who">한 지역에 관심이 있다면</span><h3>한 지역만 이어 읽기</h3>
  <ol><li><b>지역 연표</b>에서 지역(예: 이란)을 누릅니다.</li><li><b>○○의 장만 이어 읽기</b>를 누릅니다.</li><li>장 끝의 <b>다음</b>이 그 지역의 다음 장으로 이어집니다.</li></ol>
  <p>사이의 흐름은 <b>지역 통사</b>가 메워 줍니다.</p></div>
 <div class="route" style="--c:var(--c3)"><span class="who">궁금한 사건이 있다면</span><h3>한 사건에서 시작하기</h3>
  <ol><li>위의 검색창에 사건·인물·용어를 넣거나, <b>지도</b>에서 번호를 누릅니다.</li><li>장을 읽은 뒤 끝의 <b>고리</b>에서 원인과 결과를 따라갑니다.</li></ol>
  <p>고리마다 왜 이어지는지 한 문장이 붙어 있습니다.</p></div>
 <div class="route" style="--c:var(--muted)"><span class="who">한 민족·집단이 궁금하다면</span><h3>정체성을 따라가기</h3>
  <ol><li><b>정체성 변화</b>에서 집단(예: 우즈벡인)을 고릅니다.</li><li>다섯 겹이 바뀐 때를 시간순으로 훑고, 궁금한 칸의 장으로 들어갑니다.</li></ol>
  <p>“우리는 언제 우리가 되었나”를 가장 빨리 보는 길입니다.</p></div>
</div>

<h2 id="chapter"><span class="no">2</span>한 장의 짜임</h2>
<p>120개의 장은 모두 같은 틀로 쓰였습니다. 틀을 알면 필요한 부분만 골라 읽기 쉽습니다. 장의 무게에 따라 분량이 다릅니다(핵심 장 약 5천 자, 주요 장 약 2,500자, 보조 장 약 1,500자).</p>
{fig('chapter', '장 머리: 부와 장 번호, 연대와 장소, 지역 표시와 중요도, 책갈피·링크 단추, 이 장이 던지는 물음, 핵심 요약.')}
<dl class="anatomy">
 <dt>물음과 핵심</dt><dd>이 장이 답하려는 물음 한 줄과, 사건을 세 문장으로 줄인 요약.</dd>
 <dt>먼저 알아 둘 것</dt><dd>처음 접하는 독자를 위해 시대·장소·인물을 풀어 주는 상자. 배경지식이 있으면 건너뛰어도 됩니다.</dd>
 <dt>작은 지도</dt><dd>사건의 자리와, 앞뒤로 이어지는 사건의 위치(파란 선은 원인, 붉은 선은 결과).</dd>
 <dt>배경 · 원인 · 주체 · 전개</dt><dd>본문. 무슨 일이 왜, 누구에 의해, 어떤 순서로 일어났는지.</dd>
 <dt>영향</dt><dd>이 사건이 어느 집단의 어느 겹(언어·종교·정통성·이름·혈통)을 바꾸었는지 표와 서술로.</dd>
 <dt>해석의 갈림 · 흔한 오해</dt><dd>학자들의 견해가 갈리는 곳과 널리 퍼진 잘못된 이해.</dd>
 <dt>고리</dt><dd>앞선 사건(원인)과 다음 사건(결과). 각각 왜 이어지는지 한 문장 설명.</dd>
 <dt>근거 도서</dt><dd>이 장이 기댄 책과 그 책의 해당 부분.</dd>
</dl>
<div class="seq">
 {fig('term', '점선 밑줄이 그어진 말을 누르면 용어 풀이가 바로 뜹니다. ‘(38장)’처럼 붉은 장 번호를 누르면 그 장으로 갑니다.')}
 {fig('links', '장 끝의 고리. 원인과 결과마다 연결의 이유가 한 문장씩 붙어 있습니다.')}
</div>

<h2 id="views"><span class="no">3</span>여덟 개의 화면</h2>
<p>맨 위 탭으로 오갑니다. 어느 화면에서든 사건을 누르면 그 장의 요약 카드가 나오고, <b>본문 읽기</b>로 들어갈 수 있습니다.</p>
<div class="views">
 <div class="view"><h3>지도 <span class="tag">어디서</span></h3>
  <p>시대(부)를 고르면 그 부의 사건만 남고 지도가 그 무대로 다가갑니다. 번호를 누르면 원인과 결과가 화살표로 이어지고, 옆 목록에 연결 이유가 나옵니다. 희미한 회색 선은 오늘의 국경으로, 위치를 가늠하라고 넣어 둔 것입니다.</p>
  {fig('map', '지도: 79장을 고른 모습. 다른 시대의 연결 사건은 빈 원으로 표시됩니다.')}</div>
 <div class="view"><h3>지역 연표 <span class="tag">언제·어느 지역</span></h3>
  <p>다섯 지역을 가로줄로 놓은 연표입니다. 큰 점은 사건의 중심 지역, 작은 빈 점은 함께 걸린 지역입니다. 지역 이름을 누르면 그 지역이 강조되고 <b>그 지역의 장만 이어 읽기</b> 단추가 나타납니다.</p>
  <div class="seq">{fig('lanes', '이란을 고른 지역 연표.')}{fig('trail', '지역별 이어 읽기 목록. 범위(걸린 모든 장 / 중심 장만)를 고를 수 있습니다.')}</div></div>
 <div class="view"><h3>사건 연결망 <span class="tag">왜</span></h3>
  <p>고른 사건을 가운데 두고 왼쪽에 원인의 사슬, 오른쪽에 결과의 사슬을 펼칩니다. 선을 누르면 두 사건이 왜 이어지는지 위 칸에 나옵니다. 장 고르기 목록과 이전·다음 단추, 펼칠 단계(1~3)가 있습니다. <b>범주로 고르기</b>에서 부·지역·줄기·정체성의 겹·집단·중요도 가운데 하나를 고르면 그 범주에 속한 장만 목록으로 모아 보여 주고, 그림에서도 그 장들만 진하게 표시합니다. 이때 이전·다음 단추는 그 범주 안에서 움직입니다(예: ‘이란 안에서 29 / 36’).</p>
  {fig('net', '사건 연결망: 79장에서 103장으로 이어지는 선을 고른 모습.')}</div>
 <div class="view"><h3>정체성 변화 <span class="tag">무엇이 바뀌었나</span></h3>
  <p>120개 사건이 15개 집단의 어느 겹을 바꾸었는지 모은 색인입니다. 집단을 따라가거나, 겹 하나(예: 종교)를 골라 집단끼리 견주거나, 시대별 표에서 숫자를 눌러 그 칸의 기록을 펼쳐 볼 수 있습니다.</p>
  {fig('id', '이란인 화면: 다섯 겹이 바뀐 때를 부 구간 위에 장 번호로 표시합니다.')}</div>
 <div class="view"><h3>지역 통사 · 줄기 · 서가 · 용어</h3>
  <p><b>지역 통사</b>는 한 지역의 6천 년을 한 편의 글로 이어 읽는 화면입니다. <b>줄기</b>는 신화·경전·칸·민족·초원 같은 흐름을 지역을 건너 시간순으로 모았습니다. <b>서가</b>는 근거가 된 책들과 그 책이 쓰인 장을, <b>용어</b>는 391개 항목의 사전을 분야별로 보여 줍니다.</p></div>
</div>

<h2 id="tools"><span class="no">4</span>읽기 도구</h2>
<div class="tools">
 <div class="tool"><b>찾기</b><p>맨 위 검색창에 사건·집단·용어·인물을 넣으면 바로 결과가 뜹니다. <kbd>/</kbd> 키로 곧장 검색창으로 갈 수 있습니다.</p></div>
 <div class="tool"><b>차례 서랍</b><p>왼쪽 위 ☰ 단추. 120장 전체 차례가 열리고, 읽은 장에는 초록 점이 찍힙니다.</p></div>
 <div class="tool"><b>지금 읽는 절 띠</b><p>긴 글 위쪽에 따라다니는 띠. 지금 절 이름과 진행 막대가 보이고, 누르면 절 목록으로 바로 옮겨 갑니다.</p></div>
 <div class="tool"><b>직전 위치로 · 맨 위로</b><p>링크를 따라간 뒤에는 오른쪽 아래 「← 직전 위치로」가 나타납니다. 누르면 떠났던 화면의 그 스크롤 자리로 돌아갑니다. 브라우저의 뒤로가기도 똑같이 작동합니다.</p></div>
 <div class="tool"><b>책갈피 · 링크 복사</b><p>장 머리의 「☆ 책갈피」로 모아 둔 장은 첫 화면에 나타납니다. 「링크 복사」는 그 장의 주소를 복사해 다른 사람에게 보낼 수 있게 합니다.</p></div>
 <div class="tool"><b>이어 읽기</b><p>마지막에 읽던 장과 그 자리를 기억해, 첫 화면의 「읽던 곳 이어 읽기」로 곧장 돌아갑니다.</p></div>
 <div class="tool"><b>글자 크기 · 어두운 화면</b><p>오른쪽 위 Aa 단추로 글자 크기를, 달 모양 단추로 밝은·어두운 화면을 바꿉니다. 설정은 기억됩니다.</p></div>
 <div class="tool"><b>현재 국경 켜고 끄기</b><p>지도 범례의 「현재 국경」 칸으로 오늘의 국경선을 보이거나 감춥니다.</p></div>
</div>
{fig('secbar', '지금 읽는 절 띠를 누르면 이 장의 절 목록이 펼쳐집니다.')}

<h2 id="mobile"><span class="no">5</span>휴대폰에서</h2>
<div class="pair">
 {fig('m_home', '첫 화면의 「읽던 곳 이어 읽기」와 책갈피.', 'phone')}
 {fig('m_read', '읽는 동안에는 단추들이 비켜 있다가, 위로 살짝 올리면 돌아옵니다.', 'phone')}
</div>
<ol class="steps">
 <li><b>밀어서 뒤로가기</b>를 써도 직전 화면의 그 자리로 돌아옵니다.</li>
 <li>아래로 읽어 내려가는 동안 떠 있는 단추가 글을 가리지 않게 비켜 있습니다. 화면을 조금 위로 올리면 다시 나타납니다.</li>
 <li>지도와 연결망은 손가락으로 끌어 옮기고, 지도는 + − 단추로 확대·축소합니다(PC에서는 마우스 휠도 됩니다).</li>
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
<details><summary>읽은 표시, 책갈피, 이어 읽기 기록은 어디에 저장되나요?</summary><p>이 기기의 브라우저에만 저장됩니다. 다른 기기나 다른 브라우저에서는 보이지 않고, 브라우저의 사이트 데이터를 지우면 함께 지워집니다. 서버로 보내지는 것은 없습니다.</p></details>
<details><summary>특정 장을 다른 사람에게 보내고 싶어요.</summary><p>장 머리의 「링크 복사」를 누르면 그 장으로 바로 열리는 주소가 복사됩니다. 지도·연표·연결망 화면의 주소도 그대로 보내면 같은 화면이 열립니다.</p></details>
<details><summary>연대나 이름 표기가 다른 책과 다릅니다.</summary><p>이 책은 한 사람·한 지명을 처음부터 끝까지 한 가지로 적습니다(예: 칭기즈칸, 키이우, 콘스탄티노폴리스). 학설이 갈리는 연대는 본문에서 밝히고, 해석이 갈리는 문제는 각 장의 「해석의 갈림」에 모아 두었습니다.</p></details>
<details><summary>최근 사건은 어디까지 다루나요?</summary><p>2024년부터 2026년 10월까지 이어진 이란·이스라엘·미국 전쟁(120장)과 러시아-우크라이나 전쟁(119장)까지입니다. 최근 사건은 널리 인정되는 원인과 경과를 중심으로 적었습니다.</p></details>
<details><summary>지도의 국경은 언제 기준인가요?</summary><p>지도 위 사건의 자리는 그 사건이 일어난 곳이고, 희미한 회색 선은 오늘의 국경입니다. 크림은 국제적으로 인정된 경계를 따르고, 카슈미르는 실효 지배선으로 그렸습니다.</p></details>

<div class="end"><b>이제 책을 펼쳐 보세요.</b><br><a class="open" href="{BOOK}">『기원과 계승 그리고 재창조』 열기 →</a></div>
</main>
</div>
<footer>『기원과 계승 그리고 재창조』 읽는 법</footer>
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
open('/home/claude/eurasia/guide.html', 'w').write(html)
print(len(html) // 1024, 'KB')
