str_1 = """Hello my kitty.The grass is green."""
for i in range(len(str_1)):
     if str_1[i] == 'e':
         print(i)
         first = i
         break
for i in range(len(str_1) -1, 0, -1):
     if str_1[i] == 'e':
        print(i)
        last = i
        break
print(str_1[first:last])



