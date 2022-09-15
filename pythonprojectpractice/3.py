import csv  # 匯入csv模組

with open('address.csv', encoding="utf-8-sig") as infile:  # with:自動關閉檔案
    data = list(csv.DictReader(infile))    # csv.DictReader(filename):以字典形式讀取檔案
    for i in data:
        print('initial data:', i['姓名'], i['縣市'], i['住址'])
        if i['縣市'][0] == '台':
            i['縣市'] = '臺' + i['縣市'][1:]
        if 'F' in i['住址']:
            i['住址'] = i['住址'].replace('F', '樓')
        if i['縣市'] == '臺中市' and '中港路' in i['住址']:
            i['住址'] = i['住址'].replace('中港路', '臺灣大道')
        print('    ', 'updated data:', i['姓名'], i['縣市'], i['住址'])
with open('new address.csv', 'w', newline='') as outfile:  # 'w'代表開啟一全新檔案，且用來寫入
    writer = csv.DictWriter(outfile, fieldnames = data[0].keys())
    writer.writeheader()
    for e in data:
        writer.writerow(e)

