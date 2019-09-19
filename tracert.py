from subprocess import *


# source_path 存放准备路径跟踪的域名
# result_path 存放检索的结果
def Tracert(source_path="source.txt", result_path='result.txt'):
    with open(result_path, 'w') as f:
        with open(source_path, 'r') as ff:
            for line in ff:
                print(line)
                p = Popen(['tracert', line], stdin=PIPE, stdout=f, shell=True)
                p.wait()

if __name__ == '__main__':
    Tracert()
