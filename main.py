import time

data = [101, 103, 107, 109, 113, 127, 131, 137, 139, 149,
        151, 157, 163, 167, 173, 179, 181, 191, 193, 197,
        199, 211, 223, 227, 229, 233, 239, 241, 251, 257,
        263, 269, 271, 277, 281, 283, 293, 307, 311, 313,
        317, 331, 337, 347, 349, 353, 359, 367, 373, 379,
        383, 389, 397, 401, 409, 419, 421, 431, 433, 439]

sum_time = 0

for i in range(len(data)):
    low = 0  # 配列の左端
    high = len(data) - 1  # 配列の右端
    mid = (low + high) // 2  # 配列の中央
    target = data[i]  # 探索する値(固定)
    start = time.perf_counter()  # 時間計測開始
    while low < high:
        mid = (low + high) // 2
        # 値が見つかればループを抜ける
        if data[mid] == target:
            sec_time = time.perf_counter() - start  # 時間計測終了
            print('値 {} は配列の {} 番目に見つかりました。'.format(target, mid))
            print(f'処理時間は{sec_time:.6f}s')
            sum_time += sec_time
            break
            # 値の大小を調べて探索範囲を狭める
        elif data[mid] > target:
            high = mid - 1
        elif data[mid] < target:
            low = mid + 1

ave_time = sum_time/i #平均処理速度の計算
print(f'平均処理時間は{ave_time:.6f}s')