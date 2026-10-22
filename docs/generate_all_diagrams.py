import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches

output_dir = r"C:\Users\Admin\Documents\DATN\docs\images"
os.makedirs(output_dir, exist_ok=True)

# Clean font setup
plt.rcParams['font.sans-serif'] = 'Segoe UI'
plt.rcParams['font.family'] = 'sans-serif'

# =============================================================================
# 1. SƠ ĐỒ USE CASE TỔNG THỂ (CLEAN & PROFESSIONAL)
# =============================================================================
def draw_use_case():
    fig, ax = plt.subplots(figsize=(16, 10.5), dpi=300)
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 10.5)
    ax.axis('off')
    fig.patch.set_facecolor('#FFFFFF')

    # Header
    ax.text(8.0, 10.0, "SƠ ĐỒ USE CASE TỔNG THỂ HỆ THỐNG WEBSITE ECT & TRỢ LÝ AGENTIC", 
            ha='center', va='center', fontsize=17, fontweight='bold', color='#0F172A')
    ax.text(8.0, 9.65, "Phân định rõ ranh giới: Thao tác trực tiếp của Kỹ sư NDT và Chuỗi điều phối tự động của Trợ lý AI", 
            ha='center', va='center', fontsize=10.5, color='#64748B')

    # Actor 1: Human User (Left Card)
    user_card = patches.FancyBboxPatch((0.5, 2.0), 3.2, 7.2, boxstyle="round,pad=0.15",
                                      fc='#F0F9FF', ec='#0284C7', lw=2)
    ax.add_patch(user_card)
    # Avatar badge
    user_badge = patches.Circle((2.1, 8.4), 0.5, fc='#BAE6FD', ec='#0284C7', lw=1.5)
    ax.add_patch(user_badge)
    ax.text(2.1, 8.4, "USER", ha='center', va='center', fontsize=10, fontweight='bold', color='#0369A1')
    ax.text(2.1, 7.6, "KỸ SƯ NDT / NGƯỜI DÙNG", ha='center', va='center', fontsize=11, fontweight='bold', color='#0C4A6E')
    ax.text(2.1, 7.25, "(Thao tác trực tiếp)", ha='center', va='center', fontsize=9.5, style='italic', color='#0369A1')
    
    user_desc = (
        "Quyền hạn & Khả năng:\n\n"
        "• Thao tác độc lập 100% qua\n  Menu, Form, Nút bấm.\n\n"
        "• Nhập tham số mô phỏng\n  Dipole (W, L, D, tần số).\n\n"
        "• Upload file CSV đo thực tế\n  và xem Heatmap 32x32.\n\n"
        "• Kích hoạt phân tích CNN.\n\n"
        "• Giao mục tiêu cho Trợ lý AI\n  và phê duyệt kế hoạch."
    )
    ax.text(0.8, 5.0, user_desc, va='center', fontsize=9, color='#1E293B', linespacing=1.4)

    # Actor 2: AI Agent (Right Card)
    agent_card = patches.FancyBboxPatch((12.3, 2.0), 3.2, 7.2, boxstyle="round,pad=0.15",
                                       fc='#FAF5FF', ec='#7C3AED', lw=2)
    ax.add_patch(agent_card)
    # Avatar badge
    agent_badge = patches.FancyBboxPatch((13.4, 7.9), 1.0, 0.9, boxstyle="round,pad=0.1",
                                         fc='#DDD6FE', ec='#7C3AED', lw=1.5)
    ax.add_patch(agent_badge)
    ax.text(13.9, 8.35, "AI", ha='center', va='center', fontsize=11, fontweight='bold', color='#6D28D9')
    ax.text(13.9, 7.6, "TRỢ LÝ AGENTIC", ha='center', va='center', fontsize=11, fontweight='bold', color='#581C87')
    ax.text(13.9, 7.25, "(Tự động hóa chuỗi)", ha='center', va='center', fontsize=9.5, style='italic', color='#6D28D9')

    agent_desc = (
        "Quyền hạn & Khả năng:\n\n"
        "• Đọc mục tiêu cấp cao qua Chat.\n\n"
        "• Tự chia nhỏ kế hoạch nhiều bước\n  (ReAct State Graph).\n\n"
        "• Tự động gọi tool: CNN, Dipole,\n  và tính sai số RMSE.\n\n"
        "• Tự động chạy sweep tham số\n  tìm kích thước khớp nhất.\n\n"
        "• Tự tổng hợp bằng chứng và\n  xuất báo cáo kỹ thuật."
    )
    ax.text(12.6, 5.0, agent_desc, va='center', fontsize=9, color='#1E293B', linespacing=1.4)

    # Center: 4 Subsystems
    subsystems = [
        # Subsystem 1: Dữ liệu
        (4.2, 6.7, 7.6, 2.5, "PHÂN HỆ 1: QUẢN LÝ DỮ LIỆU & MẪU ĐO", "#F8FAFC", "#38BDF8", [
            ("UC01: Upload file CSV đo & Tiền xử lý ma trận 32x32", True, False),
            ("UC02: Trực quan hóa Heatmap từ trường & Xử lý bù NaN", True, False),
            ("UC03: Quản lý Phiên bản Dataset & Gán nhãn mẫu vật", True, False)
        ]),
        # Subsystem 2: Mô phỏng
        (4.2, 3.8, 3.65, 2.65, "PHÂN HỆ 2: MÔ PHỎNG VẬT LÝ", "#FFFBEB", "#F59E0B", [
            ("UC04: Mô phỏng Dipole bán giải tích", True, True),
            ("UC05: Quét tham số Sweep W/L/D", True, True),
            ("UC06: Sinh ảnh từ trường Diffusion", True, False)
        ]),
        # Subsystem 3: Phân tích
        (8.15, 3.8, 3.65, 2.65, "PHÂN HỆ 3: PHÂN TÍCH & ĐỐI CHIẾU", "#F0FDF4", "#22C55E", [
            ("UC07: Phân loại biên dạng vết nứt CNN", True, True),
            ("UC08: Hồi quy kích thước W, L, D", True, True),
            ("UC09: Đối chiếu Tín hiệu Đo vs Dipole", False, True)
        ]),
        # Subsystem 4: Trợ lý & Báo cáo
        (4.2, 0.8, 7.6, 2.7, "PHÂN HỆ 4: TRỢ LÝ AGENTIC & BÁO CÁO", "#FAF5FF", "#A855F7", [
            ("UC10: Giao mục tiêu cấp cao qua Assistant Panel (ReAct Loop)", True, True),
            ("UC11: Phê duyệt kế hoạch hành động (Human-in-the-loop)", True, False),
            ("UC12: Tự động tổng hợp dữ liệu & Xuất Báo cáo PDF/Word", True, True)
        ])
    ]

    for sx, sy, sw, sh, s_title, bg_col, border_col, ucs in subsystems:
        sub_box = patches.FancyBboxPatch((sx, sy), sw, sh, boxstyle="round,pad=0.1",
                                         fc=bg_col, ec=border_col, lw=1.5)
        ax.add_patch(sub_box)
        ax.text(sx + 0.25, sy + sh - 0.25, s_title, fontsize=9.5, fontweight='bold', color=border_col)
        
        # Render Use Cases as clean pills
        for i, (uc_title, by_user, by_agent) in enumerate(ucs):
            uc_y = sy + sh - 0.7 - i * 0.65
            uc_rect = patches.FancyBboxPatch((sx + 0.2, uc_y - 0.2), sw - 0.4, 0.45,
                                             boxstyle="round,pad=0.08", fc='#FFFFFF', ec='#CBD5E1', lw=1)
            ax.add_patch(uc_rect)
            ax.text(sx + 0.35, uc_y + 0.02, uc_title, fontsize=8.2, fontweight='bold', color='#1E293B', va='center')
            
            # Badges
            tag_text = ""
            if by_user and by_agent:
                tag_text = "[User + AI]"
                tag_col = "#7C3AED"
            elif by_user:
                tag_text = "[User]"
                tag_col = "#0284C7"
            else:
                tag_text = "[Tự động AI]"
                tag_col = "#059669"
            ax.text(sx + sw - 0.35, uc_y + 0.02, tag_text, fontsize=7.5, fontweight='bold', color=tag_col, ha='right', va='center')

    # Clean connecting arrows between Actors and Subsystems
    # User -> Subsystems (Orthogonal)
    ax.annotate('', xy=(4.2, 8.0), xytext=(3.7, 8.0), arrowprops=dict(arrowstyle="->", color='#0284C7', lw=2))
    ax.annotate('', xy=(4.2, 5.0), xytext=(3.7, 5.0), arrowprops=dict(arrowstyle="->", color='#0284C7', lw=2))
    ax.annotate('', xy=(4.2, 2.0), xytext=(3.7, 2.0), arrowprops=dict(arrowstyle="->", color='#0284C7', lw=2))

    # Agent -> Subsystems (Orthogonal dotted)
    ax.annotate('', xy=(11.8, 5.0), xytext=(12.3, 5.0), arrowprops=dict(arrowstyle="->", color='#7C3AED', ls='--', lw=2))
    ax.annotate('', xy=(11.8, 2.0), xytext=(12.3, 2.0), arrowprops=dict(arrowstyle="->", color='#7C3AED', ls='--', lw=2))

    # Legend
    leg_box = patches.FancyBboxPatch((4.2, 0.1), 7.6, 0.5, boxstyle="round,pad=0.05", fc='#F1F5F9', ec='#CBD5E1')
    ax.add_patch(leg_box)
    ax.text(8.0, 0.35, "Chú thích:  [User]: Kỹ sư thao tác form trực tiếp  •  [User + AI]: Hỗ trợ cả 2 chế độ  •  [Tự động AI]: Agent tự gọi qua tool",
            ha='center', va='center', fontsize=8.5, color='#475569')

    plt.tight_layout()
    save_path = os.path.join(output_dir, "1_Use_Case_Tong_The.png")
    plt.savefig(save_path, dpi=300)
    plt.close()
    print("Regenerated:", save_path)


