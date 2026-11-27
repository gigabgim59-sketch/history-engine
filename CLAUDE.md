# 서재 작업 규칙 (이 저장소를 붙인 모든 대화에 적용)

이 저장소는 역사 서가(`gigabgim59-sketch/history-all`)에 올리는 책들의 원본, 엔진, 기록이다. 원칙은 `LIBRARY.md`(헌장), 작업 순서는 세 스킬 `library-plan`·`library-write`·`library-publish`, 열린 결함은 `DEFECTS.md`에 있다. 작업을 시작하기 전에 `LIBRARY.md`와 관련 스킬을 읽는다.

## 지금 할 일 (2026-11-21 사용자 결정)
- **새 책 『통계적 추론의 쟁점』.** `library-plan` 스킬대로 구성 질답부터 한다. 출발점은 `review/rehearsal/r4_통계적추론_계획.md`다. 리허설이 지적한 세 문제를 먼저 질답으로 정한다: 엔진이 이 책에 맞는가, 역사 서가와 어떤 관계인가, 수식·계산을 어떻게 검증하는가. 구성이 확정되기 전에는 본문을 쓰지 않는다.
- **하지 않기로 한 일.** 기존 책 정비는 2026-11-21 공개(history-all 8dceb1c)로 끝냈다. 아래는 사용자가 하지 않기로 했으니 먼저 꺼내지 않는다. `DEFECTS.md`에 '닫음'으로 적혀 있다.
  - 『제국의 경영』 28~60장 검수
  - 검수한 세 권의 보류 묶음
  - 나머지 15권 검수
  - 스킬 개정
  - 독립 검수(모든 책, 2026-11-27 사용자 결정, LIBRARY U10). st 검수에서 남은 지적은 `DEFECTS.md` st 절에 열린 채 있다.

## 작업 환경
- 세션을 시작하면 저장소 뿌리에서 `bash engine/setup_check.sh`를 먼저 실행한다.
- 빌드와 인쇄본은 리눅스 클라우드 환경을 전제로 한다(글꼴 경로 `/usr/share/fonts/opentype/noto/`, poppler, Playwright).
- 사용자 PC(Windows)에서 도는 세션이면 구성 질답과 SPEC 작성까지만 한다. 그때는 SPEC 전문을 답에 보여 주어 클라우드 세션으로 옮길 수 있게 한다. git이 없으면 커밋하지 못한다는 것도 알린다.

## 고정 규칙 (사용자 지시)
- 새 책(프로젝트)의 구성은 언제나 질답으로 정한다(고정). 바로 쓰지 말고 먼저 질문으로 구성을 확정한다.
- 작업을 마치고 GitHub(`gigabgim59-sketch/history-all`)에 올릴 때는 **이번 작업에서 새로 생성된 HTML과 그 책의 A4 PDF만** 업로드한다. zip, 소스, 기타 파일은 업로드하지 않는다.
- 새 책을 서가에 추가할 때도 카드의 PDF 버튼은 남긴다(`library/books.json`의 `pdf`에 등록). 그 PDF는 `history-all`의 `pdf/` 폴더에 함께 올린다.
- 업로드 전에는 처리 결과를 보고하고 확인을 받는다.

## 보고
- `review/지시문_아첨억제.txt`와 `LIBRARY.md` §8을 따른다. 동의로 시작하지 않고, 주장에는 근거 꼬리표와 확신도를 단다.

## 개인정보와 커밋
- 사용자의 이메일 주소를 어떤 파일, 커밋, 메시지에도 넣지 않는다.
- 커밋은 `git -c user.name="Claude" -c user.email="noreply@users.noreply.github.com" commit …`으로 한다.

## 저장소 구성
- `books/<id>/`: 책마다 소스(`data.mjs`, `events.mjs`, `body_p*.mjs`, `people*`, `sp/` …), `dist/`(빌드본), `print/`(A4 인쇄본), `errata/`(정오 스크립트와 처리 기록)
- `engine/`: 템플릿, 빌드, 검사(`checks/`), 인쇄(`print/`). 명령은 `engine/README.md`
- `library/`: 서가 등록부 `books.json`, 합치기 `merge.py` → `library/dist/index.html`
- `review/`: 검수 원문(`batch1/`), 리허설(`rehearsal/`)

## 작업 요령
- 빌드 의존성과 빌드본은 저장소에 없다(`node_modules`, `dist/`, `books/*/ref`는 무시 목록). 책 폴더에서 `bash ../../engine/restore.sh`로 의존성을 설치하고, `ln -s ../../engine/ref ref`로 지리 자료를 잇는다. 그다음 빌드한다.
- 출간본을 직접 고치지 않는다. 소스를 고치고 다시 빌드한다(`node build.mjs && python3 font.py dist/index.html`).
- 검수에서 나온 수정은 `books/<id>/errata/<날짜>.py`(옛 문구가 소스 전체에서 꼭 한 번 나올 때만 쓴다)로 하고, 처리·보류를 `errata/<날짜>_처리.md`에 적는다. 인물 파일(`people*.mjs`, `sp/`)은 따로 고친다.
- 독립 검수는 장 7~10개씩 나누어 맡기고, 3~4권씩 진행한다.
