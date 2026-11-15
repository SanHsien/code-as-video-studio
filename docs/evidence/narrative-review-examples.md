# 敘事審片合成範例與文件檢查證據

任務 `T-20261115-19`；日期 2026-11-15；基準 HEAD `03bec21f69795cf6f320c7441d792a69061efb53`，分支 `worker/t19`。本檔所有角色、鏡頭、台詞、ASR 文字及時間碼都是合成設計資料；沒有圖片、影片或音訊，未生成、未跑 ASR、未人工聽審，不能當模型品質驗證。

欄位依[分鏡範本](../../templates/cinematic-storyboard-template.md)，採納條件及來源見 [SOP](../narrative-video-review-sop.md)。以下「導演甲／連戲乙／語言丙／素材丁」是合成角色，實作時須填真實承辦人；目前所有成品比對／聽審皆未完成。

## A：連續動作，末幀可作條件性參照

設定：8 秒，24fps，16:9；角色 R1/v1：灰外套、深藍長褲、黑鞋、右手持紅封套。角色全身正側背參考 `R1-sheet-v1` 僅為規劃 ID，尚無檔案。全片中性低飽和、無顆粒；場景西側窗光 5000K，畫面由左向右走向桌面。

```text
A01 [0,4s) 右手持封套走向桌子 -> 末幀：手到桌沿、封套未放下
                                        |
                     同機位/動作接續 + 模型支援才可作起始參照
                                        |
A02 [4,8s) 同一姿勢 -> 右手把封套放上桌 -> cut 收尾
```

### Shot A01｜4s｜交代封套去向

| 欄位 | 合成填寫 |
| --- | --- |
| ① 主體／動作 | R1 右手持紅封套向桌子走近，一個主要動作 |
| ② 景別／機位 | WS、平視，人物朝畫面右側 |
| ③ 光學 | 35mm、f/5.6、中等景深、16:9 |
| ④ 光源 | 左側西窗柔光、5000K |
| ⑤ 運鏡 | static，維持 4s |
| ⑥ 調色 | 中性低飽和，無顆粒 |
| 角色參考／連戲 | R1-sheet-v1 規劃全身三視，需可見下衣鞋襪；灰外套、深藍褲、黑鞋固定。起點人物左、桌右；終點右手到桌沿，封套仍在手中；連戲乙待比對 |
| 台詞／讀音／ASR／聽審 | N/A：無台詞；語言丙核准此設計省略 |
| 前鏡／start_image | N/A：首鏡無前鏡末幀；導演甲核准 |
| 反應／Insert | N/A：單人動作清楚，保留空間關係；導演甲 |
| 轉場／理由 | 動作接點 hard cut 到 A02，讓右手動作接續；導演甲／剪輯者 |
| 接點／回饋 | 計畫取局部末幀 00:03:23（24fps，第 95 格，零起算）；素材未產，無實際比對或修正結論 |

最終 Prompt（設計）：

```text
Wide shot, eye-level, 16:9. R1 in a gray jacket, navy trousers and black shoes walks toward a table on screen right, holding a red envelope in the right hand. 35mm lens, f/5.6, moderate depth of field. Soft window key light from screen left at 5000K. Static camera for 4 seconds. Neutral low-saturation grade, no grain.
```

### Shot A02｜4s｜封套落桌

| 欄位 | 合成填寫 |
| --- | --- |
| ① 主體／動作 | R1 用右手把紅封套放上桌 |
| ② 景別／機位 | WS、平視，與 A01 同構圖 |
| ③ 光學 | 35mm、f/5.6、中等景深、16:9 |
| ④ 光源 | 左側西窗柔光、5000K，同 A01 |
| ⑤ 運鏡 | static，維持 4s |
| ⑥ 調色 | 同 A01，中性低飽和，無顆粒 |
| 角色參考／連戲 | 沿用 R1-sheet-v1 規劃；服裝與右手不變。起點手到桌沿、封套未放下，終點封套在桌上；連戲乙待驗 |
| 台詞／讀音／ASR／聽審 | N/A：無台詞；語言丙 |
| 前鏡接點 | 計畫 A01 00:03:23 → A02 00:00:00；實際末幀 ID 待素材，不能假稱已擷取 |
| start_image 決策 | 條件採用：同機位、動作連續，可考慮前鏡末幀；模型／版本未選、官方能力 URL／查證日／實際參數皆未查證，因此目前停止送出。操作者補證，導演甲核准後才可用 |
| 接點人工比對 | 連戲乙待比較末／首幀衣褲、鞋、右手、封套位置、光向，並播放接點；末幀不保證一致 |
| 反應／Insert | N/A：本設計不需額外資訊；導演甲 |
| 轉場／理由 | cut 收尾，封套落桌後留停頓；導演甲 |
| 修正／回饋 | 待素材，無可審結論；若持物手突變，先記時間碼與預期右手，再由導演決定修正 |