# =============================================================================
# HELPER: DRAW CLEAN SEQUENCE DIAGRAM
# =============================================================================
def draw_clean_sequence(title, subtitle, participants, messages, save_filename, height=9.5):
    fig, ax = plt.subplots(figsize=(16, height), dpi=300)
    ax.set_xlim(0, 16)
    ax.set_ylim(0, height)
    ax.axis('off')
    fig.patch.set_facecolor('#FFFFFF')

    # Title
    ax.text(8.0, height - 0.4, title, ha='center', va='center', fontsize=16, fontweight='bold', color='#0F172A')
    ax.text(8.0, height - 0.75, subtitle, ha='center', va='center', fontsize=10, color='#64748B')

    # Draw Lifelines
    p_x_map = {}
    top_y = height - 1.2
    bot_y = 0.6

    for p_id, p_name, p_role, bg_col, border_col in participants:
        px = participants.index((p_id, p_name, p_role, bg_col, border_col))
        # Distribute participants evenly
        x = 1.2 + px * (13.6 / (len(participants) - 1))
        p_x_map[p_id] = x

        # Participant Box Header
        p_box = patches.FancyBboxPatch((x - 1.1, top_y - 0.65), 2.2, 0.65, boxstyle="round,pad=0.08",
                                       fc=bg_col, ec=border_col, lw=2)
        ax.add_patch(p_box)
        ax.text(x, top_y - 0.22, p_name, ha='center', va='center', fontsize=9.2, fontweight='bold', color='#0F172A')
        ax.text(x, top_y - 0.48, p_role, ha='center', va='center', fontsize=7.8, color='#475569')

        # Lifeline vertical dash
        ax.plot([x, x], [top_y - 0.65, bot_y], color='#CBD5E1', ls='--', lw=1.5, zorder=1)

    # Draw Sequence Messages
    curr_y = top_y - 1.1
    y_step = (curr_y - bot_y) / (len(messages) + 0.5)

    for i, msg in enumerate(messages):
        msg_y = curr_y - i * y_step

        if len(msg) == 5:
            # Normal Call: (from_id, to_id, text, is_sync, is_return)
            f_id, t_id, text, is_sync, is_return = msg
            x1 = p_x_map[f_id]
            x2 = p_x_map[t_id]

            # Line & Arrow
            ls = '--' if is_return else '-'
            col = '#2563EB' if not is_return else '#059669'
            ax.annotate('', xy=(x2, msg_y), xytext=(x1, msg_y),
                        arrowprops=dict(arrowstyle="->", color=col, ls=ls, lw=1.6), zorder=2)

            # Clean Pill Box for text (Prevents overlapping!)
            mid_x = (x1 + x2) / 2
            pill_w = abs(x2 - x1) * 0.82
            pill_h = 0.32
            pill = patches.FancyBboxPatch((mid_x - pill_w/2, msg_y + 0.06), pill_w, pill_h,
                                          boxstyle="round,pad=0.05", fc='#FFFFFF', ec='#E2E8F0', lw=1, zorder=3)
            ax.add_patch(pill)
            num_str = f"[{i+1}] "
            ax.text(mid_x, msg_y + 0.22, num_str + text, ha='center', va='center', 
                    fontsize=8.0, fontweight='bold', color='#1E293B', zorder=4)

        elif len(msg) == 3:
            # Self-Call: (at_id, text, dummy)
            at_id, text, _ = msg
            x = p_x_map[at_id]
            col = '#D97706'
            
            # Orthogonal bracket: right -> down -> left
            bracket_w = 0.6
            bracket_h = 0.25
            ax.plot([x, x + bracket_w, x + bracket_w, x], 
                    [msg_y, msg_y, msg_y - bracket_h, msg_y - bracket_h], color=col, lw=1.6, zorder=2)
            ax.annotate('', xy=(x, msg_y - bracket_h), xytext=(x + 0.1, msg_y - bracket_h),
                        arrowprops=dict(arrowstyle="->", color=col, lw=1.6), zorder=2)

            # Self call text box
            pill = patches.FancyBboxPatch((x + bracket_w + 0.1, msg_y - bracket_h/2 - 0.15), 3.2, 0.32,
                                          boxstyle="round,pad=0.05", fc='#FEF3C7', ec='#F59E0B', lw=1, zorder=3)
            ax.add_patch(pill)
            num_str = f"[{i+1}] "
            ax.text(x + bracket_w + 0.2, msg_y - bracket_h/2 + 0.01, num_str + text, 
                    va='center', fontsize=7.8, fontweight='bold', color='#92400E', zorder=4)

    plt.tight_layout()
    save_path = os.path.join(output_dir, save_filename)
    plt.savefig(save_path, dpi=300)
    plt.close()
    print("Regenerated:", save_path)


