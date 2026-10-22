# Hướng dẫn làm việc trong dự án DATN

Phạm vi: thư mục DATN và các thư mục con. Đây là website ECT có màn hình thao tác trực tiếp, tích hợp thêm Assistant agentic. Các bản kế hoạch mô tả định hướng; chỉ triển khai phạm vi người dùng đã duyệt.

Stack người dùng đã chốt: frontend **React**, backend **FastAPI**. Tái sử dụng thư viện hiện hữu; không tự thêm package trùng chức năng, đổi framework hoặc nâng version ngoài phạm vi. Áp dụng [dependency policy](skills/datn-web-structure/references/dependency-policy.md) trước khi thay dependency.

## Skills bắt buộc theo công việc

- Trước mọi thay đổi source website, đọc [datn-web-structure](skills/datn-web-structure/SKILL.md): chia module/file theo trách nhiệm và sửa ngay trong folder/file đang sở hữu chức năng.
- Trước khi thêm trường dữ liệu, đối tượng, chức năng, màn hình hoặc API chưa được duyệt: trình ý tưởng, lý do cần, phương án tái sử dụng, file bị ảnh hưởng; chờ người dùng đồng ý/acp. Giữ chấp thuận đã có, không hỏi lại cùng phạm vi.
- Khi tạo/sửa UI, dùng [ux-ui-agent-skills](skills/ux-ui-agent-skills/SKILL.md) trong phạm vi đã duyệt.
- Sau mỗi đợt sinh/sửa/refactor code, chạy quy trình [datn-code-integrity](skills/datn-code-integrity/SKILL.md) trên toàn bộ source ứng dụng: tên/hàm/import không tồn tại, code nghi không dùng, lint, typecheck, build, test và liên kết giữa các lớp.
- Sau khi công việc được kiểm tra đạt, áp dụng [datn-github-delivery](skills/datn-github-delivery/SKILL.md): tự commit tiếng Việt và push tới repository/branch đã xác nhận, ghi rõ đã sửa gì. Người dùng đã cấp quyền này; chỉ hỏi khi thiếu đích, danh tính/quyền truy cập hoặc phát sinh thay đổi ngoài phạm vi.

Đọc skill áp dụng ở đầu tác vụ; không chỉ đọc sau khi code đã sinh. Tác vụ chỉ đọc, giải thích, lập kế hoạch hoặc chỉnh tài liệu không cần tạo/chạy một ứng dụng giả để thỏa kiểm tra code.

## Lưu trữ và phạm vi kiểm tra

- `skills/` là thư mục nguồn duy nhất của bộ skill: chỉ chứa các folder skill cùng tài nguyên phục vụ chúng. Không đặt source sản phẩm, dataset, checkpoint hoặc báo cáo ứng dụng trong đây.
- `.agents/skills/`, `.codex/skills/` và `.claude/skills/` chứa các liên kết tới cùng các folder nguồn để các công cụ (Codex, Antigravity, Claude Code) tự động nhận diện skill. Cấu hình `.agents/skills.json` giúp Antigravity nhận diện trực tiếp thư mục `skills/`. Khi sửa skill, sửa file gốc trong `skills/`. Sau khi clone/chuyển đường dẫn trên Windows, chạy `powershell -NoProfile -File skills/datn-web-structure/scripts/register-project-skills.ps1 [-Global]` để tạo liên kết local hoặc toàn cục; không commit bản sao qua junction.
- `skills/ux-ui-agent-skills/references/upstream/` là tài nguyên bên thứ ba, không phải source website. Không lấy app mẫu hoặc self-test ở đó làm bằng chứng website đã hoạt động.
- Code phải được đặt trong folder phù hợp cấu trúc đã duyệt; không tạo bản `new/fixed/v2` song song để né sửa code gốc.
- Với hàm nghi không dùng, xác minh callback, route, decorator, registry và public export trước khi xóa. Không tạo stub/no-op hoặc gọi hàm vô nghĩa để làm sạch báo cáo.
- Báo rõ kiểm tra nào PASS, FAIL hoặc chưa chạy. Skill/hướng dẫn là quy trình làm việc của agent; chỉ tuyên bố có enforcement bằng hook/CI khi hook/CI đó đã được triển khai và kiểm chứng.
