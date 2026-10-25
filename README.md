# code-as-video-studio

用程式碼產生產品展示影片（Code-as-Video）的工具與參考手冊：讓 Coding Agent 把影片當成「時間的函式」來寫，畫面可重現、可逐格檢查，並在渲染前先過分鏡驗收。

```text
產品網頁 ──video_asset_capture──▶ 截圖 + 色彩 theme.json + seek(t) 範例
音樂 BPM ──beat_grid────────────▶ 每一拍落在第幾格
分鏡 JSON ──verify_video_storyboard──▶ 逐格打分、反 AI 套路檢查、縮圖總覽 → 放行或擋下
```

## 工具

| 指令 | 用途 |
| :--- | :--- |
| `python tools/beat_grid.py --bpm 120 --fps 60 --seconds 5 [--json]` | 節拍網格：算出每一拍的影格位置，讓動畫與音樂同步 |
| `python tools/video_asset_capture.py --url https://example.com -o assets/captured [--offline]` | 擷取產品網頁截圖與主色，產生 `seek(t)` 動畫範例；只接受 http(s) 網址 |
| `python tools/verify_video_storyboard.py --input storyboard.json [--output 報告目錄] [--threshold 8.0] [--json]` | 分鏡驗收閘門：8~12 張關鍵影格逐格打分，有違規或低於門檻就擋下 |
| `python tools/verify_motion_and_video_specs.py` | 檢查本 repo 的手冊結構沒被改壞 |

`video_asset_capture.py` 有安裝 [Playwright](https://playwright.dev/python/) 時會開真瀏覽器截圖；沒有安裝或離線時，自動改用內建的預設素材。其餘工具只用 Python 標準庫。

## 參考手冊

| 路徑 | 內容 |
| :--- | :--- |
| `templates/video-studio-harness.md` | Code-as-Video 工作流規範：`V = f(t)`、反 AI 套路清單、確定性渲染、專案常駐規範範本 |
| `templates/beat-grid-motion-example.ts` | Remotion／GSAP 依節拍網格對齊動畫的範例 |
| `docs/cinetic-motion-dictionary.md` | Cinetic 動態技法手冊（273 種技法、14 類） |
| `docs/motion-prompt-cheatsheet.md` | Motion Prompt 動效字典速查（144 款） |
| `docs/cinematic-shot-camera-guide.md` | cinematic-shot 運鏡語法 |
| `assets/openlibrary_demo/` | `video_asset_capture.py` 的實際產出範例 |
| `notes/` | 這些工具與手冊的來源分析筆記（原在 [ai-inbox](https://github.com/SanHsien/ai-inbox)） |

## 測試

```bash
python -m unittest discover -s tests
```

CI 在 Ubuntu 與 Windows 上執行（不設 `PYTHONUTF8`，確保 Windows 終端也不會因編碼出錯）。

## 來源

2026-10-25 從 [`SanHsien/ai-inbox`](https://github.com/SanHsien/ai-inbox) 獨立出來，保留相關檔案的 git 歷史。手冊內容整理自各開源專案，出處見各檔開頭。

## 授權

[MIT](LICENSE)（各手冊引用的第三方專案依其原授權）
