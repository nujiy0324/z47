import os
import xlrd
import urllib.request
import ssl


# open info.xls file and get the attributes
book = xlrd.open_workbook('./info/info.xls')
sheet = book.sheets()[0]
num_rows = sheet.nrows
num_cols = sheet.ncols


headers = {'User-Agent',
           'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
opener = urllib.request.build_opener()
opener.addheaders = [headers]
ssl._create_default_https_context = ssl._create_unverified_context
print("downloading with urllib")
url0 = "https://old.tcmsp-e.com/tcmspmol/"


for i in range(1,num_rows):
    if float(sheet.cell(i,8).value) < 30.0 or float(sheet.cell(i,11).value) < 0.18:
        file = str(sheet.cell(i,0).value)+".mol2"
        url = url0 + file
        print("downloading " + file)
        localPath = os.path.join("./result", file)
        urllib.request.urlretrieve(url, localPath)
