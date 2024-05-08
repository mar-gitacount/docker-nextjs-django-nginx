from django.db import models

# Create your models here.


class Todo(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()

    def __str__(self):
        return self.title



# 時計アイテムテーブル
class WatchItem(models.Model):
    itemname = models.CharField(max_length=100)
    
    def __str__(self):
        return self.itemname


# 時計テーブル
class Watch(models.Model):
    # 時計の属性
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    reference = models.CharField(max_length=100,null=True)
    # 時計が所持するアイテムへの外部キー
    item = models.ForeignKey(WatchItem, on_delete=models.CASCADE)
    # ブレスレット
    brecelet = models.CharField(max_length=100,null=True)
    # 年代
    year =  models.CharField(max_length=100,null=True)
    
    size = models.CharField(max_length=100,null=True)
    # ダイアル
    dial = models.CharField(max_length=100,null=True)
    def __str__(self):
        # 以下をリファレンスに変える?
        return self.reference


# class BuchererItems(Watch):
#     item_number =  models.CharField(max_length=100) # ブヘラ特有のアイテムナンバーを追加する。
#      # 値段
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#      # 入力した日付
#     date = models.DateField()
#     def __str__(self):
#         return f"{self.item_number}-{self.price}-{self.date}"


# ブヘラから接続する場合、ブヘラテーブルは、リファレンスナンバーと、値段のみ？
# リファレンスナンバーで参照する。
class BuchererItem(models.Model):
    watch = models.ForeignKey(Watch, on_delete=models.CASCADE)
    # モデルアイテム名を取得する。
    model = models.ForeignKey(WatchItem, on_delete=models.CASCADE, default=1)
    
   
    # 年代
    year =  models.CharField(max_length=100,null=True)
    
    # リファレンス
    reference = models.CharField(max_length=100,null=True)

    # 値段
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # 入力した日付
    date = models.DateField()
    # item_number = models.IntegerField(default=0)  # ブヘラ特有のアイテムナンバーを追加する。
    item_number =  models.CharField(max_length=20) # ブヘラ特有のアイテムナンバーを追加する。
    url = models.CharField(max_length=200,default='')
    
    dial = models.CharField(max_length=100,null=True)
    size = models.CharField(max_length=100,null=True)
    
    def __str__(self):
        return f"{self.watch.name} - {self.date} - {self.price} - {self.item_number}-{self.url}"

# USA番も別テーブルで定義する。
