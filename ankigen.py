import sys, json 

input=json.load(sys.stdin)
for card in range(len(input)):
        print('"' + input[card]['front'] + '"' + ';' + '"' + input[card]['back'] + '"' +';')
