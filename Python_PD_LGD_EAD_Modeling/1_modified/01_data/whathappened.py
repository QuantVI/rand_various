import csv
fn1 = "loan_sample_40mb.csv"
fn2 = "loan_sample_200mb.csv"

file = open(fn1,newline='',encoding='utf-8',errors='ignore')
data_str = file.read()
data_lin = data_str.split("\n")
data_lin = data_lin[:len(data_lin)-1]

data_row = [ r.split(",") for r in data_lin]


hdr = data_row[0]
stat = hdr.index("loan_status")


