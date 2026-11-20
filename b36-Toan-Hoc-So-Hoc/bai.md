# Bài 36 — Toán Học & Số Học Thuật Toán

> Ã°ÂÂÂ **DÃÂ£y phÃ¡ÂºÂ³ng b1Ã¢ÂÂb46 Ã¢ÂÂ NÃ¡Â»Ân tÃ¡ÂºÂ£ng + ThuÃ¡ÂºÂ­t toÃÂ¡n**

> Ã°ÂÂÂ·Ã¯Â¸Â **NhÃÂ³m bÃÂ i:** ChuyÃÂªn ÃÂÃ¡Â»Â ÃÂ· ToÃÂ¡n hÃ¡Â»Âc & sÃ¡Â»Â hÃ¡Â»Âc thuÃ¡ÂºÂ­t toÃÂ¡n

---

## Ã°ÂÂ§Â  ÃÂiÃ¡Â»Âu kiÃ¡Â»Ân tiÃÂªn quyÃ¡ÂºÂ¿t

- [BÃÂ i 31 Ã¢ÂÂ ÃÂÃ¡Â»Â Quy](../b31-De-Quy/bai.md) (lÃÂ©y thÃ¡Â»Â«a nhanh, Euclid ÃÂÃ¡Â»Â quy)
- [BÃÂ i 25 Ã¢ÂÂ ÃÂÃ¡Â»Â PhÃ¡Â»Â©c TÃ¡ÂºÂ¡p](../b25-Do-Phuc-Tap/bai.md)
- [BÃÂ i 8 Ã¢ÂÂ VÃÂ²ng LÃ¡ÂºÂ·p For](../b08-Vong-Lap-For/bai.md)

---

## Ã°ÂÂÂ¯ MÃ¡Â»Â¥c tiÃÂªu

Sau bÃÂ i hÃ¡Â»Âc nÃÂ y, hÃ¡Â»Âc viÃÂªn sÃ¡ÂºÂ½:

* Ã¢ÂÂ KiÃ¡Â»Âm tra nguyÃÂªn tÃ¡Â»Â ÃÂÃÂºng cÃÂ¡ch: thÃ¡Â»Â­ ÃÂÃ¡ÂºÂ¿n Ã¢ÂÂn, vÃÂ  sÃÂ ng Eratosthenes cho nhiÃ¡Â»Âu truy vÃ¡ÂºÂ¥n.
* Ã¢ÂÂ HiÃ¡Â»Âu vÃÂ  cÃÂ i ÃÂÃÂ°Ã¡Â»Â£c thuÃ¡ÂºÂ­t toÃÂ¡n Euclid tÃÂ¬m GCD trong O(log min(a,b)).
* Ã¢ÂÂ DÃÂ¹ng lÃÂ©y thÃ¡Â»Â«a nhanh + modulo cho sÃ¡Â»Â mÃÂ© khÃ¡Â»Âng lÃ¡Â»Â (n Ã¢ÂÂ¤ 10ÃÂ¹Ã¢ÂÂ¸).
* Ã¢ÂÂ BiÃ¡ÂºÂ¿t ÃÂÃ¡Â»Ânh lÃÂ½ Fermat nhÃ¡Â»Â ÃÂÃ¡Â»Â tÃÂ­nh nghÃ¡Â»Âch ÃÂÃ¡ÂºÂ£o modulo (mod nguyÃÂªn tÃ¡Â»Â).
* Ã¢ÂÂ XÃ¡Â»Â­ lÃÂ½ ÃÂÃÂ°Ã¡Â»Â£c bÃÂ i tÃ¡Â»Â hÃ¡Â»Â£p C(n,k) mod M vÃÂ  ÃÂÃ¡ÂºÂ¿m ÃÂ°Ã¡Â»Âc.
* Ã¢ÂÂ TrÃÂ¡nh bÃ¡ÂºÂ«y float vÃ¡Â»Âi sÃ¡Â»Â lÃ¡Â»Ân (dÃÂ¹ng `//`, sÃ¡Â»Â nguyÃÂªn, `math.isqrt`).

---

## Ã°ÂÂÂ MÃ¡Â»Â ÃÂÃ¡ÂºÂ§u

RÃ¡ÂºÂ¥t nhiÃ¡Â»Âu bÃÂ i HSG "trÃÂ¡ hÃÂ¬nh sÃ¡Â»Â hÃ¡Â»Âc": sÃÂ ng, ÃÂ°Ã¡Â»Âc, chia hÃ¡ÂºÂ¿t, ÃÂÃ¡Â»Âng dÃÂ°, tÃ¡Â»Â hÃ¡Â»Â£p...
ChÃÂºng khÃÂ´ng ÃÂÃÂ²i toÃÂ¡n cao siÃÂªu Ã¢ÂÂ chÃ¡Â»Â ÃÂÃÂ²i 6 cÃÂ´ng cÃ¡Â»Â¥ trong bÃÂ i nÃÂ y, dÃÂ¹ng ÃÂÃÂºng
chÃ¡Â»Â. NÃ¡ÂºÂ¯m chÃ¡ÂºÂ¯c, bÃ¡ÂºÂ¡n "ÃÂn miÃ¡Â»Ân phÃÂ­" 1Ã¢ÂÂ2 bÃÂ i mÃ¡Â»Âi kÃ¡Â»Â³ thi.

---

## Ã°ÂÂÂ¡ ÃÂ tÃÂ°Ã¡Â»Âng trÃ¡Â»Â±c quan

* **SÃÂ ng Eratosthenes:** ÃÂiÃ¡Â»Âm danh lÃ¡Â»Âp Ã¢ÂÂ gÃ¡Â»Âi sÃ¡Â»Â 2, mÃ¡Â»Âi bÃ¡Â»Âi cÃ¡Â»Â¥a 2 ÃÂÃ¡Â»Â©ng lÃÂªn
  (hÃ¡Â»Â£p sÃ¡Â»Â, loÃ¡ÂºÂ¡i); gÃ¡Â»Âi sÃ¡Â»Â tiÃ¡ÂºÂ¿p theo cÃÂ²n ngÃ¡Â»Âi (3), loÃ¡ÂºÂ¡i bÃ¡Â»Âi cÃ¡Â»Â¥a 3... CuÃ¡Â»Âi giÃ¡Â»Â,
  ai cÃÂ²n ngÃ¡Â»Âi lÃÂ  nguyÃÂªn tÃ¡Â»Â.
* **Euclid:** GCD(a, b) = GCD(b, a mod b) Ã¢ÂÂ "cÃ¡ÂºÂ¯t bÃ¡Â»Ât" sÃ¡Â»Â lÃ¡Â»Ân bÃ¡ÂºÂ±ng phÃ¡ÂºÂ§n dÃÂ°,
  lÃ¡ÂºÂ·p ÃÂÃ¡ÂºÂ¿n khi mÃ¡Â»Ât sÃ¡Â»Â bÃ¡ÂºÂ±ng 0. NhÃÂ° cÃ¡ÂºÂ¯t vÃ¡ÂºÂ£i: cÃ¡ÂºÂ¯t mÃ¡ÂºÂ£nh dÃÂ i bÃ¡Â»Ât ÃÂi ÃÂÃÂºng phÃ¡ÂºÂ§n thÃ¡Â»Â«a.
* **ÃÂÃ¡Â»Âng dÃÂ°:** ÃÂÃ¡Â»Âng hÃ¡Â»Â 12 giÃ¡Â»Â Ã¢ÂÂ 15 giÃ¡Â»Â "ÃÂÃ¡Â»Âng dÃÂ°" 3 giÃ¡Â»Â (mod 12). ChÃ¡Â»Â quan tÃÂ¢m
  phÃ¡ÂºÂ§n dÃÂ°, bÃ¡Â»Â phÃ¡ÂºÂ§n nguyÃÂªn.

```mermaid
flowchart TD
    A{"DÃ¡ÂºÂ¡ng bÃÂ i sÃ¡Â»Â hÃ¡Â»ÂcÃ¡Â»Â"} -->|NguyÃÂªn tÃ¡Â»Â nhiÃ¡Â»Âu truy vÃ¡ÂºÂ¥n| B["SÃÂ ng O(n log log n)"]
    A -->|NguyÃÂªn tÃ¡Â»Â 1 sÃ¡Â»Â lÃ¡Â»Ân| C["ThÃ¡Â»Â­ ÃÂÃ¡ÂºÂ¿n Ã¢ÂÂn O(Ã¢ÂÂn)"]
    A -->|ÃÂ¯Ã¡Â»Âc chung / rÃÂºt gÃ¡Â»Ân| D["Euclid O(log)"]
    A -->|MÃÂ© khÃ¡Â»Âng lÃ¡Â»Â + mod| E["LÃÂ©y thÃ¡Â»Â«a nhanh O(log n)"]
    A -->|Chia modulo nguyÃÂªn tÃ¡Â»Â| F["Fermat: nghÃ¡Â»Âch ÃÂÃ¡ÂºÂ£o"]
    A -->|ÃÂÃ¡ÂºÂ¿m / tÃ¡Â»Â hÃ¡Â»Â£p| G["TiÃ¡Â»Ân xÃ¡Â»Â­ lÃÂ½ giai thÃ¡Â»Â«a + nghÃ¡Â»Âch ÃÂÃ¡ÂºÂ£o"]
```

---

## Ã°ÂÂÂ KiÃ¡ÂºÂ¿n thÃ¡Â»Â©c

### 1. KiÃ¡Â»Âm tra nguyÃÂªn tÃ¡Â»Â mÃ¡Â»Ât sÃ¡Â»Â Ã¢ÂÂ thÃ¡Â»Â­ ÃÂÃ¡ÂºÂ¿n Ã¢ÂÂn

n lÃÂ  hÃ¡Â»Â£p sÃ¡Â»Â Ã¢ÂÂ cÃÂ³ ÃÂ°Ã¡Â»Âc d Ã¢ÂÂ¤ Ã¢ÂÂn (vÃÂ¬ nÃ¡ÂºÂ¿u cÃ¡ÂºÂ£ hai ÃÂ°Ã¡Â»Âc ÃÂÃ¡Â»Âu > Ã¢ÂÂn thÃÂ¬ tÃÂ­ch > n).
ChÃ¡Â»Â thÃ¡Â»Â­ ÃÂÃ¡ÂºÂ¿n `isqrt(n)`:

```python
import math

def la_nguyen_to(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    r = math.isqrt(n)
    for u in range(3, r + 1, 2):   # chÃ¡Â»Â thÃ¡Â»Â­ lÃ¡ÂºÂ»
        if n % u == 0:
            return False
    return True
```

O(Ã¢ÂÂn). ÃÂÃ¡Â»Â§ cho n Ã¢ÂÂ¤ 10ÃÂ¹ÃÂ² (~10Ã¢ÂÂ¶ vÃÂ²ng lÃ¡ÂºÂ·p, ~0.5s) vÃÂ  kiÃ¡Â»Âm tra ÃÂÃÂ¡n lÃ¡ÂºÂ».
`math.isqrt` trÃ¡ÂºÂ£ cÃÂn nguyÃÂªn chÃÂ­nh xÃÂ¡c (float `n**0.5` sai sÃ¡Â»Â vÃ¡Â»Âi sÃ¡Â»Â lÃ¡Â»Ân!).

