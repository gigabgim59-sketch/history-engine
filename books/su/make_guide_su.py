import json
D = '/tmp/claude-0/-home-claude/4a153826-8782-5b1f-a4c8-74dc680cb13e/scratchpad/guide_su/'
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
<title>읽는 법 · 깃발이 내려지기까지</title>
<meta name="description" content="『깃발이 내려지기까지』을 잘 읽는 방법: 다섯 갈래 읽는 길, 한 장의 짜임, 지도·무대 연표·연결망·인물·사람들의 변화·요소별 변천 화면, 밑줄과 책갈피와 이어 읽기.">
<meta name="theme-color" content="#f4f2ee" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#121417" media="(prefers-color-scheme: dark)">
<link rel="icon" href="{FAV}">
<meta property="og:type" content="article">
<meta property="og:site_name" content="깃발이 내려지기까지">
<meta property="og:title" content="읽는 법 — 깃발이 내려지기까지">
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
.parts{{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:.4rem;margin:.8rem 0}}
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
 <div class="in"><a class="brand" href="#start">읽는 법<small>깃발이 내려지기까지</small></a><span class="sp"></span><a class="open" href="{BOOK}">책 열기 →</a></div>
 <nav class="chipnav" aria-label="이 안내의 차례">{''.join(f'<a href="#{i}">{t}</a>' for i, t in TOC)}</nav>
</header>
<div class="wrap">
<aside class="side" aria-label="이 안내의 차례"><ol>{''.join(f'<li><a href="#{i}">{t}</a></li>' for i, t in TOC)}</ol>
<p class="book"><a class="open" href="{BOOK}">책 열기 →</a></p></aside>
<main>
<section class="hero" id="start">
 <div class="strata" aria-hidden="true"><i style="background:var(--c1)"></i><i style="background:var(--c2)"></i><i style="background:var(--c3)"></i></div>
 <h1>『깃발이 내려지기까지』<br>읽는 법</h1>
 <p class="sub">1905년 혁명에서 소련 해체와 1993년 10월까지</p>
 <p class="lede">이 책은 한 권의 웹 페이지입니다. 처음부터 끝까지 차례대로 읽어도 되고, 지도나 연표, 연결망에서 궁금한 사건 하나를 골라 들어가도 됩니다. 이 안내는 읽는 길을 고르는 법, 한 장을 읽는 법, 편리한 도구를 쓰는 법을 화면 사진과 함께 보여 드립니다.</p>
 <div class="box"><p class="lbl">이 책을 한눈에</p>
 <p><b>물음</b> 1905년 1월 겨울궁전 앞에서 1993년 10월 모스크바의 의회 포격까지, 88년 사이에 붉은 깃발은 어떻게 올라갔다가 내려갔나. 그 아래의 사람들은 무엇을 믿고, 견디고, 잃었나.<br>
 <b>두 종류의 장</b> 권력과 경제, 민족과 전쟁의 분기점을 다루는 <b>사건</b> 장 84개와, 그 시대 러시아가 스스로를 무엇이라 여겼는지 묻는 <b>문화</b> 장 15개.<br>
 <b>세 힘</b> 당과 국가, 사회와 민족, 전쟁과 세계. 장마다 어느 힘이 흐름을 움직였는지 읽습니다.<br>
 <b>다섯 줄기</b> 혁명과 권력, 공업화와 계획, 제국과 민족, 전쟁과 세계, 러시아란 무엇인가.<br>
 <b>8부 99장</b> 시대순의 일곱 부에 각 12개의 사건 장과 1개의 짧은 문화 장을 두고, 마지막 제8부는 주제의 부로 묶었습니다.</p></div>
 <div class="parts" aria-label="여덟 부">
  <div><b>제1부</b>제국의 황혼<br><span>1905–1917</span></div>
  <div><b>제2부</b>혁명과 내전<br><span>1917–1921</span></div>
  <div><b>제3부</b>신경제정책과 권력 투쟁<br><span>1921–1928</span></div>
  <div><b>제4부</b>위로부터의 혁명<br><span>1928–1941</span></div>
  <div><b>제5부</b>대조국전쟁과 초강대국<br><span>1941–1953</span></div>
  <div><b>제6부</b>해빙과 정체<br><span>1953–1985</span></div>
  <div><b>제7부</b>개혁과 해체<br><span>1985–1993</span></div>
  <div><b>제8부</b>나타샤의 춤: 러시아란 무엇인가<br><span>1905–1993 · 주제</span></div>
 </div>
 <p>사건은 그 시대 사람들이 무엇을 알고 무엇을 두려워했는지에서 출발해 설명합니다. 권력만이 아니라 경제와 사회, 민족, 문화에 같은 무게를 두었습니다. 제8부는 영국 역사가 올랜도 피지스의 『나타샤의 춤』(Natasha’s Dance)이 던진 물음, 곧 러시아는 유럽인가 아시아인가, 귀족과 민중은 하나의 민족인가를 빌려, 그 물음이 혁명 국가 안에서 어떻게 이어지고 바뀌었는지 따라갑니다. 마지막의 <b>맺음</b>은 다섯 갈래 길을 따라 88년을 다시 정리합니다.</p>
 <p>사실과 해석을 나누어 적었습니다. 평가가 갈리는 문제는 장마다 「해석의 갈림」에, 널리 퍼진 잘못된 이해는 「흔한 오해」에 따로 모았습니다.</p>
