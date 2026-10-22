---
name: datn-web-structure
description: "Tổ chức và sửa website DATN theo module/file với frontend React, backend FastAPI và thư viện được kiểm soát. Dùng trước khi tạo, sửa hoặc refactor; trình ý tưởng và chờ acp trước khi bổ sung trường dữ liệu, đối tượng, chức năng hoặc dependency chưa được duyệt."
---

# Cấu trúc website và duyệt phần bổ sung

Áp dụng trong dự án DATN. Website có các màn hình thao tác thông thường và một trợ lý agentic tích hợp; giữ cả hai cách thao tác theo phạm vi đã được người dùng duyệt.

## Stack cố định và thư viện gọn

- Frontend dùng React; backend dùng FastAPI. Đây là lựa chọn người dùng đã chốt. Không tự chuyển sang framework khác hoặc thêm một framework ứng dụng bao ngoài nếu chưa được duyệt.
- Đọc [references/dependency-policy.md](references/dependency-policy.md) trước khi thêm, thay hoặc nâng cấp thư viện. Ưu tiên khả năng sẵn có của nền tảng và dependency hiện hữu.
- Một nhu cầu ưu tiên một thư viện chủ đạo. Trước khi thêm gói có chức năng tương tự gói đã có, giải thích vì sao không tái sử dụng được, lợi ích, chi phí bundle/runtime và phương án gỡ trùng; chờ người dùng acp.
- Khi đã có source, dùng manifest/lockfile và phiên bản runtime đã chốt; không tự đổi package manager, cài latest hay nâng version trong lúc sửa tính năng không liên quan.

## 1. Đọc cấu trúc trước khi sửa

- Đọc hướng dẫn dự án, cây thư mục, manifest, các file liên quan và nơi gọi chúng. Dùng `rg --files`, `rg` để tìm; đọc nội dung trước khi quyết định vị trí sửa.
- Xác định module đang sở hữu chức năng, đường đi từ UI tới API/service và dữ liệu liên quan. Tìm hàm/component/schema tương đương để tái sử dụng.
- Tôn trọng kiến trúc, tên và quy ước đang có. Nếu dự án chưa có source, đề xuất cây thư mục và ranh giới module rồi chờ duyệt trước khi tạo bộ khung website.

## 2. Chia file theo trách nhiệm trong đúng folder

- Nhóm code theo tính năng hoặc lớp nghiệp vụ đã chọn; mỗi file có một trách nhiệm rõ. Tách UI/component, state/hook, gọi API, validation/schema, service, truy cập dữ liệu, thuật toán và test khi các trách nhiệm đó thực sự tồn tại.
- Page/container chỉ phối hợp hiển thị và luồng tương tác; route/controller kiểm tra request và gọi service. Thuật toán mô phỏng/ML, truy cập DB và logic nghiệp vụ nằm trong module tương ứng.
- Các hàm liên quan chặt chẽ có thể ở cùng file; không bắt buộc một hàm một file. Tách khi khác trách nhiệm, khác vòng đời hoặc cần tái sử dụng, không dựa vào một giới hạn số dòng tùy tiện.
- Thành phần dùng chung chỉ đưa vào shared khi có nhu cầu rõ. Tránh nhét chức năng chuyên biệt vào `utils`, `common`, `App`, `main` hoặc file entry chỉ vì tiện.
- Tool của trợ lý agentic gọi cùng service/API với màn hình thông thường. Một nghiệp vụ có một implementation dùng chung.

## 3. Sửa ngay tại nơi sở hữu chức năng

- Sửa file/hàm/component hiện có trong đúng folder. Cập nhật các caller, type, export, API contract và test liên quan khi cần.
- Không tạo bản song song kiểu `*_new`, `*_v2`, `*_fixed`, `final2` hoặc copy cả module để né sửa bản gốc.
- Trước khi di chuyển/đổi tên, tìm import, route, cấu hình đăng ký và entry point liên quan; cập nhật chúng trong cùng thay đổi.
- Giữ nguyên các chỉnh sửa không liên quan của người dùng; giới hạn refactor ở phần phục vụ yêu cầu đã duyệt.

