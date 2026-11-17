# 계몽의 갈래 — 이어서 작업하기
- 빌드: `node build.mjs` → `python3 font.py dist/index.html` → `python3 t1.py <스크린샷 폴더>` (390 [] / 1280 [] 이 나와야 함)
- 분량 검사: `node chk.mjs` (! 표시 = 최소 분량 미달, w1 4500 · w2 2300)
- 본문: body_p1a … body_p6a.mjs (l01–l70). 보충은 /tmp/a.json + `node addp.mjs` 뒤 갈림 중복 줄 제거.
- 인물: sp/p1–p6rows.txt, at는 sp/atA–atE.txt(장|id:글) → `python3 tools/at2.py sp/atA.txt … sp/atE.txt` → `python3 tools/genp.py N sp/pNrows.txt sp/pNat.txt sp/pNdeny.txt`. 검사 `node atcheck.mjs l`, 누락 문맥 `node tools/miss.mjs 1 70`.
- 부: part1–6.mjs (P n, GROUP_CH n, AXCH n). 용어: terms.mjs. 서가: tools/books_src.py → books.mjs. 맺음: concl.mjs.
- 서가 합본: /home/claude/library/merge.py 의 'lm' 항목.
- 인쇄본(A4): python3 print/render.py → print/enl_a4.pdf (make.mjs가 front/body HTML 생성, print.css 판형)
