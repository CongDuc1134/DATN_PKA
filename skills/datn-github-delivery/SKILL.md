---
name: datn-github-delivery
description: "Bàn giao thay đổi DATN lên GitHub sau khi kiểm tra đạt: rà diff, commit tiếng Việt mô tả thay đổi và tự push tới remote/branch đã xác nhận. Dùng khi kết thúc công việc hoặc sửa lỗi đã chạy ổn định; không push code đang lỗi, không ghi đè lịch sử hoặc gom thay đổi ngoài phạm vi."
---

# Commit và cập nhật GitHub cho DATN

Người dùng đã cho phép: sau khi hoàn thành hoặc sửa thành công, kiểm tra chạy ổn định rồi tự cập nhật GitHub; commit bằng tiếng Việt và nói rõ đã sửa gì. Quyền này áp dụng cho dự án DATN, remote/branch đã xác nhận và nội dung thuộc công việc được giao. Không hỏi lại quyền commit/push thông thường trong phạm vi này.

Repository người dùng đã cung cấp: https://github.com/CongDuc1134/DATN_PKA.git. Remote local là `origin`; nhánh khởi tạo là `main`. Kiểm tra lại remote/branch thực tế trước mỗi lần push và tuân thủ nhánh làm việc hoặc branch protection được cấu hình về sau.

## 1. Xác định đúng repository và đích

- Kiểm tra repository root phải là DATN, branch hiện tại, remote, upstream tracking, git status và cấu hình danh tính commit. Không dùng nhầm repository của folder cha hoặc kit UX/UI.
- Nếu DATN chưa có Git, có thể khởi tạo local repository để chuẩn bị bàn giao; hỏi URL GitHub nếu chưa biết đích. Không tự tạo public repository, chọn tài khoản, bịa email commit hoặc dùng nhầm remote của repo tham khảo.
- Nếu có nhiều remote/branch đích không rõ, hỏi lựa chọn còn thiếu. Chấp thuận push không phải chấp thuận merge vào branch được bảo vệ hoặc thay đổi policy GitHub.
- Không yêu cầu người dùng gửi token/mật khẩu vào chat. Khi thiếu xác thực, nêu bước đăng nhập Git/GitHub cần thực hiện trong môi trường của họ.

## 2. Điều kiện trước commit/push

- Đọc và thực hiện [datn-code-integrity](../datn-code-integrity/SKILL.md). Với UI, có kiểm tra tương tác/render phù hợp; với backend, có kiểm tra API/service bị tác động.
- Chỉ bàn giao code khi kiểm tra bắt buộc của dự án đạt, chức năng sửa chạy đúng và không còn lỗi mới chưa xử lý. Nếu công cụ/môi trường thiếu làm không kiểm chứng được phần quan trọng, báo chưa đủ điều kiện push code và giữ thay đổi local.
- Với thay đổi chỉ gồm tài liệu hoặc skill, kiểm tra đúng loại file: cấu trúc, frontmatter, liên kết và script đi kèm nếu có. Không giả vờ ứng dụng đã chạy ổn định khi chưa có source ứng dụng.
- Nếu tồn tại lỗi cũ ngoài phạm vi khiến kiểm tra bắt buộc không đạt, nêu lỗi và chờ hướng xử lý/ngoại lệ rõ ràng; không tự đánh dấu xanh hoặc đẩy như đã đạt.

## 3. Rà và tạo commit tiếng Việt

- Đọc diff và danh sách file mới; stage bằng đường dẫn cụ thể theo phạm vi đã được giao. Không gom sửa đổi không liên quan của người dùng.
- Loại khỏi commit: credential/.env bí mật, token, log nhạy cảm, dependency cài đặt, build/cache, file tạm Office, checkpoint/dataset lớn chưa được duyệt đưa lên GitHub.
- Bộ skill và tài nguyên tham khảo đã được người dùng yêu cầu có thể được commit; giữ license và nguồn gốc. Các junction đăng ký skill trên máy là metadata local, không sao chép thành nhiều bản thư viện lên Git.
- Dùng danh tính Git đã được người dùng cấu hình. Nếu chưa có, hỏi tên/email mong muốn; không tự dùng danh tính của người khác hoặc giá trị giả.
- Tạo commit mới cho đợt sửa hoàn chỉnh; không tự amend lịch sử đã có. Subject tiếng Việt ngắn và cụ thể, ví dụ `Sửa kiểm tra dữ liệu CSV và cập nhật thông báo lỗi`.
- Body khi cần: những module/hành vi đã sửa; lý do; các lệnh kiểm tra và kết quả; giới hạn còn lại. Dùng file UTF-8 với `git commit -F <file>` để giữ tiếng Việt và xuống dòng đúng.
- Không có diff thì không tạo commit rỗng. Nếu có commit của công việc hiện tại đã sẵn sàng nhưng chưa push, kiểm tra rồi push đúng commit đó.

## 4. Push và xác nhận

- Fetch remote trước khi push nếu cần kiểm tra trạng thái. Khi remote thay đổi, so sánh hai phía; đồng bộ bằng quy trình của repo, giữ thay đổi người dùng và chạy lại kiểm tra bị ảnh hưởng sau tích hợp.
- Nếu remote không rỗng và lịch sử local không liên quan, không force-push hoặc ép merge lịch sử; chuẩn bị checkout/worktree riêng từ remote để đưa thay đổi đã duyệt vào, hoặc hỏi khi không rõ cách tích hợp mong muốn.
- Push tới đúng remote/branch được xác nhận. Không dùng `--force`, reset phá hủy, bỏ hook/check hoặc tự tắt branch protection để cho push thành công.
- Nếu branch bị bảo vệ hoặc quyền push bị chặn, báo lỗi thật và giữ commit local; chuẩn bị nhánh/PR khi phù hợp quyền đã có. Không tuyên bố GitHub đã cập nhật nếu push thất bại.
- Sau push, kiểm tra SHA remote branch khớp commit cần bàn giao và trạng thái local. Nếu repo có CI bắt buộc, xem kết quả khi có công cụ; CI chưa xong phải báo đang chờ, không nói đã xanh.
- Nếu CI phát hiện lỗi do thay đổi, sửa trong cùng phạm vi, kiểm tra và tạo commit tiếng Việt tiếp theo. Dừng và báo khi lỗi lặp lại do thiếu quyền, cấu hình ngoài phạm vi hoặc thông tin còn thiếu; không retry vô hạn.

## Báo cáo bàn giao

Nêu ngắn gọn: đã sửa gì; đã kiểm tra gì; commit SHA/subject; remote/branch và link commit khi có; kết quả push/CI hoặc lý do chưa đẩy được. Việc push thành công không tự có nghĩa website đã được deploy.
