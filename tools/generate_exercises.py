# -*- coding: utf-8 -*-
"""Generate 30 exercises (10 easy, 10 medium, 10 hard) for each algorithm lesson."""
import re
from pathlib import Path

ROOT = Path(r"D:\HyperHub - HSG Tin")

EASY_TITLES = ['Cài đặt cơ bản', 'Trace code', 'Điền khuyết', 'So sánh', 'Áp dụng trực tiếp', 'Biến thể đơn giản', 'Debug', 'Độ phức tạp', 'Kiểm tra hiểu', 'Mở rộng']
EASY_TASKS = [
    "Viết hàm {algo}_basic thực hiện {basic}",
    "Trace code: cho đoạn code mẫu {algo}, hãy viết ra kết quả",
    "Hoàn thiện hàm {algo} đã cho sẵn",
    "So sánh 2 cách giải cho {topic}",
    "Áp dụng thuật toán {algo} trực tiếp",
    "Viết biến thể đơn giản của {algo}",
    "Sửa lỗi trong code {algo} cho trước",
    "Tính độ phức tạp O() của {algo}",
    "Giải thích bước quan trọng của {algo}",
    "Mở rộng {algo} cho trường hợp mới"
]
EASY_HINTS = [
    "Cài đặt theo định nghĩa",
    "Chạy thủ từng bước",
    "Hoàn thiện code còn thiếu",
    "So sánh ưu nhược điểm",
    "Áp dụng trực tiếp thuật toán",
    "Thay đổi tham số nhỏ",
    "Sửa try/except",
    "Đếm phép toán",
    "Giải thích logic",
    "Mở rộng tham số"
]

MED_TITLES = ['Cài đặt đầy đủ', 'Biến thể', 'Tối ưu hóa', 'Kết hợp', 'Trace phức tạp', 'Biến thể ngược', 'Giới hạn lớn', 'So sánh thực tế', 'Mở rộng', 'Áp dụng thực tế']
MED_TASKS = [
    "Viết chương trình hoàn chỉnh cho {algo}",
    "Sửa thuật toán {algo}",
    "Cải tiến độ phức tạp của {algo}",
    "Kết hợp {algo} với thuật toán khác",
    "Chạy trace thủ công cho {algo}",
    "Tìm input từ output cho {algo}",
    "Xử lý n lớn cho {algo}",
    "So sánh thực tế các thuật toán",
    "Mở rộng {algo}",
    "Áp dụng {algo} vào thực tế"
]
MED_HINTS = [
    "Viết full code",
    "Sửa logic core",
    "Cải tiến cấu trúc dữ liệu",
    "Kết hợp 2 hàm",
    "Viết nhật ký chạy",
    "Ngược logic",
    "Dùng cấu trúc dữ liệu phù hợp",
    "Dùng timeit",
    "Thêm tham số",
    "Áp dụng thực tế"
]

HARD_TITLES = ['Thiết kế thuật toán', 'Chứng minh', 'Giới hạn dưới', 'Tối ưu cực hạn', 'Biến thể nghiên cứu', 'Kết hợp nâng cao', 'Đối kháng', 'Mở rộng lý thuyết', 'Cài đặt production', 'Nghiên cứu mở']
HARD_TASKS = [
    'Thiết kế thuật toán O() cho {algo}',
    'Chứng minh đúng đắn cho {algo}',
    'Chứng minh lower bound cho {algo}',
    'Tối ưu {algo} chạy trong time limit',
    'Viết biến thể của {algo}',
    'Kết hợp 3 thuật toán cho {algo}',
    'Viết generator test phá {algo}',
    'Mở rộng định lý cho {algo}',
    'Cài {algo} production-ready',
    'Đề xuất cải tiến mới cho {algo}'
]
HARD_HINTS = [
    'Tham khảo CLRS',
    'Dùng exchange argument',
    'Dùng adversary argument',
    'Profile + tối ưu',
    'Tham khảo paper',
    'Phân chia rõ ràng',
    'Sinh test adversarial',
    'Generalize định lý',
    'Production checklist',
    'Đọc paper mới'
]

