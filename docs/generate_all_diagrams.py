import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.lines import Line2D

# Setup output directory
output_dir = r"C:\Users\Admin\Documents\DATN\docs\images"
os.makedirs(output_dir, exist_ok=True)

plt.rcParams['font.sans-serif'] = 'Segoe UI'
plt.rcParams['font.family'] = 'sans-serif'

# -----------------------------------------------------------------------------
# 1. USE CASE DIAGRAM
# -----------------------------------------------------------------------------
def draw_use_case():
    fig, ax = plt.subplots(figsize=(16, 11), dpi=300)
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 11)
    ax.axis('off')

    # Background
    fig.patch.set_facecolor('#F8FAFC')
    ax.set_facecolor('#F8FAFC')

    # Title
    ax.text(8, 10.4, "SƠ ĐỒ USE CASE TỔNG THỂ HỆ THỐNG WEBSITE ECT & TRỢ LÝ AGENTIC", 
            ha='center', va='center', fontsize=18, fontweight='bold', color='#1E293B')
    ax.text(8, 10.0, "Đồ án: Mô phỏng Dipole • Sinh ảnh Diffusion • Phân tích vết nứt ECT • Trợ lý AI", 
            ha='center', va='center', fontsize=11, color='#64748B')

    # Boundary Box (System Boundary)
    system_rect = patches.FancyBboxPatch((3.8, 0.6), 8.4, 9.0, boxstyle="round,pad=0.2",
                                         facecolor='#FFFFFF', edgecolor='#CBD5E1', linewidth=2)
    ax.add_patch(system_rect)
    ax.text(8.0, 9.35, "HỆ THỐNG WEBSITE ECT", ha='center', va='center', 
            fontsize=13, fontweight='bold', color='#0F172A', 
            bbox=dict(boxstyle="round,pad=0.3", fc="#E2E8F0", ec="#94A3B8"))

    # Actors
    # Actor 1: Human User (Left)
    ax.plot([1.8, 1.8], [6.2, 5.2], color='#0284C7', lw=3) # Body
    circle1 = patches.Circle((1.8, 6.6), 0.35, fc='#BAE6FD', ec='#0284C7', lw=2)
    ax.add_patch(circle1)
    ax.plot([1.2, 2.4], [5.9, 5.9], color='#0284C7', lw=3) # Arms
    ax.plot([1.8, 1.3], [5.2, 4.4], color='#0284C7', lw=3) # Leg L
    ax.plot([1.8, 2.3], [5.2, 4.4], color='#0284C7', lw=3) # Leg R
    ax.text(1.8, 3.9, "KỸ SƯ NDT / NGƯỜI DÙNG\n(Thao tác trực tiếp)", ha='center', va='center', 
            fontsize=10, fontweight='bold', color='#0369A1')

    # Actor 2: AI Agent (Right)
    # Robot Head
    robot_rect = patches.FancyBboxPatch((13.7, 6.2), 0.8, 0.7, boxstyle="round,pad=0.1",
                                        facecolor='#DDD6FE', edgecolor='#7C3AED', lw=2)
    ax.add_patch(robot_rect)
    # Eyes
    ax.plot([13.9, 14.3], [6.6, 6.6], 'o', color='#7C3AED', markersize=5)
    # Antenna
    ax.plot([14.1, 14.1], [7.0, 7.3], color='#7C3AED', lw=2)
    ax.plot([14.1], [7.3], 'o', color='#7C3AED', markersize=4)
    # Body
    robot_body = patches.FancyBboxPatch((13.6, 5.0), 1.0, 1.0, boxstyle="round,pad=0.1",
                                        facecolor='#EDE9FE', edgecolor='#7C3AED', lw=2)
    ax.add_patch(robot_body)
    ax.text(14.1, 4.4, "TRỢ LÝ AI AGENTIC\n(Tự động điều phối)", ha='center', va='center', 
            fontsize=10, fontweight='bold', color='#6D28D9')

    # Use cases definitions: (x, y, text, category, color)
    use_cases = [
        # Quản lý dữ liệu
        (5.8, 8.4, "UC01: Upload & Tiền xử lý CSV 32x32", "#EFF6FF", "#1D4ED8"),
        (5.8, 7.4, "UC02: Trực quan hóa Heatmap & Bù NaN", "#EFF6FF", "#1D4ED8"),
        (5.8, 6.4, "UC03: Quản lý Dataset & Gán nhãn", "#EFF6FF", "#1D4ED8"),
        
        # Mô phỏng & Sinh dữ liệu
        (5.8, 5.2, "UC04: Chạy Mô phỏng Dipole bán giải tích", "#FEF3C7", "#B45309"),
        (10.2, 5.2, "UC05: Quét tham số Sweep W/L/D", "#FEF3C7", "#B45309"),
        (5.8, 4.0, "UC06: Sinh ảnh từ trường bằng Diffusion", "#FEF3C7", "#B45309"),

        # Phân tích & Đối chiếu
        (10.2, 7.4, "UC07: Phân loại biên dạng vết nứt (CNN)", "#F0FDF4", "#15803D"),
        (10.2, 6.4, "UC08: Hồi quy kích thước W, L, D", "#F0FDF4", "#15803D"),
        (10.2, 4.0, "UC09: Đối chiếu Tín hiệu Đo vs Dipole", "#F0FDF4", "#15803D"),

        # Trợ lý & Báo cáo
        (10.2, 8.4, "UC10: Giao mục tiêu qua Assistant Chat", "#FAF5FF", "#7E22CE"),
        (8.0, 2.7, "UC11: Phê duyệt kế hoạch (Human-in-the-loop)", "#FAF5FF", "#7E22CE"),
        (8.0, 1.5, "UC12: Tự động xuất Báo cáo PDF/Word", "#FAF5FF", "#7E22CE")
    ]

    for x, y, label, bg, border in use_cases:
        ellipse = patches.FancyBboxPatch((x-1.8, y-0.35), 3.6, 0.7, boxstyle="round,pad=0.2",
                                         facecolor=bg, edgecolor=border, lw=1.5)
        ax.add_patch(ellipse)
        ax.text(x, y, label, ha='center', va='center', fontsize=8.5, fontweight='bold', color='#1E293B')

    # Draw Connections from User (Left)
    user_conns = [(5.8, 8.4), (5.8, 7.4), (5.8, 6.4), (5.8, 5.2), (10.2, 5.2), (5.8, 4.0), (10.2, 7.4), (10.2, 6.4), (10.2, 8.4), (8.0, 2.7)]
    for tx, ty in user_conns:
        ax.plot([2.5, tx - 1.8], [5.6, ty], color='#94A3B8', linestyle='-', lw=1.2, alpha=0.8)

    # Draw Connections from Agent (Right)
    agent_conns = [(10.2, 5.2), (10.2, 7.4), (10.2, 6.4), (10.2, 4.0), (8.0, 1.5)]
    for tx, ty in agent_conns:
        ax.annotate('', xy=(tx + 1.8, ty), xytext=(13.5, 5.6),
                    arrowprops=dict(arrowstyle="->", color='#8B5CF6', linestyle='--', lw=1.4))

    # Notes & Legend
    ax.text(8.0, 0.2, "Đường nét liền: Tương tác người dùng • Đường nét đứt: Trợ lý AI tự động gọi",
            ha='center', va='center', fontsize=9.5, style='italic', color='#64748B')

    plt.tight_layout()
    save_path = os.path.join(output_dir, "1_Use_Case_Tong_The.png")
    plt.savefig(save_path, dpi=300)
    plt.close()
    print("Saved:", save_path)

