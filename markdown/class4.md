## 一、class4-1.py：圖片 & 網頁訊息元件 🖼️📢

### 1️⃣ 顯示圖片（st.image）

👉 功能：把圖片放到網頁上

```python
st.image("image/apple.png", width=300, caption="蘋果")
```

📌 重點：

- `"image/apple.png"`：圖片位置
- `width=300`：圖片寬度
- `caption`：圖片下面的說明文字

📘 想像成：

> 把照片貼在網頁上，順便寫一句說明

---

### 2️⃣ 一次顯示資料夾裡「所有圖片」

```python
image_files = os.listdir("image")
```

📌 這行的意思：

- 把 `image` 資料夾裡的檔名全部拿出來

```python
for image_file in image_files:
    st.image("image/" + image_file)
```

📘 想像成：

> 老師說：「把資料夾裡的每一張照片都貼出來」

---

### 3️⃣ 下拉選單（selectbox）⬇️

```python
selected_image = st.selectbox("請選擇圖片", image_files)
```

📌 功能：

- 讓使用者「選一張圖片」

📘 想像成：

> 點選清單，挑你最喜歡的照片

---

### 4️⃣ 網頁提示訊息（success / error / warning / info）

```python
st.success("成功")
st.error("錯誤")
st.warning("警告")
st.info("資訊")
```

📌 用來告訴使用者：

- 成功了 ✅
- 出錯了 ❌
- 要小心 ⚠️
- 給你資訊 ℹ️

📘 像遊戲跳出提示視窗一樣！

---

## 二、class4-2.py：簡單購物平台 🛒

### 1️⃣ session_state（記住資料的小本本）

```python
ss = st.session_state
```

📌 功能：

- 記住「買過什麼」
- 記住「庫存剩多少」

📘 想像成：

> 網頁的記憶本，不會因為重整就忘記

---

### 2️⃣ 商品資料（名字、圖片、價格、庫存）

```python
ss.products[name] = {
    "image_path": "...",
    "price": 10,
    "stock": 10
}
```

📌 每個商品都有：

- 圖片
- 價格
- 庫存數量

📘 就像便利商店的商品標籤

---

### 3️⃣ 點「購買」按鈕

```python
if details["stock"] > 0:
    details["stock"] -= 1
```

📌 規則：

- 有庫存 ➜ 可以買
- 沒庫存 ➜ 顯示「賣完了」

📘 像自動販賣機一樣

---

### 4️⃣ 新增庫存（補貨）

```python
ss.products[selected_product]["stock"] += add_stock
```

📌 功能：

- 老闆幫商品補貨

📘 商品不會一直賣完 👍

---

## 三、class4-3.py：函數（function）📦

### 1️⃣ 什麼是函數？

👉 函數 = 幫你做事情的小機器

```python
def hello():
    print("hello")
```

📘 叫一次，就做一次
📘 叫三次，就做三次

---

### 2️⃣ 有參數的函數（可以丟東西進去）

```python
def greet(name):
    print("Hello", name)
```

📌 name 是你給它的名字

📘 像對不同同學打招呼

---

### 3️⃣ 有回傳值的函數（會給你答案）

```python
def two_num_min(a, b):
    return 比較小的數
```

📘 像計算機：

> 丟數字進去 ➜ 拿答案出來

---

### 4️⃣ 預設參數（不給也沒關係）

```python
def calculate_circle_area(radius, pi=3.14):
```

📌 如果沒給 `pi`
👉 會自動用 3.14

📘 像作業有「預設答案」

---

## 四、class4-4.py：全域變數 & 區域變數 🌍📦

### 1️⃣ 全域變數（大家都看得到）

```python
length = 5
```

📌 在函數外面
👉 全世界都能用

---

### 2️⃣ 區域變數（只有函數裡能用）

```python
def f():
    area = length * length
```

📌 area 只存在函數裡
👉 外面看不到

📘 像放在書包裡的東西

---

### 3️⃣ 回傳值是最安全的做法 ⭐

```python
def calculate():
    return area
```

📌 好處：

- 不會搞混
- 不會出錯

👉 **最推薦寫法**

---

### 4️⃣ global（不太推薦）

```python
global area
```

📌 可以改全域變數
❌ 容易亂掉、出錯

📘 像偷偷改老師的成績表 😅

---

## 🌟 今天最重要的 5 個重點

1. `st.image` 可以顯示圖片
2. `selectbox` 可以做下拉選單
3. `session_state` 可以記住資料
4. 函數可以「重複使用」
5. **用 return 比 global 安全**
