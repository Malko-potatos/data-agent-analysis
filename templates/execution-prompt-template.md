# Execution Prompt Template

```text
목표:
- 무엇을 알고 싶거나 완성하고 싶은가?

입력:
- 파일, URL, 앱, API, DB, Slack/Gmail/GitHub 등 출처는 무엇인가?
- 분석 기간과 필터는 무엇인가?

역할:
- 분석가, 데이터 감사자, 번역자, 구현자, QA 담당 중 무엇인가?

절차:
- 먼저 inventory를 하고, 그 다음 정제/분석/작성/수정으로 진행하라.

제약:
- 원본 보존
- 외부 전송 금지
- 삭제/발송/승인 금지
- read-only
- 민감정보 처리 기준

검증:
- 어떤 기준으로 맞았다고 볼 것인가?
- row count, total, test, screenshot, source link 등.

출력:
- 표, 리포트, draft, workbook, dashboard, action queue 등.

승인 경계:
- 발송, 삭제, 배포, DB write, 권한 변경은 실행하지 말고 승인 요청으로 남겨라.
```
