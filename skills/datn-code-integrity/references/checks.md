# Chọn công cụ kiểm tra theo stack

Đọc phần phù hợp manifest thực tế. Các lệnh dưới đây là mẫu cho công cụ đã cài và cấu hình; tên script, root và tham số phải được xác nhận trước khi chạy. Không thay stack hoặc cài toàn bộ danh sách này.

## JavaScript / TypeScript

- Dùng script lint/typecheck/build/test đã có trong package.json và chạy trên mọi workspace ứng dụng. Đọc script để tránh lệnh tên `test` nhưng chỉ echo hoặc watch vô hạn.
- TypeScript: chạy cấu hình kiểm tra type thực của dự án. `tsc --noEmit -p <tsconfig>` chỉ phù hợp khi config cho phép; với project references/Vue/Svelte dùng build graph hoặc checker của framework. Xác nhận include/exclude không bỏ sót source mới.
- Bật/kiểm tra `noUnusedLocals` và `noUnusedParameters` khi phù hợp cấu hình đã duyệt. Chúng không thay thế phân tích export/file không được sử dụng xuyên module. [TypeScript — noUnusedLocals](https://www.typescriptlang.org/tsconfig/noUnusedLocals.html)
- ESLint: kiểm tra unused imports/variables và unresolved imports với plugin/resolver đúng stack. Với JavaScript, `no-undef` phát hiện tên không được khai báo; với TypeScript dùng checker cho tên/thuộc tính và quy tắc lint tương thích.
- Knip, khi đã được phê duyệt/cấu hình, phân tích unused exports, files và dependencies từ entry point. Cấu hình framework/plugin, workspace, alias và dynamic entry trước khi chấp nhận kết quả. [Knip — Getting Started](https://knip.dev/overview/getting-started)
- Một export không có caller nội bộ vẫn có thể là API public; một route file có thể được framework nạp theo tên. Không xóa trước khi xác minh.
- Kiểm tra test runner ở chế độ chạy một lần, rồi build và smoke các UI/API bị tác động. Chỉ chạy smoke trên môi trường test phù hợp, tránh gửi thao tác có tác dụng phụ vào dữ liệu thật.

Ví dụ khi package.json đã khai báo các script tương ứng:

```text
npm run lint
npm run typecheck
npm run knip
npm run test:run
npm run build
```

Đây không phải danh sách lệnh mặc định để chạy mù. Dùng pnpm/yarn/bun nếu lockfile và quy ước dự án yêu cầu.

## Python

- Chạy trong môi trường Python của ứng dụng và trên đầy đủ root nguồn/tests phù hợp cấu hình.
- Ruff `F821` phát hiện tên chưa định nghĩa; `F401`/`F841` hỗ trợ import/biến không dùng. Ruff không chứng minh tất cả method tồn tại hoặc tất cả hàm được sử dụng. [Ruff — undefined-name](https://docs.astral.sh/ruff/rules/undefined-name/)
- Dùng Pyright hoặc mypy đã cấu hình để kiểm tra attribute/method, import và kiểu. Kiểu động/Any làm giảm phạm vi chứng minh; không tăng Any để làm sạch báo cáo. [Pyright — Configuration](https://github.com/microsoft/pyright/blob/main/docs/configuration.md)
- Dùng Vulture khi đã được phê duyệt để tìm code nghi không dùng; rà decorator, route, task registry và callback trước khi kết luận. Whitelist phải cụ thể và có lý do. [Vulture — Documentation](https://github.com/jendrikseipp/vulture)
- `compileall` chỉ phát hiện vấn đề biên dịch cú pháp; pytest chỉ chứng minh các đường chạy được test. Phối hợp lint, typecheck, unused analysis, tests và kiểm tra đăng ký API/task.

Ví dụ khi các công cụ và root đã tồn tại:

```text
python -m ruff check <source-roots>
pyright --project <project-config>
python -m vulture <source-roots> <test-roots>
python -m pytest
```

Không tạo endpoint/hàm giả để thỏa bài test. Với lỗi caller gọi nhầm method, kiểm tra method đúng hoặc hợp đồng đã duyệt trước khi thêm implementation.

## Hệ thống nhiều lớp

- Đối chiếu UI event → hook/API client → route/schema → service → repository/worker/tool → kết quả. Các tên hợp lệ riêng lẻ vẫn có thể nối sai nhau.
- So sánh HTTP method/path, request/response schema, tên queue/task/tool và chỗ đăng ký. Nếu có codegen, xác nhận dữ liệu sinh khớp schema nguồn.
- Kiểm tra form và Assistant cùng gọi service nghiệp vụ như thiết kế DATN; kết quả do hai đường tạo ra cùng xuất hiện trong dự án.
- Với stack khác, chọn compiler/linter/analyzer chính thức hoặc đã có trong repo cho cùng các lớp kiểm tra. Nêu rõ phần chưa được công cụ bao phủ.
