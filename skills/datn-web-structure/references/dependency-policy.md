# Framework và dependency của DATN

## Lựa chọn người dùng đã xác nhận

| Phần | Lựa chọn cố định | Cách thay đổi |
| --- | --- | --- |
| Frontend | React | Chỉ đổi sau đề xuất và người dùng acp |
| Backend | FastAPI trên Python | Chỉ đổi sau đề xuất và người dùng acp |
| Thư viện bổ sung | Dùng danh sách và version đã duyệt trong manifest/lockfile | Phải đánh giá nhu cầu/tái sử dụng trước khi thêm hoặc thay |

Hiện tại chưa có source hoặc manifest ứng dụng nên chưa có danh sách version/dependency thực thi được khóa. Các package trong `skills/ux-ui-agent-skills/references/upstream/` chỉ thuộc bộ tài nguyên UX/UI, không phải dependency của website. Không sao chép package.json của kit vào ứng dụng.

## Trước khi thêm dependency

1. Đọc manifest/lockfile toàn workspace và tìm cách đang xử lý nhu cầu đó. Nhận diện package trực tiếp, package dùng chung và dependency bắc cầu; không coi mọi dependency bắc cầu là thư viện trùng cần xóa.
2. Ưu tiên hàm/component nội bộ đã có và khả năng tích hợp của nền tảng. Ví dụ, một HTTP request đơn giản có thể dùng fetch nếu ứng dụng đã dùng fetch; không thêm cả một HTTP client khác chỉ cho một màn hình.
3. Chỉ đề xuất gói mới khi có nhu cầu cụ thể trong phạm vi đã duyệt. Nêu chức năng, gói tương tự hiện có, vì sao tái sử dụng không phù hợp, dung lượng/chi phí và các file bị tác động.
4. Chờ acp trước khi sửa manifest/lockfile hoặc cài dependency mới. Không lách bằng CDN, script tải từ xa, import từ URL hay npx tự tải gói để thực hiện cùng chức năng.
5. Một gói đã duyệt có thể được tái sử dụng ở nhiều module mà không hỏi lại. Nếu nhu cầu mới đòi thêm một thư viện trùng vai trò, xin duyệt ngoại lệ cụ thể.

Các nhóm cần kiểm tra trùng: UI component, HTTP client, quản lý state, form/validation, date/time, chart, icon, animation, ORM/database client và job queue. Hai thư viện phục vụ nhu cầu khác nhau có thể cùng tồn tại khi có lý do; không áp quy tắc “một package cho toàn bộ project”.

## Khóa phiên bản và giữ project nhẹ

- Khi thiết lập source đã được duyệt, chốt phiên bản tương thích của React/FastAPI, runtime và công cụ build; ghi vào manifest cùng lockfile hoặc constraints tương ứng.
- Pin dependency trực tiếp bằng phiên bản cụ thể khi cơ chế đóng gói hỗ trợ; lockfile giữ cây dependency tái lập. Một workspace dùng package manager và bộ lockfile thống nhất.
- Cài lại từ lockfile bằng chế độ frozen/ci phù hợp; không dùng việc cài dependency để nâng phiên bản ngầm.
- Tách runtime dependency và dev dependency. Không đưa công cụ lint/test hoặc toàn bộ kit UX/UI vào bundle sản phẩm.
- Tái sử dụng icon/chart/component đã có; tránh kéo một bộ thư viện lớn cho một chi tiết nhỏ. Với dependency có ảnh hưởng đáng kể, đo build/bundle trước và sau nếu môi trường cho phép; ghi số đo thật, không bịa kích thước.
- Nâng cấp hoặc thay thư viện phải có lý do, đánh giá tương thích, chấp thuận và kiểm tra lại. Dọn gói không còn dùng sau khi xác minh và trong phạm vi đã duyệt; cập nhật lockfile cùng thay đổi.

Đầu ra khi đề xuất: “Nhu cầu → giải pháp hiện có → gói đề nghị/version → vì sao cần → tác động → cách kiểm tra → chờ acp.”