</section>
<h2 id="routes"><span class="no">1</span>다섯 갈래 읽는 길</h2>
<p>어디서 시작해도 됩니다. 장과 장이 서로 이어져 있어서 어느 길로 들어와도 다른 길로 건너갈 수 있습니다.</p>
<div class="routes">
 <div class="route" style="--c:var(--c1)"><span class="who">처음부터 차례대로</span><h3>책처럼 읽기</h3>
  <ol><li><b>읽기</b> 탭의 차례에서 제1부 배경 장을 엽니다.</li><li>장 끝의 <b>다음</b>을 눌러 넘어갑니다.</li><li>부의 끝에는 그 부의 문화 장이, 제7부 다음에는 제8부의 주제 장들이, 그 뒤에 <b>맺음</b>이 이어집니다.</li></ol>
  <p>배경 장은 그 시대의 큰 그림과 세 힘을 먼저 보여 주므로 건너뛰지 않기를 권합니다.</p></div>
 <div class="route" style="--c:var(--c2)"><span class="who">문화와 정체성이 궁금하다면</span><h3>러시아란 무엇인가 따라가기</h3>
  <ol><li><b>줄기</b>에서 ‘러시아란 무엇인가’를 고르면 은세기와 아방가르드, 사회주의 리얼리즘, 마을 산문, 망명 문학이 시간순으로 이어집니다.</li><li>제8부의 여덟 장은 유럽과 아시아, 민중, 신앙, 망명 같은 물음을 88년에 걸쳐 따라갑니다.</li></ol></div>
 <div class="route" style="--c:var(--c3)"><span class="who">궁금한 사건이 있다면</span><h3>한 사건에서 시작하기</h3>
  <ol><li>맨 위 검색창에 사건·인물·용어를 넣거나, <b>지도</b>에서 번호를 누릅니다.</li><li>장을 읽은 뒤 끝의 <b>고리</b>에서 원인과 결과를 따라갑니다.</li></ol>
  <p>고리마다 왜 이어지는지 한 문장이 붙어 있습니다.</p></div>
 <div class="route" style="--c:var(--muted)"><span class="who">한 지역이 궁금하다면</span><h3>무대별로 이어 읽기</h3>
  <ol><li><b>무대 연표</b>에서 수도, 러시아 내륙, 서부 변경, 남부 변경, 바깥 세계 가운데 하나를 누릅니다.</li><li><b>그 무대의 장만 이어 읽기</b>로 우크라이나와 발트, 캅카스와 중앙아시아의 길을 따로 따라갑니다.</li></ol></div>
 <div class="route" style="--c:var(--c2)"><span class="who">한 사람·한 집단·한 요소가 궁금하다면</span><h3>하나만 골라 끝까지 따라가기</h3>
  <ol><li><b>인물</b>에서 이름(예: 이오시프 스탈린)을 누르면 그 사람이 나오는 장과 행적이 모입니다.</li><li><b>사람들의 변화</b>에서 집단(노동자, 농민, 지식인과 예술가, 비러시아 민족들, 여성과 가족, 당과 간부)을 고릅니다.</li><li><b>요소별 변천</b>에서 항목(예: 소비에트, 붉은 깃발과 삼색기, 고려인)을 엽니다.</li></ol></div>
