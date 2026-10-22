---
name: ux-ui-agent-skills
description: "Thiết kế, sửa và kiểm tra UI/UX website DATN bằng bộ tài nguyên plugin87/ux-ui-agent-skills. Dùng khi làm layout, component, design tokens, responsive hoặc accessibility; áp dụng phạm vi đã duyệt và dùng kèm quy tắc cấu trúc/kiểm tra code của DATN."
metadata:
  upstream-repository: "https://github.com/plugin87/ux-ui-agent-skills"
  upstream-commit: "55156b40e3a9aafa52448bde76cdcb5147b958db"
---

# UX/UI cho website DATN

Đây là skill tích hợp bộ tài nguyên từ [plugin87/ux-ui-agent-skills](https://github.com/plugin87/ux-ui-agent-skills). Bản nguồn tại [references/upstream/](references/upstream/) được xuất từ Git commit ghi trong metadata sau khi clone; giữ nguyên cấu trúc tài nguyên và [LICENSE](references/upstream/LICENSE). Mục tiêu là dùng tài nguyên trong DATN, không cài plugin/hooks trên toàn máy.

## Quy tắc tích hợp

1. Đọc và áp dụng [datn-web-structure](../datn-web-structure/SKILL.md) trước khi tạo/sửa UI. Ý tưởng của kit về màn hình, đối tượng, trường hoặc hành vi mới vẫn phải được người dùng duyệt trước khi tạo.
2. Tôn trọng stack, cấu trúc folder, component và design system đã được dự án chọn. Không copy cả app mẫu, ghi đè hướng dẫn dự án hoặc tự đổi framework để khớp ví dụ upstream.
3. Trước khi tạo UI mới, mô tả ngắn hướng thiết kế: người dùng, mục đích màn hình, bố cục, trạng thái và thành phần tái sử dụng. Với phần đã duyệt, triển khai đúng phương án mà không yêu cầu duyệt lặp lại.
4. Chọn tài liệu theo bảng dưới; không nạp toàn bộ kit. Các tham chiếu trong một skill upstream được giải quyết tương đối với chính folder skill upstream đó.

## Tài liệu theo công việc

| Công việc | Tài liệu cần đọc |
| --- | --- |
| Nguyên tắc thiết kế và kiểm chứng | [AGENTS.md của kit](references/upstream/AGENTS.md) |
| Tạo màn hình | [design-screen](references/upstream/.claude/skills/design-screen/SKILL.md) |
| Dashboard dữ liệu | [data-dashboard](references/upstream/.claude/skills/data-dashboard/SKILL.md) |
| Sửa thiết kế đang có | [redesign](references/upstream/.claude/skills/redesign/SKILL.md) |
| Component/code theo stack | [design-code](references/upstream/.claude/skills/design-code/SKILL.md), [adapter protocol](references/upstream/frameworks/adapter-protocol.md) |
| Design tokens | [design-tokens](references/upstream/.claude/skills/design-tokens/SKILL.md) |
| Rà UI/accessibility | [design-review](references/upstream/.claude/skills/design-review/SKILL.md), [a11y-audit](references/upstream/.claude/skills/a11y-audit/SKILL.md) |
| Kiểm tra giao diện | [design-qa](references/upstream/.claude/skills/design-qa/SKILL.md) |

Upstream có thể nhắc `${CLAUDE_SKILL_DIR}`. Khi đang đọc `references/upstream/.claude/skills/design-code/SKILL.md`, giá trị tương ứng là folder `design-code` đó; `../../../` trở về `references/upstream/`. Không lấy folder wrapper hiện tại làm gốc cho những đường dẫn của skill upstream. Với shell khác Bash, dùng cú pháp tương đương của shell đang chạy.

## Thực thi có phạm vi và kiểm chứng đúng đối tượng

- Áp dụng hướng dẫn về token, accessibility, trạng thái tương tác, responsive và tính nhất quán lên các file ứng dụng trong phạm vi đã duyệt. Mỗi sửa đổi thực hiện tại component/style/module đang sở hữu giao diện đó.
- Quy tắc của người dùng và hướng dẫn DATN có ưu tiên khi khác với đề xuất upstream. Ví dụ kit đề nghị scaffold, thêm adapter, thêm luồng sản phẩm hoặc triển khai thiết kế mới: chỉ thực hiện sau khi phần tương ứng được duyệt.
- Nếu kit dẫn tới skill khác, đọc file tương ứng bên trong `.claude/skills/` của upstream. Chỉ dùng cơ chế subagent khi môi trường/hướng dẫn hiện hành cho phép; nếu thiếu công cụ thì báo giới hạn của phần kiểm tra đó.
- Chạy gate phù hợp lên source hoặc trang thực tế của DATN. Đường dẫn script ở `references/upstream/scripts/`; dùng đường dẫn đầy đủ nếu CWD là project.
- `accuracy_report.mjs` là self-test của kit trên tài nguyên của kit. Kết quả của nó không chứng minh website DATN đạt kiểm tra. Dùng các gate nhận file/trang cụ thể để đo đầu ra DATN.
- Kiểm tra browser render phải thật sự chạy; `SKIPPED` hoặc thiếu browser không phải PASS. Khi cần tin exit code của gate render, dùng `DS_REQUIRE_BROWSER=1` theo tài liệu kit.
- Đọc script/package manifest trước khi cài dependency hoặc chạy công cụ. Việc có source upstream không đồng nghĩa đã cài browser, npm dependency, plugin hook hay MCP server.
- Kết thúc bằng [datn-code-integrity](../datn-code-integrity/SKILL.md) và báo các kiểm tra UI/code đã thực sự chạy, lỗi còn lại và giới hạn.