LESSON_CONFIG = {
    "b23-Regex": {"topic": "Regex", "algo": "Regex", "basic_task": "trích xuất số điện thoại"},
    "b24-Tu-Duy-Thuat-Toan": {"topic": "Tư duy thuật toán", "algo": "Phân rã bài toán", "basic_task": "phân rã bài toán"},
    "b25-Do-Phuc-Tap": {"topic": "Độ phức tạp", "algo": "Phân tích độ phức tạp", "basic_task": "tính O(n)"},
    "b26-Vet-Can": {"topic": "Vét cạn", "algo": "Brute Force", "basic_task": "tìm max/min"},
    "b27-Tim-Kiem": {"topic": "Tìm kiếm", "algo": "Binary Search", "basic_task": "tìm kiếm nhị phân"},
    "b28-Sap-Xep": {"topic": "Sắp xếp", "algo": "Merge Sort", "basic_task": "cài merge sort"},
    "b29-Stack-Queue-Hashing": {"topic": "Stack/Queue/Hashing", "algo": "Stack/Queue/Hash", "basic_task": "kiểm tra ngoặc"},
    "b30-Tan-Suat": {"topic": "Tần suất", "algo": "Frequency Counting", "basic_task": "đếm tần suất"},
    "b31-De-Quy": {"topic": "Đệ quy", "algo": "Recursion", "basic_task": "tính giai thừa"},
    "b32-Quay-Lui": {"topic": "Quay lui", "algo": "Backtracking", "basic_task": "liệt kê hoán vị"},
    "b33-Hai-Con-Tro": {"topic": "Hai con trỏ", "algo": "Two Pointers", "basic_task": "tìm cặp tổng S"},
    "b34-Tham-Lam": {"topic": "Tham lam", "algo": "Greedy", "basic_task": "đổi tiền"},
    "b35-Quy-Hoach-Dong": {"topic": "Quy hoạch động", "algo": "DP", "basic_task": "bậc thang DP"},
    "b36-Toan-Hoc-So-Hoc": {"topic": "Toán học/Số học", "algo": "Number Theory", "basic_task": "kiểm tra nguyên tố"},
    "b37-Do-Thi-BFS-DFS": {"topic": "Đồ thị BFS/DFS", "algo": "BFS/DFS", "basic_task": "BFS đường ngắn"},
    "b38-Duong-Di-Ngan-Nhat": {"topic": "Đường đi ngắn nhất", "algo": "Dijkstra", "basic_task": "Dijkstra cơ bản"},
    "b39-Cay-Va-DSU": {"topic": "Cây & DSU", "algo": "DSU/Tree", "basic_task": "DSU cơ bản"},
    "b40-Segment-Tree": {"topic": "Segment Tree", "algo": "Segment Tree", "basic_task": "Segment tree sum"},
    "b41-Xu-Ly-Chuoi": {"topic": "Xử lý chuỗi", "algo": "KMP/Z/Hash", "basic_task": "KMP tìm pattern"},
    "b42-Bitmask": {"topic": "Bitmask", "algo": "Bitmask DP", "basic_task": "DP bitmask TSP"},
    "b43-DP-Nang-Cao": {"topic": "DP nâng cao", "algo": "Advanced DP", "basic_task": "DP trên cây"},
    "b44-Chien-Luoc-Thi-HSG": {"topic": "Chiến lược thi HSG", "algo": "Contest Strategy", "basic_task": "phân loại bài"},
    "b45-Itertools": {"topic": "Itertools", "algo": "Itertools", "basic_task": "liệt kê tổ hợp"},
    "b46-Ly-Thuyet-Tro-Choi": {"topic": "Lý thuyết trò chơi", "algo": "Game Theory", "basic_task": "Nim game"},
}

def make_exercise(num, title, task, hint, algo):
    return """### Bài {num}: {title} {algo}

* **Đề bài:** {task}.
* **Input:** (theo đề bài)
* **Output:** (theo đề bài)
* **Gợi ý:** {hint}.
""".format(num=num, title=title, task=task, hint=hint, algo=algo)

