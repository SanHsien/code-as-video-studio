# code-as-video-studio

用程式碼產生產品展示影片（Code-as-Video）的工具與參考手冊：讓 Coding Agent 把影片當成「時間的函式」來寫，畫面可重現、可逐格檢查，並在渲染前先過分鏡驗收。

```text
產品網頁 ──video_asset_capture──▶ 截圖 + 色彩 theme.json + seek(t) 範例
音樂 BPM ──beat_grid────────────▶ 每一拍落在第幾格
分鏡 JSON ──verify_video_storyboard──▶ 逐格打分、反 AI 套路檢查、縮圖總覽 → 放行或擋下
動畫 HTML ──audit_motion_storyboard──▶ 開瀏覽器 seek 擷取影格、量測像素與文字 → PASS 或擋下
```

## 工具

| 指令 | 用途 |
| :--- | :--- |
| `python tools/beat_grid.py --bpm 120 --fps 60 --seconds 5 [--json]` | 節拍網格：算出每一拍的影格位置，讓動畫與音樂同步 |
| `python tools/video_asset_capture.py --url https://example.com -o assets/captured [--offline]` | 擷取產品網頁截圖與主色，產生 `seek(t)` 動畫範例；只接受 http(s) 網址 |
| `python tools/verify_video_storyboard.py --input templates/storyboard-example.json [--output 報告目錄] [--threshold 8.0] [--json]` | 分鏡驗收閘門：8~12 張關鍵影格逐格打分，有違規或低於門檻就擋下 |
| `python tools/audit_motion_storyboard.py index.html --duration 3000 --frames 6 --output-dir artifacts/storyboard [--json]` | 動態設計審查：用瀏覽器對動畫 HTML 做 `seek(t)` 實際擷取影格，量測相鄰影格像素差、正逆序一致、文字碰撞／超出畫面、對比與頁面錯誤；需 Pillow＋Playwright，缺依賴 exit 2、逾時 exit 3（INCOMPLETE） |
| `python tools/verify_motion_and_video_specs.py` | 檢查本 repo 的手冊結構沒被改壞 |

### 兩支分鏡工具的分工

| | `verify_video_storyboard.py` | `audit_motion_storyboard.py` |
| :--- | :--- | :--- |
| 檢查對象 | 分鏡 **JSON**（你寫下的關鍵影格描述） | 真實的動畫 **HTML 頁面** |
| 做法 | 對描述逐格打分、反 AI 套路檢查；不開瀏覽器 | 用 Playwright 實際 seek、截圖，再用 Pillow 量測像素與文字 |
| 依賴 | 只用標準庫 | Pillow＋Playwright |
| 適用時機 | 動手做之前，先驗分鏡規劃 | 動畫做出來之後，驗實際畫面 |

兩支工具刻意分開、不合併：前者驗「計畫」，後者驗「成品」。共用的評審輔助函式在 `tools/_judge_common.py`。詳見 `docs/code-driven-motion-design-studio-spec.md`。

`video_asset_capture.py` 有安裝 [Playwright](https://playwright.dev/python/) 時會開真瀏覽器截圖；沒有安裝或離線時，自動改用內建的預設素材。其餘工具只用 Python 標準庫（`audit_motion_storyboard.py` 需要 Pillow＋Playwright）。

## 參考手冊

| 路徑 | 內容 |
| :--- | :--- |
| `templates/video-studio-harness.md` | Code-as-Video 工作流規範：`V = f(t)`、反 AI 套路清單、確定性渲染、專案常駐規範範本 |
| `templates/storyboard-example.json` | 可直接通過分鏡閘門的 8 張關鍵影格範例（格式參考） |
| `templates/beat-grid-motion-example.ts` | Remotion／GSAP 依節拍網格對齊動畫的範例 |
| `docs/code-driven-motion-design-studio-spec.md` | 程式碼驅動動態設計工作室規格：seek(t)、分鏡像素與文字量測、PNG 序列與 FFmpeg 導出 |
| `templates/motion-design-studio-skill.md` | Motion Design Studio 可攜 skill 範本（含 `render_frames.py` 導出器） |
| `docs/cinematic-ai-video-prompt-guide.md` | 電影感 AI 影片提示詞指南：光學參數對照、黑名單詞彙、經典風格範例 |
| `templates/cinematic-storyboard-template.md` | 電影感逐鏡分鏡填寫範本 |
| `docs/cinetic-motion-dictionary.md` | Cinetic 動態技法手冊（273 種技法、14 類） |
| `docs/motion-prompt-cheatsheet.md` | Motion Prompt 動效字典速查（144 款） |
| `docs/cinematic-shot-camera-guide.md` | cinematic-shot 運鏡語法 |
| `assets/openlibrary_demo/` | `video_asset_capture.py` 的實際產出範例 |
| `notes/` | 這些工具與手冊的來源分析筆記（原在 [ai-inbox](https://github.com/SanHsien/ai-inbox)） |

## 測試

```bash
python -m unittest discover -s tests
```

預設不開瀏覽器。`audit_motion_storyboard` 的像素測試需要 Pillow（`python -m pip install pillow==12.3.0`），沒裝會明確 skip；CI 固定安裝 `pillow==12.3.0` 才會實際跑到。

### 瀏覽器端到端測試（選用）

需要 Pillow、Playwright 與本機的 Edge 或 Chrome。設環境變數 `CODE_AS_VIDEO_BROWSER_TESTS=1` 才會跑（CI 不跑）：

```bash
CODE_AS_VIDEO_BROWSER_TESTS=1 python -m unittest discover -s tests -p test_audit_motion_storyboard.py
```

PowerShell：`$env:CODE_AS_VIDEO_BROWSER_TESTS=1`。Windows 預設用 `msedge`，其他平台用 Chromium，可用 `CODE_AS_VIDEO_MOTION_TEST_CHANNEL`（msedge／chrome）覆寫；單一子程序逾時 `CODE_AS_VIDEO_MOTION_TEST_TIMEOUT_SECONDS`（預設 90）。逾時只代表 **INCOMPLETE**（測試以 skip 並註明 `INCOMPLETE` 呈現），不是通過也不是品質失敗，不可當作綠燈；驗收須看輸出有無 skip。

CI 在 Ubuntu 與 Windows 上執行（不設 `PYTHONUTF8`，確保 Windows 終端也不會因編碼出錯）。

## 來源

2026-10-25 從 [`SanHsien/ai-inbox`](https://github.com/SanHsien/ai-inbox) 獨立出來，保留相關檔案的 git 歷史。手冊內容整理自各開源專案，出處見各檔開頭。

## 授權

[MIT](LICENSE)（各手冊引用的第三方專案依其原授權）
