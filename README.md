# history-engine

서재의 책을 만드는 헌장·엔진·도구·기록을 두는 비공개 저장소다. 공개 서가는 `gigabgim59-sketch/history-all`이다.

| 위치 | 내용 |
|---|---|
| `LIBRARY.md` | 서재 헌장. 불변 원칙, 주제가 정하는 변수, 검증된 변형, 계보, 엄밀의 규칙, 작업 흐름, 보고 방식, 교훈 |
| `DEFECTS.md` | 결함 대장. 검수 지적과 처리 상태 |
| `skills/` | 세 스킬의 사본: `library-plan`, `library-write`, `library-publish` |
| `engine/` | 책 엔진(빌드, 템플릿, 검사, 인쇄). `engine/README.md` |
| `library/` | 서가 등록부(`books.json`), 병합 도구(`merge.py`, `shell.html`), 책 사이 검사(`xcheck.py`), 기존 서가에서 책 꺼내기(`extract.py`) |
| `books/<id>/` | 책별 소스와 기록(SPEC·STATUS·UNVERIFIED). `je`·`jh`는 소스가 사라져 출간본 자료(`book.json`)만 있다 |
| `review/` | 사용자의 검수 지시문, 『충격과 대응』 목차 검토(리허설 정답지) |

새 세션에서는 `LIBRARY.md`와 `DEFECTS.md`를 먼저 읽는다.
