from multiprocessing import Process
import os


# 子进程要执行的代码
def run_proc(name):
    print('run child process %s (%s)'(name, os.getpid()))


print('Parent process %s.' % os.getpid())
p = Process(target=run_proc, args=('test',))
print('Child process will start.')
p.start()
p.join()
print('Child process end.')
