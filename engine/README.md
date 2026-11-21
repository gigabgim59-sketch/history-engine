# 엔진 안내 (engine/)

서재의 책 한 권을 한 HTML 파일로 만드는 도구다. 원칙은 `../LIBRARY.md`, 작업 순서는 세 스킬(`library-plan`, `library-write`, `library-publish`)에 있다. 이 문서는 파일 형식과 명령만 다룬다.

## 쓰는 법
- **새 책:** 이 폴더의 파일을 모두 `books/<id>/`에 복사한다. 그 폴더에서 `bash restore.sh`(npm·파이썬 의존성)를 실행한다.
- **고친 엔진을 기존 책에 옮길 때:** 그 책이 템플릿을 고쳐 썼는지 STATUS의 `엔진 수정` 칸을 먼저 본다. 고친 부분을 지키면서 옮긴다.
- **엔진에 넣을 것:** 책 하나에만 필요한 수정은 그 책 폴더에서 한다. 다른 책에도 쓸 수정만 여기에 넣고 `DEFECTS.md`에 적는다.

## 책 폴더의 파일
| 파일 | 내용 |
|---|---|
| `data.mjs` | `META`, `REGIONS`, `AXES`, `ENGINES`, `KINDS`, `SLOTH`(장 종류별 절 이름 `{kd:{배경:'…',원인:'…',…}}`. 없으면 절 이름이 '배경·원인…' 그대로 나온다), `PARTS`, `GROUPS`, `THREADS`, `THREAD_EV`, `SEAS`(지도 바다 이름 `[이름, 경도, 위도]`) |
| `events.mjs` | `EVENTS`: 장 목록 `{id,p,t,y,yr,r,pl:[이름,경도,위도],w,g,nx,kd,q,s}` |
| `links.mjs` | `WHY`: `'원인>결과': '이유 한 문장'`. `nx`마다 하나(빌드가 검사). `data.mjs`에 `LINKK`가 있으면 값은 `[종류 id, '이유']`(아래 '연결 종류') |
| `body_p<N>[a-z].mjs` | `B<N><A..>`: 장별 본문 `{안내,배경,원인,주체,전개,영향,사관,갈림,오해,말,작품}`. 앞의 여덟과 갈림·오해는 문단 배열, `사관`은 `[[흐름, 글]]`, `말`은 `[[낱말, 풀이]]`, `작품`은 `[[제목, '연도 · 사람', 설명]]`. 다른 장은 `[[id]]` |
| `part<N>.mjs` | `P<N>`(부 머리: `f`{힘별}, `bg`{무대별}, `bgx`[문단, '## 소제목'], `sum`[문단]), `GROUP_CH<N>`, `AXCH<N>` |
| `people.mjs`, `people_p<N>.mjs` | `FACTS`(진영), `PEOPLE`, `AT<N>`(장별 행적), `REL<N>`, `PDENY<N>`. 행 파일 `sp/p<N>rows.txt` 등에서 `tools/genp.py`로 만든다 |
| `terms.mjs` | `TCATS`, `TERMS`: `[표제, 풀이, 분야]` |
| `books.mjs` | `BOOKS`: `{id,lang,t,a,o,role,warn}`, `BK`: `{장: [[책 id, 근거 부분]]}` |
| `concl.mjs` | `CONCL`: 맺음 문단 배열('## 소제목' 가능) |
| `lineage.mjs`, `lnb1~3.mjs` | (선택) 요소별 변천 |
| `econ.mjs` | (선택) 경제 지표 |
| `geo.mjs` | 지도 투영과 범위. 책마다 쓴다 |

### META에서 엔진이 읽는 칸
- 기본: `title`, `sub`, `span`, `eyebrow`, `q`, `desc`, `intro`, `engines`, `engn`(힘 이름), `axn`(축 이름), `gl`, `pen`, `pes`, `ticks`, `life`, `lifeTicks`, `endT`
- `pfx`: 브라우저 저장소 접두. 책마다 다르게 준다(없으면 빌드가 경고한다).
- `len`: 등급별 분량 `{1:{min,target,draft},2:{…},3:{…}}`. 장 종류 이름으로 따로 줄 수도 있다(`cul:{min}`). `chk`와 `checks/lengths`가 읽는다.
- `draft`: true면 자리표시('집필 예정')를 보인다. 출간본에는 넣지 않는다.
- 문구:
  - `debl`: 갈림 상자 이름. 기본 '해석의 갈림'.
  - `hvl`: 사관(여러 목소리) 상자 이름. 기본 '관점들의 풀이'.
  - `mapnote`: 지도 아래 설명.
  - `srcnote`: 원전 서가 설명.
- 화면 끄기: `nomap`, `nolanes`.
- 목소리 검사:
  - `evalw`: 서술자 문장에 쓰지 않을 평가어 목록.
  - `formulas`, `formulaMax`: 귀속 공식과 장당 허용 횟수. 기본은 '이 서사에서·이 서사는', 2회.
  - `outerMin`: 바깥 점검(갈림+오해) 비중의 하한(%).
- 빌드가 채우는 칸: `wl`(장 머리 분량 표시, 등급별 실제 중앙값), `lenStat`. `wl`이 없으면 템플릿이 실행 중에 같은 값을 계산한다.

### 연결 종류 (DEFECTS E-15)
- `data.mjs`의 `LINKK = [[id, 이름, 색, 설명], …]`. 있으면 모든 `WHY` 값이 `[id, 이유]`여야 하고, 종류 빈칸이나 목록에 없는 종류에서 빌드가 멈춘다.
- 화면: 장의 고리 목록과 연결망에 종류 칩, 선 색, 범례(종류별 수). 고리 이름은 '앞선 고리/다음 고리', 탭은 '연결망'.
- `LINKK`가 없으면 옛 방식(이유 문장만) 그대로다.

