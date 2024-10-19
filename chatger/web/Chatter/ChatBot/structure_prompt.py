"""
At the command line, only need to run once to install the package via pip:

$ pip install google-generativeai
"""

import os

import google.generativeai as genai


async def structured_prompt(message):
    # 從環境變數讀取 API 金鑰
    API_KEY = os.environ.get("GEMINI_API_KEY")

    if not API_KEY:
        raise ValueError("GEMINI_API_KEY 環境變數未設置")

    genai.configure(api_key=API_KEY)
    # Set up the model
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 0,
        "max_output_tokens": 8192,
    }

    safety_settings = [
        {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
        {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
        {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
        {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"},
    ]

    model = genai.GenerativeModel(
        model_name="gemini-1.5-pro",
        generation_config=generation_config,
        safety_settings=safety_settings,
    )

    prompt_parts = [
        "請根據給予的程式碼，程式碼的運行狀態與訊息，請簡潔的給予問題分析與簡潔的程式碼改進建議(繁體中文)，不需要展示程式碼",
        "input: year = float(input('请输入年份: '))\nis_leap == year % 4 == 0 and year % 100 != 0 or year % 400 == 0\nprint(is_leap)\nruntime_error\nNameError: name 'is_leap' is not defined",
        "output: ## 問題分析：\n\n程式碼出現 `NameError`，原因是使用了未定義的變數 `is_leap`。應是 `==` 符號誤用，導致變數賦值操作 (`=`) 沒有執行。\n\n\n## 改進建議：\n\n將 `is_leap ==` 修改為 `is_leap =` 即可。",
        'input: import math\n\ndef calculate_triangle_properties(a, b, c):\n    """\n    計算三角形的周長和面積\n\n    參數:\n    a (float): 第一條邊長\n    b (float): 第二條邊長\n    c (float): 第三條邊長\n\n    返回:\n    tuple: 包含周長和面積的元組 (perimeter, area)，如果無法構成三角形，則返回 None\n    """\n    perimeter = a + b + c\n    s = perimeter / 2\n    area = math.sqrt(s * (s - a) * (s - b) * (s - c))\n    return perimeter, area\n\n# 輸入三條邊長\na = float(input("請輸入第一條邊長: "))\nb = float(input("請輸入第二條邊長: "))\nc = float(input("請輸入第三條邊長: "))\n\n# 計算三角形的周長和面積\nperimeter, area = calculate_triangle_properties(a, b, c)\nprint("三角形的周長為:", perimeter)\nprint("三角形的面積為:", area)\nsuccess\nWA',
        "output: ## 問題分析：\n\n程式碼缺少判斷輸入的三邊長是否能構成三角形的邏輯。\n\n## 改進建議：\n\n1. **加入三角形判斷**: 在計算周長和面積之前，加入判斷式，檢查三邊長是否滿足三角形法則 (任意兩邊之和大於第三邊)。\n2. **處理非法輸入**: 如果輸入無法構成三角形，則返回 `None` 或輸出錯誤訊息。",
        'input: def print_triangle(height):\n    if height == 0:\n        return\n    print_triangle(height - 1)\n    print("*" * height)\n\n# 輸出一個高度為 10000 的三角形金字塔\nprint_triangle(10000)\ntime_limit_exceed',
        "output: ## 問題分析\n\n程式碼使用遞迴方式印出三角形，但當高度過大 (例如 10000) 時，會超出系統堆疊限制，導致執行時間過長或崩潰。\n\n## 改進建議\n\n1. **使用迴圈**: 將遞迴改寫為迴圈，避免堆疊溢位問題。\n2. **優化輸出**: 可考慮使用字串拼接，一次性輸出，減少輸出次數，提高效率。",
        "input: import math\n\nfor num in range(2, 100):\n    is_prime = True\n    for factor in range(2, int(math.sqrt(num)) + 1):\n        if num % factor == 0:\n            is_prime = False\n            break\n    if is_prime:\n        print(num, end=' ')\ncompile_error\nModuleNotFoundError: No module named 'math'",
        "output: ## 問題分析\n\n程式碼出現 `ModuleNotFoundError`，表明 Python 找不到名為 `math` 的模組。\n\n## 改進建議\n\n1. **確認安裝**: 檢查是否已安裝 `math` 模組。可以使用 `pip list` 命令查看已安裝的模組列表。\n2. **安裝模組**: 若未安裝，使用 `pip install math` 命令安裝 `math` 模組。\n3. **檢查環境**: 若在虛擬環境中，確保在正確的環境中安裝和運行程式碼。",
        "input: primes = []\nfor num in range(2, 100):\n  is_prime = True\n  for factor in range(2, num):\n    if num % factor == 0:\n      is_prime = False\n      break\n  if is_prime:\n    primes.append(num)\nprint(primes)\nsuccess\nWA",
        "output: ## 問題分析：\n\n程式碼的目標是找出 2 到 100 之間的質數，但判斷質數的邏輯存在錯誤。目前的程式碼會將所有數字都判斷為質數，因為 `factor` 的範圍是從 1 到 `num-1`，而任何數字都能被 1 整除。\n\n## 改進建議：\n\n1. **修改 `factor` 的範圍**: 將 `factor` 的範圍修改為從 2 到 `num` 的平方根，因為一個數如果不能被 2 到其平方根之間的任何整數整除，那它就是質數。\n2. **優化判斷條件**: 可以優化判斷條件，當找到一個能整除的 `factor` 時，直接跳出迴圈，避免不必要的計算。",
        "input: def is_palindrome(num):\n    num_str = str(num)\n    reversed_num_str = num_str[::-1]\n    return num_str == reversed_num_str\nsuccess\nWA",
        "output: ## 問題分析與改進建議\n\n**問題:** 程式碼邏輯正確，但可能未通過所有測試案例，導致 WA (Wrong Answer) 結果。\n\n**可能原因:**\n\n* **未考慮負數：** 負數的反轉與正數不同，例如 `-121` 的反轉應為 `-121` 而不是 `121-`。\n* **未考慮前導零：** 數字 `012` 應視為 `12`，但程式碼可能將其視為不同的數字。\n\n**改進建議:**\n\n1. **處理負數：** 在轉換為字串前，先取絕對值 `abs(num)`，確保處理的是正數。\n2. **處理前導零：** 使用 `int(num_str)` 將字串轉回數字，去除前導零。",
        'input: def is_palindrome(num):\n    """判斷一個數是否是回文數"""\n    temp = num\n    total = 0\n    while temp > 0:\n        total = total * 10 + temp % 10\n        temp //= 10\n    return total == num\nsuccess\nAC',
        "output: ## 程式碼分析與改進建議\n\n**分析：** 程式碼的功能是判斷一個數是否為回文數，實現方法是將數字反轉後與原數字比較。\n\n**改進建議：**\n\n* **字串操作：** 可以考慮將數字轉換為字串，利用字串切片功能反轉字串，再與原字串比較，這樣可以簡化程式碼。\n* **遞迴函數：** 可以使用遞迴函數來實現數字反轉，這樣可以使程式碼更加簡潔優雅。\n* **效能：** 如果需要處理大量數字或大型數字，可以考慮使用更高效的演算法，例如利用數學特性來判斷回文數。",
        'input: def get_file_extension(file_name):\n """\n 取得檔案的副檔名\n\n Args:\n  file_name: 檔案名稱，包含副檔名\n\n Returns:\n  副檔名，若無副檔名則回傳空字串\n """\n # 使用 rsplit() 從右側分割檔名，最多分割一次\n # 取得副檔名\n file_extension = file_name.split(\'.\', 1)[-1]\n return file_extension\nsuccess \nWA',
        "output: ## 問題分析：\n\n程式碼邏輯看似正確，但 `WA` 提示可能代表在某些邊界情況下出錯。\n\n## 改進建議：\n\n1. **檢查空檔名情況**: 若 `file_name` 為空字串，`rsplit` 會返回 `['']`，導致 `[-1]` 取值錯誤。應在分割前檢查 `file_name` 是否為空。\n2. **考慮無副檔名情況**: 若檔名無 `.`，`rsplit` 會返回原字串，導致錯誤的副檔名。應檢查分割後的列表長度，若為 1 則代表無副檔名，應返回空字串。",
        "input: persons = [True] * 30\ncounter, index, number = 0, 0, 0\nwhile counter < 15:\n  if persons[index]:\n    number += 1\n    if number == 9:\n      persons[index] = False\n      counter += 1\n      number = 0\n  index += 1\n  print(persons)\nfor person in persons:\n  print('基' if person else '非', end='')\nruntime_error",
        'output: ## 問題分析：\n\n程式碼的目的是從 30 個人中挑選 15 個人，每隔 8 個人淘汰第 9 個人。 錯誤訊息 "runtime_error" 顯示程式運行時出現問題。\n\n主要問題在於 `index` 變數可能超出 `persons` 列表的索引範圍 (30)，導致錯誤。\n\n## 改進建議：\n\n1. **限制 `index` 範圍**: 在每次 `index += 1` 後，檢查 `index` 是否達到 30。如果達到，將 `index` 重置為 0，使其回到列表開頭。\n2. **結束條件**: 目前的結束條件是 `counter < 15`，但有可能在淘汰 15 人之前，`index` 就已經循環完整個列表。建議增加一個條件，例如設定一個最大循環次數，避免無限循環。',
        'input: import math\nclass Point:\n  """\n  描述平面上的点的类\n  """\n  def __init__(self, x=0, y=0):\n    """\n    初始化点的坐标\n\n    Args:\n      x: 横坐标\n      y: 纵坐标\n    """\n    self.x = x\n    self.y = y\n\n  def move(self, dx, dy):\n    """\n    移动点的位置\n\n    Args:\n      dx: 横向移动距离\n      dy: 纵向移动距离\n    """\n    self.x += dx\n    self.y += dy\n\n  def __distance_to(self, other_point):\n    """\n    计算到另一个点的距离\n\n    Args:\n      other_point: 另一个 Point 对象\n\n    Returns:\n      到另一个点的距离\n    """\n    dx = self.x - other_point.x\n    dy = self.y - other_point.y\n    return math.sqrt(dx**2 + dy**2)\np1 = Point(3,4)\nP2 = Point()\np1.distance_to(P2)\ncompile_error\nAttributeError: \'Point\' object has no attribute \'distance_to\'',
        "output: 問題分析：\n程式碼出現 AttributeError，顯示 Point 物件沒有 distance_to 屬性。這是因為 __distance_to 方法使用了兩個底線開頭的命名方式，這在 Python 中代表私有方法。私有方法無法直接從物件外部調用。\n\n改進建議：\n移除 __distance_to 方法名稱中的雙底線： 將方法名稱改為 distance_to，使其成為公開方法，即可從外部調用。\n(可選) 使用 @property 裝飾器： 若希望像訪問屬性一樣調用 distance_to 方法，可以使用 @property 裝飾器將其轉換為屬性。",
        "input: def string_to_matrix(input_string):\n  \"\"\"將字串轉換為矩陣。\n\n  Args:\n    input_string: 代表矩陣的字串，例如 \"[1,2,3,4]\"。\n\n  Returns:\n    表示輸入矩陣的一維列表(float)。\n  \"\"\"\n  # 移除方括號並按行拆分字串\n  rows = input_string.strip('[]').split('],[')\n\n  # 將每行拆分為數字並轉換為整數\n  matrix = [[int(num) for num in row.split(',')] for row in rows]\n  return matrix\n\n# 測試字串\ninput_string = \"[5,6,7,8]\"\n\n# 將字串轉換為矩陣\nmatrix = string_to_matrix(input_string)\n\n# 輸出結果\nprint(matrix)\nsuccess\nWA",
        "output: 問題分析\n程式碼執行時，雖然沒有發生錯誤，但輸出結果與預期不符，屬於 Wrong Answer (WA) 的情況。這可能是因為函數的邏輯存在缺陷，無法正確將字串轉換成矩陣。\n\n程式碼改進建議\n檢查輸入格式:\n程式碼假設輸入字串格式為 \"[1,2,3,4]\"，其中每個數字都以逗號分隔，並且每一行都以 ],[ 分隔。\n應檢查輸入字串是否符合預期格式，若不符合格式，則應處理錯誤情況。\n處理空行:\n若輸入字串存在空行，例如 \"[1,2,3],[,4]\"，程式碼會將空行當作一個空列表，導致矩陣的維度不正確。\n應檢查每行是否為空，若為空則跳過該行。\n資料類型轉換:\n程式碼直接將每行元素轉換為整數，若輸入字串包含非數字元素，則會發生錯誤。\n應檢查每行元素是否為數字，若不是數字，則應處理錯誤情況或進行相應的轉換。",
        "input: import numpy \nimport random\ndef merge(A, p, q, r):\n    #定義subarray的邊界與建立subarray(divide)。此為python程式碼，A為list型態\n    n_L = q - p + 1\n    n_R = r - q\n    L = []\n    R = []\n    for i in range(n_L):\n        L[i] = A[p+i]\n    for j in range(n_R):\n        R[j] = A[q+j+1] \n    \n    i = 0\n    j = 0\n    k = p\n    #比大小~小的先排\n    while i < n_L and j < n_R:\n        if L[i] <= R[j]:\n            A[k] = L[i]\n            i += 1\n        else:\n            A[k] = R[j]\n            j += 1\n        k += 1\n\n    \n    #剩餘元素處理\n    while i < n_L:\n        A[k] = L[i]\n        i += 1\n        k += 1\n\n    while j < n_R:\n        A[k] = R[j]\n        j += 1\n        k += 1\ndef Merge_Sort(A, p, r, i):\n    #前index<尾index時，繼續分治\n    if p < r:\n        i+=1\n        q = (p+r)//2\n        Merge_Sort(A, p, q, i)      #對左邊subarray進行Merge Sort(Conquer)\n        Merge_Sort(A, q + 1, r, i)  #對右邊subarray進行Merge Sort(Conquer)\n        merge(A, p, q, r)           #兩邊subarray合併排序(Combine)\n    \n\ndef Merge_Sort_Run(A):\n    length = len(A)\n    Merge_Sort(A, 0, length-1, 0)\n\n\ninput_arr = list(range(1, 51))\nrandom.shuffle(input_arr)        #洗牌\nMerge_Sort_Run(input_arr.copy())\nruntime error",
        "output: ## 問題分析：\n\n程式碼中存在一個運行時錯誤，原因是 `L` 和 `R` 列表在 `merge` 函數中被定義為空列表，但之後的循環嘗試訪問這些列表的元素，導致索引超出範圍的錯誤。\n\n## 程式碼改進建議：\n\n1. **初始化列表大小**: 在 `merge` 函數中，將 `L` 和 `R` 列表初始化為正確的大小，而不是空列表。可以使用列表推導式或 `[0] * n` 來完成。\n\n```python\nL = [0] * n_L\nR = [0] * n_R\n```\n\n2. **使用 `enumerate` 循環**: 在 `merge` 函數中，使用 `enumerate` 循環來同時獲取索引和元素，避免使用 `i` 和 `j` 進行索引計算。\n\n```python\nfor i, val in enumerate(L):\nA[k] = val\nk += 1\n```\n\n3. **考慮使用 `collections.deque`**: 如果需要頻繁地從列表頭部或尾部添加或刪除元素，可以考慮使用 `collections.deque`，它比列表更適合這種操作。",
        "input: Code:\ndef selection_sort(data):\n  for i in range(len(data)):\n    min_index = i\n    for j in range(i + 1, len(data) + 1):  # 錯誤：索引超出範圍\n      if data[j] < data[min_index]:\n        min_index = j\n    data[i], data[min_index] = data[min_index], data[i]\n\n# 測試\ndata = [5, 3, 8, 6, 7, 2]\nselection_sort(data)\nprint(data)\n\nOutput:\nTraceback (most recent call last):\n    if data[j] < data[min_index]:\nIndexError: list index out of range\n\nRun status::\nruntime_error\n\nAnswer status:\nRE",
        "output: ## 問題分析\n\n程式碼中存在一個索引超出範圍的錯誤。在 `selection_sort` 函數的內層迴圈中，`j` 的範圍是 `i + 1` 到 `len(data) + 1`，這導致 `j` 在最後一次迭代時會超出 `data` 列表的索引範圍，從而引發 `IndexError`。\n\n## 程式碼改進建議\n\n將內層迴圈的範圍修改為 `i + 1` 到 `len(data)`，即可避免索引超出範圍的錯誤。",
        "input: Code:\ndef insertion_sort(arr):\n    for i in range(1, len(arr)):\n        key = arr[i]\n        j = i - 1\n        while j >= 0 and arr[j] < key:  # 错误：此处应为 >\n            arr[j+1] = arr[j]\n            j = j - 1\n        arr[j+1] = key\n    \n    return arr\n\n# Example usage\ndata = [64, 34, 25, 12, 22, 11, 90]\nsorted_data = insertion_sort(data)\nprint(sorted_data) \n\nOutput:\n[90, 64, 34, 25, 22, 12, 11]\n\nExpected output:\n[11, 12, 22, 25, 34, 64, 90]\n\nRun status:\nsuccess\n\nAnswer Status:\nWA",
        "output: ## 問題分析\n\n程式碼的輸出與預期不符，原因在於插入排序的比較邏輯錯誤。程式碼中 `while` 迴圈的條件 `arr[j] < key` 應該為 `arr[j] > key`。\n\n## 程式碼改進建議\n\n將 `while` 迴圈的條件修改為 `arr[j] > key`，以確保插入排序正確地將比 `key` 大的元素往後移動，以便將 `key` 插入到正確的位置。",
        "input: Code：\ndef quick_sort(arr):\n    \"\"\"\n    使用快速排序算法对数组进行排序。\n\n    Args:\n        arr: 要排序的数组。\n\n    Returns:\n        排序后的数组。\n    \"\"\"\n\n    if len(arr) < 2:\n        return arr  # 基线情况：长度为 0 或 1 的数组已排序\n\n    pivot = arr[0]  # 选择第一个元素作为基准点\n    left = [x for x in arr[1:] if x <= pivot]\n    right = [x for x in arr[1:] if x > pivot]\n\n    # 这里修改：将 list 替换为其他类型，导致类型错误\n    return quick_sort(left) + pivot + quick_sort(right)  # 错误：无法将 int 与列表相加\n\narr = [3, 7, 8, 5, 2, 1, 9, 5]\nsorted_arr = quick_sort(arr)\nprint(sorted_arr)  \n\nOutput:\nTraceback (most recent call last):\n    return quick_sort(left) + pivot + quick_sort(right)\nTypeError: can only concatenate list (not \"int\") to list\n\nRun status:\nruntime_error\n\nAnswer status:\nRE",
        "output: ## 問題分析\n\n程式碼中，`quick_sort` 函數在遞迴調用後，嘗試將排序後的子列表 `left`、基准值 `pivot` 和排序後的子列表 `right` 相加。然而，`pivot` 是整數，而 `left` 和 `right` 是列表，導致了 `TypeError: can only concatenate list (not \"int\") to list` 的錯誤。\n\n## 程式碼改進建議\n\n1. **使用 `extend` 方法合併列表:**\n- 將 `return quick_sort(left) + pivot + quick_sort(right)` 替換為 `return quick_sort(left) + [pivot] + quick_sort(right)`。\n- `extend` 方法可以將一個列表的元素添加到另一個列表的末尾，而不會創建新的列表。\n\n2. **使用 `+=` 运算符:**\n- 將 `return quick_sort(left) + [pivot] + quick_sort(right)` 替換為 `result = quick_sort(left); result.extend([pivot]); result.extend(quick_sort(right)); return result`。\n- `+=` 运算符可以将一个列表的元素添加到另一个列表的末尾，并返回修改后的列表。",
        "input: Code：\ndef merge_sort(arr):\n    \"\"\"\n    使用 merge_sort 排列數組，但會導致無窮遞迴。\n\n    Args:\n        arr: 要排序的數組。\n\n    Returns:\n        永遠不會返回，因為它會陷入無窮遞迴。\n    \"\"\"\n\n    mid = len(arr) // 2\n    left_half = merge_sort(arr[:mid])\n    right_half = merge_sort(arr[mid:])\n    return merge(left_half, right_half)  # 這裡也應該返回合併結果，但我們故意不返回\n\ndef merge(left, right):\n  \"\"\"\n  合併兩個已排序的子數組。\n\n  Args:\n    left: 左子數組。\n    right: 右子數組。\n\n  Returns:\n    合併後的排序數組。\n  \"\"\"\n  result = []\n  i, j = 0, 0\n  while i < len(left) and j < len(right):\n    if left[i] <= right[j]:\n      result.append(left[i])\n      i += 1\n    else:\n      result.append(right[j])\n      j += 1\n#   print(result)\n  result += left[i:]\n  result += right[j:]\n  return result\n\n# 測試\narr = [38, 27, 43, 3, 9, 82, 10]\nsorted_arr = merge_sort(arr)\nprint(sorted_arr)  # 輸出：[3, 9, 10, 27, 38, 43, 82]\n\nOutput:\nTraceback (most recent call last):\nleft_half = merge_sort(arr[:mid])\nmid = len(arr) // 2\nRecursionError: maximum recursion depth exceeded while calling a Python object\n\nRun status::\nruntime_error\n\nAnswer status:\nRE",
        "output: ## 問題分析\n\n程式碼中存在無窮遞迴問題。在 `merge_sort` 函數中，它會不斷地將輸入陣列拆分為左右子陣列，並遞迴地調用自身進行排序。然而，由於 `merge_sort` 函數中沒有終止條件，它會一直遞迴下去，直到超出 Python 的遞迴深度限制，導致 `RecursionError`。\n\n## 程式碼改進建議\n\n1. **添加終止條件:** 在 `merge_sort` 函數中，需要添加一個終止條件，例如當輸入陣列的長度為 1 或 0 時，直接返回該陣列，因為單元素陣列或空陣列已經是排序好的。\n\n2. **返回合併結果:** 在 `merge_sort` 函數中，需要在合併左右子陣列後，將合併後的結果返回，而不是像現在這樣故意不返回。",
        "input: Code:\nimport numpy as np\nimport random\n\n#找出節點之parent, left node, right node之位置\ndef Parent(i):\n  return (i+1) // 2 - 1\n\ndef Left_Node(i):\n  return 2 * (i+1) - 1\n\ndef Right_Node(i):\n  return 2 * (i+1)\n\n#部分排序_父節點須大於子節點\ndef Max_Heapify(A, i, index):\n  l = Left_Node(i)\n  r = Right_Node(i)\n  if l <= index and A[l] > A[i]:\n    largest = l\n  else:\n    largest = i\n   \n  if r <= index and A[r] > A[largest]:\n    largest = r\n  if largest != i:\n    A[i], A[largest] = A[largest], A[i]\n    Max_Heapify(A, largest, index)\n\n#全部排序_每個父節點須大於自己的子節點\ndef Build_Max_Heap(A):\n  n = len(A)\n  i = n//2 - 1\n  while i >= 0:\n    Max_Heapify(A, i, n-1)\n    i -= 1\n\ndef HeapSort(A, n):\n  Build_Max_Heap(A)\n  i = n - 1\n  range_index = n - 1\n  while i >= 1:\n    #頭尾交換(頭為最大值)\n    A[0], A[i] = A[i], A[0]\n    range_index -= 1\n    i -= 1\n  print(A)\n\n#--------------------------\n#Main\n#--------------------------\n\ndef main():\n  input_arr = list(range(1, 51))\n  random.shuffle(input_arr)    #洗牌\n\n  HeapSort(input_arr.copy(), len(input_arr.copy()))\n\nif __name__ == \"__main__\":\n  main()\n\nOutput:\n[49, 47, 46, 48, 45, 37, 36, 44, 43, 39, 40, 33, 28, 23, 21, 22, 29, 31, 41, 42, 13, 35, 30, 32, 2, 20, 18, 26, 4, 14, 8, 5, 16, 15, 7, 27, 17, 6, 38, 11, 10, 3, 1, 12, 9, 34, 24, 19, 25, 50]\n\nExpected output:\n[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]\n\nRun status:\nsuccess\n\nAnswer Status:\nWA",
        "output: ## 問題分析\n\n程式碼中缺少了 `Max_Heapify` 函數，導致堆排序無法正確執行。`Max_Heapify` 函數負責將一個子樹調整為最大堆，是堆排序的核心步驟。\n\n## 程式碼改進建議\n\n1. **添加 `Max_Heapify` 函數:**\n- 參考給定的程式碼，將 `Max_Heapify` 函數的定義添加至程式碼中。\n- 確保 `Max_Heapify` 函數能夠正確地將子樹調整為最大堆，即父節點的值大於其子節點的值。\n\n2. **檢查 `Build_Max_Heap` 函數:**\n- 確保 `Build_Max_Heap` 函數正確地调用 `Max_Heapify` 函數，将整个数组调整为最大堆。\n\n3. **測試程式碼:**\n- 运行修改后的代码，并使用不同的输入数据进行测试，确保排序结果正确。",
        "input: " + message,
        "output: ",
    ]

    response = model.generate_content(prompt_parts)
    print(response.text)
    return response.text
