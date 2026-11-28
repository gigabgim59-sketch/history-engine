#!/usr/bin/env bash
# 새 세션에서 맨 먼저 실행: 서재 작업에 필요한 도구가 있는지 확인한다. 저장소 뿌리에서 bash engine/setup_check.sh
ok=1
chk() { if eval "$2" >/dev/null 2>&1; then echo "  있음  $1"; else echo "  없음  $1 — $3"; ok=0; fi; }
echo "서재 작업 환경 점검"
chk "git"                 "git --version"                         "커밋·업로드에 필요"
chk "node 18 이상"         "node -e \"process.exit(parseInt(process.versions.node)<18?1:0)\"" "빌드에 필요"
chk "python3"             "python3 -V"                            "글꼴·인쇄·검사에 필요"
chk "playwright(파이썬)"   "python3 -c 'import playwright'"         "인쇄본(PDF)에 필요"
chk "pdftotext"           "pdftotext -v"                          "인쇄본 빈 쪽 조임에 필요(poppler-utils)"
chk "Noto Serif CJK 글꼴"  "test -f /usr/share/fonts/opentype/noto/NotoSerifCJK-Regular.ttc" "인쇄본 본문 글꼴"
if [ $ok = 1 ]; then echo "모두 있음. 책 폴더에서 bash ../../engine/restore.sh 로 npm·파이썬 의존성을 설치한다."
else echo "빠진 것이 있다. 클라우드 환경(리눅스)에서 작업하면 대부분 갖추어져 있다. 구성 질답과 SPEC 작성은 빠진 것이 있어도 할 수 있다."; fi
