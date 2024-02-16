import random
import time

# 連想配列の定義
items = {
    "decide": "決める",
    "understand": "理解する",
    "mean": "意味する。",
    "notice": "気づく",
    "waste": "無駄にする",
    "discover": "発見する",
    "wake": "目覚める",
    "invite": "招待する",
    "pick": "つまむ",
    "borrow": "借りる",
    "introduce": "導入、紹介する",
    "wonder": "不思議な",
    "receive": "受け取る",
}


def auto_extract_random(items):
    # 辞書のコピーを作成してイテレーションする
    items_copy = dict(items)
    for key, value in items_copy.items():
        print("連想配列内の要素をランダムに抽出中...")
        time.sleep(2)  # 2秒待機（仮の処理として）
        # ランダムに要素を選択
        random_key, random_value = random.choice(list(items.items()))
        print("抽出が完了しました。エンターキーを押して結果を表示します。")
        print(f"{random_key}: はなに")
        input()  # エンターキーを待機
        print(f"選択された要素: {random_key}: {random_value}")
        # 選択された要素を元の辞書から削除
        del items[random_key]


# プログラムの実行
auto_extract_random(items)