</div>
<h2 id="chapter"><span class="no">2</span>한 장의 짜임</h2>
<p>99개의 장은 모두 같은 틀로 쓰였습니다. 장의 무게에 따라 분량이 다릅니다(핵심 장 약 4,600자, 주요 장 약 2,300자, 각 부 끝의 문화 장은 2,000자 안팎). 문화 장은 본문의 절 이름이 조금 다릅니다. ‘배경·원인·주체·전개’ 대신 ‘뿌리’, ‘맞선 두 극’, ‘작품과 목소리’, ‘흐름’으로 이어집니다.</p>
{fig('chapter', '장 머리: 부와 장 번호, 연대와 장소, 장의 종류와 무대와 중요도, 이 장을 움직인 힘, 책갈피·링크 단추, 이 장이 던지는 물음, 핵심 요약.')}
<dl class="anatomy">
 <dt>종류와 힘</dt><dd>장 머리의 작은 표시. 사건 장인지 문화 장인지, 당과 국가·사회와 민족·전쟁과 세계 가운데 어느 힘으로 움직였는지 보여 줍니다.</dd>
 <dt>물음과 핵심</dt><dd>이 장이 답하려는 물음 한 줄과 요약.</dd>
 <dt>먼저 알아 둘 것</dt><dd>낯선 말과 제도를 풀어 주는 상자.</dd>
 <dt>본문</dt><dd>배경에서 전개까지. 무슨 일이 왜, 누구에 의해, 어떤 순서로 일어났는지.</dd>
 <dt>그 시대의 말 · 이 장의 작품</dt><dd>그 시대의 구호와 말, 그리고 그 시대를 보여 주는 소설·시·영화·음악.</dd>
 <dt>영향</dt><dd>이 사건이 권력·경제·사회·민족·사상과 문화의 어느 축을 바꾸었고, 어느 집단의 삶에 닿았는지.</dd>
 <dt>해석의 갈림 · 흔한 오해</dt><dd>견해가 갈리는 곳과 널리 퍼진 잘못된 이해.</dd>
 <dt>고리 · 근거 도서</dt><dd>앞선 사건과 다음 사건, 그리고 이 장이 기댄 책.</dd>
</dl>
<p>본문에서 이름 아래 색 밑줄이 그어진 사람을 누르면 러시아어 원명과 생몰년, 역할이, 점선이 그어진 말을 누르면 용어 풀이가 뜹니다.</p>
<div class="seq">
 {fig('term', '이름을 누르면 원명과 생몰년, 이 장에서의 행적이 바로 뜹니다.')}
 {fig('links', '장 끝의 고리. 원인과 결과마다 연결의 이유가 한 문장씩 붙어 있습니다.')}