> BÃ¡ÂºÂ«y float: `int(10**18 ** 0.5)` cÃÂ³ thÃ¡Â»Â lÃ¡Â»Âch 1 Ã¢ÂÂ bÃ¡Â»Â sÃÂ³t ÃÂ°Ã¡Â»Âc hoÃ¡ÂºÂ·c lÃ¡ÂºÂ·p thÃ¡Â»Â«a.
> VÃ¡Â»Âi sÃ¡Â»Â nguyÃÂªn, luÃÂ´n dÃÂ¹ng `isqrt` vÃÂ  `//`.

### 2. SÃÂ ng Eratosthenes Ã¢ÂÂ nguyÃÂªn tÃ¡Â»Â ÃÂÃ¡ÂºÂ¿n N, nhiÃ¡Â»Âu truy vÃ¡ÂºÂ¥n

CÃ¡ÂºÂ§n liÃ¡Â»Ât kÃÂª/ÃÂÃ¡ÂºÂ¿m nguyÃÂªn tÃ¡Â»Â ÃÂÃ¡ÂºÂ¿n N (N Ã¢ÂÂ¤ 10Ã¢ÂÂ¶Ã¢ÂÂ10Ã¢ÂÂ·) hoÃ¡ÂºÂ·c trÃ¡ÂºÂ£ lÃ¡Â»Âi nhiÃ¡Â»Âu truy vÃ¡ÂºÂ¥n:
sÃÂ ng mÃ¡Â»Ât lÃ¡ÂºÂ§n O(n log log n), mÃ¡Â»Âi truy vÃ¡ÂºÂ¥n O(1):

```python
def sang(n):
    la_nt = [True] * (n + 1)
    la_nt[0] = la_nt[1] = False
    for i in range(2, math.isqrt(n) + 1):
        if la_nt[i]:
            buoc = i
            bat_dau = i * i          # bÃ¡Â»Âi nhÃ¡Â»Â hÃÂ¡n ÃÂÃÂ£ bÃ¡Â»Â sÃÂ ng bÃ¡Â»Âi ÃÂ°Ã¡Â»Âc nhÃ¡Â»Â hÃÂ¡n
            la_nt[bat_dau:n + 1:buoc] = [False] * ((n - bat_dau) // buoc + 1)
    return la_nt

la_nt = sang(10**6)
print(sum(la_nt))   # 78498 sÃ¡Â»Â nguyÃÂªn tÃ¡Â»Â Ã¢ÂÂ¤ 10^6
```

Hai tÃ¡Â»Âi ÃÂ°u quan trÃ¡Â»Âng: chÃ¡Â»Â sÃÂ ng ÃÂÃ¡ÂºÂ¿n Ã¢ÂÂn, vÃÂ  bÃ¡ÂºÂ¯t ÃÂÃ¡ÂºÂ§u tÃ¡Â»Â« `i*i` (bÃ¡Â»Âi nhÃ¡Â»Â hÃÂ¡n ÃÂÃÂ£
bÃ¡Â»Â loÃ¡ÂºÂ¡i bÃ¡Â»Âi ÃÂ°Ã¡Â»Âc nhÃ¡Â»Â hÃÂ¡n). GÃÂ¡n lÃÂ¡t (slice) dÃÂ¹ng code C bÃÂªn dÃÂ°Ã¡Â»Âi Ã¢ÂÂ nhanh gÃ¡ÂºÂ¥p
hÃÂ ng chÃ¡Â»Â¥c lÃ¡ÂºÂ§n vÃÂ²ng lÃ¡ÂºÂ·p Python.

### 3. GCD & LCM Ã¢ÂÂ Euclid O(log min(a,b))

```python
import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# ThÃ¡Â»Â±c tÃ¡ÂºÂ¿ dÃÂ¹ng luÃÂ´n:
math.gcd(48, 18)      # 6
math.lcm(4, 6)        # 12 (Python 3.9+)
```

**VÃÂ¬ sao nhanh:** `a % b < a / 2` sau tÃ¡Â»Âi ÃÂa 2 bÃÂ°Ã¡Â»Âc (tÃÂ­nh chÃ¡ÂºÂ¥t modulo) Ã¢ÂÂ sÃ¡Â»Â
giÃ¡ÂºÂ£m ÃÂ­t nhÃ¡ÂºÂ¥t mÃ¡Â»Ât nÃ¡Â»Â­a mÃ¡Â»Âi 2 vÃÂ²ng Ã¢ÂÂ O(log). VÃÂ­ dÃ¡Â»Â¥ gcd(48, 18): (48,18) Ã¢ÂÂ
(18,12) Ã¢ÂÂ (12,6) Ã¢ÂÂ (6,0) Ã¢ÂÂ **6**, chÃ¡Â»Â 3 bÃÂ°Ã¡Â»Âc.

Ã¡Â»Â¨ng dÃ¡Â»Â¥ng: rÃÂºt gÃ¡Â»Ân phÃÂ¢n sÃ¡Â»Â, kiÃ¡Â»Âm tra nguyÃÂªn tÃ¡Â»Â cÃÂ¹ng nhau (`gcd == 1`),
chu kÃ¡Â»Â³ lÃ¡ÂºÂ·p, LCM tÃÂ­nh qua GCD: `lcm = a // gcd * b` (chia trÃÂ°Ã¡Â»Âc nhÃÂ¢n sau
trÃÂ¡nh sÃ¡Â»Â phÃÂ¬nh Ã¢ÂÂ trong Python khÃÂ´ng trÃÂ n nhÃÂ°ng vÃ¡ÂºÂ«n nhanh hÃÂ¡n).

### 4. LÃÂ©y thÃ¡Â»Â«a nhanh + modulo (ÃÂ´n BÃÂ i 31, bÃ¡ÂºÂ£n vÃÂ²ng lÃ¡ÂºÂ·p)

Thi cÃ¡Â»Â­ chuÃ¡Â»Âng bÃ¡ÂºÂ£n vÃÂ²ng lÃ¡ÂºÂ·p (khÃÂ´ng lo ÃÂÃ¡Â»Â quy, hÃ¡ÂºÂ±ng sÃ¡Â»Â nhÃ¡Â»Â):

```python
def pow_mod(x, n, m):
    kq = 1 % m
    x %= m
    while n:
        if n & 1:        # bit cuÃ¡Â»Âi = 1 Ã¢ÂÂ nhÃÂ¢n x vÃÂ o kÃ¡ÂºÂ¿t quÃ¡ÂºÂ£
            kq = kq * x % m
        x = x * x % m    # bÃÂ¬nh phÃÂ°ÃÂ¡ng cÃÂ¡ sÃ¡Â»Â
        n >>= 1          # bÃ¡Â»Â bit ÃÂÃÂ£ xÃ¡Â»Â­ lÃÂ½
    return kq

# ThÃ¡Â»Â±c tÃ¡ÂºÂ¿ dÃÂ¹ng luÃÂ´n hÃÂ m cÃÂ³ sÃ¡ÂºÂµn (C, nhanh nhÃ¡ÂºÂ¥t):
pow(2, 10**18, 10**9 + 7)
```

MÃ¡Â»Âi vÃÂ²ng lÃ¡ÂºÂ·p xÃ¡Â»Â­ lÃÂ½ 1 bit cÃ¡Â»Â¥a n Ã¢ÂÂ O(log n) Ã¢ÂÂ 60 bÃÂ°Ã¡Â»Âc vÃ¡Â»Âi n = 10ÃÂ¹Ã¢ÂÂ¸.
`pow(x, n, m)` cÃÂ³ sÃ¡ÂºÂµn Ã¢ÂÂ trong thi **dÃÂ¹ng luÃÂ´n**, tÃ¡Â»Â± cÃÂ i chÃ¡Â»Â ÃÂÃ¡Â»Â hiÃ¡Â»Âu.

### 5. NghÃ¡Â»Âch ÃÂÃ¡ÂºÂ£o modulo & Fermat nhÃ¡Â»Â

MuÃ¡Â»Ân tÃÂ­nh `(a / b) mod M` (M nguyÃÂªn tÃ¡Â»Â, b khÃÂ´ng chia hÃ¡ÂºÂ¿t cho M): khÃÂ´ng chia
trÃ¡Â»Â±c tiÃ¡ÂºÂ¿p ÃÂÃÂ°Ã¡Â»Â£c (modulo khÃÂ´ng cÃÂ³ phÃÂ©p chia!) Ã¢ÂÂ nhÃÂ¢n vÃ¡Â»Âi nghÃ¡Â»Âch ÃÂÃ¡ÂºÂ£o:
bÃ¢ÂÂ»ÃÂ¹ Ã¢ÂÂ¡ b^(MÃ¢ÂÂ2) (mod M) theo Fermat nhÃ¡Â»Â.

```python
MOD = 10**9 + 7   # sÃ¡Â»Â nguyÃÂªn tÃ¡Â»Â "quÃ¡Â»Âc dÃÂ¢n" trong thi cÃ¡Â»Â­

def nghich_dao(b):
    return pow(b, MOD - 2, MOD)

# (a / b) mod MOD = a * nghich_dao(b) % MOD
```

> VÃÂ¬ sao M = 10Ã¢ÂÂ¹+7 phÃ¡Â»Â biÃ¡ÂºÂ¿n: ÃÂÃ¡Â»Â§ lÃ¡Â»Ân ÃÂÃ¡Â»Â ÃÂÃÂ¡p ÃÂ¡n ÃÂ­t va chÃ¡ÂºÂ¡m, vÃ¡Â»Â«a trong int64
> (bÃÂ¬nh phÃÂ°ÃÂ¡ng 2 sÃ¡Â»Â < MÃÂ² Ã¢ÂÂ 10ÃÂ¹Ã¯Â¿Â½8 < 9.2ÃÂ10ÃÂ¹8 = int64 max) cho C++, nguyÃÂªn tÃ¡Â»Â
> ÃÂÃ¡Â»Â dÃÂ¹ng Fermat. GÃ¡ÂºÂ·p M nÃÂ y trong ÃÂÃ¡Â»Â Ã¢ÂÂ nghÃÂ© ngay modular.

### 6. TÃ¡Â»Â hÃ¡Â»Â£p C(n,k) mod M Ã¢ÂÂ tiÃ¡Â»Ân xÃ¡Â»Â­ lÃÂ½ giai thÃ¡Â»Â«a

n Ã¢ÂÂ¤ 10Ã¢ÂÂ¶, nhiÃ¡Â»Âu truy vÃ¡ÂºÂ¥n C(n,k) mod M: tiÃ¡Â»Ân xÃ¡Â»Â­ lÃÂ½ `fact[i] = i! mod M` vÃÂ 
`inv_fact` (giai thÃ¡Â»Â«a nghÃ¡Â»Âch ÃÂÃ¡ÂºÂ£o) mÃ¡Â»Ât lÃ¡ÂºÂ§n O(N), mÃ¡Â»Âi truy vÃ¡ÂºÂ¥n O(1):

C(n,k) = fact[n] ÃÂ· inv_fact[k] ÃÂ· inv_fact[nÃ¢ÂÂk] mod M.

```python
MOD = 10**9 + 7

def chuan_bi_to_hop(n_max):
    fact = [1] * (n_max + 1)
    for i in range(1, n_max + 1):
        fact[i] = fact[i - 1] * i % MOD
    inv_fact = [1] * (n_max + 1)
    inv_fact[n_max] = pow(fact[n_max], MOD - 2, MOD)
    for i in range(n_max, 0, -1):   # ÃÂi ngÃÂ°Ã¡Â»Â£c tÃ¡Â»Â« nghÃ¡Â»Âch ÃÂÃ¡ÂºÂ£o lÃ¡Â»Ân nhÃ¡ÂºÂ¥t
        inv_fact[i - 1] = inv_fact[i] * i % MOD
    return fact, inv_fact

def C(n, k, fact, inv_fact):
    if k < 0 or k > n:
        return 0
    return fact[n] * inv_fact[k] % MOD * inv_fact[n - k] % MOD
```

