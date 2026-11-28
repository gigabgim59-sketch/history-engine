# 물음으로 읽는 신학 (tq) — 진행 상태

- 상태: **출간 2026-11-28, history-all 커밋 4e20d4d** (index.html·pdf/물음으로읽는신학_A4.pdf만, 사용자 확인 뒤).
  - 구성: 8부 34장. 쟁점 26장(핵심 10, 주요 16)과 교파 8장(◆, kd `cf`).
  - 인물: 241명. th 사전에서 230여 명을 옮기고, tq에만 나오는 인물을 people_extra.mjs에 더했다. 장별 행적은 507개.
  - 그 밖: 연결 23, 용어 113, 서지 111(th 원서 서가에서 관련 장의 책을 가져옴), 맺음(쟁점×전통 표와 축별 정리).
  - 검사(2026-11-28, Windows):
    - build 통과(457KB), font 196면
    - chk 하한 미달 없음, atcheck 빈칸 없음, lengths 표시=계산
    - voice 평가어 0, 공식 2회(장당 초과 0), 바깥 점검 13.4%
    - consistency 연도 엇갈림 없음
    - residue '잔재 없음', t1 390·1280 넘침 없음, 이메일 0
  - A4 인쇄본: `print/tq_a4.pdf` 166쪽, 44구획. pdfcheck 형식 통과, 거의 빈 쪽 없음.
  - 서가 병합: 21권, 묶음 6('사상과 신앙' 2권). 390·1280에서 카드, PDF 버튼, 책 안 이동, 인물 화면을 확인했다.

## 만든 방식
- 원고가 한 곳에 있다: `books/tq/src`(같은 원고가 세션의 outputs에도 있다).
  - issues_a–e.mjs: 쟁점 원고
  - extra_a–c.mjs: 서가 책용 보강
  - appendix.mjs: 비교표·연표
- 생성 도구(tools/):
  - gen.mjs: 원고에서 body_p1–7.mjs와 issues.json, threads.json을 만든다.
  - parts.mjs: 부 머리
  - extras.mjs: 용어·서지·맺음
  - peoplesnap.mjs + autoat.mjs: 인물 사전과 행적
- 손으로 쓴 것: 교파 장 body_p8a·p8b·p8c(보강 병합), data.mjs, events.mjs, links.mjs, people_extra.mjs.
- 다시 만드는 순서:
  1. node tools/gen.mjs
  2. node tools/parts.mjs
  3. node tools/extras.mjs
  4. node build.mjs
  5. node tools/autoat.mjs
  6. node tools/peoplesnap.mjs tools/keep.json
  7. node build.mjs
  8. node chk.mjs
  9. python font.py dist/index.html — chk가 dist를 다시 빌드하므로 font는 마지막에 돌린다(DEFECTS E-24 주석).
- 같은 원고에서 단독 자료 『쟁점별 신학 정리』(HTML·PDF)도 만든다(src 폴더에서 node build.mjs).

## 알려진 약점
- **사실 확인:** 모든 사실은 웹이나 원전과 대조하지 않고 기억으로 썼다(UNVERIFIED). 독립 검수는 하지 않았다(2026-11-27 사용자 결정, LIBRARY U10).
- **장별 행적:** 자동으로 뽑은 문장이다. 그 인물이 처음 나오는 문장이 대표 행적이 아닐 수 있다.
- **서지:** th에서 가져왔으므로 tq에만 있는 쟁점(신정론, 창조와 진화, 여성 안수 등)의 원서가 적다.
- **분량 표시(E-23):** 교파 장(cf)이 쟁점 핵심 장과 같은 '핵심' 표시를 단다.
- **표기 통일:** th와 다른 인명 표기 여섯 개(흐로티위스, 될링거, 플로롭스키, 바를라암, 프르치바라, 드 뤼박)는 th 쪽으로 맞췄다.
- **엔진 변경:** META.ppT로 인물 화면 제목을 바꿀 수 있게 했다(E-25).