# =============================================================================
# 2. SEQUENCE 1: DIPOLE SIMULATION
# =============================================================================
def draw_seq_dipole():
    participants = [
        ("USER", "Kỹ sư NDT", "Client User", "#E0F2FE", "#0284C7"),
        ("UI", "Giao diện Web", "React + TS", "#F1F5F9", "#64748B"),
        ("API", "Backend API", "FastAPI Service", "#FEF3C7", "#D97706"),
        ("QUEUE", "Hàng đợi Task", "Redis + Celery", "#F3E8FF", "#A855F7"),
        ("WORKER", "Worker Tính toán", "NumPy Simulator", "#DCFCE7", "#16A34A")
    ]
    messages = [
        ("USER", "UI", "Nhập thông số (W, L, D, tần số 10kHz) & Bấm Run", True, False),
        ("UI", "API", "POST /api/v1/simulations/dipole (Parameters JSON)", True, False),
        ("API", "API", "Kiểm tra miền vật lý Al7075 & Schema Pydantic", False),
        ("API", "QUEUE", "Đẩy tác vụ vào hàng đợi calculate_dipole_job", True, False),
        ("API", "UI", "HTTP 202 Accepted {run_id: '...', status: 'QUEUED'}", False, True),
        ("UI", "API", "SSE /api/v1/runs/{id}/events (Lắng nghe tiến độ)", True, False),
        ("QUEUE", "WORKER", "Giao tác vụ cho Celery Worker rảnh rỗi", True, False),
        ("WORKER", "WORKER", "Tính phân bố Dipole Bz, delta-Bz ma trận 32x32", False),
        ("WORKER", "WORKER", "Xuất file ma trận tensor.npy & Heatmap.png", False),
        ("WORKER", "API", "Báo hoàn thành: Cập nhật status='SUCCESS'", True, False),
        ("API", "UI", "SSE Event: Gửi đường dẫn Heatmap & Metrics kết quả", False, True),
        ("UI", "USER", "Hiển thị ảnh Heatmap 32x32 và biểu đồ phân bố", False, True)
    ]
    draw_clean_sequence(
        "SƠ ĐỒ TUẦN TỰ: MÔ PHỎNG DIPOLE BÁN GIẢI TÍCH",
        "Luồng chạy bất đồng bộ giữa Web UI, FastAPI, Redis Queue và Worker tính toán ma trận 32x32",
        participants, messages, "2_Sequence_Mo_Phong_Dipole.png", height=9.5
    )


