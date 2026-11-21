#!/usr/bin/env bash
# 책 폴더에서 실행: 엔진이 쓰는 npm·파이썬 의존성을 설치한다. Playwright와 Chromium은 작업 환경에 미리 있다.
set -e
[ -f package.json ] || echo '{"type":"module","private":true}' > package.json
npm install --silent --no-audit --no-fund d3-geo@3 topojson-client@3 topojson-simplify@3 world-atlas@2 us-atlas@3 @fontsource/noto-sans-kr@5 @fontsource/noto-sans-math@5.3.0 temml@0.13.5 >/dev/null
pip install --quiet --break-system-packages fonttools brotli pypdf pdfplumber >/dev/null 2>&1 || true
echo "restore ok"
