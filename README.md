# Commit-Craft-AI

![Commit-Craft-AI Logo](https://img.shields.io/badge/Commit--Craft--AI-Smart%20Commit%20Messages-blueviolet?style=for-the-badge&logo=openai)

## 簡介

`Commit-Craft-AI` 是一個創新的命令列工具 (CLI)，旨在透過人工智慧的力量，徹底改變開發者撰寫 Git Commit Message 的方式。傳統上，撰寫清晰、簡潔且具描述性的 Commit Message 是一項耗時且需要高度專注的任務。`Commit-Craft-AI` 透過分析 Git 變更內容 (diff)，自動生成高品質的 Commit Message 建議，大幅提升開發效率與程式碼品質。

本專案的目標是幫助開源專案維護者和團隊，更輕鬆地保持 Git 歷史記錄的整潔與一致性，進而加速程式碼審查流程，並提高專案的可維護性。

## 核心功能

*   **智慧分析**：自動解析 `git diff` 輸出，理解程式碼變更的意圖。
*   **AI 生成**：利用先進的語言模型，根據變更內容生成多個 Commit Message 建議。
*   **可自訂模板**：支援多種 Commit Message 規範 (如 Conventional Commits)，並允許使用者自訂生成模板。
*   **互動式選擇**：提供互動式介面，讓使用者輕鬆選擇、編輯或接受生成的 Commit Message。

## 為什麼選擇 Commit-Craft-AI？

在快速迭代的開發環境中，良好的 Commit Message 是團隊協作與專案管理不可或缺的一環。`Commit-Craft-AI` 不僅能節省開發者撰寫 Commit Message 的時間，更能確保訊息的品質與一致性，降低溝通成本，並使未來的程式碼回溯與維護變得更加容易。

本專案特別適合：

*   **開源專案維護者**：輕鬆管理大量貢獻，保持專案歷史的清晰。
*   **敏捷開發團隊**：加速開發流程，提升團隊協作效率。
*   **個人開發者**：養成良好的 Commit 習慣，提高個人專案品質。

## 安裝

```bash
pip install commit-craft-ai
```

## 使用方式

1.  **在 Git 專案目錄中執行**：

    ```bash
    commit-craft-ai generate
    ```

2.  **選擇或編輯建議的 Commit Message**：

    工具將會顯示 AI 生成的 Commit Message 建議，您可以選擇其中一個，或進行修改。

3.  **自動提交**：

    選定後，工具將自動執行 `git commit -m "您的 Commit Message"`。

## 開發與貢獻

我們非常歡迎任何形式的貢獻，無論是功能建議、Bug 回報、文件改進或是程式碼提交。請參考我們的 [CONTRIBUTING.md](CONTRIBUTING.md) 以了解更多。

## 授權

本專案採用 MIT 授權條款。詳情請見 [LICENSE](LICENSE) 檔案。

## 聯絡我們

如果您有任何問題或建議，歡迎透過 GitHub Issues 與我們聯繫。

---

**Commit-Craft-AI** – 讓您的 Commit Message 充滿智慧與效率。