</div>
<h3>배경 장, 제8부, 맺음</h3>
<p>여덟 부는 저마다 배경 장으로 시작합니다. 그 시대의 큰 그림, 다섯 무대의 모습, 세 힘이 어떻게 맞물렸는지를 먼저 보여 줍니다. 제8부는 시대가 아니라 주제의 부여서, 연표와 무대 연표의 띠에는 나타나지 않고 1905년부터 1993년까지를 가로지릅니다. 책의 끝에는 <b>맺음</b>이 있어, 88년을 혁명과 권력, 공업화와 계획, 제국과 민족, 전쟁과 세계, 러시아란 무엇인가의 다섯 갈래로 다시 정리합니다.</p>
<div class="seq">{fig('part', '제3부 배경 장: 이 시대의 큰 그림과 세 힘.')}{fig('theme', '제8부 배경 장: 피지스의 물음에서 출발하는 주제의 부.')}</div>
<h2 id="views"><span class="no">3</span>열 개의 화면</h2>
<p>맨 위 탭으로 오갑니다. 어느 화면에서든 사건을 누르면 그 장의 요약 카드가 나오고, <b>본문 읽기</b>로 들어갈 수 있습니다.</p>
<div class="views">
 <div class="view"><h3>지도 <span class="tag">어디서</span></h3>
  <p>시대(부)를 고르면 그 부의 사건만 남습니다. 번호를 누르면 원인과 결과가 화살표로 이어지고, 옆 목록에 연결 이유가 나옵니다. 베를린과 워싱턴, 쿠바처럼 멀리 떨어진 사건은 가장자리에 놓았습니다.</p>
  {fig('map', '지도: 47장 대테러를 고른 모습.')}</div>
 <div class="view"><h3>무대 연표 <span class="tag">언제·어느 지역</span></h3>
  <p>수도(페테르부르크와 모스크바), 러시아 내륙, 서부 변경(우크라이나·벨라루스·발트), 남부 변경(캅카스와 중앙아시아), 바깥 세계의 다섯 무대를 가로줄로 놓은 연표입니다. 무대 이름을 누르면 <b>그 무대의 장만 이어 읽기</b> 단추가 나타납니다.</p>
  <div class="seq">{fig('lanes', '수도를 고른 무대 연표.')}{fig('trail', '무대별 이어 읽기 목록.')}</div></div>
 <div class="view"><h3>사건 연결망 <span class="tag">왜</span></h3>
  <p>고른 사건을 가운데 두고 왼쪽에 원인의 사슬, 오른쪽에 결과의 사슬을 펼칩니다. 선을 누르면 두 사건이 왜 이어지는지 나옵니다. <b>범주로 고르기</b>에서 부·무대·줄기·축·집단·장의 종류·중요도로 장을 모을 수 있습니다.</p>
  {fig('net', '사건 연결망: 47장 대테러를 가운데 둔 모습.')}</div>
 <div class="view"><h3>인물 <span class="tag">누가</span></h3>
  <p>책에 나오는 402명을 분야별 색(차르와 궁정, 제정 관료와 백군, 자유주의자와 온건 사회주의자, 볼셰비키와 소련 지도자, 비밀경찰과 군, 반대파와 반체제, 작가와 예술가, 학자와 사상가, 민족 운동가와 공화국 지도자, 외국의 지도자, 보통 사람들, 성직자와 신자)으로 모은 화면입니다. 띠는 생애를, 띠 위의 작은 원은 그 사람이 나오는 장의 연대를 나타냅니다.</p>
  <div class="seq">{fig('pplist', '인물 화면: 분야 고르기와 생애 띠.', 'wide')}{fig('person', '한 사람의 쪽: 이오시프 스탈린.')}</div></div>
 <div class="view"><h3>사람들의 변화 <span class="tag">누구의 삶이 바뀌었나</span></h3>
  <p>99개 장이 여섯 집단, 곧 노동자, 농민, 지식인과 예술가, 비러시아 민족들, 여성과 가족, 당과 간부의 삶을 언제 어떻게 바꾸었는지 모은 색인입니다.</p>
  {fig('id', '노동자: 다섯 축이 바뀐 때를 일곱 부 위에 장 번호로 표시합니다.')}</div>
 <div class="view"><h3>요소별 변천 <span class="tag">하나만 끝까지</span></h3>
  <p>제도와 권력, 상징, 인물, 장소, 사람들의 다섯 갈래 16개 항목이 거쳐 온 길을 한 편의 글로 이어 읽는 화면입니다. 소비에트와 체카, 공산당, 레닌의 몸과 붉은 깃발, 원자력, 스탈린과 아흐마토바와 솔제니친, 페테르부르크와 우크라이나와 카자흐 초원, 농민과 여성과 유대인과 고려인을 88년에 걸쳐 따라갑니다.</p>
  <div class="seq">{fig('lnlist', '요소별 변천 목록.')}{fig('lineage', '고려인 항목의 첫머리: 물음, 핵심, 해설.')}{fig('lnglance', '항목 맨 아래의 한눈에 보기와 단계별 정리.')}</div></div>
 <div class="view"><h3>줄기 · 서가 · 용어</h3>
  <p><b>줄기</b>는 혁명과 권력, 공업화와 계획, 제국과 민족, 전쟁과 세계, 러시아란 무엇인가의 다섯 흐름을 부를 건너 시간순으로 모았습니다. <b>서가</b>는 근거가 된 132권의 책을 영어 원서 113권과 러시아어 원서 19권으로 나누어 보여 주고, <b>용어</b>는 350여 항목의 사전을 분야별로 보여 줍니다.</p></div>