MÃ¡ÂºÂ¹o `inv_fact` ngÃÂ°Ã¡Â»Â£c: tÃ¡Â»Â« (n!)Ã¢ÂÂ»ÃÂ¹ suy ra ((nÃ¢ÂÂ1)!)Ã¢ÂÂ»ÃÂ¹ = (n!)Ã¢ÂÂ»ÃÂ¹ ÃÂ· n Ã¢ÂÂ chÃ¡Â»Â 1 lÃ¡ÂºÂ§n
lÃÂ©y thÃ¡Â»Â«a thay vÃÂ¬ n lÃ¡ÂºÂ§n.

---

## Ã°ÂÂÂ» VÃÂ­ dÃ¡Â»Â¥

### VÃÂ­ dÃ¡Â»Â¥ 1 Ã¢ÂÂ DÃ¡Â»Â: ÃÂÃ¡ÂºÂ¿m nguyÃÂªn tÃ¡Â»Â trong ÃÂoÃ¡ÂºÂ¡n + rÃÂºt gÃ¡Â»Ân phÃÂ¢n sÃ¡Â»Â

```python
import sys, math

def sang(n):
    la_nt = bytearray(b"\x01") * (n + 1)   # bytearray: nhÃ¡ÂºÂ¹ hÃÂ¡n list bool
    la_nt[0:2] = b"\x00\x00"
    for i in range(2, math.isqrt(n) + 1):
        if la_nt[i]:
            la_nt[i * i:n + 1:i] = b"\x00" * ((n - i * i) // i + 1)
    return la_nt

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    l, r = int(data[0]), int(data[1])
    la_nt = sang(r)
    print(sum(la_nt[l:r + 1]))
    a, b = int(data[2]), int(data[3])
    u = math.gcd(a, b)
    print(f"{a // u}/{b // u}")

main()
```

Input `10 20\n48 18` Ã¢ÂÂ nguyÃÂªn tÃ¡Â»Â 11,13,17,19 = **4**; 48/18 rÃÂºt gÃ¡Â»Ân **8/3**.

### VÃÂ­ dÃ¡Â»Â¥ 2 Ã¢ÂÂ ThÃ¡Â»Â±c tÃ¡ÂºÂ¿: kiÃ¡Â»Âm tra sÃ¡Â»Â nguyÃÂªn tÃ¡Â»Â lÃ¡Â»Ân + lÃÂ©y thÃ¡Â»Â«a mod

```python
import sys, math

def la_nguyen_to(n):
    if n < 2:
        return False
    nho = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    if n in nho:
        return True
    for p in nho:
        if n % p == 0:
            return False
    r = math.isqrt(n)
    f = 41
    while f <= r:
        if n % f == 0:
            return False
        f += 2
    return True

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    print("YES" if la_nguyen_to(n) else "NO")
    print(pow(2, n, 10**9 + 7))   # 2^n mod MOD Ã¢ÂÂ demo lÃÂ©y thÃ¡Â»Â«a nhanh

main()
```

**GiÃ¡ÂºÂ£i thÃÂ­ch:** thÃ¡Â»Â­ ÃÂ°Ã¡Â»Âc nhÃ¡Â»Â trÃÂ°Ã¡Â»Âc (loÃ¡ÂºÂ¡i nhanh hÃ¡Â»Â£p sÃ¡Â»Â cÃÂ³ ÃÂ°Ã¡Â»Âc nhÃ¡Â»Â Ã¢ÂÂ ÃÂa sÃ¡Â»Â),
rÃ¡Â»Âi vÃÂ²ng lÃ¡ÂºÂ» ÃÂÃ¡ÂºÂ¿n Ã¢ÂÂn. VÃ¡Â»Âi n Ã¢ÂÂ¤ 10ÃÂ¹ÃÂ²: ~5ÃÂ10Ã¢ÂÂµ vÃÂ²ng Ã¢ÂÂ ~0.3s. Ã¢ÂÂ

### VÃÂ­ dÃ¡Â»Â¥ 3 Ã¢ÂÂ KhÃÂ³: ÃÂÃ¡ÂºÂ¿m ÃÂ°Ã¡Â»Âc + tÃ¡Â»Âng ÃÂ°Ã¡Â»Âc bÃ¡ÂºÂ±ng phÃÂ¢n tÃÂ­ch thÃ¡Â»Â«a sÃ¡Â»Â

> n Ã¢ÂÂ¤ 10ÃÂ¹ÃÂ². ÃÂÃ¡ÂºÂ¿m sÃ¡Â»Â ÃÂ°Ã¡Â»Âc vÃÂ  tÃ¡Â»Âng cÃÂ¡c ÃÂ°Ã¡Â»Âc cÃ¡Â»Â¥a n.

PhÃÂ¢n tÃÂ­ch n = Ã¢ÂÂ pÃ¡ÂµÂ¢^eÃ¡ÂµÂ¢ (thÃ¡Â»Â­ ÃÂÃ¡ÂºÂ¿n Ã¢ÂÂn, cÃÂ²n dÃÂ° > 1 lÃÂ  mÃ¡Â»Ât nguyÃÂªn tÃ¡Â»Â mÃÂ© 1).
SÃ¡Â»Â ÃÂ°Ã¡Â»Âc = Ã¢ÂÂ(eÃ¡ÂµÂ¢+1); tÃ¡Â»Âng ÃÂ°Ã¡Â»Âc = Ã¢ÂÂ(pÃ¡ÂµÂ¢^(eÃ¡ÂµÂ¢+1) Ã¢ÂÂ 1)/(pÃ¡ÂµÂ¢ Ã¢ÂÂ 1):

```python
import sys, math

def phan_tich(n):
    ts = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            ts[d] = ts.get(d, 0) + 1
            n //= d
        d += 1 if d == 2 else 2   # 2 rÃ¡Â»Âi chÃ¡Â»Â thÃ¡Â»Â­ lÃ¡ÂºÂ»
    if n > 1:
        ts[n] = ts.get(n, 0) + 1
    return ts

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    ts = phan_tich(n)
    so_uoc = 1
    tong_uoc = 1
    for p, e in ts.items():
        so_uoc *= e + 1
        tong_uoc *= (p ** (e + 1) - 1) // (p - 1)
    print(so_uoc, tong_uoc)

main()
```

ChÃ¡ÂºÂ¡y tay n = 36 = 2ÃÂ²ÃÂ·3ÃÂ²: sÃ¡Â»Â ÃÂ°Ã¡Â»Âc (2+1)(2+1) = **9**; tÃ¡Â»Âng (2ÃÂ³Ã¢ÂÂ1)/(2Ã¢ÂÂ1) ÃÂ
(3ÃÂ³Ã¢ÂÂ1)/(3Ã¢ÂÂ1) = 7 ÃÂ 13 = **91**. KiÃ¡Â»Âm chÃ¡Â»Â©ng: ÃÂ°Ã¡Â»Âc cÃ¡Â»Â¥a 36 lÃÂ 
1,2,3,4,6,9,12,18,36 Ã¢ÂÂ 9 ÃÂ°Ã¡Â»Âc, tÃ¡Â»Âng 91. Ã¢ÂÂ

---

## Ã°ÂÂÂ Minh hÃ¡Â»Âa

SÃÂ ng ÃÂÃ¡ÂºÂ¿n 30 (chÃ¡Â»Â ghi sÃ¡Â»Â cÃÂ²n lÃ¡ÂºÂ¡i sau mÃ¡Â»Âi bÃÂ°Ã¡Â»Âc):

```
Ban ÃÂÃ¡ÂºÂ§u: 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30
LoÃ¡ÂºÂ¡i bÃ¡Â»Âi 2: 2 3 5 7 9 11 13 15 17 19 21 23 25 27 29
LoÃ¡ÂºÂ¡i bÃ¡Â»Âi 3: 2 3 5 7 11 13 17 19 23 25 29
LoÃ¡ÂºÂ¡i bÃ¡Â»Âi 5: 2 3 5 7 11 13 17 19 23 29  (25 bÃ¡Â»Â loÃ¡ÂºÂ¡i; 7ÃÂ²=49 > 30 Ã¢ÂÂ dÃ¡Â»Â«ng)
Ã¢ÂÂ 10 sÃ¡Â»Â nguyÃÂªn tÃ¡Â»Â Ã¢ÂÂ¤ 30 Ã¢ÂÂ
```

Euclid gcd(1071, 462):

```
1071 % 462 = 147  Ã¢ÂÂ (462, 147)
462 % 147 = 21    Ã¢ÂÂ (147, 21)
147 % 21 = 0      Ã¢ÂÂ (21, 0) Ã¢ÂÂ ÃÂÃÂ¡p ÃÂ¡n 21 (3 bÃÂ°Ã¡Â»Âc!)
```

---

## Ã¢ÂÂ Ã¯Â¸Â NhÃ¡Â»Â¯ng lÃ¡Â»Âi thÃÂ°Ã¡Â»Âng gÃ¡ÂºÂ·p

### LÃ¡Â»Âi 1: DÃÂ¹ng float cho sÃ¡Â»Â nguyÃÂªn lÃ¡Â»Ân

```python
r = int(n ** 0.5)   # Ã¢ÂÂ lÃ¡Â»Âch 1 vÃ¡Â»Âi n ~ 10^18
r = math.isqrt(n)   # Ã¢ÂÂ chÃÂ­nh xÃÂ¡c tuyÃ¡Â»Ât ÃÂÃ¡Â»Âi
```

### LÃ¡Â»Âi 2: SÃÂ ng bÃ¡ÂºÂ¯t ÃÂÃ¡ÂºÂ§u tÃ¡Â»Â« `2*i` thay vÃÂ¬ `i*i`

* ÃÂÃÂºng nhÃÂ°ng chÃ¡ÂºÂ­m gÃ¡ÂºÂ¥p nhiÃ¡Â»Âu lÃ¡ÂºÂ§n (sÃÂ ng lÃ¡ÂºÂ¡i bÃ¡Â»Âi ÃÂÃÂ£ bÃ¡Â»Â loÃ¡ÂºÂ¡i). VÃ¡Â»Âi N = 10Ã¢ÂÂ·,
  khÃÂ¡c biÃ¡Â»Ât giÃ¡Â»Â¯a AC vÃÂ  TLE trong Python.

### LÃ¡Â»Âi 3: QuÃÂªn `n > 1` sau vÃÂ²ng phÃÂ¢n tÃÂ­ch (thÃ¡Â»Â«a sÃ¡Â»Â nguyÃÂªn tÃ¡Â»Â lÃ¡Â»Ân cÃÂ²n lÃ¡ÂºÂ¡i)

```python
# n = 2 ÃÂ 10^12+39... vÃÂ­ dÃ¡Â»Â¥ n = 14: vÃÂ²ng lÃ¡ÂºÂ·p xong n cÃÂ²n 7 Ã¢ÂÂ phÃ¡ÂºÂ£i ghi nhÃ¡ÂºÂ­n
if n > 1:
    ts[n] = ts.get(n, 0) + 1
```

