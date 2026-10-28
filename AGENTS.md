# AGENTS.md — code-as-video-studio

給在本 repo 工作的 AI Agent（Claude Code、Codex、Antigravity 等）。

## 鐵律

1. **影片是時間的函式。** 畫面只能由 `t`（或影格編號）決定，不用 `Math.random()`、`Date.now()` 這類每次結果不同的來源，才能逐格重現與檢查。規範見 `templates/video-studio-harness.md`。
2. **渲染前先過分鏡閘門。** 交付影片前，用 `tools/verify_video_storyboard.py` 驗收分鏡；被擋下就照報告的修正建議改，不可調低門檻硬過。
3. **真實素材優先。** 產品畫面用 `tools/video_asset_capture.py` 擷取的實際截圖與色彩，不自行編造介面。
4. **不新增關鍵字型驗證器。** `verify_motion_and_video_specs.py` 只用來防止既有手冊被改壞；新增檢查要能攔下真正的錯誤。

## 開發流程

- 改動後執行 `python -m unittest discover -s tests`，全綠才提交（測試與 `git commit` 用 `&&` 串接，不用 `;`）。
- 不要設 `PYTHONUTF8` 來讓測試通過；Windows 終端的編碼問題要在程式裡處理。
- 新增第三方依賴前先確認必要；`video_asset_capture.py` 的 Playwright 必須維持「選用、缺了能降級」。

## 路線圖

- `ROADMAP.md` 是本 repo 後續工作的單一真相源。完成或新增工作時，在同一個 commit 更新它：做完的列刪掉、新工作加進去。不要在其他文件另列待辦。
