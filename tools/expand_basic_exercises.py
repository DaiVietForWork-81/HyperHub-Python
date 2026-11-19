# -*- coding: utf-8 -*-
"""Add 10 more exercises to basic lessons (b01-b22) to reach 30 each."""
import re
from pathlib import Path

ROOT = Path(r"D:\HyperHub - HSG Tin")

# Additional exercises for basic lessons - exactly 10 extra per lesson
# Distribution: 3 easy + 3 medium + 4 hard = 10 extra
BASIC_EXTRA = {
    "b01-Gioi-Thieu": {
        "topic": "Python cơ bản",
        "algo": "Python cơ bản",
        "extra_easy": [
            ("In ra thông tin", "Viết chương trình in ra tên, tuổi, lớp của bạn.", "Dùng print() nhiều lần."),
            ("Tính tuổi", "Nhập năm sinh, in ra tuổi hiện tại.", "Dùng 2024 - năm_sinh."),
            ("Chào hỏi", "Nhập tên, in 'Xin chào [tên]!'.", "Dùng input() và f-string."),
        ],
        "extra_medium": [
            ("Máy tính đơn giản", "Nhập 2 số, in ra tổng, hiệu, tích, thương.", "Dùng float() và các phép toán."),
            ("Đổi đơn vị", "Nhập số mét, in ra cm, km.", "Nhân 100 cho cm, chia 1000 cho km."),
            ("Hộp số", "Nhập 3 số, in ra số lớn nhất, nhỏ nhất, trung bình.", "Dùng max(), min(), sum()/3."),
        ],
        "extra_hard": [
            ("Tìm ước chung lớn nhất", "Nhập 2 số, tìm UCLN (không dùng math.gcd).", "Thuật toán Euclid."),
            ("Số nguyên tố", "Kiểm tra số n có phải nguyên tố không (O(√n)).", "Duyệt từ 2 đến √n."),
            ("Fibonacci", "In 20 số Fibonacci đầu tiên (không đệ quy).", "Dùng vòng lặp a, b = b, a+b."),
            ("Bảng cửu chương", "In bảng cửu chương 2-9 (dùng nested loop).", "Nested loop range(2,10) và range(1,10)."),
        ]
    },
    "b02-Cai-Dat-Python": {
        "topic": "Cài đặt Python",
        "algo": "Cài đặt",
        "extra_easy": [
            ("Kiểm tra cài đặt", "Chạy python --version và pip --version.", "Đọc output."),
            ("Hello World", "Tạo file hello.py in 'Hello World'.", "Chạy bằng python hello.py."),
            ("Thử pip", "Chạy pip list để xem các thư viện có sẵn.", "pip list"),
        ],
        "extra_medium": [
            ("Virtual env", "Tạo venv, kích hoạt, cài requests.", "python -m venv venv."),
            ("Requirements", "Tạo requirements.txt từ pip freeze.", "pip freeze > requirements.txt"),
            ("Pip upgrade", "Nâng cấp pip lên phiên bản mới nhất.", "python -m pip install --upgrade pip"),
        ],
        "extra_hard": [
            ("Quản lý package", "Viết script cài package từ requirements.txt tự động.", "subprocess.run pip install."),
            ("Đa phiên bản", "Giải thích cách quản lý nhiều phiên bản Python (pyenv).", "Tìm hiểu pyenv."),
            ("Virtualenv so sánh", "So sánh venv vs virtualenv vs conda.", "So sánh ưu/nhược điểm"),
            ("Dockerfile", "Viết Dockerfile cài Python + requirements.txt.", "FROM python:3.10-slim"),
        ]
    },
    "b03-Bien": {
        "topic": "Biến",
        "algo": "Biến",
        "extra_easy": [
            ("Đổi giá trị", "a=5, b=10 -> hoán đổi không dùng biến tạm.", "a, b = b, a"),
            ("Kiểu dữ liệu", "In type() của 5, 5.0, 'hello', True.", "type()"),
            ("Naming", "Đặt tên biến cho: điểm toán, tên học sinh, có đỗ không.", "snake_case"),
        ],
        "extra_medium": [
            ("Đổi kiểu", "Nhập chuỗi '123', ép thành int, nhân 2.", "int(), float()"),
            ("Copy list", "a=[1,2]; b=a.copy(); b.append(3); in a.", "Shallow copy"),
            ("F-string", "ten='An'; tuoi=15; print(f'{ten} {tuoi} tuoi').", "f-string"),
        ],
        "extra_hard": [
            ("Reference", "a=[1,2]; b=a; b.append(3); in a -> giải thích.", "Tham chiếu"),
            ("Deep copy", "Sao chép list lồng nhau không dùng copy.deepcopy.", "List comprehension hoặc pickle"),
            ("Mutable default", "def f(x=[]): x.append(1); return x -> giải thích bug.", "Mutable default argument"),
            ("Global vs nonlocal", "x=1; def f(): global x; x=2 -> giải thích.", "LEGB rule"),
        ]
    },
    "b04-Kieu-Du-Lieu": {
        "topic": "Kiểu dữ liệu",
        "algo": "Kiểu dữ liệu",
        "extra_easy": [
            ("bool()", "In bool(0), bool(1), bool(''), bool('a').", "False, True, False, True"),
            ("None", "x = None; in type(x), x is None.", "NoneType"),
            ("Complex", "z = 3+4j; in z.real, z.imag, abs(z).", "Complex number"),
        ],
        "extra_medium": [
            ("Ép kiểu an toàn", "Nhập '123abc', ép int trong try/except.", "try/except ValueError"),
            ("isinstance", "Kiểm tra x là int, float, str, list.", "isinstance(x, int)"),
            ("Type conversion", "int('3.14') -> lỗi; float('3.14') -> OK.", "int() chỉ nhận int string"),
        ],
        "extra_hard": [
            ("Duck typing", "Viết hàm nhận 'bất cứ gì có .append()'.", "hasattr(x, 'append')"),
            ("Type hint", "Viết hàm có type hint đầy đủ cho list[int] -> int.", "typing.List"),
            ("Mutable default", "def f(x=[]): x.append(1); return x -> bug.", "Mutable default argument"),
            ("Dataclass", "@dataclass class Point: x: int; y: int.", "Python 3.7+"),
        ]
    },
    "b05-Toan-Tu": {
        "topic": "Toán tử",
        "algo": "Toán tử",
        "extra_easy": [
            ("Modulo", "10 % 3, 10 // 3, 2 ** 10.", "%, //, **"),
            ("Logic", "True and False, not True.", "and, or, not"),
            ("Comparison", "5 > 3, 5 >= 5, 'a' < 'b'.", "Comparison operators"),
        ],
        "extra_medium": [
            ("Bitwise", "5 & 3, 5 | 3, 5 ^ 3, ~5.", "&, |, ^, ~"),
            ("String compare", "'abc' < 'abd', '10' > '2'.", "Lexicographic"),
            ("Short-circuit", "True or print('hi') -> không in hi.", "Short-circuit eval"),
        ],
        "extra_hard": [
            ("Overflow", "Giải thích tại sao 0.1 + 0.2 != 0.3.", "IEEE 754 float"),
            ("Short-circuit", "Viết f() and g() nơi f() trả False, g() không chạy.", "Short-circuit eval"),
            ("Chained comparison", "1 < x < 10 tương đương 1 < x and x < 10.", "Chained comparison"),
            ("Walrus", "if (n := len(s)) > 5: print(n).", "Walrus operator 3.8+"),
        ]
    },
    "b06-Input-Output": {
        "topic": "Nhập/Xuất",
        "algo": "I/O",
        "extra_easy": [
            ("Nhập tên tuổi", "input() tên, int(input()) tuổi.", "input() luôn trả str"),
            ("Print format", "print('Tên:', ten, 'Tuổi:', tuoi, sep=' | ').", "sep, end"),
            ("Multi input", "a, b = input().split(); a=int(a); b=int(b).", "Multiple assignment"),
        ],
        "extra_medium": [
            ("Nhập nhiều", "Nhập '1 2 3' -> list map(int, input().split()).", "split()"),
            ("File I/O", "Đọc file.txt, in dòng đầu.", "open().readline()"),
            ("Fast output", "sys.stdout.write() vs print().", "Performance"),
        ],
        "extra_hard": [
            ("Fast I/O", "sys.stdin.buffer.read() vs input().", "Performance"),
            ("Parse phức tạp", "Parse '1,2;3,4' -> list tuple int.", "split + map"),
            ("Binary I/O", "struct.pack/unpack cho binary.", "struct module"),
            ("Custom format", "f'{x:.2%}' format phần trăm.", "Format spec"),
        ]
    },
    "b07-Cau-Lenh-If": {
        "topic": "Câu lệnh if",
        "algo": "If",
        "extra_easy": [
            ("If đơn", "Nhập số, in 'dương'/'âm'/'không'.", "if/elif/else"),
            ("Chuỗi", "'a' < 'b', 'abc' == 'abc'.", "String compare"),
            ("Boolean", "if x: print('True') else: print('False').", "Truthiness"),
        ],
        "extra_medium": [
            ("Nested if", "Xếp loại điểm: >=8 giỏi, >=6.5 khá, >=5 trung bình.", "elif chain"),
            ("Logic phức tạp", "Năm nhuận: chia 400 hoặc (chia 4 và không chia 100).", "Logic phức hợp"),
            ("Pass", "if x > 0: pass  # placeholder.", "Pass statement"),
        ],
        "extra_hard": [
            ("Ternary", "max = a if a>b else b.", "Ternary operator"),
            ("Guard clause", "Viết hàm return sớm thay vì nested if.", "Guard clause pattern"),
            ("Match-case", "match x: case 1: ... case _: ... (Py 3.10+).", "Pattern matching"),
            ("Walrus if", "if (n := len(s)) > 5: print(n).", "Walrus operator"),
        ]
    },
    "b08-Vong-Lap-For": {
        "topic": "Vòng lặp for",
        "algo": "For",
        "extra_easy": [
            ("range()", "In 1..10, 10..1, 0..9.", "range(start, stop, step)"),
            ("Duyệt list", "for x in ds: print(x).", "Iterate values"),
            ("enumerate", "for i, x in enumerate(ds, 1): print(i, x).", "Index + value"),
        ],
        "extra_medium": [
            ("zip", "for a, b in zip(a_list, b_list): print(a, b).", "Parallel iterate"),
            ("Nested", "Ma trận 3x3: for i in range(3): for j in range(3).", "Nested loop"),
            ("List comp", "[x*x for x in range(5) if x%2==0].", "Filter + map"),
        ],
        "extra_hard": [
            ("Nested comp", "[[i*j for j in range(3)] for i in range(3)].", "Matrix comp"),
            ("Zip longest", "itertools.zip_longest cho list khác độ dài.", "itertools"),
            ("Generator", "(x*x for x in range(1000000)) - lazy.", "Memory efficient"),
            ("Else for", "for...else: else chạy khi không break.", "Search pattern"),
        ]
    },
    "b09-Vong-Lap-While": {
        "topic": "Vòng lặp while",
        "algo": "While",
        "extra_easy": [
            ("Đếm ngược", "while n > 0: print(n); n -= 1.", "Countdown"),
            ("Input loop", "while True: x=input(); if x=='q': break.", "while True + break"),
            ("Counter", "i=1; while i<=10: print(i); i+=1.", "Counter pattern"),
        ],
        "extra_medium": [
            ("Đoán số", "Random 1-100, nhập đến khi đúng.", "random + while"),
            ("Menu", "Menu 1-3, nhập 0 để thoát.", "while True + if/elif"),
            ("Flag", "done=False; while not done: ... if ok: done=True.", "Flag pattern"),
        ],
        "extra_hard": [
            ("Sieve", "Sàng Eratosthenes tìm SNT <= n.", "while + list bool"),
            ("Collatz", "n -> n/2 (chẵn), 3n+1 (lẻ), dừng ở 1.", "Unsolved problem"),
            ("Euclid GCD", "while b: a, b = b, a%b; return a.", "Euclidean algorithm"),
            ("Bisection", "Tìm nghiệm f(x)=0 bằng chia đôi đoạn.", "Binary search on continuous"),
        ]
    },
    "b10-Ham": {
        "topic": "Hàm",
        "algo": "Function",
        "extra_easy": [
            ("Def cơ bản", "def greet(name): return f'Hello {name}'.", "def + return"),
            ("Default arg", "def pow(x, n=2): return x**n.", "Default parameter"),
            ("Docstring", "def f():\n    '''Docstring'''\n    return 1", "Documentation"),
        ],
        "extra_medium": [
            ("*args/**kwargs", "def sum_all(*a): return sum(a).", "*args, **kwargs"),
            ("Lambda", "square = lambda x: x*x.", "Lambda expression"),
            ("Type hints", "def f(x: int) -> int: return x+1.", "Type annotation"),
        ],
        "extra_hard": [
            ("Decorator", "@timer def f(): pass -> in thời gian chạy.", "Closure + wrapper"),
            ("Recursion limit", "sys.setrecursionlimit(10**6).", "Stack frame"),
            ("Closure", "def make_adder(n): return lambda x: x+n.", "Closure captures"),
            ("Generator func", "def gen(): yield 1; yield 2.", "yield vs return"),
        ]
    },
    "b11-Scope": {
        "topic": "Phạm vi",
        "algo": "Scope",
        "extra_easy": [
            ("Local vs Global", "x=1; def f(): x=2; print(x); f(); print(x).", "LEGB"),
            ("global", "x=1; def f(): global x; x=2.", "global keyword"),
            ("Built-in", "print(len) - built-in len().", "Built-in scope"),
        ],
        "extra_medium": [
            ["nonlocal", "def outer(): x=1; def inner(): nonlocal x; x=2.", "nonlocal keyword"],
            ["Mutable default", "def f(x=[]): x.append(1); return x -> bug.", "Mutable default"],
        ],
        "extra_hard": [
            ["Closure", "def make_adder(n): return lambda x: x+n.", "Closure captures"],
            ["Descriptor", "class Property: __get__/__set__.", "Descriptor protocol"],
            ["__slots__", "class A: __slots__=['x'] -> tiết kiệm memory.", "Memory optimization"],
        ]
    },
    "b12-List": {
        "topic": "List",
        "algo": "List",
        "extra_easy": [
            ("Tạo list", "ds = [1,2,3] + [4,5].", "Nối list"),
            ("Index", "ds[-1], ds[1:3], ds[::-1].", "Index âm, slice"),
            ("append", "ds.append(4) -> [1,2,3,4].", "Append one"),
        ],
        "extra_medium": [
            ("Mutability", "a=[1,2]; b=a; b.append(3); print(a).", "Tham chiếu"),
            ("Sort vs sorted", "ds.sort() vs sorted(ds).", "In-place vs new list"),
            ("Copy", "b = a.copy() hoặc b = a[:].", "Shallow copy"),
        ],
        "extra_hard": [
            ("List comp", "Ma trận 3x3: [[0]*3 for _ in range(3)].", "Nested comprehension"),
            ("Sort key", "sorted(ds, key=lambda x: (x[1], -x[0])).", "Tuple key"),
            ("Heapq", "import heapq; heapq.heappush/pop.", "Priority queue"),
            ("Deque", "from collections import deque; dq.appendleft(1).", "Double-ended queue"),
        ]
    },
    "b13-Tuple": {
        "topic": "Tuple",
        "algo": "Tuple",
        "extra_easy": [
            ("Tạo tuple", "t = (1, 2, 3) hoặc t = 1, 2, 3.", "Packing"),
            ("Index", "t[0], t[-1], t[1:3].", "Index/slice"),
            ("Unpack", "a, b, c = (1, 2, 3).", "Unpacking"),
        ],
        "extra_medium": [
            ("Named tuple", "from collections import namedtuple; Point = namedtuple('Point', 'x y').", "Named access"),
            ("Dict key", "d = {(1,2): 'a'} - tuple làm key.", "Immutable key"),
            ("Return multi", "return a, b -> tuple.", "Multiple return"),
        ],
        "extra_hard": [
            ("Namedtuple defaults", "Point = namedtuple('P', 'x y', defaults=[0,0]).", "Defaults"),
            ("Immutable", "t[0]=1 -> TypeError -> list(t).", "Immutability"),
            ("Dataclass", "@dataclass class Point: x: int; y: int.", "Modern alternative"),
        ]
    },
    "b14-Set": {
        "topic": "Set",
        "algo": "Set",
        "extra_easy": [
            ("Tạo set", "s = {1,2,3} hoặc set([1,2,2]).", "Auto dedup"),
            ("in check", "1 in {1,2,3} -> True. O(1).", "Membership O(1)"),
            ("add/discard", "s.add(4); s.discard(2).", "Add/remove"),
        ],
        "extra_medium": [
            ("Set ops", "A|B, A&B, A-B, A^B.", "Union, inter, diff, symdiff"),
            ("Counter", "Counter(['a','a','b']) -> {'a':2, 'b':1}.", "Count elements"),
            ("Frozenset", "frozenset([1,2]) -> hashable.", "Dict key"),
        ],
        "extra_hard": [
            ("Ordered dedup", "list(dict.fromkeys([1,2,1,3])) -> [1,2,3].", "Ordered dedup"),
            ("Bitset", "int bitmask cho set nhỏ.", "Bit manipulation"),
            ["Set comp", "{x*x for x in range(5)} -> {0,1,4,9,16}.", "Set comprehension"],
        ]
    },
    "b15-Dictionary": {
        "topic": "Dictionary",
        "algo": "Dict",
        "extra_easy": [
            ("Tạo dict", "d = {'a':1, 'b':2} hoặc dict(a=1, b=2).", "Key-value"),
            ("get()", "d.get('x', 0) tránh KeyError.", "Default value"),
            ("keys/values", "d.keys(), d.values(), d.items().", "View objects"),
        ],
        "extra_medium": [
            ("update()", "d1.update(d2) - ghi đè key trùng.", "Merge dict"),
            ("setdefault", "d.setdefault(k, []).append(x).", "Group by key"),
            ("pop", "d.pop('x') trả giá trị rồi xóa.", "Pop returns value"),
        ],
        "extra_hard": [
            ["Dict comp", "{x: x*x for x in range(5)}.", "Comprehension"],
            ["Merge deep", "def merge(d1,d2): ... đệ quy merge nested.", "Recursive merge"],
            ["Defaultdict", "defaultdict(list) - auto create list.", "Auto init"],
        ]
    },
    "b16-String": {
        "topic": "String",
        "algo": "String",
        "extra_easy": [
            ["f-string", "f'{x:.2f}' format 2 chữ số.", "Format spec"],
            ["split/join", "'a,b,c'.split(',') -> list; '-'.join(lst).", "Split/join"],
            ["strip", "'  a  '.strip() -> 'a'.", "Strip whitespace"],
        ],
        "extra_medium": [
            ["replace", "'hello'.replace('l','L') -> 'heLLo'.", "Replace all"],
            ["Regex", "re.sub(r'\\d+', '*', 'a1b2') -> 'a*b*'.", "re.sub"],
            ["Format", "'{:>10}'.format(42) -> '        42'.", "Alignment"],
        ],
        "extra_hard": [
            ["Template", "string.Template('$x $y').substitute(x=1,y=2).", "Safe subst"],
            ["Encoding", "s.encode('utf-8') -> bytes; b.decode('utf-8').", "Bytes/str"],
            ["IO StringIO", "io.StringIO() - file-like string buffer.", "In-memory file"],
        ]
    },
    "b17-Module": {
        "topic": "Module",
        "algo": "Module",
        "extra_easy": [
            ["import as", "import math as m; m.sqrt(4).", "Alias"],
            ["from import", "from math import sqrt; sqrt(4).", "Direct import"],
            ["__main__", "if __name__ == '__main__': test().", "Entry point"],
        ],
        "extra_medium": [
            ["__all__", "__all__ = ['func1'] - kiểm soát import *.", "Public API"],
            ["Package", "pkg/__init__.py quản lý submodule.", "Package structure"],
            ["Relative import", "from . import sibling.", "Relative import"],
        ],
        "extra_hard": [
            ["Reload", "importlib.reload(module) - reload runtime.", "Hot reload"],
            ["Namespace pkg", "pkg/__init__.py quản lý submodule.", "Package structure"],
            ["Dynamic import", "importlib.import_module('module_name').", "Runtime import"],
        ]
    },
    "b18-File": {
        "topic": "File I/O",
        "algo": "File",
        "extra_easy": [
            ["read()", "f.read() đọc cả file.", "Small file"],
            ["readline", "f.readline() đọc 1 dòng.", "Line by line"],
            ["write", "f.write('text') - ghi đè; f.write('\\n').", "Mode w/a"],
        ],
        "extra_medium": [
            ["with", "with open() as f: - tự đóng.", "Context manager"],
            ["readlines", "f.readlines() -> list lines.", "All lines"],
            ["encoding", "open(..., encoding='utf-8').", "UTF-8 required"],
        ],
        "extra_hard": [
            ["Binary", "wb/rb + struct.pack/unpack.", "Binary I/O"],
            ["Mmap", "mmap.mmap - map file vào memory.", "Large file"],
            ["Temp file", "tempfile.NamedTemporaryFile().", "Temporary file"],
            ["Seek/tell", "f.seek(0), f.tell() - vị trí con trỏ.", "Random access"],
        ]
    },
    "b19-OOP": {
        "topic": "OOP",
        "algo": "OOP",
        "extra_easy": [
            ["Class cơ bản", "class Dog: def __init__(self,name): self.name=name.", "Constructor"],
            ["Method", "def bark(self): print('Woof').", "Instance method"],
            ["Attribute", "self.name = name - instance attribute.", "Instance attr"],
        ],
        "extra_medium": [
            ["Inheritance", "class Cat(Animal): def sound(): 'Meow'.", "Super()"],
            ["Property", "@property def age(self): return self._age.", "Getter/setter"],
            ["Classmethod", "@classmethod def create(cls, name): return cls(name).", "Alternative constructor"],
        ],
        "extra_hard": [
            ["MRO", "class A(B,C): print(A.__mro__).", "Diamond problem"],
            ["ABC", "from abc import ABC, abstractmethod.", "Abstract base class"],
            ["Descriptor", "class Prop: __get__/__set__/__delete__.", "Descriptor protocol"],
            ["Dataclass", "@dataclass class Point: x: int; y: int.", "Auto methods"],
        ]
    },
    "b20-Lambda": {
        "topic": "Lambda",
        "algo": "Lambda",
        "extra_easy": [
            ["Lambda cơ bản", "f = lambda x: x*2; f(3) -> 6.", "One-liner"],
            ["key=sorted", "sorted(lst, key=lambda x: -x).", "Key function"],
            ["lambda arg", "lambda x, y=10: x+y (default arg).", "Default arg"],
        ],
        "extra_medium": [
            ["map/filter", "list(map(lambda x: x*2, lst)).", "Functional"],
            ["lambda default", "lambda x, y=10: x+y (default arg).", "Late binding"],
            ["Reduce", "functools.reduce(lambda a,b: a+b, lst).", "Reduce"],
        ],
        "extra_hard": [
            ["Partial", "functools.partial(func, arg) -> fix arg.", "Currying"],
            ["Closure lambda", "def make_adder(n): return lambda x: x+n.", "Factory"],
            ["Callable", "class C: __call__(self, x): return x+1.", "Callable object"],
        ]
    },
    "b21-List-Comprehension": {
        "topic": "List Comprehension",
        "algo": "ListComp",
        "extra_easy": [
            ["Basic", "[x*2 for x in range(5)] -> [0,2,4,6,8].", "Basic syntax"],
            ["Filter", "[x for x in lst if x%2==0].", "Filter clause"],
            ["If-else", "['chẵn' if x%2==0 else 'lẻ' for x in lst].", "If-else expr"],
        ],
        "extra_medium": [
            ["Nested", "[[i*j for j in range(3)] for i in range(3)].", "Matrix"],
            ["Dict comp", "{x: x*x for x in range(5)}.", "Dict comprehension"],
            ["Set comp", "{x for x in lst if x>0}.", "Set comprehension"],
        ],
        "extra_hard": [
            ["Walrus", "[y for x in data if (y:=f(x)) > 0].", "Walrus operator"],
            ["Flatten", "[x for row in matrix for x in row].", "Flatten 2D"],
            ["Generator", "(x*x for x in range(5)) -> generator.", "Gen expression"],
        ]
    },
    "b22-Generator": {
        "topic": "Generator",
        "algo": "Generator",
        "extra_easy": [
            ["yield", "def gen(): yield 1; yield 2; yield 3.", "yield keyword"],
            ["gen expr", "(x*x for x in range(5)) -> generator.", "Gen expression"],
            ["next()", "next(gen) -> lấy 1 giá trị.", "Manual iteration"],
        ],
        "extra_medium": [
            ["yield from", "yield from subgen() - delegate.", "Delegation"],
            ["itertools", "itertools.count/cycle/islice.", "Itertools"],
            ["send()", "gen.send(value) - send vào generator.", "Two-way"],
        ],
        "extra_hard": [
            ["Coroutine", "async/await vs generator.", "Async vs sync"],
            ["Pipeline", "gen1 | gen2 | gen3 pipeline.", "Pipeline pattern"],
            ["Async gen", "async def gen(): yield await f().", "Async generator"],
        ]
    },
}