### LÃ¡Â»Âi 4: Chia trÃÂ°Ã¡Â»Âc khi mod / chia trong modulo

```python
# Ã¢ÂÂ (a // b) % M Ã¢ÂÂ  (a / b) mod M
# Ã¢ÂÂ a * pow(b, M - 2, M) % M  (M nguyÃÂªn tÃ¡Â»Â)
```

### LÃ¡Â»Âi 5: `gcd(0, x)` vÃÂ  sÃ¡Â»Â ÃÂ¢m

* `math.gcd` xÃ¡Â»Â­ lÃÂ½ ÃÂÃÂºng (gcd(0, x) = |x|); tÃ¡Â»Â± cÃÂ i vÃÂ²ng `while b` cÃÂ©ng ÃÂÃÂºng.
  NhÃÂ°ng `gcd` sÃ¡Â»Â ÃÂ¢m trong C++ khÃÂ¡c Python Ã¢ÂÂ biÃ¡ÂºÂ¿t khi ÃÂÃ¡Â»Âc editorial nÃÂ°Ã¡Â»Âc ngoÃÂ i.

---

## Ã°ÂÂ§Âª TrÃÂ°Ã¡Â»Âng hÃ¡Â»Â£p ÃÂÃ¡ÂºÂ·c biÃ¡Â»Ât

* **n < 2** khÃÂ´ng nguyÃÂªn tÃ¡Â»Â (kÃ¡Â»Â cÃ¡ÂºÂ£ 0, 1, sÃ¡Â»Â ÃÂ¢m) Ã¢ÂÂ kiÃ¡Â»Âm tra ÃÂÃ¡ÂºÂ§u hÃÂ m.
* **SÃÂ ng N < 2**: `la_nt[0:2]` lÃ¡Â»Âi nÃ¡ÂºÂ¿u list ngÃ¡ÂºÂ¯n Ã¢ÂÂ ÃÂÃ¡ÂºÂ£m bÃ¡ÂºÂ£o N Ã¢ÂÂ¥ 2 hoÃ¡ÂºÂ·c xÃ¡Â»Â­ lÃÂ½ riÃÂªng.
* **mod = 1**: mÃ¡Â»Âi thÃ¡Â»Â© mod 1 = 0 Ã¢ÂÂ `pow(x, n, 1)` trÃ¡ÂºÂ£ 0, code tÃ¡Â»Â± cÃÂ i `1 % m`
  cÃÂ©ng ra 0. Ã¢ÂÂ
* **b chia hÃ¡ÂºÂ¿t cho M** (nghÃ¡Â»Âch ÃÂÃ¡ÂºÂ£o khÃÂ´ng tÃ¡Â»Ân tÃ¡ÂºÂ¡i): Fermat khÃÂ´ng ÃÂ¡p dÃ¡Â»Â¥ng Ã¢ÂÂ
  ÃÂÃ¡Â»Â chuÃ¡ÂºÂ©n trÃÂ¡nh trÃÂ°Ã¡Â»Âng hÃ¡Â»Â£p nÃÂ y hoÃ¡ÂºÂ·c yÃÂªu cÃ¡ÂºÂ§u xÃ¡Â»Â­ lÃÂ½ riÃÂªng.
* **C(n,k) vÃ¡Â»Âi k > n**: = 0 (khÃÂ´ng cÃÂ³ cÃÂ¡ch) Ã¢ÂÂ kiÃ¡Â»Âm tra biÃÂªn trong hÃÂ m C.

---

## Ã°ÂÂÂ Ã¡Â»Â¨ng dÃ¡Â»Â¥ng thÃ¡Â»Â±c tÃ¡ÂºÂ¿

* MÃÂ£ hÃÂ³a RSA (nguyÃÂªn tÃ¡Â»Â lÃ¡Â»Ân, Euclid mÃ¡Â»Â rÃ¡Â»Âng, lÃÂ©y thÃ¡Â»Â«a mod).
* BÃÂm, checksum, sinh sÃ¡Â»Â ngÃ¡ÂºÂ«u nhiÃÂªn (ÃÂÃ¡Â»Âng dÃÂ° tuyÃ¡ÂºÂ¿n tÃÂ­nh).
* LÃ¡Â»Âch, chu kÃ¡Â»Â³, ÃÂÃ¡Â»Âng bÃ¡Â»Â (LCM).

---

## Ã°ÂÂ§Â© BÃÂ i tÃ¡ÂºÂ­p

### BÃÂ i 1: CÃÂ i ÃÂÃ¡ÂºÂ·t cÃÂ¡ bÃ¡ÂºÂ£n Number Theory Number Theory

* **ÃÂÃ¡Â»Â bÃÂ i:** ViÃ¡ÂºÂ¿t hÃÂ m Number Theory_basic thÃ¡Â»Â±c hiÃ¡Â»Ân kiÃ¡Â»Âm tra nguyÃÂªn tÃ¡Â»Â.
* **Input:** (theo ÃÂÃ¡Â»Â bÃÂ i)
* **Output:** (theo ÃÂÃ¡Â»Â bÃÂ i)
* **GÃ¡Â»Â£i ÃÂ½:** CÃÂ i ÃÂÃ¡ÂºÂ·t theo ÃÂÃ¡Â»Ânh nghÃÂ©a.

### BÃÂ i 2: Trace code Number Theory Number Theory

* **ÃÂÃ¡Â»Â bÃÂ i:** Trace code: cho ÃÂoÃ¡ÂºÂ¡n code mÃ¡ÂºÂ«u Number Theory, hÃÂ£y viÃ¡ÂºÂ¿t ra kÃ¡ÂºÂ¿t quÃ¡ÂºÂ£.
* **Input:** (theo ÃÂÃ¡Â»Â bÃÂ i)
* **Output:** (theo ÃÂÃ¡Â»Â bÃÂ i)
* **GÃ¡Â»Â£i ÃÂ½:** ChÃ¡ÂºÂ¡y thÃ¡Â»Â§ tÃ¡Â»Â«ng bÃÂ°Ã¡Â»Âc.

### BÃÂ i 3: ÃÂiÃ¡Â»Ân khuyÃ¡ÂºÂ¿t Number Theory Number Theory

* **ÃÂÃ¡Â»Â bÃÂ i:** HoÃÂ n thiÃ¡Â»Ân hÃÂ m Number Theory ÃÂÃÂ£ cho sÃ¡ÂºÂµn.
* **Input:** (theo ÃÂÃ¡Â»Â bÃÂ i)
* **Output:** (theo ÃÂÃ¡Â»Â bÃÂ i)
* **GÃ¡Â»Â£i ÃÂ½:** HoÃÂ n thiÃ¡Â»Ân code cÃÂ²n thiÃ¡ÂºÂ¿u.

### BÃÂ i 4: So sÃÂ¡nh Number Theory Number Theory

* **ÃÂÃ¡Â»Â bÃÂ i:** So sÃÂ¡nh 2 cÃÂ¡ch giÃ¡ÂºÂ£i cho ToÃÂ¡n hÃ¡Â»Âc/SÃ¡Â»Â hÃ¡Â»Âc.
* **Input:** (theo ÃÂÃ¡Â»Â bÃÂ i)
* **Output:** (theo ÃÂÃ¡Â»Â bÃÂ i)
* **GÃ¡Â»Â£i ÃÂ½:** So sÃÂ¡nh ÃÂ°u nhÃÂ°Ã¡Â»Â£c ÃÂiÃ¡Â»Âm.

### BÃÂ i 5: ÃÂp dÃ¡Â»Â¥ng trÃ¡Â»Â±c tiÃ¡ÂºÂ¿p Number Theory Number Theory

* **ÃÂÃ¡Â»Â bÃÂ i:** ÃÂp dÃ¡Â»Â¥ng thuÃ¡ÂºÂ­t toÃÂ¡n Number Theory trÃ¡Â»Â±c tiÃ¡ÂºÂ¿p.
* **Input:** (theo ÃÂÃ¡Â»Â bÃÂ i)
* **Output:** (theo ÃÂÃ¡Â»Â bÃÂ i)
* **GÃ¡Â»Â£i ÃÂ½:** ÃÂp dÃ¡Â»Â¥ng trÃ¡Â»Â±c tiÃ¡ÂºÂ¿p thuÃ¡ÂºÂ­t toÃÂ¡n.

### BÃÂ i 6: BiÃ¡ÂºÂ¿n thÃ¡Â»Â ÃÂÃÂ¡n giÃ¡ÂºÂ£n Number Theory Number Theory

* **ÃÂÃ¡Â»Â bÃÂ i:** ViÃ¡ÂºÂ¿t biÃ¡ÂºÂ¿n thÃ¡Â»Â ÃÂÃÂ¡n giÃ¡ÂºÂ£n cÃ¡Â»Â¥a Number Theory.
* **Input:** (theo ÃÂÃ¡Â»Â bÃÂ i)
* **Output:** (theo ÃÂÃ¡Â»Â bÃÂ i)
* **GÃ¡Â»Â£i ÃÂ½:** Thay ÃÂÃ¡Â»Âi tham sÃ¡Â»Â nhÃ¡Â»Â.

### BÃÂ i 7: Debug Number Theory Number Theory

* **ÃÂÃ¡Â»Â bÃÂ i:** SÃ¡Â»Â­a lÃ¡Â»Âi trong code Number Theory cho trÃÂ°Ã¡Â»Âc.
* **Input:** (theo ÃÂÃ¡Â»Â bÃÂ i)
* **Output:** (theo ÃÂÃ¡Â»Â bÃÂ i)
* **GÃ¡Â»Â£i ÃÂ½:** SÃ¡Â»Â­a try/except.

### BÃÂ i 8: ÃÂÃ¡Â»Â phÃ¡Â»Â©c tÃ¡ÂºÂ¡p Number Theory Number Theory

* **ÃÂÃ¡Â»Â bÃÂ i:** TÃÂ­nh ÃÂÃ¡Â»Â phÃ¡Â»Â©c tÃ¡ÂºÂ¡p O() cÃ¡Â»Â¥a Number Theory.
* **Input:** (theo ÃÂÃ¡Â»Â bÃÂ i)
* **Output:** (theo ÃÂÃ¡Â»Â bÃÂ i)
* **GÃ¡Â»Â£i ÃÂ½:** ÃÂÃ¡ÂºÂ¿m phÃÂ©p toÃÂ¡n.

### BÃÂ i 9: KiÃ¡Â»Âm tra hiÃ¡Â»Âu Number Theory Number Theory

* **ÃÂÃ¡Â»Â bÃÂ i:** GiÃ¡ÂºÂ£i thÃÂ­ch bÃÂ°Ã¡Â»Âc quan trÃ¡Â»Âng cÃ¡Â»Â¥a Number Theory.
* **Input:** (theo ÃÂÃ¡Â»Â bÃÂ i)
* **Output:** (theo ÃÂÃ¡Â»Â bÃÂ i)
* **GÃ¡Â»Â£i ÃÂ½:** GiÃ¡ÂºÂ£i thÃÂ­ch logic.

### BÃÂ i 10: MÃ¡Â»Â rÃ¡Â»Âng Number Theory Number Theory

