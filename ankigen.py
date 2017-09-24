import sys, json 

f = open(sys.argv[1],'r')
input=json.load(f)
for card in range(len(input)):
        print('"' + input[card]['front'] + '"' + ';' + '"' + input[card]['back'] + '"' +';')
