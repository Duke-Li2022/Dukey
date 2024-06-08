import multiprocessing
import subprocess
import os


def run_main_py():
    subprocess.run(["python", "main.py"])


if __name__ == "__main__":
    # 获取当前脚本所在的目录
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # 切换到脚本所在的目录
    os.chdir(script_dir)

    # 创建四个进程
    processes = []
    for _ in range(4):
        p = multiprocessing.Process(target=run_main_py)
        p.start()
        processes.append(p)

    # 等待所有进程完成
    for p in processes:
        p.join()
