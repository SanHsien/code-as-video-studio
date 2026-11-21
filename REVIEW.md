# REVIEW.md

> latest-only：只保留最近一次覆核。修好的項目回註修復 commit 與日期。

## 2026-11-21 獨立覆核（`main` `609bc4e` 起）

範圍：`tools/` 六支工具、`tests/`、README／ROADMAP／`docs/` 抽查。覆核者：Claude（Opus 5.5），沒有參與先前的實作。

總評：`audit_motion_storyboard.py` 是真量測，防線完整（正逆序 seek、閒置計時器、對比、遮蔽與未量測揭露、門檻下限）；`video_asset_capture.py` 的網址與色碼過濾也健全。問題集中在 `verify_video_storyboard.py`：它只讀分鏡 JSON 自己寫的內容，空白分鏡能拿滿分放行。

### 發現

| # | 嚴重度 | 問題 | 重現 | 狀態 |
| --- | --- | --- | --- | --- |
| 1 | 高 | 分鏡閘門放行 8 張空白影格（`[{}]` × 8），每張 10 分：沒有違規就等於滿分，空白描述也算 | `verify_video_storyboard.py --input` 8 個空物件，exit 0 | 已修 `ade529e`（2026-11-21）：空白描述扣 10 分並列違規 |
| 2 | 中 | `camera_angle`、`focal_plane` 大小寫敏感、不檢查合法值：`FLAT`、`Full_Sharp` 躲過扣分，`dutch` 這種不存在的值照樣放行 | 單張 `camera_angle: "FLAT"`、`pitch_deg: 34` 得 10 分 | 已修 `ade529e`（2026-11-21）：比對前轉小寫，不認得的值列違規 |
| 3 | 中 | `pitch_deg`、`timestamp` 可為 `NaN`／`inf`／負值，`NaN` 讓「正視角」檢查永遠不成立 | `pitch_deg: NaN` 得 10 分 | 已修 `ade529e`（2026-11-21）：非有限數值與負時間點列違規 |
| 4 | 中 | 欄位型別錯（`description: 123`、`effects: [1]`）在評分階段丟出 traceback；`effects` 給字串會被逐字元拆開 | CLI 直接 traceback | 已修 `ade529e`（2026-11-21）：載入時檢查型別，回報「無法解析分鏡 JSON」、exit 1 |
| 5 | 中 | `--threshold` 可以調低（`--threshold 0`），與 `AGENTS.md` 鐵律 2「不可調低門檻硬過」、以及 `audit_motion_storyboard.py --min-score` 的 8～10 限制不一致 | `--threshold 0` | 已修 `ade529e`（2026-11-21）：不在 8～10 回 exit 2 |
| 6 | 低 | 8 張同一時間點的分鏡照樣放行 | `[good]*8` | 未修：既有測試的範例分鏡就是同一時間點，要改既有測試的資料；列入 `ROADMAP.md` 中期 |
| 7 | 低（限制） | 關鍵字比對擋不住改寫（「置中的大標題」比對不到「置中大標題」）；`fade-in all`、`centered-title` 這類分隔符號變化原本也躲得過 | — | 分隔符號已修 `ade529e`（2026-11-21；空白、連字號、底線視為相同）；改寫屬於本工具本質限制，README 已寫明，成品要交給 `audit_motion_storyboard.py` 量測 |
| 8 | 中 | 動態設計審查的反罐頭原始碼檢查只看 HTML 本身，把 `transition: opacity` 或 `Math.random()` 搬到外部 `.css`／`.js` 就躲過 | `<link rel="stylesheet" href="fade.css">` | 已修 `ade529e`（2026-11-21）：讀頁面以相對路徑引用的本機 CSS／JS 與 `@import`（不連網、上限 50 檔、處理循環引用） |
| 9 | 中 | `beat_grid.py --seconds 1e9`（或 `--bpm 1e9`）沒有上限，CLI 卡住並持續吃記憶體 | 20 秒未結束 | 已修 `ade529e`（2026-11-21）：一次超過 100 萬拍回報錯誤 |
| 10 | 低（設計） | 文字全畫在 Canvas／SVG 時，對比與碰撞量不到，審查仍可能 PASS，只附 `[WARN]` 與「含未量測項目」 | — | 不改：`AGENTS.md` 已規定未量測要揭露、不可把 exit 0 當完整驗收；維持現狀 |

### 測試品質（mutation）

暫時改壞程式、跑 `python -m unittest discover -s tests`（不含瀏覽器測試），再還原：

| 改壞的地方 | 結果 |
| --- | --- |
| 影格數 8～12 限制拿掉 | 1 個失敗 |
| 「有違規就不通過」拿掉 | 5 個失敗 |
| 關鍵字比對關掉 | 3 個失敗 |
| 縮圖色碼白名單拿掉 | 原本**沒有測試會紅**（`html.escape` 擋得住跳出屬性，擋不住在 `style` 多塞一條 CSS）；已補 `test_css_declarations_cannot_ride_in_thumbnail_color`，現在 1 個失敗 |
| 審查的 errors 硬閘門拿掉 | 1 個失敗 |
| 對比門檻 4.5 → 1.0 | 1 個失敗 |
| 文字碰撞比例 0.25 → 0.99 | 2 個失敗 |
| `--min-score` 下限拿掉 | 3 個失敗 |
| 拍點時間計算偏移 0.1% | 1 個失敗 |
| 本次新增的規則 | 每條都先寫測試、確認修前會紅 |

### 文件事實抽查

| 主張 | 一手來源 | 結果 |
| --- | --- | --- |
| CI 固定安裝 `pillow==12.3.0` | `.github/workflows/ci.yml` 第 37 行 | 符合 |
| 敘事審片 SOP：來源案例的影片模型是 Seedance 2.5、圖片是 GPT Image 2，經 Higgsfield 由 Claude Code 呼叫；第一版 79 秒、第二版 76 秒、最終版 68 秒 | 作者說明文章（okihiro-school.com，2026-11-21 讀取） | 符合 |
| 快門角 180°、24fps 即 1/48 秒 | 換算：曝光時間 = (180/360) × (1/24) = 1/48 | 符合 |
| 分鏡 8～12 張關鍵影格 | `templates/video-studio-harness.md` 第 128 行與工具常數 | 一致 |

### 驗證範圍

- 非瀏覽器測試全綠（Windows，Python 3.14）。
- 瀏覽器端到端測試（`CODE_AS_VIDEO_BROWSER_TESTS=1`）本機實跑：34 個測試 OK、2 個 skip，757 秒（`ade529e` 前的工作樹）；CI 不跑。