* **ÃÂÃ¡Â»Â bÃÂ i:** MÃ¡Â»Â rÃ¡Â»Âng Number Theory cho trÃÂ°Ã¡Â»Âng hÃ¡Â»Â£p mÃ¡Â»Âi.
* **Input:** (theo ÃÂÃ¡Â»Â bÃÂ i)
* **Output:** (theo ÃÂÃ¡Â»Â bÃÂ i)
* **GÃ¡Â»Â£i ÃÂ½:** MÃ¡Â»Â rÃ¡Â»Âng tham sÃ¡Â»Â.

### BÃÂ i 11: CÃÂ i ÃÂÃ¡ÂºÂ·t ÃÂÃ¡ÂºÂ§y ÃÂÃ¡Â»Â§ Number Theory

* **ÃÂÃ¡Â»Â bÃÂ i:** ViÃ¡ÂºÂ¿t chÃÂ°ÃÂ¡ng trÃÂ¬nh hoÃÂ n chÃ¡Â»Ânh cho Number Theory.
* **Input:** (theo ÃÂÃ¡Â»Â bÃÂ i)
* **Output:** (theo ÃÂÃ¡Â»Â bÃÂ i)
* **GÃ¡Â»Â£i ÃÂ½:** ViÃ¡ÂºÂ¿t full code.

### BÃÂ i 12: BiÃ¡ÂºÂ¿n thÃ¡Â»Â Number Theory

* **ÃÂÃ¡Â»Â bÃÂ i:** SÃ¡Â»Â­a thuÃ¡ÂºÂ­t toÃÂ¡n Number Theory.
* **Input:** (theo ÃÂÃ¡Â»Â bÃÂ i)
* **Output:** (theo ÃÂÃ¡Â»Â bÃÂ i)
* **GÃ¡Â»Â£i ÃÂ½:** SÃ¡Â»Â­a logic core.

### BÃÂ i 13: TÃ¡Â»Âi ÃÂ°u hÃÂ³a Number Theory

* **ÃÂÃ¡Â»Â bÃÂ i:** CÃ¡ÂºÂ£i tiÃ¡ÂºÂ¿n ÃÂÃ¡Â»Â phÃ¡Â»Â©c tÃ¡ÂºÂ¡p cÃ¡Â»Â¥a Number Theory.
* **Input:** (theo ÃÂÃ¡Â»Â bÃÂ i)
* **Output:** (theo ÃÂÃ¡Â»Â bÃÂ i)
* **GÃ¡Â»Â£i ÃÂ½:** CÃ¡ÂºÂ£i tiÃ¡ÂºÂ¿n cÃ¡ÂºÂ¥u trÃÂºc dÃ¡Â»Â¯ liÃ¡Â»Âu.

### BÃÂ i 14: KÃ¡ÂºÂ¿t hÃ¡Â»Â£p Number Theory

* **ÃÂÃ¡Â»Â bÃÂ i:** KÃ¡ÂºÂ¿t hÃ¡Â»Â£p Number Theory vÃ¡Â»Âi thuÃ¡ÂºÂ­t toÃÂ¡n khÃÂ¡c.
* **Input:** (theo ÃÂÃ¡Â»Â bÃÂ i)
* **Output:** (theo ÃÂÃ¡Â»Â bÃÂ i)
* **GÃ¡Â»Â£i ÃÂ½:** KÃ¡ÂºÂ¿t hÃ¡Â»Â£p 2 hÃÂ m.

### BÃÂ i 15: Trace phÃ¡Â»Â©c tÃ¡ÂºÂ¡p Number Theory

* **ÃÂÃ¡Â»Â bÃÂ i:** ChÃ¡ÂºÂ¡y trace thÃ¡Â»Â§ cÃÂ´ng cho Number Theory.
* **Input:** (theo ÃÂÃ¡Â»Â bÃÂ i)
* **Output:** (theo ÃÂÃ¡Â»Â bÃÂ i)
* **GÃ¡Â»Â£i ÃÂ½:** ViÃ¡ÂºÂ¿t nhÃ¡ÂºÂ­t kÃÂ½ chÃ¡ÂºÂ¡y.

### BÃÂ i 16: BiÃ¡ÂºÂ¿n thÃ¡Â»Â ngÃÂ°Ã¡Â»Â£c Number Theory

* **ÃÂÃ¡Â»Â bÃÂ i:** TÃÂ¬m input tÃ¡Â»Â« output cho Number Theory.
* **Input:** (theo ÃÂÃ¡Â»Â bÃÂ i)
* **Output:** (theo ÃÂÃ¡Â»Â bÃÂ i)
* **GÃ¡Â»Â£i ÃÂ½:** NgÃÂ°Ã¡Â»Â£c logic.

### BÃÂ i 17: GiÃ¡Â»Âi hÃ¡ÂºÂ¡n lÃ¡Â»Ân Number Theory

* **ÃÂÃ¡Â»Â bÃÂ i:** XÃ¡Â»Â­ lÃÂ½ n lÃ¡Â»Ân cho Number Theory.
* **Input:** (theo ÃÂÃ¡Â»Â bÃÂ i)
* **Output:** (theo ÃÂÃ¡Â»Â bÃÂ i)
* **GÃ¡Â»Â£i ÃÂ½:** DÃÂ¹ng cÃ¡ÂºÂ¥u trÃÂºc dÃ¡Â»Â¯ liÃ¡Â»Âu phÃÂ¹ hÃ¡Â»Â£p.

### BÃÂ i 18: So sÃÂ¡nh thÃ¡Â»Â±c tÃ¡ÂºÂ¿ Number Theory

* **ÃÂÃ¡Â»Â bÃÂ i:** So sÃÂ¡nh thÃ¡Â»Â±c tÃ¡ÂºÂ¿ cÃÂ¡c thuÃ¡ÂºÂ­t toÃÂ¡n.
* **Input:** (theo ÃÂÃ¡Â»Â bÃÂ i)
* **Output:** (theo ÃÂÃ¡Â»Â bÃÂ i)
* **GÃ¡Â»Â£i ÃÂ½:** DÃÂ¹ng timeit.

### BÃÂ i 19: MÃ¡Â»Â rÃ¡Â»Âng Number Theory

* **ÃÂÃ¡Â»Â bÃÂ i:** MÃ¡Â»Â rÃ¡Â»Âng Number Theory.
* **Input:** (theo ÃÂÃ¡Â»Â bÃÂ i)
* **Output:** (theo ÃÂÃ¡Â»Â bÃÂ i)
* **GÃ¡Â»Â£i ÃÂ½:** ThÃÂªm tham sÃ¡Â»Â.

### BÃÂ i 20: ÃÂp dÃ¡Â»Â¥ng thÃ¡Â»Â±c tÃ¡ÂºÂ¿ Number Theory

* **ÃÂÃ¡Â»Â bÃÂ i:** ÃÂp dÃ¡Â»Â¥ng Number Theory vÃÂ o thÃ¡Â»Â±c tÃ¡ÂºÂ¿.
* **Input:** (theo ÃÂÃ¡Â»Â bÃÂ i)
* **Output:** (theo ÃÂÃ¡Â»Â bÃÂ i)
* **GÃ¡Â»Â£i ÃÂ½:** ÃÂp dÃ¡Â»Â¥ng thÃ¡Â»Â±c tÃ¡ÂºÂ¿.

### BÃÂ i 21: ThiÃ¡ÂºÂ¿t kÃ¡ÂºÂ¿ thuÃ¡ÂºÂ­t toÃÂ¡n Number Theory

* **ÃÂÃ¡Â»Â bÃÂ i:** ThiÃ¡ÂºÂ¿t kÃ¡ÂºÂ¿ thuÃ¡ÂºÂ­t toÃÂ¡n O() cho Number Theory.
* **Input:** (theo ÃÂÃ¡Â»Â bÃÂ i)
* **Output:** (theo ÃÂÃ¡Â»Â bÃÂ i)
* **GÃ¡Â»Â£i ÃÂ½:** Tham khÃ¡ÂºÂ£o CLRS.

### BÃÂ i 22: ChÃ¡Â»Â©ng minh Number Theory

* **ÃÂÃ¡Â»Â bÃÂ i:** ChÃ¡Â»Â©ng minh ÃÂÃÂºng ÃÂÃ¡ÂºÂ¯n cho Number Theory.
* **Input:** (theo ÃÂÃ¡Â»Â bÃÂ i)
* **Output:** (theo ÃÂÃ¡Â»Â bÃÂ i)
* **GÃ¡Â»Â£i ÃÂ½:** DÃÂ¹ng exchange argument.

### BÃÂ i 23: GiÃ¡Â»Âi hÃ¡ÂºÂ¡n dÃÂ°Ã¡Â»Âi Number Theory

* **ÃÂÃ¡Â»Â bÃÂ i:** ChÃ¡Â»Â©ng minh lower bound cho Number Theory.
* **Input:** (theo ÃÂÃ¡Â»Â bÃÂ i)
* **Output:** (theo ÃÂÃ¡Â»Â bÃÂ i)
* **GÃ¡Â»Â£i ÃÂ½:** DÃÂ¹ng adversary argument.

### BÃÂ i 24: TÃ¡Â»Âi ÃÂ°u cÃ¡Â»Â±c hÃ¡ÂºÂ¡n Number Theory

* **ÃÂÃ¡Â»Â bÃÂ i:** TÃ¡Â»Âi ÃÂ°u Number Theory chÃ¡ÂºÂ¡y trong time limit.
* **Input:** (theo ÃÂÃ¡Â»Â bÃÂ i)
* **Output:** (theo ÃÂÃ¡Â»Â bÃÂ i)
* **GÃ¡Â»Â£i ÃÂ½:** Profile + tÃ¡Â»Âi ÃÂ°u.

### BÃÂ i 25: BiÃ¡ÂºÂ¿n thÃ¡Â»Â nghiÃÂªn cÃ¡Â»Â©u Number Theory

* **ÃÂÃ¡Â»Â bÃÂ i:** ViÃ¡ÂºÂ¿t biÃ¡ÂºÂ¿n thÃ¡Â»Â cÃ¡Â»Â¥a Number Theory.
* **Input:** (theo ÃÂÃ¡Â»Â bÃÂ i)
* **Output:** (theo ÃÂÃ¡Â»Â bÃÂ i)
* **GÃ¡Â»Â£i ÃÂ½:** Tham khÃ¡ÂºÂ£o paper.

### BÃÂ i 26: KÃ¡ÂºÂ¿t hÃ¡Â»Â£p nÃÂ¢ng cao Number Theory

* **ÃÂÃ¡Â»Â bÃÂ i:** KÃ¡ÂºÂ¿t hÃ¡Â»Â£p 3 thuÃ¡ÂºÂ­t toÃÂ¡n cho Number Theory.
* **Input:** (theo ÃÂÃ¡Â»Â bÃÂ i)
* **Output:** (theo ÃÂÃ¡Â»Â bÃÂ i)
* **GÃ¡Â»Â£i ÃÂ½:** PhÃÂ¢n chia rÃÂµ rÃÂ ng.

### BÃÂ i 27: ÃÂÃ¡Â»Âi khÃÂ¡ng Number Theory

* **ÃÂÃ¡Â»Â bÃÂ i:** ViÃ¡ÂºÂ¿t generator test phÃÂ¡ Number Theory.
* **Input:** (theo ÃÂÃ¡Â»Â bÃÂ i)
* **Output:** (theo ÃÂÃ¡Â»Â bÃÂ i)
* **GÃ¡Â»Â£i ÃÂ½:** Sinh test adversarial.

### BÃÂ i 28: MÃ¡Â»Â rÃ¡Â»Âng lÃÂ½ thuyÃ¡ÂºÂ¿t Number Theory