def add_extra_exercises(lesson_dir, extra_config):
    """Add extra exercises to a basic lesson to reach 30 total."""
    f = ROOT / lesson_dir / "bai.md"
    if not f.exists():
        print(f"SKIP {lesson_dir}: file not found")
        return False
    
    text = f.read_text(encoding="utf-8")
    
    # Find answer section
    ans_pos = text.find("## ✅ Đáp án")
    if ans_pos == -1:
        print(f"SKIP {lesson_dir}: no answer section")
        return False
    
    # Build extra exercises
    algo = extra_config.get("algo", "Python")
    extra_exercises = []
    
    # Add extra easy
    for i, (title, task, hint) in enumerate(extra_config.get("extra_easy", [])):
        num = 21 + i
        extra_exercises.append(f"""### Bài {num}: {title} {algo}

* **Đề bài:** {task}.
* **Input:** (theo đề bài)
* **Output:** (theo đề bài)
* **Gợi ý:** {hint}.
""")
    
    # Add extra medium
    for i, (title, task, hint) in enumerate(extra_config.get("extra_medium", [])):
        num = 24 + i
        extra_exercises.append(f"""### Bài {num}: {title} {algo}

* **Đề bài:** {task}.
* **Input:** (theo đề bài)
* **Output:** (theo đề bài)
* **Gợi ý:** {hint}.
""")
    
    # Add extra hard
    for i, (title, task, hint) in enumerate(extra_config.get("extra_hard", [])):
        num = 27 + i
        extra_exercises.append(f"""### Bài {num}: {title} {algo}

* **Đề bài:** {task}.
* **Input:** (theo đề bài)
* **Output:** (theo đề bài)
* **Gợi ý:** {hint}.
""")
    
    extra_text = "\n".join(extra_exercises)
    
    # Insert before ## ✅ Đáp án
    new_text = text[:ans_pos] + "\n\n" + extra_text + "\n\n" + text[ans_pos:]
    f.write_text(new_text, encoding="utf-8", newline="\n")
    print(f"Added extra exercises to {lesson_dir}")
    return True

def main():
    for lesson_dir, extra_config in BASIC_EXTRA.items():
        print(f"Processing {lesson_dir}...")
        add_extra_exercises(lesson_dir, extra_config)

if __name__ == "__main__":
    main()