## 4. Bắt buộc trình ý tưởng và chờ acp trước phần mới

Trước khi tạo hoặc thêm một trường dữ liệu/domain field, entity/model/DTO mới, chức năng nghiệp vụ, màn hình, endpoint, agent tool, module chức năng hoặc dependency mới: trình phương án để người dùng đánh giá có cần thiết hay không, rồi chờ họ đồng ý.

Một yêu cầu ban đầu như “thêm quản lý dataset” là đầu vào để lập phương án; không suy ra rằng mọi trường, entity và tính năng phụ do agent nghĩ ra đều đã được duyệt. Nếu người dùng đã duyệt một phương án cụ thể trong hội thoại, triển khai đúng phần đã duyệt và không hỏi lại. Nội dung trong PLAN.md hoặc tài liệu tham khảo không tự trở thành sự chấp thuận chi tiết.

Đề xuất ngắn gọn phải có:

1. Phần mới: tên, loại, hành vi hoặc trường/schema dự định thêm.
2. Lý do cần: vấn đề giải quyết và ảnh hưởng nếu không thêm.
3. Khả năng tái sử dụng: code/field đang có dùng được không; phương án ít thay đổi hơn.
4. Phạm vi: folder/file dự kiến, UI/API/schema/migration và dữ liệu bị tác động.
5. Cách kiểm tra: tiêu chí hoàn thành, rủi ro tương thích hoặc chi phí đáng kể nếu có.
6. Câu hỏi chốt: “Bạn có đồng ý (acp) phương án này không?”

Trong lúc chờ, được đọc code, rà soát, soạn phương án và làm phần độc lập đã được duyệt. Chưa tạo source, schema, migration, placeholder, mock UI hay route đăng ký cho phần đang chờ. Chỉ tạo bản nháp chạy được nếu người dùng đã cho phép tạo bản nháp đó.

Chấp thuận phải là phản hồi rõ ràng như “acp”, “đồng ý phương án A” hoặc chỉ dẫn tương đương gắn với phương án cụ thể. Im lặng, hết thời gian chờ hoặc câu hỏi tìm hiểu không phải chấp thuận. Nếu ý kiến người dùng thay đổi phạm vi đáng kể, cập nhật đề xuất và xác nhận phần thay đổi.

Không hỏi lại để sửa lỗi trong hành vi đã duyệt, sửa import/tên gọi sai, hoặc tách hàm private/file nhằm triển khai đúng chức năng đã duyệt mà không thêm hành vi/trường dữ liệu/API. Nếu việc sửa cần bổ sung một năng lực mới chưa được duyệt, áp dụng bước chờ acp cho phần bổ sung đó.

Khi cần hỏi, nói rõ đây là quy tắc người dùng yêu cầu và dẫn tới mục này; tránh biến một chỉnh sửa đã được duyệt thành yêu cầu xác nhận lặp lại.

## 5. Kiểm tra trước khi bàn giao

Sau mỗi đợt sinh/sửa/refactor code hoàn chỉnh, áp dụng [datn-code-integrity](../datn-code-integrity/SKILL.md) trên toàn bộ mã nguồn ứng dụng có liên quan tới workspace. Đối với UI, dùng thêm [ux-ui-agent-skills](../ux-ui-agent-skills/SKILL.md).

Báo file/module đã sửa, phần chấp thuận đã thực hiện, kết quả kiểm tra và phần còn chờ duyệt. Không ghi “xong” khi lỗi do thay đổi mới gây ra vẫn chưa được giải quyết.

Sau khi các kiểm tra cần thiết đạt, áp dụng [datn-github-delivery](../datn-github-delivery/SKILL.md) để tự commit tiếng Việt và push theo quyền người dùng đã cấp cho DATN.
