# External Action Approval Checklist

다음 action은 반드시 사람이 승인해야 한다.

## Messaging

- [ ] 이메일 발송
- [ ] Slack/DM 발송
- [ ] 댓글 작성
- [ ] 게시글 작성

## Data And Files

- [ ] 원본 파일 덮어쓰기
- [ ] 파일 삭제
- [ ] 민감정보 포함 파일 공유
- [ ] 외부 저장소 업로드

## Systems

- [ ] DB write
- [ ] schema 변경
- [ ] 권한 변경
- [ ] 배포
- [ ] 유료 API 또는 광고 캠페인 변경

## Approval Request Format

```text
Action:
Target:
Recipient or system:
Payload:
Expected effect:
Risk:
Rollback or stop plan:
```

## Before Approval

- [ ] 대상이 정확하다.
- [ ] payload 전문을 사람이 볼 수 있다.
- [ ] 위험과 되돌리기 방안이 적혀 있다.
- [ ] 승인 전에는 draft 또는 proposal 상태로만 남겼다.