# -----------------------------------------------------------------------------
# 2. SEQUENCE DIAGRAM: DIPOLE SIMULATION
# -----------------------------------------------------------------------------
def draw_seq_dipole():
    fig, ax = plt.subplots(figsize=(15, 10), dpi=300)
    ax.set_xlim(0, 15)
    ax.set_ylim(0, 10)
    ax.axis('off')
    fig.patch.set_facecolor('#FFFFFF')

    # Title
    ax.text(7.5, 9.6, "SƠ ĐỒ TUẦN TỰ: MÔ PHỎNG DIPOLE BÁN GIẢI TÍCH", ha='center', va='center', 
            fontsize=16, fontweight='bold', color='#1E293B')
    ax.text(7.5, 9.25, "Luồng chạy bất đồng bộ qua FastAPI, Redis Queue và Worker tính toán NumPy", 
            ha='center', va='center', fontsize=10, color='#64748B')

    # Lifeline participants
    participants = [
        (1.5, " Kỹ sư NDT\n(User)", "#E0F2FE", "#0284C7"),
        (4.5, " Web UI\n(React)", "#F1F5F9", "#475569"),
        (7.5, " API Backend\n(FastAPI)", "#FEF3C7", "#D97706"),
        (10.5, " Database\n(PostgreSQL)", "#DCFCE7", "#16A34A"),
        (13.5, " Simulation Worker\n(NumPy / Celery)", "#EDE9FE", "#7C3AED")
    ]

    for x, label, bg, border in participants:
        box = patches.FancyBboxPatch((x-1.1, 8.2), 2.2, 0.7, boxstyle="round,pad=0.1",
                                     facecolor=bg, edgecolor=border, lw=2)
        ax.add_patch(box)
        ax.text(x, 8.55, label, ha='center', va='center', fontsize=9, fontweight='bold', color='#0F172A')
        # Lifeline vertical dash
        ax.plot([x, x], [8.1, 0.8], color='#CBD5E1', linestyle='--', lw=1.5)

    # Sequence Messages
    steps = [
        (1, 1.5, 4.5, 7.8, "1. Nhập tham số (W, L, D, tần số 10kHz) & Bấm Run", "#1E293B", True),
        (2, 4.5, 7.5, 7.2, "2. POST /api/v1/simulations/dipole (JSON)", "#2563EB", True),
        (3, 7.5, 10.5, 6.6, "3. INSERT INTO runs (status='QUEUED')", "#16A34A", True),
        (4, 7.5, 13.5, 6.0, "4. Push task calculate_dipole(run_id)", "#7C3AED", True),
        (5, 7.5, 4.5, 5.4, "5. HTTP 202 Accepted {run_id, status: 'QUEUED'}", "#D97706", False),
        (6, 4.5, 7.5, 4.8, "6. SSE subscribe /runs/{id}/events", "#475569", True),
        (7, 13.5, 10.5, 4.2, "7. UPDATE runs SET status='RUNNING'", "#16A34A", True),
        (8, 13.5, 13.5, 3.6, "8. [Self] Tính ma trận Bz 32x32 & Tạo Heatmap PNG", "#7C3AED", False),
        (9, 13.5, 10.5, 3.0, "9. INSERT INTO artifacts & UPDATE runs (SUCCESS)", "#16A34A", True),
        (10, 7.5, 4.5, 2.4, "10. SSE Broadcast: {status: 'SUCCESS', heatmap_url}", "#2563EB", False),
        (11, 4.5, 1.5, 1.8, "11. Render Heatmap 32x32 trực quan & cho phép tải CSV", "#0284C7", False)
    ]

    for num, x1, x2, y, text, col, is_forward in steps:
        if x1 == x2: # Self call
            arc = patches.Arc((x1+0.4, y), 0.8, 0.4, angle=0, theta1=270, theta2=90, color=col, lw=1.8)
            ax.add_patch(arc)
            ax.annotate('', xy=(x1, y-0.2), xytext=(x1+0.4, y-0.2),
                        arrowprops=dict(arrowstyle="->", color=col, lw=1.8))
            ax.text(x1+0.9, y, text, va='center', fontsize=8.5, fontweight='bold', color=col)
        else:
            style = "->" if is_forward else "-->"
            ls = '-' if is_forward else '--'
            ax.annotate('', xy=(x2, y), xytext=(x1, y),
                        arrowprops=dict(arrowstyle="->", color=col, linestyle=ls, lw=1.8))
            mid_x = (x1 + x2) / 2
            ax.text(mid_x, y + 0.15, text, ha='center', va='bottom', fontsize=8.5, fontweight='bold', color=col)

    plt.tight_layout()
    save_path = os.path.join(output_dir, "2_Sequence_Mo_Phong_Dipole.png")
    plt.savefig(save_path, dpi=300)
    plt.close()
    print("Saved:", save_path)