最終 Prompt（設計）：

```text
Wide shot, eye-level, same composition, 16:9. R1 in a gray jacket, navy trousers and black shoes places the red envelope on the table with the right hand, starting with the hand at the table edge. 35mm lens, f/5.6, moderate depth of field. Soft window key light from screen left at 5000K. Static camera for 4 seconds. Neutral low-saturation grade, no grain.
```

## B：切換機位，不套前鏡末幀

設定：8 秒，24fps，16:9；R2/v1 灰上衣講者、R3/v1 藍上衣聽者，桌兩側對坐，固定各自角色參考；下衣鞋襪不入鏡，經連戲乙同意不另製全身三視，仍需可見上衣與臉部參考。中性低飽和、無顆粒；西窗 5000K。以下 B 組從片頭獨立計時。

```text
B01 [0,4s) R2 說話、視線向畫右 --切換機位--> B02 [4,8s) R3 反應、視線向畫左
                               前鏡末幀不作 B02 起始構圖
```

### Shot B01｜4s｜給出指示

| 欄位 | 合成填寫 |
| --- | --- |
| ① 主體／動作 | R2 說「請重新核對資料。」 |
| ② 景別／機位 | MCU、平視、桌南側拍攝，R2 視線向畫右 |
| ③ 光學 | 50mm、f/2.8、淺景深、16:9 |
| ④ 光源 | 西窗柔光 5000K；維持實體光源方向，不以各機位畫面左右取代場景方位 |
| ⑤ 運鏡 | static，4s |
| ⑥ 調色 | 中性低飽和，無顆粒 |
| 角色／站位 | R2 灰上衣，對坐 R3；R2-face-v1 規劃 ID；下衣／鞋襪 N/A（不入鏡），連戲乙核准；成品尚未比對 |
| 台詞／讀音 | 正本 B-v1；關鍵詞「重新」，本例預期 chong2 xin1，語言丙為合成預審者；這是設計指定，非字典或音訊查證 |
| 前鏡／start_image | N/A：本組首鏡；導演甲 |
| 反應／Insert | 採用下一鏡 B02 聽者反應，目的為呈現猶豫；Insert N/A（無額外物件訊息），導演甲 |
| 轉場／理由 | 台詞結束後 cut 到 R3，讓情緒落在聽者；不強制動作接點，導演甲 |
| ASR／聽審／回饋 | 下列 SYN-01 是合成疑點；無音訊，ASR 未執行、聽審待審，不得標通過或已誤讀 |

最終 Prompt（設計）：

```text
Medium close-up, eye-level, from the south side of the table, 16:9. R2 in a gray shirt speaks to R3 off-screen right. 50mm lens, f/2.8, shallow depth of field. Soft key light from the west window at 5000K. Static camera for 4 seconds. Neutral low-saturation grade, no grain.
```

台詞正本與讀音表另交語音流程；未指定可支援語音或讀音參數的模型，不把提示詞視為發音保證。

### Shot B02｜4s｜聽者猶豫

| 欄位 | 合成填寫 |
| --- | --- |
| ① 主體／動作 | R3 聽後皺眉 |
| ② 景別／機位 | CU、平視，同在桌南側切換機位拍 R3，視線向畫左 |
| ③ 光學 | 85mm、f/2.8、淺景深、16:9 |
| ④ 光源 | 同場西窗 5000K，依新機位記錄臉部受光，不強求畫面光向相同 |
| ⑤ 運鏡 | static，4s |
| ⑥ 調色 | 同 B01，中性低飽和，無顆粒 |
| 角色／站位 | R3 藍上衣，R3-face-v1 規劃 ID；桌兩側位置不變；下衣／鞋襪 N/A（不入鏡），連戲乙核准 |
| 台詞／讀音／ASR／聽審 | N/A：本鏡無台詞，語言丙 |
| 前鏡／start_image | B01 → B02；N/A：換機位且主體由 R2 換成 R3，不沿用 R2 末幀當 R3 起始構圖；改用 R3 角色與新構圖參考，導演甲 |
| 接點人工比對 | 連戲乙待驗服裝、對坐關係、視線與光源；前鏡末幀可供人工比對，不等於起始圖 |
| 反應／Insert | 本鏡即反應鏡頭；Insert N/A（目的已完整），導演甲 |
| 轉場／理由 | dissolve 收尾，設計為轉入之後的時間段；導演甲，非一律 hard cut |
| 修正／回饋 | 無素材待審；若視線同向，記接點時間碼與預期對向，由導演／連戲乙處理 |

