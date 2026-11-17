#!/bin/bash
# 새 작업 환경에서 이 책의 빌드 도구를 되살린다
set -e
cd "$(dirname "$0")"
npm install --no-audit --no-fund
pip install --break-system-packages -q fonttools brotli 2>/dev/null || pip install -q fonttools brotli
node build.mjs && python3 font.py dist/index.html
echo "복원 완료: dist/index.html"