# -----------------------------------------------------------------------------
# 3. SEQUENCE DIAGRAM: CNN CRACK ANALYSIS
# -----------------------------------------------------------------------------
def draw_seq_cnn():
    fig, ax = plt.subplots(figsize=(15, 10), dpi=300)
    ax.set_xlim(0, 15)
    ax.set_ylim(0, 10)
    ax.axis('off')
    fig.patch.set_facecolor('#FFFFFF')

    # Title
    ax.text(7.5, 9.6, "SƠ ĐỒ TUẦN TỰ: TẢI CSV & PHÂN TÍCH VẾT NỨT BẰNG MẠNG CNN", 
            ha='center', va='center', fontsize=16, fontweight='bold', color='#1E293B')
    ax.text(7.5, 9.25, "Xử lý định dạng CSV 32x32, nạp mạng CNN phân loại 5 biên dạng & hồi quy W, L, D", 
            ha='center', va='center', fontsize=10, color='#64748B')

    participants = [
        (1.5, " Kỹ sư NDT\n(User)", "#E0F2FE", "#0284C7"),
        (4.5, " Web UI\n(React)", "#F1F5F9", "#475569"),
        (7.5, " API Backend\n(FastAPI)", "#FEF3C7", "#D97706"),
        (10.5, " Database\n(PostgreSQL)", "#DCFCE7", "#16A34A"),
        (13.5, " CNN Worker\n(PyTorch Inference)", "#FCE7F3", "#DB2777")
    ]

    for x, label, bg, border in participants:
        box = patches.FancyBboxPatch((x-1.1, 8.2), 2.2, 0.7, boxstyle="round,pad=0.1",
                                     facecolor=bg, edgecolor=border, lw=2)
        ax.add_patch(box)
        ax.text(x, 8.55, label, ha='center', va='center', fontsize=9, fontweight='bold', color='#0F172A')
        ax.plot([x, x], [8.1, 0.8], color='#CBD5E1', linestyle='--', lw=1.5)

    steps = [
        (1, 1.5, 4.5, 7.8, "1. Kéo thả file CSV tín hiệu đo (32x32) & Bấm Phân Tích", "#1E293B", True),
        (2, 4.5, 7.5, 7.2, "2. POST /api/v1/datasets/upload (Multipart CSV)", "#2563EB", True),
        (3, 7.5, 7.5, 6.6, "3. [Self] Kiểm tra shape (32x31 / 31x32), kiểm tra NaN", "#D97706", False),
        (4, 7.5, 10.5, 6.0, "4. Lưu file gốc vào Artifacts & INSERT acquisitions", "#16A34A", True),
        (5, 7.5, 13.5, 5.4, "5. Dispatch predict_crack(tensor, freq=10kHz)", "#DB2777", True),
        (6, 13.5, 13.5, 4.7, "6. [Self] Chuẩn hóa Scaler & Forward Pass CNN", "#DB2777", False),
        (7, 13.5, 7.5, 4.0, "7. Trả về: {Shape: Rectangular (94%), W: 2.1mm, L: 5.0mm, D: 1.0mm}", "#DB2777", False),
        (8, 7.5, 10.5, 3.3, "8. INSERT INTO runs (run_type='cnn_analysis', results=...)", "#16A34A", True),
        (9, 7.5, 4.5, 2.6, "9. HTTP 200 OK {predictions, confidence, run_id}", "#2563EB", False),
        (10, 4.5, 1.5, 1.8, "10. Hiển thị Card kết quả: Biên dạng, Kích thước W/L/D & Heatmap", "#0284C7", False)
    ]

    for num, x1, x2, y, text, col, is_forward in steps:
        if x1 == x2:
            arc = patches.Arc((x1+0.4, y), 0.8, 0.4, angle=0, theta1=270, theta2=90, color=col, lw=1.8)
            ax.add_patch(arc)
            ax.annotate('', xy=(x1, y-0.2), xytext=(x1+0.4, y-0.2),
                        arrowprops=dict(arrowstyle="->", color=col, lw=1.8))
            ax.text(x1+0.9, y, text, va='center', fontsize=8.5, fontweight='bold', color=col)
        else:
            ls = '-' if is_forward else '--'
            ax.annotate('', xy=(x2, y), xytext=(x1, y),
                        arrowprops=dict(arrowstyle="->", color=col, linestyle=ls, lw=1.8))
            mid_x = (x1 + x2) / 2
            ax.text(mid_x, y + 0.15, text, ha='center', va='bottom', fontsize=8.5, fontweight='bold', color=col)

    plt.tight_layout()
    save_path = os.path.join(output_dir, "3_Sequence_Phan_Tich_CNN.png")
    plt.savefig(save_path, dpi=300)
    plt.close()
    print("Saved:", save_path)