* **ÃÂÃ¡Â»Â bÃÂ i:** MÃ¡Â»Â rÃ¡Â»Âng ÃÂÃ¡Â»Ânh lÃÂ½ cho Number Theory.
* **Input:** (theo ÃÂÃ¡Â»Â bÃÂ i)
* **Output:** (theo ÃÂÃ¡Â»Â bÃÂ i)
* **GÃ¡Â»Â£i ÃÂ½:** Generalize ÃÂÃ¡Â»Ânh lÃÂ½.

### BÃÂ i 29: CÃÂ i ÃÂÃ¡ÂºÂ·t production Number Theory

* **ÃÂÃ¡Â»Â bÃÂ i:** CÃÂ i Number Theory production-ready.
* **Input:** (theo ÃÂÃ¡Â»Â bÃÂ i)
* **Output:** (theo ÃÂÃ¡Â»Â bÃÂ i)
* **GÃ¡Â»Â£i ÃÂ½:** Production checklist.

### BÃÂ i 30: NghiÃÂªn cÃ¡Â»Â©u mÃ¡Â»Â Number Theory

* **ÃÂÃ¡Â»Â bÃÂ i:** ÃÂÃ¡Â»Â xuÃ¡ÂºÂ¥t cÃ¡ÂºÂ£i tiÃ¡ÂºÂ¿n mÃ¡Â»Âi cho Number Theory.
* **Input:** (theo ÃÂÃ¡Â»Â bÃÂ i)
* **Output:** (theo ÃÂÃ¡Â»Â bÃÂ i)
* **GÃ¡Â»Â£i ÃÂ½:** ÃÂÃ¡Â»Âc paper mÃ¡Â»Âi.


## Ã¢ÂÂ ÃÂÃÂ¡p ÃÂ¡n

> Ã°ÂÂÂ¡ **HÃÂ£y tÃ¡Â»Â± lÃÂ m bÃÂ i tÃ¡ÂºÂ­p trÃÂ°Ã¡Â»Âc** rÃ¡Â»Âi mÃ¡Â»Âi mÃ¡Â»Â ÃÂÃÂ¡p ÃÂ¡n.

<details>
<summary>Ã¢ÂÂ BÃÂ i 1: SÃÂ ng tay</summary>

* p=2: loÃ¡ÂºÂ¡i 4,6,...,50 (chÃ¡ÂºÂµn > 2).
* p=3: loÃ¡ÂºÂ¡i 9,15,21,27,33,39,45 (lÃ¡ÂºÂ» chÃÂ°a bÃ¡Â»Â loÃ¡ÂºÂ¡i).
* p=5: loÃ¡ÂºÂ¡i 25,35,49 (bÃ¡ÂºÂ¯t ÃÂÃ¡ÂºÂ§u 25).
* p=7: loÃ¡ÂºÂ¡i ÃÂÃÂºng sÃ¡Â»Â 49 (bÃ¡Â»Âi 7 tiÃ¡ÂºÂ¿p theo 77 > 50). SÃ¡Â»Â 49 chÃÂ°a bÃ¡Â»Â loÃ¡ÂºÂ¡i Ã¡Â»Â cÃÂ¡c
  bÃÂ°Ã¡Â»Âc trÃÂ°Ã¡Â»Âc vÃÂ¬ ÃÂ°Ã¡Â»Âc nguyÃÂªn tÃ¡Â»Â nhÃ¡Â»Â nhÃ¡ÂºÂ¥t cÃ¡Â»Â¥a nÃÂ³ chÃÂ­nh lÃÂ  7.
* NguyÃÂªn tÃ¡Â»Â Ã¢ÂÂ¤ 50: 2,3,5,7,11,13,17,19,23,29,31,37,41,43,47 = **15 sÃ¡Â»Â**.

</details>

<details>
<summary>Ã¢ÂÂ BÃÂ i 2: Euclid tay</summary>

270 % 192 = 78 Ã¢ÂÂ (192, 78); 192 % 78 = 36 Ã¢ÂÂ (78, 36); 78 % 36 = 6 Ã¢ÂÂ
(36, 6); 36 % 6 = 0 Ã¢ÂÂ (6, 0) Ã¢ÂÂ **gcd = 6**.

```python
import math
assert math.gcd(270, 192) == 6
```

</details>

<details>
<summary>Ã¢ÂÂ BÃÂ i 3: RÃÂºt gÃ¡Â»Ân</summary>

```python
import math

def rut_gon(a, b):
    u = math.gcd(a, b)
    return f"{a // u}/{b // u}"

print(rut_gon(1071, 462))  # 51/22
```

1071/21 = 51, 462/21 = 22 Ã¢ÂÂ **51/22**. Ã¢ÂÂ

</details>

<details>
<summary>Ã¢ÂÂ BÃÂ i 4: SÃÂ ng ÃÂoÃ¡ÂºÂ¡n</summary>

```python
import math

def dem_nt_doan(l, r):
    la_nt = bytearray(b"\x01") * (r - l + 1)
    if l == 0:
        la_nt[0] = 0
    if l <= 1 <= r:
        la_nt[1 - l] = 0
    for p in range(2, math.isqrt(r) + 1):
        # bÃ¡Â»Âi nhÃ¡Â»Â nhÃ¡ÂºÂ¥t cÃ¡Â»Â¥a p mÃÂ  Ã¢ÂÂ¥ l (vÃÂ  Ã¢ÂÂ¥ p*p)
        bat_dau = max(p * p, (l + p - 1) // p * p)
        for m in range(bat_dau, r + 1, p):
            la_nt[m - l] = 0
    return sum(la_nt)
```

VÃÂ¬ sao chÃ¡Â»Â cÃ¡ÂºÂ§n p Ã¢ÂÂ¤ Ã¢ÂÂr: mÃ¡Â»Âi hÃ¡Â»Â£p sÃ¡Â»Â Ã¢ÂÂ¤ r ÃÂÃ¡Â»Âu cÃÂ³ ÃÂ°Ã¡Â»Âc nguyÃÂªn tÃ¡Â»Â Ã¢ÂÂ¤ Ã¢ÂÂr (nhÃÂ° mÃ¡Â»Â¥c 1).
ÃÂÃ¡Â»Â phÃ¡Â»Â©c tÃ¡ÂºÂ¡p O((rÃ¢ÂÂl+1) log log r + Ã¢ÂÂr) Ã¢ÂÂ sÃÂ ng ÃÂÃÂ°Ã¡Â»Â£c ÃÂoÃ¡ÂºÂ¡n tÃ¡Â»Âi 10ÃÂ¹ÃÂ².

</details>

<details>
<summary>Ã¢ÂÂ BÃÂ i 5: Fibonacci mod M</summary>

```python
MOD = 10**9 + 7

def nhan(a, b):
    return [[(a[0][0]*b[0][0] + a[0][1]*b[1][0]) % MOD,
             (a[0][0]*b[0][1] + a[0][1]*b[1][1]) % MOD],
            [(a[1][0]*b[0][0] + a[1][1]*b[1][0]) % MOD,
             (a[1][0]*b[0][1] + a[1][1]*b[1][1]) % MOD]]

def mu_mt(mt, n):
    kq = [[1, 0], [0, 1]]
    while n:
        if n & 1:
            kq = nhan(kq, mt)
        mt = nhan(mt, mt)
        n >>= 1
    return kq

def fib_mod(n):
    if n == 0:
        return 0
    return mu_mt([[1, 1], [1, 0]], n - 1)[0][0]
```

[[1,1],[1,0]]Ã¢ÂÂ¿ chÃ¡Â»Â©a F(n+1), F(n)... nÃÂªn F(n) = gÃÂ³c [0][0] cÃ¡Â»Â¥a mÃÂ© (nÃ¢ÂÂ1).
O(log n) phÃÂ©p nhÃÂ¢n ma trÃ¡ÂºÂ­n 2ÃÂ2 Ã¢ÂÂ n = 10ÃÂ¹Ã¢ÂÂ¸ chÃ¡Â»Â ~60 bÃÂ°Ã¡Â»Âc.

</details>

<details>
<summary>Ã¢ÂÂ BÃÂ i 6: C(n,k) mod</summary>

DÃÂ¹ng nguyÃÂªn code mÃ¡Â»Â¥c 6:

```python
MOD = 10**9 + 7
fact, inv_fact = chuan_bi_to_hop(10**6)
assert C(10, 3, fact, inv_fact) == 120
print(C(100, 50, fact, inv_fact))  # 538992043
```

C(100,50) = 100891344545564193334812497256, mod 10Ã¢ÂÂ¹+7 = 538992043
(kiÃ¡Â»Âm chÃ¡Â»Â©ng bÃ¡ÂºÂ±ng `math.comb(100, 50) % MOD`).

</details>

<details>
<summary>Ã¢ÂÂ BÃÂ i 7: TÃ¡Â»Âng ÃÂ°Ã¡Â»Âc</summary>

360 = 2ÃÂ³ÃÂ·3ÃÂ²ÃÂ·5ÃÂ¹. SÃ¡Â»Â ÃÂ°Ã¡Â»Âc = 4ÃÂ3ÃÂ2 = **24**. TÃ¡Â»Âng = (2Ã¢ÂÂ´Ã¢ÂÂ1)/1 ÃÂ (3ÃÂ³Ã¢ÂÂ1)/2 ÃÂ
(5ÃÂ²Ã¢ÂÂ1)/4 = 15 ÃÂ 13 ÃÂ 6 = **1170**. KiÃ¡Â»Âm chÃ¡Â»Â©ng brute force:

```python
n = 360
uoc = [d for d in range(1, n + 1) if n % d == 0]
assert len(uoc) == 24 and sum(uoc) == 1170
```

</details>

<details>
<summary>Ã¢ÂÂ BÃÂ i 8: MÃÂ© thÃÂ¡p (nÃÂ¢ng cao)</summary>

ÃÂ tÃÂ°Ã¡Â»Âng (Euler + overflow-cap): ÃÂÃ¡Â»Ânh nghÃÂ©a ÃÂÃ¡Â»Â quy f(k, m) = thÃÂ¡p k sÃ¡Â»Â 2 mod m.
NÃ¡ÂºÂ¿u m = 1 Ã¢ÂÂ 0. NgÃÂ°Ã¡Â»Â£c lÃ¡ÂºÂ¡i: ÃÂ = phi(m); e = f(kÃ¢ÂÂ1, ÃÂ); sÃ¡Â»Â mÃÂ© thÃ¡ÂºÂ­t = e +
(ÃÂ nÃ¡ÂºÂ¿u thÃÂ¡p con Ã¢ÂÂ¥ ÃÂ Ã¢ÂÂ "ÃÂÃ¡Â»Â§ lÃ¡Â»Ân" thÃÂ¬ cÃ¡Â»Âng bÃÂ¹ ÃÂÃ¡Â»Â Euler ÃÂÃÂºng); kÃ¡ÂºÂ¿t quÃ¡ÂºÂ£
pow(2, mÃÂ©_thÃ¡ÂºÂ­t, m).