# =============================================================================
# 3. SEQUENCE 2: CNN CRACK ANALYSIS
# =============================================================================
def draw_seq_cnn():
    participants = [
        ("USER", "Kỹ sư NDT", "Client User", "#E0F2FE", "#0284C7"),
        ("UI", "Giao diện Web", "React + TS", "#F1F5F9", "#64748B"),
        ("API", "Backend API", "FastAPI Service", "#FEF3C7", "#D97706"),
        ("DB", "Database", "PostgreSQL", "#DCFCE7", "#16A34A"),
        ("CNN", "CNN Worker", "PyTorch Model", "#FCE7F3", "#DB2777")
    ]
    messages = [
        ("USER", "UI", "Kéo thả file CSV tín hiệu đo (32x32) & Bấm Phân Tích", True, False),
        ("UI", "API", "POST /api/v1/datasets/upload (Multipart CSV)", True, False),
        ("API", "API", "Kiểm tra shape (32x31/31x32), phát hiện sensor lỗi", False),
        ("API", "DB", "Lưu file thô vào Storage & Tạo bản ghi acquisitions", True, False),
        ("API", "CNN", "Gọi inference_crack_cnn(tensor_32x32, freq=10kHz)", True, False),
        ("CNN", "CNN", "Chuẩn hóa Scaler & Trích xuất đặc trưng bằng CNN", False),
        ("CNN", "CNN", "Head 1: Softmax (5 lớp) • Head 2: Regression (W,L,D)", False),
        ("CNN", "API", "Trả kết quả: {Shape: Rectangular (94%), W:2.1, L:5.0, D:1.0}", False, True),
        ("API", "DB", "Ghi kết quả phân tích vào bảng runs (status='SUCCESS')", True, False),
        ("API", "UI", "HTTP 200 OK: Trả về nhãn dự đoán, kích thước & độ tin cậy", False, True),
        ("UI", "USER", "Hiển thị Card kết quả nhận diện vết nứt & Heatmap đối chiếu", False, True)
    ]
    draw_clean_sequence(
        "SƠ ĐỒ TUẦN TỰ: TẢI FILE CSV & PHÂN TÍCH VẾT NỨT BẰNG MẠNG CNN",
        "Tiền xử lý tín hiệu mảng Hall 32x32, nạp mạng CNN phân loại biên dạng và hồi quy kích thước",
        participants, messages, "3_Sequence_Phan_Tich_CNN.png", height=9.5
    )


