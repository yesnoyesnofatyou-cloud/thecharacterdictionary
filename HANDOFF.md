# 인수인계 (Claude 세션 간 이어서 작업하기)

이 문서는 새 Claude 세션이 이 프로젝트를 바로 이어서 작업할 수 있도록 남긴 메모입니다.
새 세션에서는 먼저 이 파일을 읽으세요.

## 프로젝트 한 줄 요약
판타지 소설 설정집 "아르카나 인물 도감". 주인공 **왓더퍽(WhatTheFuck)** 한 명의 능력·스킬·전투 기믹·잠재 해방·스토리를 정리한다.

## 세 군데에 나뉘어 있음
| 무엇 | 어디 | 역할 |
|---|---|---|
| **원본 도감 (편집용)** | Claude 아티팩트 `https://claude.ai/artifact/G7sDgZ21bUgYe6LWA5QvTT` | 편집은 여기서만. 데이터는 아티팩트 DB(`characters`, `skills` 컬렉션), 스킬 이미지는 아티팩트 asset 저장소 |
| **공개 사이트** | https://thecharacterdictionary.netlify.app | 읽기 전용 스냅샷. 이 저장소의 `index.html` + `img/` |
| **이 저장소** | `yesnoyesnofatyou-cloud/thecharacterdictionary` | `main`에 push하면 Netlify가 자동 게시. **반드시 Public 유지** (Netlify 무료 요금제는 비공개 저장소에서 Claude 커밋을 막음) |

Netlify 사이트 ID: `2ab97681-84fd-435e-9069-7c9c89cf3447` (팀 slug `rainbowcreepergun`)

## 도구 (tools/)
- `tools/codex.html` — 원본 도감 페이지 소스. 수정 후 아티팩트에 다시 publish (capabilities: db, user, downloads, assets).
- `tools/build_site.py` — 공개 사이트 빌드. `python3 tools/build_site.py <DB 내보내기 폴더> index.html <asset 폴더>`
  - DB 내보내기: ArtifactData `list`로 `skills`, `get`으로 `characters/char-wtf`를 `out_dir`에 저장
  - asset 폴더: 스킬의 `icon`(32자 asset id)마다 Artifact `read` + `path`로 받은 파일
  - `build_site.py`는 같은 폴더의 `codex.html`을 읽음
- `tools/icon_prompts.py` — 스킬 82개의 Firefly 아이콘 프롬프트 (도감 DB의 `iconPrompt` 필드에도 들어 있음)

## "사이트 업데이트해줘" 절차
1. 아티팩트 DB에서 skills 전체 + characters/char-wtf 내려받기
2. `icon`이 있는 스킬의 이미지 asset 내려받기
3. `build_site.py`로 `index.html`, `img/` 생성 → 방문자 화면으로 열어 확인(편집 버튼 0개)
4. commit & push → Netlify 게시 상태 `ready` 확인

## 주요 설정 규칙 (사용자가 정한 것)
- **일반 스킬** = 자기 마나로 쓰는 기술 / **고유 스킬(◆ 마나 조종)** = 상대 마나를 조작하는 기술. 두 분류는 완전히 분리, 유형(공격·방어·반격·유틸 등)은 동일하게.
- 공격 범위: 사거리(근거리/원거리/자신) × 범위(단일/광역).
- 성장: 이미 강함(먼치킨). 8성 이상은 **봉인된 잠재 스킬**, 행동/상황으로 해방(강적·태도·위장·관계·초월). 최종 목표 = 초월 행동 **"등급 체계 밖으로"**(확정).
- 위장: 평소 2성, 본실력보다 낮은 어떤 등급으로든 위장 가능. 「서툰 손끝」으로 일부러 서툰 척.
- 약점: 마나를 쓰지 않는 적에게 매우 약함. 대응 스킬은 전부 8성 이상 봉인.
- 사용자가 직접 만든 스킬: 마나 웨이브(고유), 매니페스트 엣지(일반). 마력 칼날(손)과 매니페스트 엣지(검 소환)는 별개.
- 새 스킬은 `isDraft: true`(추천 가안)로 넣고, 사용자 확인 후 확정. 스토리에 큰 영향이 있으면 먼저 물어볼 것.
- 사용자가 도감에서 직접 고친 내용(desc 등)은 덮어쓰지 말 것. 쓰기 전 DB를 다시 읽고 `if_version`으로 고정.

## 진행 중인 작업 (2026-10-25 기준)
**스킬 아이콘 82개 만들기** — 1/82 완료(마나 웨이브, `sk-u01`).
- 그림체: 마나 웨이브 샘플로 확정. `tools/icon_prompts.py`의 STYLE 문장 그대로 사용, Firefly 1:1.
- 사용자가 원하는 방식: **Claude가 에이전트로 직접** Firefly 웹(firefly.adobe.com)에서 생성 → 결과를 직접 보고 골라서 → 도감에 넣고 → 사이트 업데이트.
  - 브라우저(데스크톱 앱 내장 브라우저 또는 Claude in Chrome)가 연결된 세션이 필요.
  - Adobe 커넥터는 이미지 생성 기능이 없음(편집만). 생성은 Firefly 웹에서.
  - 시작 전 확인: Firefly 크레딧 사용, 이미지 다운로드 허락을 한 번 받기. 10개 단위로 중간 결과 보여주기.
  - 도감에 넣는 방법: 512×512 webp로 맞춰 Artifact `publish`(`url` + `asset: true`)로 올리고, 해당 스킬 문서의 `icon` 필드에 asset id를 기록.
- 도감 메뉴 → "아이콘 작업" 화면에서 사용자가 직접 프롬프트 복사/이미지 올리기도 가능.
