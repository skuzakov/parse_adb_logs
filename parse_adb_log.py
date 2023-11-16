import os

path = input("Write path to folder with necessary concurrency\nThe output file will appear in the same folder:  ")
dir_path = fr'{path}'
for file in os.listdir(dir_path):
    last = []
    cur_path = os.path.join(dir_path, file)
    if os.path.isfile(cur_path):
        word1 = "Failed"
        word2 = "WARNING:  interconnect"
        list1 = []
        list2 = []
        with open(cur_path, 'r') as file:
            lines = file.readlines()
            for line1 in lines:
                if word1 in line1:
                  list1.append(line1)

            for line2 in lines:
                if word2 in line2:
                  list2.append(line2)
                 # print(list2)
        # result = [None] * (len(list1) + len(list2))
        # result[::2] = list2
        # result[1::2] = list1
#        with open("log_out_1.txt", "a") as myfile:
#            myfile.write('\n'.join(result))
#result_list = '\n'.join(result)
        log1 = []
        ip_s = []
        for u in list2:
           l = u.split(' ')
           ip = l[-2].split(':')
           ip_s.append(ip[0])
        date = []
        time = []
        ip_d = []
        for i in list1:
           k = i.split(' ')
           date.append(k[0].replace('-','.').replace('[',''))
           time.append((k[1].split('.'))[0])
           ip_d.append((k[12].split(':'))[0])

        for a in range(len(ip_s)):
           fin = f'{date[a]} {time[a]},{ip_s[a]},{ip_d[a]},'
           log1.append(fin)

    result = '\n'.join(log1)
    with open(f'{path}/parse_out.csv', "a") as myfile:
        myfile.write(result)