# =============================================================================
# 4. SEQUENCE 3: AGENTIC ORCHESTRATION
# =============================================================================
def draw_seq_agent():
    participants = [
        ("USER", "Kỹ sư NDT", "Client User", "#E0F2FE", "#0284C7"),
        ("CHAT", "Assistant Chat", "Web Panel", "#F1F5F9", "#64748B"),
        ("AGENT", "Agent Brain", "Ollama ReAct", "#EDE9FE", "#7C3AED"),
        ("TOOLS", "Tool Registry", "Backend Adapters", "#FEF3C7", "#D97706"),
        ("DB", "Database", "Tasks & State", "#DCFCE7", "#16A34A")
    ]
    messages = [
        ("USER", "CHAT", "User: 'Phân tích file specimen_01.csv rồi mô phỏng đối chứng'", True, False),
        ("CHAT", "AGENT", "POST /api/v1/agent-tasks {goal: ...}", True, False),
        ("AGENT", "DB", "Lập kế hoạch 3 bước & Lưu Checkpoint vào PostgreSQL", True, False),
        ("AGENT", "TOOLS", "[Bước 1] Gọi Tool: analyze_crack('specimen_01.csv')", True, False),
        ("TOOLS", "AGENT", "Trả kết quả: {Shape: Rectangular, W: 2.1, L: 5.0, D: 1.0}", False, True),
        ("AGENT", "TOOLS", "[Bước 2] Gọi Tool: run_dipole(W=2.1, L=5.0, D=1.0, freq=10)", True, False),
        ("TOOLS", "AGENT", "Mô phỏng xong: Trả về ma trận simulated_tensor_id", False, True),
        ("AGENT", "TOOLS", "[Bước 3] Gọi Tool: compute_metrics(measured, simulated)", True, False),
        ("TOOLS", "AGENT", "Đo sai số: {RMSE: 0.038, R2: 0.962 (ĐẠT TIÊU CHÍ)}", False, True),
        ("AGENT", "DB", "Cập nhật agent_tasks (status='COMPLETED')", True, False),
        ("AGENT", "CHAT", "Trả về kết luận: Khớp 96.2% với Dipole • Kèm link Báo cáo", False, True),
        ("CHAT", "USER", "Hiển thị hộp thoại kết luận, bảng sai số và nút Tải Báo Cáo", False, True)
    ]
    draw_clean_sequence(
        "SƠ ĐỒ TUẦN TỰ: TRỢ LÝ AGENTIC ĐIỀU PHỐI TỰ ĐỘNG & ĐỐI CHIẾU CHÉO",
        "Vòng lặp ReAct: Nhận mục tiêu -> Lập kế hoạch -> Gọi Tool CNN -> Chạy Dipole -> Đo RMSE -> Báo cáo",
        participants, messages, "4_Sequence_Tro_Ly_Agentic.png", height=9.8
    )


