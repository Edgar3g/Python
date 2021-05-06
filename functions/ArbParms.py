def table_print(**kwarg):
    for k,v in kwarg.items():
        print('%s \t %s' % (k,v))

table_print(a=1, b=2, c=3)

ds= {'a':1, 'b':2, 'c': 3}
print(table_print(**ds))