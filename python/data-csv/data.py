import csv
import datetime
import os



now = datetime.datetime.now()
FileDate = now.strftime('%m%d-%a')
dataName = "test_{0:%Y%m%d-%H%M%S}.csv".format(now)

Name = 'ジョージ'
City = '真里'
newfile = 'python-data/%s' % FileDate


# 名前が『月日-曜日-時間』 のフォルダの作成
if not os.path.isdir(newfile):
    os.mkdir(newfile)

print(FileDate)
# 現在時刻のファイル名を生成
fmt_name = "%s/%s" % (newfile,dataName)

# ここにAD変換したデータの添付
with open(fmt_name,'w') as f:
    for i in range(0,100):
        writer = csv.writer(f, lineterminator='\n')
        writer.writerow([i,Name,City])

f.close()

print(now.date())


