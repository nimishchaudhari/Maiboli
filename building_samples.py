# To build sample programs
import dix

#Star pattern:
ip = """
def star(x):
    for i in range(0,x):
        for j in range(0,i+1):
            print('*', end='')
        print('')
x = 5
print(star(x))
"""


def building_examples(ip,dix1,dix2):
    for index in range(0,len(dix1)):
            if(dix1[index].strip() in ip):
                ip = ip.replace(dix1[index].strip(),dix2[index].strip())
    return ip

for i in dix.list_of_avail_lang:
    print("```bash")
    print(building_examples(ip,dix.en_final,i))
    print("```")