```python
import math

def phi(n):
    kq, x, p = n, n, 2
    while p * p <= x:
        if x % p == 0:
            while x % p == 0:
                x //= p
            kq -= kq // p
        p += 1 if p == 2 else 2
    if x > 1:
        kq -= kq // x
    return kq

def du_lon(k, gioi_han):
    # thÃÂ¡p k sÃ¡Â»Â 2 cÃÂ³ Ã¢ÂÂ¥ gioi_han khÃÂ´ng? (tÃÂ­nh cÃÂ³ chÃ¡ÂºÂ·n trÃÂªn)
    if gioi_han <= 1:
        return True
    if k == 1:
        return 2 >= gioi_han
    # 2^e Ã¢ÂÂ¥ G Ã¢ÂÂº e Ã¢ÂÂ¥ log2(G); ÃÂÃ¡Â»Â quy vÃ¡Â»Âi log
    import math as mth
    return du_lon(k - 1, mth.log2(gioi_han))

def thap(k, m):
    if m == 1:
        return 0
    if k == 1:
        return 2 % m
    ph = phi(m)
    e = thap(k - 1, ph)
    if du_lon(k - 1, ph):
        e += ph
    return pow(2, e, m)
```

ÃÂÃÂ¢y lÃÂ  bÃÂ i khÃÂ³ cÃ¡ÂºÂ¥p quÃ¡Â»Âc gia Ã¢ÂÂ hiÃ¡Â»Âu ÃÂÃÂ°Ã¡Â»Â£c lÃ¡Â»Âi giÃ¡ÂºÂ£i ÃÂÃÂ£ lÃÂ  thÃÂ nh cÃÂ´ng;
cÃÂ i ÃÂÃÂºng + phÃÂ¢n tÃÂ­ch overflow-cap lÃÂ  xuÃ¡ÂºÂ¥t sÃ¡ÂºÂ¯c.

</details>

<details>
<summary>Ã¢ÂÂ BÃÂ i 9: GÃ¡ÂºÂ·p lÃ¡ÂºÂ¡i sau bao lÃÂ¢u</summary>

```python
import math

def gap_lai(*chu_ky):
    kq = 1
    for c in chu_ky:
        kq = kq // math.gcd(kq, c) * c   # lcm(a,b) = a*b/gcd (chia trÃÂ°Ã¡Â»Âc!)
    return kq

assert gap_lai(4, 6) == 12
assert gap_lai(4, 6, 8) == 24
```

CÃÂ¹ng chÃ¡Â»Âp Ã¢ÂÂº thÃ¡Â»Âi gian lÃÂ  bÃ¡Â»Âi chung Ã¢ÂÂ ÃÂÃÂ¡p ÃÂ¡n lÃÂ  BCNN. `kq // gcd * c` (chia
trÃÂ°Ã¡Â»Âc nhÃÂ¢n sau) trÃÂ¡nh sÃ¡Â»Â phÃÂ¬nh trung gian Ã¢ÂÂ thÃÂ³i quen tÃ¡Â»Â« C++ vÃ¡ÂºÂ«n tÃ¡Â»Ât cho Python
(nhanh hÃÂ¡n vÃ¡Â»Âi sÃ¡Â»Â khÃ¡Â»Âng lÃ¡Â»Â).

</details>

<details>
<summary>Ã¢ÂÂ BÃÂ i 10: ÃÂÃ¡ÂºÂ¿m ÃÂ°Ã¡Â»Âc 2 cÃÂ¡ch</summary>

```python
import time

def dem_uoc_naive(n):
    return sum(1 for d in range(1, n + 1) if n % d == 0)

def dem_uoc_can(n):
    import math
    dem, r = 0, math.isqrt(n)
    for d in range(1, r + 1):
        if n % d == 0:
            dem += 2 if d * d != n else 1   # cÃ¡ÂºÂ·p (d, n//d), trÃ¡Â»Â« chÃÂ­nh phÃÂ°ÃÂ¡ng
    return dem

n = 999983 * 999979
t0 = time.perf_counter()
assert dem_uoc_can(n) == 4
t1 = time.perf_counter()
print(f"Can bac 2: {t1 - t0:.3f}s")   # ~0.3s (10^6 vÃÂ²ng)
# dem_uoc_naive(n): 10^12 vÃÂ²ng ~ hÃÂ ng giÃ¡Â»Â -> KHÃÂNG CHÃ¡ÂºÂ Y, chÃ¡Â»Â tÃÂ­nh lÃÂ½ thuyÃ¡ÂºÂ¿t!
```

n = 999983 ÃÂ 999979 cÃÂ³ ÃÂÃÂºng 4 ÃÂ°Ã¡Â»Âc (1, 2 sÃ¡Â»Â nguyÃÂªn tÃ¡Â»Â, n). CÃÂ¡ch naive 10ÃÂ¹ÃÂ² vÃÂ²ng
Ã¢ÂÂ hÃÂ ng giÃ¡Â»Â/ngÃÂ y; cÃÂ¡ch cÃÂn 10Ã¢ÂÂ¶ vÃÂ²ng Ã¢ÂÂ 0.3s. BÃÂ i hÃ¡Â»Âc: **ÃÂÃ¡ÂºÂ¿m bÃ¡ÂºÂ±ng cÃ¡ÂºÂ·p ÃÂ°Ã¡Â»Âc, khÃÂ´ng
bao giÃ¡Â»Â duyÃ¡Â»Ât tÃ¡Â»Âi n** Ã¢ÂÂ vÃÂ  vÃ¡Â»Âi n Ã¢ÂÂ¤ 10ÃÂ¹ÃÂ² thÃÂ¬ O(Ã¢ÂÂn) luÃÂ´n ÃÂÃ¡Â»Â§.

</details>

<details>
<summary>Ã¢ÂÂ BÃÂ i 11: TÃ¡Â»Â hÃ¡Â»Â£p 1 truy vÃ¡ÂºÂ¥n</summary>

```python
MOD = 10**9 + 7

def Cn_k_1_truy_van(n, k):
    if k < 0 or k > n:
        return 0
    k = min(k, n - k)          # C(n,k) = C(n,n-k): vÃÂ²ng lÃ¡ÂºÂ·p ngÃ¡ÂºÂ¯n hÃÂ¡n!
    tu = mau = 1
    for i in range(k):
        tu = tu * (n - i) % MOD
        mau = mau * (i + 1) % MOD
    return tu * pow(mau, MOD - 2, MOD) % MOD

import math
assert Cn_k_1_truy_van(100, 50) == math.comb(100, 50) % MOD
assert Cn_k_1_truy_van(10, 3) == 120
```

O(k) mÃ¡Â»Âi truy vÃ¡ÂºÂ¥n, O(1) nhÃ¡Â»Â. DÃÂ¹ng khi q nhÃ¡Â»Â (vÃÂ i truy vÃ¡ÂºÂ¥n) hoÃ¡ÂºÂ·c n quÃÂ¡ lÃ¡Â»Ân
khÃÂ´ng tiÃ¡Â»Ân xÃ¡Â»Â­ lÃÂ½ nÃ¡Â»Âi. q Ã¢ÂÂ¥ 10Ã¢ÂÂµ Ã¢ÂÂ bÃ¡ÂºÂ£ng giai thÃ¡Â»Â«a (BÃÂ i 5) thÃ¡ÂºÂ¯ng vÃÂ¬ O(1)/truy vÃ¡ÂºÂ¥n
sau O(N) mÃ¡Â»Ât lÃ¡ÂºÂ§n. ChÃ¡Â»Ân cÃÂ´ng cÃ¡Â»Â¥ theo q!

</details>

<details>
<summary>Ã¢ÂÂ BÃÂ i 12: HÃÂ m phi Euler</summary>

```python
def phi(n):
    ket_qua, x, p = n, n, 2
    while p * p <= x:
        if x % p == 0:
            while x % p == 0:
                x //= p
            ket_qua -= ket_qua // p   # bÃ¡Â»Â cÃÂ¡c bÃ¡Â»Âi cÃ¡Â»Â¥a p
        p += 1 if p == 2 else 2
    if x > 1:
        ket_qua -= ket_qua // x
    return ket_qua

assert phi(36) == 12 and phi(10**9 + 7) == 10**9 + 6 and phi(1) == 1
```

VÃ¡Â»Âi n = Ã¢ÂÂp^e: tÃ¡Â»Â lÃ¡Â»Â sÃ¡Â»Â nguyÃÂªn tÃ¡Â»Â cÃÂ¹ng nhau vÃ¡Â»Âi n lÃÂ  Ã¢ÂÂ(1 Ã¢ÂÂ 1/p) Ã¢ÂÂ nhÃÂ¢n vÃ¡Â»Âi n.
Ã¡Â»Â¨ng dÃ¡Â»Â¥ng ÃÂÃÂ£ gÃ¡ÂºÂ·p: `pow(b, MOD-2, MOD)` (BÃÂ i 5) ÃÂÃÂºng vÃÂ¬ phi(MOD) = MODÃ¢ÂÂ1 khi MOD
nguyÃÂªn tÃ¡Â»Â (Fermat nhÃ¡Â»Â lÃÂ  trÃÂ°Ã¡Â»Âng hÃ¡Â»Â£p riÃÂªng cÃ¡Â»Â¥a Euler!). HiÃ¡Â»Âu phi = hiÃ¡Â»Âu vÃÂ¬ sao
nghÃ¡Â»Âch ÃÂÃ¡ÂºÂ£o modular tÃ¡Â»Ân tÃ¡ÂºÂ¡i.

</details>

---

## Ã°ÂÂ§Â  ThÃ¡Â»Â­ thÃÂ¡ch

**ThÃ¡Â»Â­ thÃÂ¡ch HSG:** ÃÂÃ¡ÂºÂ¿m sÃ¡Â»Â nguyÃÂªn tÃ¡Â»Â Ã¢ÂÂ¤ 10ÃÂ¹ÃÂ¹ (ÃÂ(10ÃÂ¹ÃÂ¹) = 4118054813) trong 2 giÃÂ¢y
bÃ¡ÂºÂ±ng **sÃÂ ng Meissel-Lehmer** (ÃÂÃ¡ÂºÂ¿m nguyÃÂªn tÃ¡Â»Â O(n^(2/3))). *GÃ¡Â»Â£i ÃÂ½: cÃÂ´ng thÃ¡Â»Â©c truy
hÃ¡Â»Âi ÃÂ(x) = ÃÂ(x, a) + b Ã¢ÂÂ ... vÃ¡Â»Âi a = ÃÂ(x^(1/4)). ÃÂÃÂ¢y lÃÂ  thuÃ¡ÂºÂ­t toÃÂ¡n ÃÂÃ¡ÂºÂ¿m nguyÃÂªn tÃ¡Â»Â
chuÃ¡ÂºÂ©n cho n lÃ¡Â»Ân Ã¢ÂÂ cÃÂ i ÃÂÃÂ°Ã¡Â»Â£c thÃÂ¬ khÃÂ´ng cÃÂ²n bÃÂ i sÃÂ ng nÃÂ o lÃÂ m khÃÂ³ bÃ¡ÂºÂ¡n.*

---

## Ã°ÂÂÂ TÃÂ³m tÃ¡ÂºÂ¯t

