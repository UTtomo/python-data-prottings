import csv
import datetime



now = datetime.datetime.now()
Name = 'ジョージ'
City = 'ハワイ'

# 現在時刻を織り込んだファイル名を生成

fmt_name = "python-data/test_{0:%Y%m%d-%H%M%S}.csv".format(now)


with open(fmt_name,'w') as f:
    for i in range(0,100):
        writer = csv.writer(f, lineterminator='\n')
        writer.writerow([i,Name,City])

f.close()

print(now.date())


