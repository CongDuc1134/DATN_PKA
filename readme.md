# VAI TRÒ

Bạn là Solution Architect + Business Analyst kiêm nhà nghiên cứu NDT (kiểm tra không phá hủy) có kinh nghiệm về Eddy Current Testing (ECT), mô phỏng điện từ và Agentic Software Engineering.

# BỐI CẢNH Ý TƯỞNG

Tôi muốn xây dựng một **trang web agentic** để mô phỏng và phân tích từ trường ECT, gồm 3 mảng chính:

1. **Dipole model** (bán giải tích): sinh nhanh ảnh từ trường Bz của vết nứt, tham số hóa theo (W, L, D) và biên dạng.
2. **Generate bằng diffusion model**: sinh/mở rộng dữ liệu ảnh từ trường (có thể điều kiện hóa theo hình dạng, kích thước, tần số), phục vụ augmentation và super-resolution.
3. **Phân tích vết nứt**: phân loại biên dạng (Rectangular, Triangular, Ellipse, Step_R, Step_T), ước lượng kích thước W/L/D, có thể dùng CNN/PINN và đối chiếu với forward model (dipole/FEM).

Thông số đầu vào điển hình: tấm Al7075 dày 5 mm, dãy 32×32 cảm biến Hall (pitch 0.78 mm), tần số 5/10/20 kHz, ảnh CSV hiệu giữa các sensor kề nhau.
"Agentic" nghĩa là: người dùng mô tả mục tiêu bằng ngôn ngữ tự nhiên, hệ thống có các AI agent tự lập kế hoạch, gọi công cụ (simulator, model, dữ liệu), chạy job, kiểm tra kết quả và báo cáo, có human-in-the-loop ở các bước quan trọng.

# NHIỆM VỤ

Hãy phân tích ý tưởng và lập tài liệu thiết kế phần mềm chi tiết, gồm các phần sau:

## 1. Tổng quan và phạm vi

- Vấn đề, mục tiêu, giá trị mang lại, phạm vi (in-scope/out-of-scope).
- Stakeholder và persona (nhà nghiên cứu, sinh viên, kỹ sư NDT, admin...).
- Giả định, ràng buộc, rủi ro chính và cách giảm thiểu.

## 2. Đề xuất chức năng chi tiết

- Chia theo module (ví dụ: quản lý dự án/thí nghiệm, dipole simulator, diffusion generator, crack analyzer, dataset manager, model registry, agent chat/orchestrator, báo cáo/xuất kết quả, quản trị người dùng).
- Mỗi chức năng: mô tả, đầu vào/đầu ra, mức ưu tiên (MoSCoW), độ phức tạp.
- Đề xuất cả các chức năng nâng cao mà tôi chưa nghĩ tới (ví dụ: so sánh dipole vs FEM vs ảnh đo, đánh giá 1−R², kiểm tra chất lượng ảnh sinh ra, explainability, batch/sweep tham số, tái lập thí nghiệm).

## 3. Đặc tả Use Case

- Sơ đồ use case tổng thể (Mermaid hoặc PlantUML).
- Đặc tả từng use case dạng bảng: ID, tên, actor, mô tả, tiền điều kiện, hậu điều kiện, luồng chính, luồng thay thế/ngoại lệ, yêu cầu phi chức năng liên quan.

## 4. Kiến trúc agentic

- Danh sách agent (ví dụ: Orchestrator/Planner, Simulation Agent, Generation Agent, Analysis Agent, QA/Validation Agent, Report Agent), vai trò, công cụ (tools) mỗi agent được gọi.
- Cơ chế: lập kế hoạch, bộ nhớ/ngữ cảnh, hàng đợi job GPU, xử lý lỗi/retry, human-in-the-loop, giới hạn quyền, ghi log hành động.

## 5. Sequence Diagram

Vẽ (Mermaid/PlantUML) cho tối thiểu các luồng:

- Người dùng yêu cầu mô phỏng dipole bằng ngôn ngữ tự nhiên.
- Sinh dữ liệu bằng diffusion model (job bất đồng bộ).
- Upload ảnh đo thật và phân tích vết nứt.
- Agent tự chạy sweep tham số và tạo báo cáo.
Mỗi sơ đồ kèm giải thích ngắn.

## 6. Flow/Activity Diagram

- Luồng tổng thể từ tạo dự án đến xuất báo cáo.
- Luồng pipeline dữ liệu (tiền xử lý ảnh, chuẩn hóa, augmentation, train/validate).
- Luồng quyết định của agent (khi nào hỏi lại người dùng, khi nào tự chạy tiếp).

## 7. Thiết kế Database

- Chọn loại CSDL (quan hệ/NoSQL/vector/object storage) và giải thích vì sao.
- ERD (Mermaid) và danh sách bảng: tên bảng, cột, kiểu dữ liệu, khóa chính/ngoại, ràng buộc, index.
- Cách lưu dữ liệu lớn (ảnh, tensor, checkpoint) và metadata, versioning dataset/model, provenance (ảnh nào sinh từ tham số/model/seed nào).
- Lưu lịch sử hội thoại và hành động của agent, quyền truy cập, chiến lược backup.

## 8. Thiết kế kỹ thuật bổ sung

- Kiến trúc tổng thể (frontend, backend, worker GPU, queue, storage), tech stack đề xuất kèm lý do.
- Danh sách API chính (REST/WebSocket/SSE cho streaming).
- Yêu cầu phi chức năng: hiệu năng, bảo mật, khả năng mở rộng, tái lập kết quả.
- Chiến lược kiểm thử (gồm kiểm chứng vật lý của kết quả mô phỏng).

## 9. Lộ trình triển khai

- Chia MVP → v1 → v2, ước lượng công việc, thứ tự ưu tiên, tiêu chí hoàn thành mỗi giai đoạn.

# YÊU CẦU ĐẦU RA

- Viết bằng **tiếng Việt**, giữ nguyên thuật ngữ kỹ thuật tiếng Anh khi cần.
- Xuất thành **một file .docx** hoàn chỉnh: trang bìa, mục lục, đánh số mục, bảng có viền rõ ràng, sơ đồ được render thành hình và chèn vào tài liệu (kèm mã nguồn Mermaid/PlantUML ở phụ lục).
- Chi tiết, cụ thể, tránh nói chung chung; nếu thiếu thông tin hãy nêu giả định rõ ràng thay vì bỏ qua.
- Cuối tài liệu, liệt kê các câu hỏi mở cần tôi quyết định.
