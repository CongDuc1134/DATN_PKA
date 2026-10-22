---
name: datn-code-integrity
description: "Kiểm tra toàn bộ source ứng dụng DATN sau mỗi đợt sinh, sửa hoặc refactor code: lint, typecheck, build, test, hàm/import/export không dùng và lời gọi tới hàm, method, module hoặc route không tồn tại. Dùng trước khi bàn giao thay đổi code; phân biệt code chết với entry point gọi động."
---

# Kiểm tra tính nhất quán của code DATN

Thực hiện sau mỗi đợt thay đổi code hoàn chỉnh và trước khi kết luận hoàn thành. “Toàn bộ” là tất cả source ứng dụng do dự án quản lý: frontend, backend, worker, service dùng chung, script ứng dụng và các workspace tương ứng; bao gồm file mới chưa được Git theo dõi. Các thư viện vendor, nội dung tham khảo trong `skills/`, dependency cài đặt, cache và output build không phải source ứng dụng.

## 1. Xác định phạm vi và lệnh kiểm tra thật

- Đọc manifest, lockfile, script build/test, cấu hình lint/typecheck và CI nếu có. Dùng package manager, interpreter, môi trường và cấu hình của dự án.
- Liệt kê các workspace và entry point; kiểm tra glob include/exclude để file mới thực sự được kiểm tra. Không chỉ quét những dòng trong diff.
- Đọc [references/checks.md](references/checks.md) cho stack đang dùng. Không chạy tên script đoán mò, không tự tải gói qua `npx` rồi coi là cấu hình dự án.
- Khi chưa có công cụ cần thiết, nêu rõ khoảng trống; đề xuất cấu hình/dependency cần bổ sung và xin duyệt nếu phần đó chưa được chấp thuận. Vẫn hoàn tất những kiểm tra có thể làm bằng công cụ hiện có.

## 2. Kiểm tra toàn bộ dự án theo các lớp

| Lớp kiểm tra | Điều cần chứng minh |
| --- | --- |
| Syntax / lint | File parse được; import, biến, tên gọi không sai; không che lỗi bằng disable rộng |
| Typecheck / symbol resolution | Hàm/method/module được gọi tồn tại và đúng tên, signature, kiểu tham số/return và async contract |
| Unused / dependency graph | Tìm hàm, import, export, file và dependency không được sử dụng từ các entry point thật |
| Build | Tất cả app/package trong workspace build theo cấu hình thực; lỗi bundle hoặc codegen được xử lý |
| Tests | Chạy bộ test tự động hiện có của các workspace; thêm test hành vi có ý nghĩa cho thay đổi logic có rủi ro |
| Integration / smoke | UI handler, route, service, worker task, registry và agent tool được nối đúng; API contract khớp hai đầu |

Chạy các lệnh độc lập song song nếu không cùng ghi vào output hoặc giành tài nguyên. Thực hiện tuần tự các bước phụ thuộc như codegen rồi typecheck/build. Sau khi sửa lỗi, chạy lại kiểm tra bị ảnh hưởng; không lặp vô hạn các kiểm tra đã đạt trên source không đổi.

## 3. Hàm không dùng: kiểm tra bằng chứng trước khi xóa

- Dùng phân tích AST/đồ thị dependency và tìm reference; `rg` hỗ trợ rà soát, số lần xuất hiện tên không đủ chứng minh một hàm là code chết.
- Kiểm tra route theo quy ước framework, export public, callback/event handler, decorator, dependency injection, plugin/agent registry, CLI entry, dynamic import và tác dụng phụ khi import.
- Với mỗi phát hiện, xác định file/symbol, công cụ báo lỗi, callers/đăng ký liên quan và kết luận: code chết, entry point hợp lệ hoặc chưa đủ bằng chứng.
- Được dọn code chết do thay đổi hiện tại tạo ra hoặc trong phạm vi cleanup đã duyệt khi đã chứng minh không còn dùng. Với public API hoặc code cũ ngoài phạm vi, báo tác động và xin duyệt trước khi loại bỏ.
- Không gọi hàm vô nghĩa để biến nó thành “được dùng”, không tạo test giả chỉ để tăng reference, không xóa hàng loạt theo cảnh báo của một công cụ.

## 4. Lời gọi tới hàm không tồn tại

- Đối chiếu caller với định nghĩa, import/export, method trên kiểu đối tượng, tên đăng ký và phiên bản dependency đang khóa.
- Với HTTP/worker/agent tool: kiểm tra cả client path/method, server route hoặc tên task/tool registry, schema và cách nhận kết quả.
- Ưu tiên sửa tên/import/caller hoặc nối lại implementation đúng đã có. Nếu thiếu implementation trong phạm vi chức năng đã duyệt, hoàn thiện theo thiết kế đó.
- Nếu giải pháp đòi thêm chức năng/entity/field/API chưa được duyệt, thực hiện quy trình đề xuất và chờ acp trong [datn-web-structure](../datn-web-structure/SKILL.md).
- Không tạo stub/no-op/trả dữ liệu giả để làm lỗi biến mất; không thêm `any`, `@ts-ignore`, `noqa` hoặc bỏ cả thư mục kiểm tra để che lỗi.

## 5. Điều kiện hoàn thành và báo cáo

- Sửa lỗi mới do thay đổi gây ra; phân biệt lỗi tồn tại sẵn và nêu tác động. Lỗi cũ không tự cho phép bỏ qua kiểm tra toàn dự án hoặc sửa lan sang chức năng ngoài phạm vi.
- Báo chính xác lệnh đã chạy, workspace/phạm vi, PASS/FAIL/SKIPPED, symbol hoặc lỗi còn lại và lý do. Kiểm tra không chạy vì thiếu môi trường phải ghi là chưa kiểm chứng.
- Build thành công không chứng minh không có code chết; lint sạch không chứng minh mọi method động hoặc API route tồn tại. Tổng hợp bằng chứng từ nhiều lớp.
- Khi workspace chưa có source ứng dụng, báo “chưa có source ứng dụng để chạy lint/typecheck/build/test”; vẫn kiểm tra cấu trúc các file vừa tạo phù hợp với loại file. Không tạo ứng dụng mẫu chỉ để có kết quả test.
- Không khẳng định phát hiện 100% mọi hàm không dùng hoặc mọi lỗi runtime. Nêu phần gọi động hoặc đường chạy chưa kiểm chứng nếu còn.

Mẫu báo cáo ngắn: “Đã kiểm tra [workspace]: lint…, typecheck…, unused…, build…, tests…, smoke…. Đã sửa [lỗi]. Còn [hạn chế/chờ duyệt].”