# -----------------------------------------------------------------------------
# 4. SEQUENCE DIAGRAM: AGENTIC ORCHESTRATION
# -----------------------------------------------------------------------------
def draw_seq_agent():
    fig, ax = plt.subplots(figsize=(15, 10), dpi=300)
    ax.set_xlim(0, 15)
    ax.set_ylim(0, 10)
    ax.axis('off')
    fig.patch.set_facecolor('#FFFFFF')

    # Title
    ax.text(7.5, 9.6, "SƠ ĐỒ TUẦN TỰ: TRỢ LÝ AGENTIC ĐIỀU PHỐI TỰ ĐỘNG & ĐỐI CHIẾU CHÉO", 
            ha='center', va='center', fontsize=16, fontweight='bold', color='#1E293B')
    ax.text(7.5, 9.25, "Vòng lặp ReAct: Nhận mục tiêu -> Lập kế hoạch -> Gọi Tool CNN -> Chạy Dipole -> Đo RMSE -> Báo cáo", 
            ha='center', va='center', fontsize=10, color='#64748B')

    participants = [
        (1.5, " Kỹ sư NDT\n(User)", "#E0F2FE", "#0284C7"),
        (4.5, " Assistant Chat\n(Frontend)", "#F1F5F9", "#475569"),
        (7.5, " Agent Brain\n(Ollama / ReAct)", "#EDE9FE", "#7C3AED"),
        (10.5, " Tool Registry\n(CNN, Dipole, Calc)", "#FEF3C7", "#D97706"),
        (13.5, " Database\n(Tasks & Checkpoints)", "#DCFCE7", "#16A34A")
    ]

    for x, label, bg, border in participants:
        box = patches.FancyBboxPatch((x-1.1, 8.2), 2.2, 0.7, boxstyle="round,pad=0.1",
                                     facecolor=bg, edgecolor=border, lw=2)
        ax.add_patch(box)
        ax.text(x, 8.55, label, ha='center', va='center', fontsize=9, fontweight='bold', color='#0F172A')
        ax.plot([x, x], [8.1, 0.8], color='#CBD5E1', linestyle='--', lw=1.5)

    steps = [
        (1, 1.5, 4.5, 7.8, "1. User: 'Phân tích file specimen_01.csv rồi mô phỏng đối chứng'", "#1E293B", True),
        (2, 4.5, 7.5, 7.2, "2. POST /api/v1/agent-tasks {goal: ...}", "#7C3AED", True),
        (3, 7.5, 13.5, 6.6, "3. Lập kế hoạch 3 bước & INSERT agent_plans", "#16A34A", True),
        (4, 7.5, 10.5, 6.0, "4. [Bước 1] Call Tool: analyze_crack('specimen_01.csv')", "#D97706", True),
        (5, 10.5, 7.5, 5.4, "5. Tool trả về: {shape: 'Rectangular', W: 2.1, L: 5.0, D: 1.0}", "#D97706", False),
        (6, 7.5, 10.5, 4.7, "6. [Bước 2] Call Tool: run_dipole(W=2.1, L=5.0, D=1.0)", "#D97706", True),
        (7, 10.5, 7.5, 4.1, "7. Tool trả về: {simulated_matrix_id: 'art_99'}", "#D97706", False),
        (8, 7.5, 10.5, 3.4, "8. [Bước 3] Call Tool: compute_rmse(measured, simulated)", "#D97706", True),
        (9, 10.5, 7.5, 2.8, "9. Tool trả về: {RMSE: 0.038, R2: 0.962 (ĐẠT TIÊU CHÍ)}", "#16A34A", False),
        (10, 7.5, 13.5, 2.2, "10. UPDATE agent_tasks (status='COMPLETED')", "#16A34A", True),
        (11, 7.5, 4.5, 1.6, "11. Trả về kết luận đối chứng & Đính kèm link Báo cáo PDF", "#7C3AED", False),
        (12, 4.5, 1.5, 1.0, "12. Hiển thị hội thoại hoàn tất, bảng sai số & Nút tải báo cáo", "#0284C7", False)
    ]

    for num, x1, x2, y, text, col, is_forward in steps:
        ls = '-' if is_forward else '--'
        ax.annotate('', xy=(x2, y), xytext=(x1, y),
                    arrowprops=dict(arrowstyle="->", color=col, linestyle=ls, lw=1.8))
        mid_x = (x1 + x2) / 2
        ax.text(mid_x, y + 0.15, text, ha='center', va='bottom', fontsize=8.5, fontweight='bold', color=col)

    plt.tight_layout()
    save_path = os.path.join(output_dir, "4_Sequence_Tro_Ly_Agentic.png")
    plt.savefig(save_path, dpi=300)
    plt.close()
    print("Saved:", save_path)

