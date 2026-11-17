# 엔진 안내 (engine/)

서재의 책 한 권을 한 HTML 파일로 만드는 도구다. 원칙은 `../LIBRARY.md`, 작업 순서는 세 스킬(`library-plan`, `library-write`, `library-publish`)에 있다. 이 문서는 파일 형식과 명령만 다룬다.

## 쓰는 법
- **새 책:** 이 폴더의 파일을 모두 `books/<id>/`에 복사한다. 그 폴더에서 `bash restore.sh`(npm·파이썬 의존성)를 실행한다.
- **고친 엔진을 기존 책에 옮길 때:** 그 책이 템플릿을 고쳐 썼는지 STATUS의 `엔진 수정` 칸을 먼저 본다. 고친 부분을 지키면서 옮긴다.
- **엔진에 넣을 것:** 책 하나에만 필요한 수정은 그 책 폴더에서 한다. 다른 책에도 쓸 수정만 여기에 넣고 `DEFECTS.md`에 적는다.

## 책 폴더의 파일
| 파일 | 내용 |
|---|---|
| `data.mjs` | `META`, `REGIONS`, `AXES`, `ENGINES`, `KINDS`, `PARTS`, `GROUPS`, `THREADS`, `THREAD_EV`, `SEAS`(지도 바다 이름 `[이름, 경도, 위도]`) |
| `events.mjs` | `EVENTS`: 장 목록 `{id,p,t,y,yr,r,pl:[이름,경도,위도],w,g,nx,kd,q,s}` |
| `links.mjs` | `WHY`: `'원인>결과': '이유 한 문장'`. `nx`마다 하나(빌드가 검사) |
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
- `len`: 등급별 분량 `{1:{min,target,draft},2:{…},3:{…}}`. `chk`와 `checks/lengths`가 읽는다.
- `draft`: true면 자리표시('집필 예정')를 보인다. 출간본에는 넣지 않는다.
- 문구:
  - `debl`: 갈림 상자 이름. 기본 '해석의 갈림'.
  - `mapnote`: 지도 아래 설명.
  - `srcnote`: 원전 서가 설명.
- 화면 끄기: `nomap`, `nolanes`.
- 목소리 검사:
  - `evalw`: 서술자 문장에 쓰지 않을 평가어 목록.
  - `formulas`, `formulaMax`: 귀속 공식과 장당 허용 횟수. 기본은 '이 서사에서·이 서사는', 2회.
  - `outerMin`: 바깥 점검(갈림+오해) 비중의 하한(%).
- 빌드가 채우는 칸: `wl`(장 머리 분량 표시, 등급별 실제 중앙값), `lenStat`.

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
node print/make.mjs && python3 print/render.py   # A4 인쇄본
python3 checks/pdfcheck.py print/<pfx>_a4.pdf    # 숨은 표지, Type 3 글꼴, 북마크, 제목 정보
```
모든 검사 도구는 HTML 경로를 인자로 받는다. 그래서 서가에서 꺼낸 책(`library/build/<id>.html`)에도 그대로 쓸 수 있다.

## 잔재 목록
`checks/residue_words.txt`는 출간본 화면에 나오면 안 되는 문구의 목록이다. 새 잔재를 찾으면 한 줄 더한다.

## 알려진 한계
- 인쇄 도구(`print/make.mjs`)에는 『충격과 대응』의 문구와 절 이름이 박혀 있다(DEFECTS P-07). 새 책은 쓰기 전에 그 책에 맞게 고치고, 기존 책 정비 때 인쇄 도구를 일반화한다.
- 연결(고리)의 종류는 아직 받지 않는다. 이유 문장만 받는다.