</div>
<h2 id="tools"><span class="no">4</span>읽기 도구</h2>
<div class="tools">
 <div class="tool"><b>찾기</b><p>맨 위 검색창에 사건·인물·용어·책 이름을 넣으면 바로 결과가 뜹니다. <kbd>/</kbd> 키로 곧장 검색창으로 갈 수 있습니다.</p></div>
 <div class="tool"><b>차례 서랍</b><p>왼쪽 위 ☰ 단추. 99장 전체 차례가 열리고, 읽은 장에는 초록 점이 찍힙니다.</p></div>
 <div class="tool"><b>지금 읽는 절 띠</b><p>긴 글 위쪽에 따라다니는 띠. 지금 절 이름과 진행 막대가 보이고, 누르면 절 목록으로 바로 옮겨 갑니다.</p></div>
 <div class="tool"><b>직전 위치로</b><p>링크를 따라간 뒤에는 오른쪽 아래 「← 직전 위치로」가 나타납니다. 브라우저의 뒤로가기도 똑같이 작동합니다.</p></div>
 <div class="tool"><b>책갈피 · 링크 복사</b><p>장 머리의 「☆ 책갈피」로 모아 둔 장은 첫 화면에 나타납니다. 「링크 복사」는 그 장의 주소를 복사합니다.</p></div>
 <div class="tool"><b>밑줄 긋기</b><p>본문에서 글을 고르면(PC는 끌어서, 휴대폰은 길게 눌러서) 「밑줄 긋기」 단추가 뜹니다. 그은 밑줄은 다시 열어도 그 자리에 남습니다.</p></div>
 <div class="tool"><b>밑줄 모음</b><p>그은 밑줄을 장별로 모아 봅니다. 문장을 누르면 그 장의 그 자리로 가고, 「모두 글로 복사」로 옮길 수 있습니다.</p></div>
 <div class="tool"><b>이어 읽기</b><p>마지막에 읽던 장과 자리를 기억해, 첫 화면의 「읽던 곳 이어 읽기」로 곧장 돌아갑니다.</p></div>
 <div class="tool"><b>글자 크기 · 어두운 화면</b><p>오른쪽 위 Aa 단추로 글자 크기를, 달 모양 단추로 밝은·어두운 화면을 바꿉니다.</p></div>
 <div class="tool"><b>원명 보기</b><p>인물 풀이 상자와 인물 쪽에는 러시아어 원명이 함께 나옵니다. 원서를 찾아 읽을 때 이름을 그대로 검색할 수 있습니다.</p></div>
</div>
{fig('search', '‘스탈린그라드’를 찾은 모습: 장, 용어, 책이 함께 나옵니다.')}
{fig('secbar', '지금 읽는 절 띠를 누르면 이 장의 절 목록이 펼쳐집니다.')}
{fig('ul', '밑줄: 그어 둔 밑줄과 새로 고른 글, 「밑줄 긋기」 단추.')}
{fig('ullist', '밑줄 모음: 장별로 모이고, 문장을 누르면 그 자리로 갑니다.')}

<h2 id="mobile"><span class="no">5</span>휴대폰에서</h2>
<div class="pair three">
 {fig('m_ul', '글을 길게 눌러 고르면 「밑줄 긋기」가 뜹니다.', 'phone')}
 {fig('m_home', '첫 화면의 「읽던 곳 이어 읽기」, 책갈피, 밑줄 모음.', 'phone')}
 {fig('m_read', '읽는 동안에는 절 띠가 위에 붙어 따라옵니다.', 'phone')}
