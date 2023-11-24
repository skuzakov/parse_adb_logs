import os


def parse(path):
  s = ""
  for file in os.listdir(fr'{path}'):
      cur_path = os.path.join(fr'{path}', file)
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
             fin = f'\n{date[a]} {time[a]},{ip_s[a]},{ip_d[a]},'
             log1.append(fin)

      result = '\n'.join(log1)
      s += result
  return s


def fin():
    folder = input("Write path to folder with necessary concurrency\nThe output file will appear in the same folder:  ")
    data = parse(folder)
    f = open(f'{folder}/parse_out.csv', "w")
    f.write(data.replace('\n\n','\n'))
    f.close()


if __name__ == "__main__":
    fin()