# -----------------------------------------------------------------------------
# 5. ERD DATABASE DIAGRAM
# -----------------------------------------------------------------------------
def draw_erd():
    fig, ax = plt.subplots(figsize=(18, 12), dpi=300)
    ax.set_xlim(0, 18)
    ax.set_ylim(0, 12)
    ax.axis('off')
    fig.patch.set_facecolor('#F8FAFC')

    # Title
    ax.text(9, 11.5, "SƠ ĐỒ CƠ SỞ DỮ LIỆU QUAN HỆ (DATABASE ERD) CHO HỆ THỐNG ECT", 
            ha='center', va='center', fontsize=18, fontweight='bold', color='#1E293B')
    ax.text(9, 11.1, "Thiết kế chuẩn hóa cho Quản lý Mẫu vật, Lần đo ECT, Lịch sử Chạy, File Nhị phân và Bộ nhớ AI Agent", 
            ha='center', va='center', fontsize=11, color='#64748B')

    # Helper function to draw an entity table box
    def draw_entity(x, y, title, fields, width=3.2, header_col="#1E40AF"):
        height = 0.5 + len(fields) * 0.28
        # Header box
        header = patches.FancyBboxPatch((x, y - 0.5), width, 0.5, boxstyle="round,pad=0.05",
                                        facecolor=header_col, edgecolor=header_col, lw=1)
        ax.add_patch(header)
        ax.text(x + width/2, y - 0.25, title, ha='center', va='center', 
                fontsize=9.5, fontweight='bold', color='#FFFFFF')
        
        # Body box
        body = patches.Rectangle((x, y - height), width, height - 0.5, 
                                 facecolor='#FFFFFF', edgecolor='#CBD5E1', lw=1.5)
        ax.add_patch(body)
        
        # Fields
        for i, (f_name, f_type, is_pk, is_fk) in enumerate(fields):
            curr_y = y - 0.7 - i * 0.28
            tag = " PK " if is_pk else (" FK " if is_fk else "   ")
            tag_color = "#DC2626" if is_pk else ("#2563EB" if is_fk else "#475569")
            ax.text(x + 0.15, curr_y, tag, fontsize=7.5, fontweight='bold', color=tag_color)
            ax.text(x + 0.7, curr_y, f_name, fontsize=8, fontweight='bold', color='#1E293B')
            ax.text(x + width - 0.15, curr_y, f_type, fontsize=7.5, style='italic', color='#64748B', ha='right')
        
        return (x + width/2, y - height/2)

    # 1. USERS & PROJECTS
    draw_entity(0.6, 10.5, "USERS", [
        ("id", "UUID", True, False),
        ("username", "VARCHAR(50)", False, False),
        ("email", "VARCHAR(100)", False, False),
        ("role", "VARCHAR(20)", False, False),
        ("created_at", "DATETIME", False, False)
    ], header_col="#1E40AF")

    draw_entity(0.6, 7.5, "PROJECTS", [
        ("id", "UUID", True, False),
        ("owner_id", "UUID", False, True),
        ("name", "VARCHAR(100)", False, False),
        ("description", "TEXT", False, False),
        ("created_at", "DATETIME", False, False)
    ], header_col="#1E40AF")

    # 2. SPECIMENS & ACQUISITIONS
    draw_entity(4.8, 10.5, "SPECIMENS (Mẫu nhôm)", [
        ("id", "UUID", True, False),
        ("project_id", "UUID", False, True),
        ("code", "VARCHAR(50)", False, False),
        ("material", "VARCHAR(50)", False, False),
        ("thickness_mm", "FLOAT", False, False),
        ("actual_shape", "VARCHAR(20)", False, False),
        ("actual_w", "FLOAT", False, False),
        ("actual_l", "FLOAT", False, False),
        ("actual_d", "FLOAT", False, False)
    ], width=3.4, header_col="#0D9488")

    draw_entity(4.8, 6.2, "ACQUISITIONS (Lần đo)", [
        ("id", "UUID", True, False),
        ("specimen_id", "UUID", False, True),
        ("frequency_hz", "INT (5k,10k,20k)", False, False),
        ("grid_size", "VARCHAR(20)", False, False),
        ("pitch_mm", "FLOAT (0.78)", False, False),
        ("operator_type", "VARCHAR(20)", False, False),
        ("raw_csv_artifact_id", "UUID", False, True),
        ("measured_at", "DATETIME", False, False)
    ], width=3.4, header_col="#0D9488")

    # 3. RUNS, JOBS & ARTIFACTS
    draw_entity(9.2, 10.5, "RUNS (Lần chạy)", [
        ("id", "UUID", True, False),
        ("project_id", "UUID", False, True),
        ("model_version_id", "UUID", False, True),
        ("run_type", "VARCHAR(30)", False, False),
        ("initiated_via", "manual | agent", False, False),
        ("agent_task_id", "UUID", False, True),
        ("parameters_json", "JSONB", False, False),
        ("results_json", "JSONB", False, False),
        ("status", "VARCHAR(20)", False, False),
        ("created_at", "DATETIME", False, False)
    ], width=3.5, header_col="#EA580C")

    draw_entity(9.2, 6.0, "JOBS (Hàng đợi)", [
        ("id", "UUID", True, False),
        ("run_id", "UUID", False, True),
        ("queue_name", "cpu | gpu", False, False),
        ("status", "queued | run...", False, False),
        ("progress_pct", "INT", False, False),
        ("error_message", "TEXT", False, False),
        ("started_at", "DATETIME", False, False)
    ], width=3.5, header_col="#EA580C")

    draw_entity(9.2, 2.5, "ARTIFACTS (Kho file)", [
        ("id", "UUID", True, False),
        ("run_id", "UUID", False, True),
        ("name", "VARCHAR(255)", False, False),
        ("file_type", "csv | png | npy", False, False),
        ("storage_path", "TEXT", False, False),
        ("file_size_bytes", "BIGINT", False, False),
        ("sha256_hash", "VARCHAR(64)", False, False)
    ], width=3.5, header_col="#475569")

    # 4. AGENT SYSTEM
    draw_entity(13.8, 10.5, "AGENT_CONVERSATIONS", [
        ("id", "UUID", True, False),
        ("project_id", "UUID", False, True),
        ("title", "VARCHAR(150)", False, False),
        ("created_at", "DATETIME", False, False)
    ], width=3.6, header_col="#7C3AED")

    draw_entity(13.8, 8.0, "AGENT_TASKS", [
        ("id", "UUID", True, False),
        ("conversation_id", "UUID", False, True),
        ("goal", "TEXT", False, False),
        ("status", "VARCHAR(30)", False, False),
        ("plan_json", "JSONB", False, False),
        ("current_step", "INT", False, False),
        ("budget_used", "INT", False, False),
        ("updated_at", "DATETIME", False, False)
    ], width=3.6, header_col="#7C3AED")

    draw_entity(13.8, 4.4, "AGENT_MESSAGES", [
        ("id", "UUID", True, False),
        ("conversation_id", "UUID", False, True),
        ("role", "user | assistant...", False, False),
        ("content", "TEXT", False, False),
        ("created_at", "DATETIME", False, False)
    ], width=3.6, header_col="#7C3AED")

    # Connectors lines
    def connect(x1, y1, x2, y2, color="#94A3B8"):
        ax.plot([x1, x2], [y1, y2], color=color, lw=1.5, linestyle='-')

    # Users -> Projects
    connect(2.2, 8.8, 2.2, 7.5)
    # Projects -> Specimens
    connect(3.8, 6.0, 4.8, 7.5)
    # Specimens -> Acquisitions
    connect(6.5, 7.2, 6.5, 6.2)
    # Projects -> Runs
    connect(3.8, 5.0, 9.2, 8.0)
    # Runs -> Jobs
    connect(10.9, 7.2, 10.9, 6.0)
    # Runs -> Artifacts
    connect(10.9, 3.8, 10.9, 2.5)
    # Projects -> Agent_Conversations
    connect(3.8, 7.0, 13.8, 9.5)
    # Agent_Conversations -> Agent_Tasks
    connect(15.6, 9.0, 15.6, 8.0)
    # Agent_Tasks -> Runs
    connect(13.8, 6.5, 12.7, 7.0)

    plt.tight_layout()
    save_path = os.path.join(output_dir, "5_ERD_Database_He_Thong.png")
    plt.savefig(save_path, dpi=300)
    plt.close()
    print("Saved:", save_path)

if __name__ == "__main__":
    print("Rendering all 5 diagrams...")
    draw_use_case()
    draw_seq_dipole()
    draw_seq_cnn()
    draw_seq_agent()
    draw_erd()
    print("All diagrams generated successfully!")