</div>
<ol class="steps">
 <li>밑줄은 글을 <b>길게 눌러</b> 고른 뒤, 손잡이로 범위를 맞추고 <b>밑줄 긋기</b>를 누릅니다.</li>
 <li><b>밀어서 뒤로가기</b>를 써도 직전 화면의 그 자리로 돌아옵니다.</li>
 <li>지도와 연결망, 무대 연표, 인물의 생애 띠는 손가락으로 끌어 옮깁니다.</li>
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
<details><summary>사람과 땅 이름은 어떻게 적었나요?</summary><p>러시아와 옛 소련의 이름은 국립국어원 외래어 표기법에 따라 원어 발음으로 적었습니다(흐루쇼프, 고르바초프, 키예프). 땅 이름은 그 사건 당시의 이름을 썼고, 바뀐 이름은 본문에서 함께 밝혔습니다(페트로그라드·레닌그라드·상트페테르부르크). 사람 이름을 누르면 러시아어 원명이 함께 나옵니다. 작품 이름은 우리말로 옮겼습니다.</p></details>
<details><summary>날짜는 어느 달력을 따랐나요?</summary><p>모두 오늘 쓰는 그레고리력으로 적었습니다. 러시아는 1918년 2월까지 율리우스력을 썼기 때문에 당시 날짜는 13일 늦습니다. 그래서 ‘2월 혁명’은 3월에, ‘10월 혁명’은 11월 7일에 일어났습니다. 이름으로 굳은 사건은 원래 이름을 그대로 썼습니다.</p></details>
<details><summary>왜 1905년에서 시작해 1993년에서 끝나나요?</summary><p>1905년은 차르의 제국이 처음으로 아래로부터의 혁명을 겪고 소비에트가 생긴 해입니다. 1991년 12월 소련은 해체되었지만, 소비에트라는 제도는 1993년 10월 대통령과 맞선 의회가 포격당하면서 끝났습니다. 이 책은 소비에트의 탄생에서 그 끝까지를 하나의 이야기로 봅니다.</p></details>
<details><summary>참고 서적에 우리말 번역서가 없는 까닭은?</summary><p>근거 도서는 영어와 러시아어 원서로만 적었습니다. 번역판은 판과 역자에 따라 쪽수와 표현이 달라 근거를 확인하기 어렵기 때문입니다. 서가에서 영어 원서와 러시아어 원서를 나누어 볼 수 있습니다.</p></details>
<details><summary>제8부의 『나타샤의 춤』은 어떤 책인가요?</summary><p>올랜도 피지스가 2002년 펴낸 러시아 문화사입니다. 18세기부터 20세기까지 러시아의 예술가와 귀족이 ‘러시아란 무엇인가’를 어떻게 상상했는지 따라갑니다. 제8부는 그 물음을 빌렸지만, 그 책이 러시아 안의 다른 민족과 민중의 목소리를 적게 다룬다는 비판도 마지막 장에서 함께 살핍니다.</p></details>
<details><summary>읽은 표시, 책갈피, 밑줄, 이어 읽기 기록은 어디에 저장되나요?</summary><p>이 기기의 브라우저에만 저장됩니다. 다른 기기나 다른 브라우저에서는 보이지 않고, 브라우저의 사이트 데이터를 지우면 함께 지워집니다. 서버로 보내지는 것은 없습니다.</p></details>
<details><summary>특정 장을 다른 사람에게 보내고 싶어요.</summary><p>장 머리의 「링크 복사」를 누르면 그 장으로 바로 열리는 주소가 복사됩니다. 지도·연표·연결망·인물 화면의 주소도 그대로 보내면 같은 화면이 열립니다.</p></details>

<div class="end"><b>이제 책을 펼쳐 보세요.</b><br><a class="open" href="{BOOK}">『깃발이 내려지기까지』 열기 →</a></div>

</main>
</div>
<footer>『깃발이 내려지기까지』 읽는 법</footer>
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
open('/home/claude/soviet/dist/guide.html', 'w').write(html)
print(len(html) // 1024, 'KB')