# =============================================================================
# 5. SƠ ĐỒ CƠ SỞ DỮ LIỆU ERD (CLEAN 3-COLUMN ARCHITECTURE)
# =============================================================================
def draw_erd():
    fig, ax = plt.subplots(figsize=(18, 12), dpi=300)
    ax.set_xlim(0, 18)
    ax.set_ylim(0, 12)
    ax.axis('off')
    fig.patch.set_facecolor('#FFFFFF')

    # Title
    ax.text(9.0, 11.5, "SƠ ĐỒ CƠ SỞ DỮ LIỆU QUAN HỆ (DATABASE ERD) CHO HỆ THỐNG ECT", 
            ha='center', va='center', fontsize=17, fontweight='bold', color='#0F172A')
    ax.text(9.0, 11.15, "Phân tách rõ ràng 3 phân hệ: Mẫu vật & Lần đo • Lịch sử chạy & File • Quản lý AI & Trợ lý Agentic", 
            ha='center', va='center', fontsize=10.5, color='#64748B')

    # Draw 3 Swimlane Backgrounds
    lane_width = 5.4
    lanes = [
        (0.6, "1. PHÂN HỆ MẪU VẬT & LẦN ĐO THỰC TẾ", "#F0FDFA", "#0D9488"),
        (6.3, "2. PHÂN HỆ THỰC THI & LƯU TRỮ ARTIFACTS", "#FFF7ED", "#EA580C"),
        (12.0, "3. PHÂN HỆ AI & BỘ NHỚ TRỢ LÝ AGENTIC", "#FAF5FF", "#7C3AED")
    ]
    for lx, ltitle, lbg, lborder in lanes:
        lane_box = patches.FancyBboxPatch((lx, 0.4), lane_width, 10.4, boxstyle="round,pad=0.1",
                                          fc=lbg, ec=lborder, lw=1.5, alpha=0.5)
        ax.add_patch(lane_box)
        ax.text(lx + lane_width/2, 10.5, ltitle, ha='center', va='center', 
                fontsize=9.5, fontweight='bold', color=lborder)

    # Function to draw clean entity cards
    def draw_table_card(x, y, w, title, rows, header_color):
        row_h = 0.28
        total_h = 0.45 + len(rows) * row_h
        # Header
        h_box = patches.FancyBboxPatch((x, y - 0.45), w, 0.45, boxstyle="round,pad=0.04",
                                       fc=header_color, ec=header_color)
        ax.add_patch(h_box)
        ax.text(x + w/2, y - 0.22, title, ha='center', va='center', fontsize=9, fontweight='bold', color='#FFFFFF')
        
        # Body
        b_box = patches.Rectangle((x, y - total_h), w, total_h - 0.45, fc='#FFFFFF', ec='#CBD5E1', lw=1.2)
        ax.add_patch(b_box)
        
        # Rows
        for i, (col_name, col_type, key_tag) in enumerate(rows):
            ry = y - 0.62 - i * row_h
            if key_tag == "PK":
                ax.text(x + 0.15, ry, "PK", fontsize=7.2, fontweight='bold', color='#DC2626')
            elif key_tag == "FK":
                ax.text(x + 0.15, ry, "FK", fontsize=7.2, fontweight='bold', color='#2563EB')
            else:
                ax.text(x + 0.15, ry, "•", fontsize=8, color='#94A3B8')

            ax.text(x + 0.55, ry, col_name, fontsize=8.0, fontweight='bold', color='#1E293B')
            ax.text(x + w - 0.15, ry, col_type, fontsize=7.5, style='italic', color='#64748B', ha='right')

        return (x, y, w, total_h)

    # COLUMN 1: SAMPLES & ACQUISITIONS
    draw_table_card(0.9, 10.0, 4.8, "PROJECTS (Dự án)", [
        ("id", "UUID", "PK"),
        ("name", "VARCHAR(100)", ""),
        ("description", "TEXT", ""),
        ("created_at", "DATETIME", "")
    ], "#0D9488")

    draw_table_card(0.9, 8.0, 4.8, "SPECIMENS (Mẫu nhôm Al7075)", [
        ("id", "UUID", "PK"),
        ("project_id", "UUID", "FK"),
        ("code", "VARCHAR(50) [UNIQUE]", ""),
        ("material", "VARCHAR(50) [Al7075]", ""),
        ("thickness_mm", "FLOAT [5.0 mm]", ""),
        ("actual_shape", "VARCHAR(20)", ""),
        ("actual_w / l / d", "FLOAT (mm)", "")
    ], "#0D9488")

    draw_table_card(0.9, 4.7, 4.8, "ACQUISITIONS (Tín hiệu đo ECT)", [
        ("id", "UUID", "PK"),
        ("specimen_id", "UUID", "FK"),
        ("frequency_hz", "INT (5k, 10k, 20k)", ""),
        ("grid_size", "VARCHAR(20) [32x32]", ""),
        ("pitch_mm", "FLOAT [0.78 mm]", ""),
        ("operator_type", "diff_x | diff_y", ""),
        ("raw_csv_artifact_id", "UUID", "FK"),
        ("measured_at", "DATETIME", "")
    ], "#0D9488")

    # COLUMN 2: EXECUTION & ARTIFACTS
    draw_table_card(6.6, 10.0, 4.8, "RUNS (Lịch sử các lần chạy)", [
        ("id", "UUID", "PK"),
        ("project_id", "UUID", "FK"),
        ("run_type", "dipole | cnn | diff | sweep", ""),
        ("initiated_via", "manual | agent", ""),
        ("agent_task_id", "UUID", "FK"),
        ("parameters_json", "JSONB", ""),
        ("results_json", "JSONB", ""),
        ("status", "QUEUED | SUCCESS | FAILED", ""),
        ("created_at", "DATETIME", "")
    ], "#EA580C")

    draw_table_card(6.6, 6.0, 4.8, "JOBS (Hàng đợi Celery Queue)", [
        ("id", "UUID", "PK"),
        ("run_id", "UUID", "FK"),
        ("queue_name", "cpu_queue | gpu_queue", ""),
        ("status", "queued | running | finished", ""),
        ("progress_pct", "INT (0 - 100%)", ""),
        ("error_message", "TEXT", ""),
        ("started_at", "DATETIME", "")
    ], "#EA580C")

    draw_table_card(6.6, 3.0, 4.8, "ARTIFACTS (Kho lưu trữ File & Tensor)", [
        ("id", "UUID", "PK"),
        ("run_id", "UUID", "FK"),
        ("name", "VARCHAR(255)", ""),
        ("file_type", "csv | heatmap_png | npy", ""),
        ("storage_path", "TEXT", ""),
        ("file_size_bytes", "BIGINT", ""),
        ("sha256_hash", "VARCHAR(64)", "")
    ], "#475569")

    # COLUMN 3: AI & AGENT MEMORY
    draw_table_card(12.3, 10.0, 4.8, "AGENT_CONVERSATIONS (Phiên chat)", [
        ("id", "UUID", "PK"),
        ("project_id", "UUID", "FK"),
        ("title", "VARCHAR(150)", ""),
        ("created_at", "DATETIME", "")
    ], "#7C3AED")

    draw_table_card(12.3, 7.8, 4.8, "AGENT_TASKS (Nhiệm vụ Agent)", [
        ("id", "UUID", "PK"),
        ("conversation_id", "UUID", "FK"),
        ("goal", "TEXT", ""),
        ("status", "planning | executing | done", ""),
        ("plan_json", "JSONB (Kế hoạch 3 bước)", ""),
        ("current_step", "INT", ""),
        ("budget_used", "INT (Số lần gọi tool)", "")
    ], "#7C3AED")

    draw_table_card(12.3, 4.4, 4.8, "AGENT_MESSAGES (Lịch sử hội thoại)", [
        ("id", "UUID", "PK"),
        ("conversation_id", "UUID", "FK"),
        ("role", "user | assistant | tool", ""),
        ("content", "TEXT", ""),
        ("created_at", "DATETIME", "")
    ], "#7C3AED")

    draw_table_card(12.3, 2.0, 4.8, "MODELS & MODEL_VERSIONS", [
        ("id", "UUID", "PK"),
        ("model_name", "CrackCNN | Diffusion_v1", ""),
        ("version", "VARCHAR(20) [v1.0]", ""),
        ("weights_artifact_id", "UUID", "FK"),
        ("metrics_json", "JSONB (F1, RMSE)", "")
    ], "#334155")

    # Clean Relationships (Connectors)
    # Between Col 1 tables
    ax.annotate('', xy=(3.3, 8.0), xytext=(3.3, 8.7), arrowprops=dict(arrowstyle="->", color='#0D9488', lw=1.5))
    ax.text(3.4, 8.35, "1 - N", fontsize=7.5, fontweight='bold', color='#0D9488')

    ax.annotate('', xy=(3.3, 4.7), xytext=(3.3, 5.8), arrowprops=dict(arrowstyle="->", color='#0D9488', lw=1.5))
    ax.text(3.4, 5.25, "1 - N", fontsize=7.5, fontweight='bold', color='#0D9488')

    # Between Col 2 tables
    ax.annotate('', xy=(9.0, 6.0), xytext=(9.0, 6.8), arrowprops=dict(arrowstyle="->", color='#EA580C', lw=1.5))
    ax.text(9.1, 6.4, "1 - N", fontsize=7.5, fontweight='bold', color='#EA580C')

    ax.annotate('', xy=(9.0, 3.0), xytext=(9.0, 3.8), arrowprops=dict(arrowstyle="->", color='#EA580C', lw=1.5))
    ax.text(9.1, 3.4, "1 - N", fontsize=7.5, fontweight='bold', color='#EA580C')

    # Between Col 3 tables
    ax.annotate('', xy=(14.7, 7.8), xytext=(14.7, 8.6), arrowprops=dict(arrowstyle="->", color='#7C3AED', lw=1.5))
    ax.text(14.8, 8.2, "1 - N", fontsize=7.5, fontweight='bold', color='#7C3AED')

    ax.annotate('', xy=(14.7, 4.4), xytext=(14.7, 5.3), arrowprops=dict(arrowstyle="->", color='#7C3AED', lw=1.5))
    ax.text(14.8, 4.85, "1 - N", fontsize=7.5, fontweight='bold', color='#7C3AED')

    # Cross-Lane Relations (Orthogonal)
    # Projects -> Runs (Col 1 to Col 2)
    ax.annotate('', xy=(6.6, 9.4), xytext=(5.7, 9.4), arrowprops=dict(arrowstyle="->", color='#64748B', lw=1.5))
    ax.text(6.15, 9.55, "1 - N", ha='center', fontsize=7.5, fontweight='bold', color='#64748B')

    # Agent_Tasks -> Runs (Col 3 to Col 2)
    ax.annotate('', xy=(11.4, 8.5), xytext=(12.3, 8.5), arrowprops=dict(arrowstyle="->", color='#7C3AED', ls='--', lw=1.5))
    ax.text(11.85, 8.65, "Kích hoạt", ha='center', fontsize=7.5, fontweight='bold', color='#7C3AED')

    plt.tight_layout()
    save_path = os.path.join(output_dir, "5_ERD_Database_He_Thong.png")
    plt.savefig(save_path, dpi=300)
    plt.close()
    print("Regenerated:", save_path)


if __name__ == "__main__":
    print("Redrawing all 5 diagrams with clean, professional layouts...")
    draw_use_case()
    draw_seq_dipole()
    draw_seq_cnn()
    draw_seq_agent()
    draw_erd()
    print("All 5 diagrams successfully redrawn and saved!")