### 수식과 본문 표 (DEFECTS E-16)
- 줄 안 수식 `$…$`, 문단 하나 전체가 수식이면 `$$…$$`. 글자 그대로의 달러는 `\$`. 문법은 LaTeX(temml). 자바스크립트 문자열 안이므로 역슬래시는 두 번 쓴다(`'$\\theta$'`).
- 표: `|`로 시작하는 문단. 줄마다 한 행(`\n`), 칸은 `|`. 둘째 줄이 `|---|---|`이면 첫 줄은 머리 행. 칸 안에 수식을 쓸 수 있다.
- 빌드가 MathML로 바꿔 `DATA.math`에 넣는다. 수식 오류는 빌드를 멈춘다. `font.py`와 인쇄본이 Noto Sans Math를 'KRMath'로 부분 심는다(`mathfont.py`).
- 분량 셈에서 수식 마크업은 빠지고, 표는 칸 글자만 센다(`checks/_text.mjs`).

### 지도를 끈 책
- `META.nomap`(필요하면 `nolanes`), `pl:[]`, `r:[]`. `geo.mjs`는 빈 바탕을 돌려준다(예: books/st/geo.mjs). 힘(`ENGINES`)·무대·집단이 비면 그 화면과 첫 화면의 절이 숨는다.
- 첫 화면 문구: `META.axnote`(축 설명), `META.wnote`(중요도 설명).

## 명령 (책 폴더에서)
```
bash restore.sh                       # 처음 한 번
node build.mjs                        # dist/index.html. 연결·참조·종류·인물 진영 검사, 분량 통계 출력
python3 font.py dist/index.html       # 쓰인 글자만 글꼴로 심는다(빌드할 때마다)
node chk.mjs                          # 등급별 하한
node addp.mjs sp/x.json               # 보강(절 이름 검사, 쓴 뒤 키 검사)
python3 tools/genp.py N rows at deny  # 인물 파일 생성
node atcheck.mjs <접두>                # 감지됐지만 행적 없는 인물
node tools/ctx.mjs <장> <낱말>          # 문맥 보기
python3 app.py terms|books|bk <파일>   # 용어·서가 덧붙이기
python3 t1.py <스크린샷 폴더>           # 390·1280 가로 넘침, 스크립트 오류
node checks/lengths.mjs               # 하한 + 장 머리 표시 = 계산값
node checks/residue.mjs dist/index.html   # 모든 메뉴 화면·장 화면의 잔재
node checks/voice.mjs                 # 평가어, 귀속 공식, 학자 없는 갈림, 바깥 점검 비중
node checks/consistency.mjs           # 책 안 연도 엇갈림, 요약↔본문
python3 ../../engine/print/render.py [dist/index.html]   # A4 인쇄본 → print/<pfx>_a4.pdf (make.mjs를 스스로 부른다)
python3 checks/pdfcheck.py print/<pfx>_a4.pdf    # 숨은 표지, Type 3 글꼴, 북마크, 제목 정보
node checks/review_text.mjs dist/index.html <폴더> [장 수]  # 독립 검수용 본문 묶음(part_NN.md, front.md, index.md)
```
정비(E-10 이전에 낸 책)에서는 `node checks/lengths.mjs --tol 0.02`로 옛 셈법의 측정 차이를 허용한다(DEFECTS all-07).
모든 검사 도구는 HTML 경로를 인자로 받는다. 그래서 서가에서 꺼낸 책(`library/build/<id>.html`)에도 그대로 쓸 수 있다.

## 잔재 목록
`checks/residue_words.txt`는 출간본 화면에 나오면 안 되는 문구의 목록이다. 새 잔재를 찾으면 한 줄 더한다.

## 인쇄본
- `print/render.py`가 `print/make.mjs`로 한 문서(표제지·일러두기·차례·본문)를 만들고, 크로뮴으로 두세 번 짠다. 북마크로 구획의 첫 쪽을 찾아 차례에 넣고, 마지막 쪽에 몇 줄만 넘어간 구획은 줄 간격을 조인다(`print/state.json`).
- 글꼴은 `print/serif.py`가 Noto Serif CJK KR을 그 책의 글자만 남겨 TrueType으로 바꿔 넣는다(Type 3 방지).
- 절 이름과 상자 이름은 그 책 HTML의 템플릿에서 읽는다. 엔진 템플릿은 `DATA.sloth`, `META.debl`, `META.hvl`.
- 책 폴더의 `print/meta.json`(선택)으로 덮어쓴다: `title`·`sub`·`eyebrow`·`span`·`endT`(meta가 없는 옛 책), `printFoot`(표제지 아래 줄), `introReplace`([[원문, 인쇄 문구]]), `introPrint`(머리말 전체). 머리말에서 화면을 가리키는 문장은 자동으로 빼고 알린다.

## 알려진 한계
- 엔진을 고치면 있는 책의 자료로 보통·DRAFT 두 번 시험 빌드하고 residue를 돌린다(DEFECTS E-11).
- 장의 단위가 사건이 아니면 `META.unitn`을 준다(DEFECTS E-20). 지도·무대 화면의 '사건' 문구는 그대로이므로 지도를 쓰는 책에서는 확인한다.
- 읽는 법(`dist/guide.html`)은 엔진이 만들지 않는다. 있으면 첫 화면에 고리만 건다(eu가 따로 만든 것).
