# AGENTS.md — code-as-video-studio

給在本 repo 工作的 AI Agent（Claude Code、Codex、Antigravity 等）。

## 鐵律

1. **影片是時間的函式。** 畫面只能由 `t`（或影格編號）決定，不用 `Math.random()`、`Date.now()` 這類每次結果不同的來源，才能逐格重現與檢查。規範見 `templates/video-studio-harness.md`。
2. **渲染前先過分鏡閘門。** 交付影片前，用 `tools/verify_video_storyboard.py` 驗收分鏡；被擋下就照報告的修正建議改，不可調低門檻硬過。
3. **真實素材優先。** 產品畫面用 `tools/video_asset_capture.py` 擷取的實際截圖與色彩，不自行編造介面。
4. **不新增關鍵字型驗證器。** `verify_motion_and_video_specs.py` 只用來防止既有手冊被改壞；新增檢查要能攔下真正的錯誤。`tools/audit_motion_storyboard.py` 屬於「實際量測型」工具（開瀏覽器 seek 擷取影格、量像素差與文字位置），不是關鍵字比對，不違反本條；新增這類工具必須同樣以真實量測為依據，並附反例測試證明能攔下真正的錯誤。
5. **兩支分鏡工具分工，不合併。** `verify_video_storyboard.py` 檢查分鏡 JSON（計畫）；`audit_motion_storyboard.py` 擷取網頁實際影格並量測（成品）。

## 目錄結構

- `tools/`：`beat_grid.py`、`video_asset_capture.py`、`verify_video_storyboard.py`、`audit_motion_storyboard.py`、`verify_motion_and_video_specs.py`、共用 `_judge_common.py`
- `tests/`：每支工具一份 `test_*.py`
- `docs/`：動效、運鏡、動態設計規格、電影感提示詞手冊
- `templates/`：工作流範本、分鏡範例、skill 範本
- `notes/`：來源分析筆記（保留原文，任務表停在移出 ai-inbox 當時）
- `assets/`：`video_asset_capture.py` 的實際產出範例

## 開發流程

- 改動後執行 `python -m unittest discover -s tests`，全綠才提交（測試與 `git commit` 用 `&&` 串接，不用 `;`）。
- 不要設 `PYTHONUTF8` 來讓測試通過；Windows 終端的編碼問題要在程式裡處理。
- 新增第三方依賴前先確認必要；`video_asset_capture.py` 的 Playwright 必須維持「選用、缺了能降級」。`audit_motion_storyboard.py` 需要 Pillow＋Playwright，缺依賴時要回 exit 2、對應測試要明確 skip，不可變紅也不可假裝通過；CI 固定安裝 `pillow==12.3.0`（升級時改 `.github/workflows/ci.yml`）。
- 瀏覽器端到端測試預設不跑，設 `CODE_AS_VIDEO_BROWSER_TESTS=1` 才執行（`python -m unittest discover -s tests -p test_audit_motion_storyboard.py`）。逾時是 INCOMPLETE，不是綠燈也不是品質失敗；回報時要揭露 skip，不可把 exit 0 當成完整瀏覽器驗收。相關環境變數：`CODE_AS_VIDEO_MOTION_TIMEOUT_MS`、`CODE_AS_VIDEO_MOTION_TOTAL_TIMEOUT_S`、`CODE_AS_VIDEO_MOTION_TEST_TIMEOUT_SECONDS`、`CODE_AS_VIDEO_MOTION_TEST_WORKERS`、`CODE_AS_VIDEO_MOTION_TEST_CHANNEL`。

## 路線圖

- `ROADMAP.md` 是本 repo 後續工作的單一真相源。完成或新增工作時，在同一個 commit 更新它：做完的列刪掉、新工作加進去。不要在其他文件另列待辦。