def generate_30_exercises(config):
    algo = config["algo"]
    topic = config["topic"]
    basic = config["basic_task"]
    
    exercises = []
    
    # 10 Easy
    easy_titles = ['Cài đặt cơ bản', 'Trace code', 'Điền khuyết', 'So sánh', 'Áp dụng trực tiếp', 'Biến thể đơn giản', 'Debug', 'Độ phức tạp', 'Kiểm tra hiểu', 'Mở rộng']
    easy_tasks = [
        "Viết hàm {algo}_basic thực hiện {basic}".format(algo=algo.lower(), basic=basic),
        "Trace code: cho đoạn code mẫu {algo}, hãy viết ra kết quả".format(algo=algo),
        "Hoàn thiện hàm {algo} đã cho sẵn".format(algo=algo.lower()),
        "So sánh 2 cách giải cho {topic}".format(topic=topic),
        "Áp dụng thuật toán {algo} trực tiếp".format(algo=algo),
        "Viết biến thể đơn giản của {algo}".format(algo=algo),
        "Sửa lỗi trong code {algo} cho trước".format(algo=algo),
        "Tính độ phức tạp O() của {algo}".format(algo=algo),
        "Giải thích bước quan trọng của {algo}".format(algo=algo),
        "Mở rộng {algo} cho trường hợp mới".format(algo=algo)
    ]
    easy_hints = [
        "Cài đặt theo định nghĩa",
        "Chạy thủ từng bước",
        "Hoàn thiện code còn thiếu",
        "So sánh ưu nhược điểm",
        "Áp dụng trực tiếp thuật toán",
        "Thay đổi tham số nhỏ",
        "Sửa try/except",
        "Đếm phép toán",
        "Giải thích logic",
        "Mở rộng tham số"
    ]
    
    MED_TITLES = ['Cài đặt đầy đủ', 'Biến thể', 'Tối ưu hóa', 'Kết hợp', 'Trace phức tạp', 'Biến thể ngược', 'Giới hạn lớn', 'So sánh thực tế', 'Mở rộng', 'Áp dụng thực tế']
    MED_TASKS = [
        "Viết chương trình hoàn chỉnh cho {0}".format(algo),
        "Sửa thuật toán {0}".format(algo),
        "Cải tiến độ phức tạp của {0}".format(algo),
        "Kết hợp {0} với thuật toán khác".format(algo),
        "Chạy trace thủ công cho {0}".format(algo),
        "Tìm input từ output cho {0}".format(algo),
        "Xử lý n lớn cho {0}".format(algo),
        "So sánh thực tế các thuật toán",
        "Mở rộng {0}".format(algo),
        "Áp dụng {0} vào thực tế".format(algo)
    ]
    MED_HINTS = [
        "Viết full code",
        "Sửa logic core",
        "Cải tiến cấu trúc dữ liệu",
        "Kết hợp 2 hàm",
        "Viết nhật ký chạy",
        "Ngược logic",
        "Dùng cấu trúc dữ liệu phù hợp",
        "Dùng timeit",
        "Thêm tham số",
        "Áp dụng thực tế"
    ]
    
    HARD_TITLES = ['Thiết kế thuật toán', 'Chứng minh', 'Giới hạn dưới', 'Tối ưu cực hạn', 'Biến thể nghiên cứu', 'Kết hợp nâng cao', 'Đối kháng', 'Mở rộng lý thuyết', 'Cài đặt production', 'Nghiên cứu mở']
    HARD_TASKS = [
        'Thiết kế thuật toán O() cho {0}'.format(algo),
        'Chứng minh đúng đắn cho {0}'.format(algo),
        'Chứng minh lower bound cho {0}'.format(algo),
        'Tối ưu {0} chạy trong time limit'.format(algo),
        'Viết biến thể của {0}'.format(algo),
        'Kết hợp 3 thuật toán cho {0}'.format(algo),
        'Viết generator test phá {0}'.format(algo),
        'Mở rộng định lý cho {0}'.format(algo),
        'Cài {0} production-ready'.format(algo),
        'Đề xuất cải tiến mới cho {0}'.format(algo)
    ]
    HARD_HINTS = [
        'Tham khảo CLRS',
        'Dùng exchange argument',
        'Dùng adversary argument',
        'Profile + tối ưu',
        'Tham khảo paper',
        'Phân chia rõ ràng',
        'Sinh test adversarial',
        'Generalize định lý',
        'Production checklist',
        'Đọc paper mới'
    ]
    
    exercises = []
    
    # 10 Easy
    for i in range(10):
        title_str = EASY_TITLES[i] + " " + algo
        task_str = EASY_TASKS[i].format(algo=algo, basic=basic, topic=topic)
        hint_str = EASY_HINTS[i]
        exercises.append("""### Bài {num}: {title} {algo}

* **Đề bài:** {task}.
* **Input:** (theo đề bài)
* **Output:** (theo đề bài)
* **Gợi ý:** {hint}.
""".format(num=i+1, title=title_str, algo=algo, task=task_str, hint=EASY_HINTS[i]))
    
    # 10 Medium
    MED_TITLES = ['Cài đặt đầy đủ', 'Biến thể', 'Tối ưu hóa', 'Kết hợp', 'Trace phức tạp', 'Biến thể ngược', 'Giới hạn lớn', 'So sánh thực tế', 'Mở rộng', 'Áp dụng thực tế']
    MED_TASKS = [
        "Viết chương trình hoàn chỉnh cho {0}".format(algo),
        "Sửa thuật toán {0}".format(algo),
        "Cải tiến độ phức tạp của {0}".format(algo),
        "Kết hợp {0} với thuật toán khác".format(algo),
        "Chạy trace thủ công cho {0}".format(algo),
        "Tìm input từ output cho {0}".format(algo),
        "Xử lý n lớn cho {0}".format(algo),
        "So sánh thực tế các thuật toán",
        "Mở rộng {0}".format(algo),
        "Áp dụng {0} vào thực tế".format(algo)
    ]
    MED_HINTS = [
        "Viết full code",
        "Sửa logic core",
        "Cải tiến cấu trúc dữ liệu",
        "Kết hợp 2 hàm",
        "Viết nhật ký chạy",
        "Ngược logic",
        "Dùng cấu trúc dữ liệu phù hợp",
        "Dùng timeit",
        "Thêm tham số",
        "Áp dụng thực tế"
    ]
    for i in range(10):
        exercises.append("""### Bài {num}: {title} {algo}

* **Đề bài:** {task}.
* **Input:** (theo đề bài)
* **Output:** (theo đề bài)
* **Gợi ý:** {hint}.
""".format(num=i+11, title=MED_TITLES[i], algo=algo, task=MED_TASKS[i].format(algo=algo, topic=topic), hint=MED_HINTS[i]))
    
    # 10 Hard
    HARD_TITLES = ['Thiết kế thuật toán', 'Chứng minh', 'Giới hạn dưới', 'Tối ưu cực hạn', 'Biến thể nghiên cứu', 'Kết hợp nâng cao', 'Đối kháng', 'Mở rộng lý thuyết', 'Cài đặt production', 'Nghiên cứu mở']
    HARD_TASKS = [
        'Thiết kế thuật toán O() cho {algo}',
        'Chứng minh đúng đắn cho {algo}',
        'Chứng minh lower bound cho {algo}',
        'Tối ưu {algo} chạy trong time limit',
        'Viết biến thể của {algo}',
        'Kết hợp 3 thuật toán cho {algo}',
        'Viết generator test phá {algo}',
        'Mở rộng định lý cho {algo}',
        'Cài {algo} production-ready',
        'Đề xuất cải tiến mới cho {algo}'
    ]
    HARD_HINTS = [
        'Tham khảo CLRS',
        'Dùng exchange argument',
        'Dùng adversary argument',
        'Profile + tối ưu',
        'Tham khảo paper',
        'Phân chia rõ ràng',
        'Sinh test adversarial',
        'Generalize định lý',
        'Production checklist',
        'Đọc paper mới'
    ]
    for i in range(10):
        exercises.append("""### Bài {num}: {title} {algo}

* **Đề bài:** {task}.
* **Input:** (theo đề bài)
* **Output:** (theo đề bài)
* **Gợi ý:** {hint}.
""".format(num=i+21, title=HARD_TITLES[i], algo=algo, task=HARD_TASKS[i].format(algo=algo, topic=topic), hint=HARD_HINTS[i]))
    
    return "\n".join(exercises)

