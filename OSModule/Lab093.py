# Wal IN dIR
import os

for root, dir, files in os.walk("/Users/promode/PycharmProjects/PythonForAutomationEngineer/ex_July/0072024"):
    print(f"Current Dir {root}")
    print(f"Sub Dir Dir {dir}")
    print(f"files Dir Dir {files}")
    print(len(files))

    import os

    file_name = os.open('testdata.txt', os.O_)
    os.write(file_name, b'Hello I am writing')
    os.close(file_name)