最終 Prompt（設計）：

```text
Close-up, eye-level, from the south side of the table, 16:9. R3 in a blue shirt frowns while looking toward R2 off-screen left. 85mm lens, f/2.8, shallow depth of field. Soft key light from the west window at 5000K. Static camera for 4 seconds. Neutral low-saturation grade, no grain.
```

## SYN-01：關鍵詞疑似誤讀修正單（合成，待聽審）

| 欄位 | 設計資料／狀態 |
| --- | --- |
| 素材版本／Shot | B-v1 計畫／B01，沒有實際音訊檔 |
| 全片時間窗 | 00:00:01.000–00:00:02.200（合成預定位置，非音訊定位結果） |
| 正本／預期讀音 | 「請重新核對資料。」；「重新」預期 chong2 xin1 |
| ASR 疑點 | 假設轉錄成「請重心核對資料」；工具／模型版本 N/A（未執行）。只示範文字差異，不可據此推斷 zhong4 或任何實際發音 |
| 人工聽審結論 | 待審：無音訊，沒有「實際聽到的讀音」或已誤讀結論；語言丙尚未聽審 |
| 預期修正／決策者 | 語言丙先聽原片段；若實際讀音正確，只記 ASR 誤辨並核字幕；若確認誤讀，由導演甲選局部重錄並保留表演接點；聽不清則仍待審 |
| 複核／放行 | 待素材與修正後版本：核關鍵詞讀音、字幕時間窗、音畫接點並簽名；目前未完成，不可標 Retake 已執行／成片通過 |
| 隱私 | 僅合成文字與時間碼；不錄影、不外送；素材丁為設計中的資料負責人 |

## 文件驗證紀錄

本次只驗文件與既有工具回歸，未生成影片、接 MCP、呼叫付費／中國服務、安裝套件或執行參照 repo 程式；未驗證模型能力或真人素材。未設定 `PYTHONUTF8`；現有 Pillow／Playwright 可發現，但未開瀏覽器。

| 2026-11-15 檢查命令／方法 | 結束碼／結果 | 證據限制 |
| --- | --- | --- |
| `python -m unittest discover -s tests` | 0；Ran 52 tests in 4.289s，OK (skipped=1) | BrowserTests 類別預設略過，不是完整瀏覽器驗收；輸出中的故意失敗案例屬反例測試，不是整套失敗 |
| `python tools/verify_motion_and_video_specs.py` | 0；四份既有手冊 PASS | 只驗既有手冊結構，未自動驗本次敘事決策內容 |
| `python -m unittest discover -s tests -p test_audit_motion_storyboard.py -v` | 0；14 tests，OK (skipped=1) | 為釐清 skip 範圍追加的 focused 檢查：像素／CLI 單元測試執行，BrowserTests 預設略過；終端中文 skip 訊息有亂碼，依來源檔確認原因，未以編碼環境變數掩蓋 |
| `git diff --check` | 0；無空白錯誤 | 新檔另以 UTF-8 讀取核對 |
| `python -c` 一次性文件檢查（標準庫 pathlib／re） | 0；UTF-8、四檔本地連結目標存在、無真實家目錄路徑 | 本機檢查，未驗網頁連結持續可用；未新增驗證器或依賴 |

人工 DoD 核對：SOP 七列涵蓋採納決策、適用／N/A 與人工角色；A01／A02 為連續動作，B01／B02 為換機位；SYN-01 含時間窗、預期詞、合成 ASR 疑點及未聽審結論。來源、既有 QA 重疊與缺口、錄影隱私及 48 小時清理責任均列於 SOP。改動限三個任務文件與 repo 強制同步的 `ROADMAP.md`，沒有另列待辦。

提交準備：`git add -- templates/cinematic-storyboard-template.md docs/narrative-video-review-sop.md docs/evidence/narrative-review-examples.md ROADMAP.md` 結束碼 1，沙盒拒絕建立 `.git/index.lock`（Permission denied）。未 commit、未 push；依派工例外保留工作樹，由整合者在沙盒外接續提交，屆時依 repo 規則將測試與 commit 用 `&&` 串接。未建立任務暫存目錄或額外腳本。
