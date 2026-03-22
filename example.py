def main()
  with open('passlist.txt') as ls:
    for line in ls:
      print(line.strip())
      # you may also add other code here to do with the dict attack

if __name__=="__main__":
  main()