| KhÃÂ¡i niÃ¡Â»Âm | NÃ¡Â»Âi dung |
|---|---|
| Ã°ÂÂÂ¢ NguyÃÂªn tÃ¡Â»Â 1 sÃ¡Â»Â | ThÃ¡Â»Â­ ÃÂÃ¡ÂºÂ¿n `isqrt`, chÃ¡Â»Â lÃ¡ÂºÂ» Ã¢ÂÂ O(Ã¢ÂÂn) |
| Ã°ÂÂªÂ¤ SÃÂ ng | Eratosthenes O(n log log n); bÃ¡ÂºÂ¯t ÃÂÃ¡ÂºÂ§u iÃÂ²; slice gÃÂ¡n |
| Ã¢ÂÂ Euclid | GCD O(log); LCM qua GCD; `math.gcd` |
| Ã¢ÂÂ¡ MÃÂ© mod | LÃÂ©y thÃ¡Â»Â«a nhanh O(log n); `pow(x,n,m)` cÃÂ³ sÃ¡ÂºÂµn |
| Ã°ÂÂÂ Fermat | bÃ¢ÂÂ»ÃÂ¹ = b^(MÃ¢ÂÂ2); C(n,k) bÃ¡ÂºÂ±ng fact + inv_fact |
| Ã¢ÂÂ Ã¯Â¸Â BÃ¡ÂºÂ«y | Float vÃ¡Â»Âi sÃ¡Â»Â lÃ¡Â»Ân Ã¢ÂÂ `isqrt`, `//`, int |

---

## Ã°ÂÂÂ  BÃÂ i tÃ¡ÂºÂ­p vÃ¡Â»Â nhÃÂ 

> Ã°ÂÂÂ LÃÂ m vÃÂ o vÃ¡Â»Â (hoÃ¡ÂºÂ·c nÃ¡Â»Âp GV). ÃÂÃÂ¡p ÃÂ¡n chi tiÃ¡ÂºÂ¿t sÃ¡ÂºÂ½ bÃ¡Â»Â sung trong ÃÂÃ¡Â»Â£t hoÃÂ n thiÃ¡Â»Ân.

1. **SÃÂ ng lÃ¡Â»Âc:** viÃ¡ÂºÂ¿t sÃÂ ng Eratosthenes tÃÂ¬m sÃ¡Â»Â nguyÃÂªn tÃ¡Â»Â Ã¢ÂÂ¤ 10Ã¢ÂÂ¶ Ã¢ÂÂ so vÃ¡Â»Âi `is_prime` lÃ¡ÂºÂ·p Ã¢ÂÂn.
2. **Euclid & lÃÂ©y thÃ¡Â»Â«a nhanh:** cÃÂ i `gcd` vÃÂ  `pow_mod(a, n, m)` tay (khÃÂ´ng dÃÂ¹ng `math`/`pow`) Ã¢ÂÂ test 5 cÃ¡ÂºÂ·p sÃ¡Â»Â lÃ¡Â»Ân.
3. **TÃ¡Â»Â hÃ¡Â»Â£p C(n,k) mod M:** giÃ¡ÂºÂ£i bÃÂ i chÃ¡Â»Ân k mÃÂ³n tÃ¡Â»Â« n mÃÂ³n, kÃ¡ÂºÂ¿t quÃ¡ÂºÂ£ modulo 10Ã¢ÂÂ¹+7 Ã¢ÂÂ dÃÂ¹ng Fermat + fact/invfact.

---

## Ã°ÂÂÂ Tra cÃ¡Â»Â©u nhanh Ã¢ÂÂ SÃÂ ng, Euclid, lÃÂ©y thÃ¡Â»Â«a, Fermat, tÃ¡Â»Â hÃ¡Â»Â£p

| KÃ¡Â»Â¹ thuÃ¡ÂºÂ­t | Template | VÃÂ­ dÃ¡Â»Â¥ |
|---|---|---|
| SÃÂ ng Eratosthenes | `s = [True]*(n+1); for i in range(2, isqrt(n)+1):` | LiÃ¡Â»Ât kÃÂª nguyÃÂªn tÃ¡Â»Â Ã¢ÂÂ¤ 10Ã¢ÂÂ¶ |
| KiÃ¡Â»Âm tra nguyÃÂªn tÃ¡Â»Â | Miller-Rabin (n Ã¢ÂÂ¤ 10ÃÂ¹Ã¢ÂÂ¸) | `pow(a, n-1, n) == 1` |
| GCD | `def gcd(a,b): return gcd(b, a%b) if b else a` | `gcd(48, 18)` Ã¢ÂÂ 6 |
| LÃÂ©y thÃ¡Â»Â«a nhanh | `pow_mod(x, n, m)` chia ÃÂÃÂ´i mÃÂ© | `pow(x, n, m)` cÃÂ³ sÃ¡ÂºÂµn |
| Fermat nhÃ¡Â»Â | `a^(p-1) Ã¢ÂÂ¡ 1 (mod p)` | NghÃ¡Â»Âch ÃÂÃ¡ÂºÂ£o modulo |
| TÃ¡Â»Â hÃ¡Â»Â£p C(n,k) mod p | `fact[n] * invfact[k] * invfact[n-k] % p` | `n, k Ã¢ÂÂ¤ 10Ã¢ÂÂ¶` |

**Ghi nhÃ¡Â»Â:** Python cÃÂ³ sÃ¡ÂºÂµn `math.gcd`, `math.comb`, `pow(x, n, m)` Ã¢ÂÂ thi dÃÂ¹ng luÃÂ´n, tÃ¡Â»Â± cÃÂ i chÃ¡Â»Â ÃÂÃ¡Â»Â hiÃ¡Â»Âu bÃ¡ÂºÂ£n chÃ¡ÂºÂ¥t.

---


---

## Ã°ÂÂÂ Cheatsheet Ã¢ÂÂ SÃÂ ng, Euclid, lÃÂ©y thÃ¡Â»Â«a, Fermat, tÃ¡Â»Â hÃ¡Â»Â£p

| KÃ¡Â»Â¹ thuÃ¡ÂºÂ­t | Template | VÃÂ­ dÃ¡Â»Â¥ |
|---|---|---|
| SÃÂ ng Eratosthenes | `s = [True]*(n+1); for i in range(2, isqrt(n)+1):` | LiÃ¡Â»Ât kÃÂª nguyÃÂªn tÃ¡Â»Â Ã¢ÂÂ¤ 10Ã¢ÂÂ¶ |
| KiÃ¡Â»Âm tra nguyÃÂªn tÃ¡Â»Â | Miller-Rabin (n Ã¢ÂÂ¤ 10ÃÂ¹Ã¢ÂÂ¸) | `pow(a, n-1, n) == 1` |
| GCD | `def gcd(a,b): return gcd(b, a%b) if b else a` | `gcd(48, 18)` Ã¢ÂÂ 6 |
| LÃÂ©y thÃ¡Â»Â«a nhanh | `pow_mod(x, n, m)` chia ÃÂÃÂ´i mÃÂ© | `pow(x, n, m)` cÃÂ³ sÃ¡ÂºÂµn |
| Fermat nhÃ¡Â»Â | `a^(p-1) Ã¢ÂÂ¡ 1 (mod p)` | NghÃ¡Â»Âch ÃÂÃ¡ÂºÂ£o modulo |
| TÃ¡Â»Â hÃ¡Â»Â£p C(n,k) mod p | `fact[n] * invfact[k] * invfact[n-k] % p` | `n, k Ã¢ÂÂ¤ 10Ã¢ÂÂ¶` |

**Ghi nhÃ¡Â»Â:** Python cÃÂ³ sÃ¡ÂºÂµn `math.gcd`, `math.comb`, `pow(x, n, m)` Ã¢ÂÂ thi dÃÂ¹ng luÃÂ´n, tÃ¡Â»Â± cÃÂ i chÃ¡Â»Â ÃÂÃ¡Â»Â hiÃ¡Â»Âu bÃ¡ÂºÂ£n chÃ¡ÂºÂ¥t.

---

## Ã°ÂÂÂ Cheatsheet Ã¢ÂÂ SÃ¡Â»Â chÃÂ­nh phÃÂ°ÃÂ¡ng

```python
import math
def is_square(n):
    r = int(math.isqrt(n))  # Python 3.8+
    return r * r == n
# hoÃ¡ÂºÂ·c khÃÂ´ng dÃÂ¹ng math:
x = 0
while x * x <= n:
    if x * x == n: return True
    x += 1
```

---

## Ã°ÂÂÂ Cheatsheet Ã¢ÂÂ Fibonacci lÃ¡ÂºÂ·p (O(n), khÃÂ´ng ÃÂÃ¡Â»Â quy)

```python
# CÃÂ¡ch 1: 2 biÃ¡ÂºÂ¿n (tÃ¡Â»Âi ÃÂ°u bÃ¡Â»Â nhÃ¡Â»Â)
a, b = 0, 1
for _ in range(n):
    a, b = b, a + b
print(a)  # F(n)

# CÃÂ¡ch 2: MÃ¡ÂºÂ£ng (khi cÃ¡ÂºÂ§n truy xuÃ¡ÂºÂ¥t nhiÃ¡Â»Âu lÃ¡ÂºÂ§n, n Ã¢ÂÂ¤ 10^6)
f = [0] * 1_000_006
f[1] = f[2] = 1
for i in range(3, n+1):
    f[i] = f[i-1] + f[i-2]
```

---

## Ã°ÂÂÂ Cheatsheet Ã¢ÂÂ KiÃ¡Â»Âm tra SNT (3 mÃ¡Â»Â©c ÃÂÃ¡Â»Â)

```python
# CÃÂ¡ch 1: O(n) - cÃÂ¡ bÃ¡ÂºÂ£n
def is_prime_basic(n):
    if n < 2: return False
    for i in range(2, n):
        if n % i == 0: return False
    return True

# CÃÂ¡ch 2: O(Ã¢ÂÂn) - TÃ¡Â»ÂI ÃÂ¯U (cÃ¡ÂºÂ§n nhÃ¡Â»Â!)
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

# CÃÂ¡ch 3: Sieve (Eratosthenes) - cho nhiÃ¡Â»Âu truy vÃ¡ÂºÂ¥n, n Ã¢ÂÂ¤ 10^6
N = 1_000_006
is_prime = [True] * N
is_prime[0] = is_prime[1] = False
for i in range(2, int(N**0.5)+1):
    if is_prime[i]:
        for j in range(i*i, N, i):
            is_prime[j] = False
```

---

## Ã°ÂÂÂ Cheatsheet Ã¢ÂÂ PhÃÂ¢n tÃÂ­ch thÃ¡Â»Â«a sÃ¡Â»Â nguyÃÂªn tÃ¡Â»Â

```python
x = int(input())
y = 1
d = 2
while d * d <= x:
    cnt = 0
    while x % d == 0:
        x //= d
        cnt += 1
    if cnt % 2 == 1:      # sÃ¡Â»Â mÃÂ© lÃ¡ÂºÂ» Ã¢ÂÂ nhÃÂ¢n vÃÂ o kÃ¡ÂºÂ¿t quÃ¡ÂºÂ£
        y *= d
    d += 1
if x > 1:                 # thÃ¡Â»Â«a sÃ¡Â»Â nguyÃÂªn tÃ¡Â»Â lÃ¡Â»Ân cuÃ¡Â»Âi cÃÂ¹ng
    y *= x
print(y)
```

---



## Ã¢ÂÂ¡Ã¯Â¸Â ÃÂiÃ¡Â»Âu hÃÂ°Ã¡Â»Âng

**VÃ¡Â»Â trÃÂ­:** `b36-Toan-Hoc-So-Hoc/bai.md`

**BÃÂ i tiÃ¡ÂºÂ¿p theo:** [BÃÂ i 37 Ã¢ÂÂ ÃÂÃ¡Â»Â ThÃ¡Â»Â: BFS & DFS](../b37-Do-Thi-BFS-DFS/bai.md)
`
