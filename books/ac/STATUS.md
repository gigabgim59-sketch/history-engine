# 미국 교회사 (ac) — 진행 상태

- **상태: 계획 확정, 집필 전 준비 끝** (2026-11-28, library-plan 질답 3회차, 사용자 지시 "본문 작성은 나중에 한다. 그전의 작업까지만 완전히 확정하자").
- SPEC: `books/ac/SPEC.md` (6부 60장: 사건 48 · ◆교단·운동 12, 약 20만 자).
- 작업 환경: 사용자 PC(Windows) 세션. 이 세션은 th·tq를 같은 환경(휴대용 Node, Python, Playwright, poppler, Noto Serif CJK)에서 빌드·출간했다.

## 집필 전 준비 (끝남, 2026-11-28)
- 엔진 파일: tq 판(E-24·E-25 반영)을 복사했다. 지도는 us의 geo.mjs(북아메리카 등장방형, 오늘의 주 경계).
- data.mjs:
  - META(`draft:true`, 머리말 가안 4문단, `len` 1·2·3·dn, `evalw`, `ppT`)
  - SLOTH(ev·dn), LINKK(ca·rs·re·in), AXES 5, THREADS 8과 THREAD_EV, REGIONS 5, SEAS, PARTS 6
- events.mjs: 60장 모두 채웠다.
  - 칸: 제목·연도·대표 연도·무대·장소·등급·종류·물음·계획 요약(s)
  - 축 표시는 part1–6.mjs의 AXCH로 만들었다.
- links.mjs: 계획 연결 71개(인과 17, 부흥에서 분열로 12, 반응과 반동 9, 계승 33)와 이유. 집필 때 문장을 다듬는다.
- people.mjs: 진영(FACTS) 9개. 인물은 집필하면서 더한다.
- terms·books·concl, part 머리글(bgx·sum): 빈 뼈대. 집필 때 쓴다.
- 확인:
  - draft 빌드가 통과했다(지도 높이 691, 본문 자리표시).
  - font, t1은 390·1280 넘침과 스크립트 오류 없음.
  - 지도 화면에서 제1부 10곳이 제자리에 찍힌다.
- 빌드 환경: 휴대용 Node(_tools), Python 3.12, Playwright, poppler, Noto Serif CJK(_tools/fonts, NOTO_SERIF_DIR). 리눅스 세션에서는 engine/README.md의 restore 절차를 따른다.

## 다음 할 일
1. `library-write`로 보정 장 셋을 먼저 쓴다: 핵심 ac30(남북 분열), 주요 ac23(피니), ◆ac14(장로교).
   - 계획 요약(s)과 물음(q)은 집필 때 다시 쓴다. 연결 이유도 다듬는다.
2. 보정 측정 뒤 분량과 문단 계획을 정한다(SPEC 열린 문제 1).
3. 겹치는 장(us u05·u14·u24·u42, th31·38·41·54·55·58, tq32·33·34)은 쓰기 전에 읽고, 되풀이하지 않을 사실과 가리킬 장을 아래 '겹침 대조'에 적는다.
4. 조건부 3장(ac10·ac50·ac60)은 대표 사건으로 확인한다.

## 장별 상태
(집필 전.)

## 겹침 대조
(집필 중에 채운다.)