def inject_exercises():
    ROOT = Path(r"D:\HyperHub - HSG Tin")
    
    # Algorithm lessons (b23-b46)
    algo_lessons = []
    for d in ROOT.iterdir():
        if d.is_dir() and re.match(r'b\d{2}-', d.name):
            num = int(d.name[1:3])
            if 23 <= num <= 46:
                algo_lessons.append(d.name)
    
    for lesson_dir in sorted(algo_lessons):
        config = LESSON_CONFIG.get(lesson_dir)
        if not config:
            continue
            
        f = ROOT / lesson_dir / "bai.md"
        if not f.exists():
            print(f"SKIP {lesson_dir}: file not found")
            continue
            
        text = f.read_text(encoding="utf-8")
        
        # Find exercise section
        ex_match = re.search(r'## 🧩 Bài tập', text)
        if not ex_match:
            print(f"SKIP {lesson_dir}: No exercise section")
            continue
        
        ans_match = re.search(r'## ✅ Đáp án', text)
        if not ans_match:
            print(f"SKIP {lesson_dir}: No answer section")
            continue
        
        # Generate exercises
        exercises_text = generate_30_exercises(config)
        
        # Replace section
        start = ex_match.end()
        end = ans_match.start()
        
        new_text = text[:ex_match.end()] + "\n\n" + exercises_text + "\n\n" + text[ans_match.start():]
        
        f.write_text(new_text, encoding="utf-8", newline="\n")
        print(f"Updated {lesson_dir}")

if __name__ == "__main__":
    inject_exercises()