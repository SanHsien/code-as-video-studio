# 路線圖

> 本 repo 後續工作的單一真相源。做完一項，就在同一個 commit 刪掉那一列；新工作只加在這裡。
> 現況段的數字是 2026-10-29 依 `main` `dc973bbb0535` 查的快照，開工前先重查 GitHub。

## 現況

Code-as-Video 工具與手冊（節拍網格、網頁素材擷取、分鏡驗收閘門、動效與運鏡字典），自有 repo（public，非 fork）。健康：`CI`（ubuntu＋windows）最近一次 success（2026-10-25）、`CodeQL` success（2026-10-26 排程）；open issue 0 筆、open PR 0 筆；Dependabot 與 Code scanning 告警 0 筆；無 release。只用 Python 標準庫，沒有依賴宣告（`.github/dependabot.yml` 以 `fleet-waiver: freshness` 豁免），只有 workflow 引用的 Actions 由 Dependabot 更新。目前沒有卡住的事。

## 近期：可以直接動手
| 項目 | 為什麼 | 驗收方式 | 建議執行者 | 證據 |
| --- | --- | --- | --- | --- |
| 無 | 深掃已修三個缺陷（`8bfd719`、`7e80631`、`dc973bb`），工作樹乾淨、無告警、無 open PR/issue；剩下的疑點都是有取捨的行為，列在「中期」等條件，不是明確 bug | — | — | 2026-10-29 證據快照；接續開發報告（2026-10-26）、深掃報告（2026-10-26） |

## 中期：等條件成立再做
| 項目 | 觸發條件 | 驗收方式 | 建議執行者 | 證據 |
| --- | --- | --- | --- | --- |
| 決定 `beat_grid` 負 offset 與捨入規則 | 有人實際用負 `offset_seconds` 或對拍點整數幀對齊結果有疑義時（目前 `round()` 為銀行家捨入、負 offset 會產生負時間拍點，未確認為缺陷） | 先在 `tests/test_beat_grid.py` 寫出期望行為的測試（拒絕負 offset 或明確允許並文件化）；`python -m unittest discover -s tests` 綠 | Claude Opus | `tools/beat_grid.py:39-45,60-66,94-101`；深掃報告（2026-10-26）「檢視後刻意不修」 |
| 擷取離線降級時標示截圖來源 | 有使用者在離線降級時拿到與本次網址不符的舊 `screenshot.png` 並造成誤判 | 離線降級的輸出（metadata）記錄截圖是沿用舊檔；不覆寫既有真實截圖；有對應測試且 `python -m unittest discover -s tests` 綠 | Claude Sonnet | `tools/video_asset_capture.py:346-357`；深掃報告（2026-10-26） |
| 補齊 SCAFFOLD 選配檔（README.en.md、CONTRIBUTING、SECURITY） | 維護者要求對齊其他 repo | 檔案存在且 `python -m fleet_ops audit` 對本 repo 仍 0 gaps（在 repo-fleet-ops 執行） | Claude Haiku | 接續開發報告（2026-10-26）「刻意不做」 |

## 刻意不做
| 不做什麼 | 理由 | 什麼情況下重新考慮 |
| --- | --- | --- |
| 新增關鍵字型驗證器 | `AGENTS.md` 鐵律 4：`verify_motion_and_video_specs.py` 只防手冊被改壞，新檢查必須能攔下真正的錯誤 | 出現一個現有檢查攔不住的真實錯誤案例 |
| 加 upstream-check 或 pip／npm 依賴宣告 | 非 fork、沒有上游；只用標準庫，Playwright 必須維持選用（`AGENTS.md` 開發流程） | 變成 fork，或核心功能必須依賴第三方套件 |
| 放寬顏色白名單以接受 `hsl(… / a)` | 偏嚴但安全，`thumbnail_color` 曾可注入屬性（`dc973bb`） | 有實際需要且附注入防護測試 |

## 維護方式

自有 repo：沒有發版節奏，改動以 `python -m unittest discover -s tests` 全綠為閘門；Actions 由 Dependabot 每週更新，`CodeQL` 每週排程。
