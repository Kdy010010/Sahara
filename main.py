# 예제 코드: sahara_compiler.py

import subprocess
import sys
import importlib.util

def compile_sahara(source_path, output_path):
    with open(source_path, 'r') as source_file:
        sahara_code = source_file.read()

    # 파싱 및 원하는 작업 수행
    lines = sahara_code.split('\n')
    for line in lines:
        if line.startswith('call='):
            module_name = line.split('"')[1]
            compile_and_execute_module(module_name, output_path)

def compile_and_execute_module(module_name, output_path):
    # 모듈을 가져와서 컴파일
    spec = importlib.util.spec_from_file_location(module_name, module_name)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    # nutikia를 사용하여 .o 파일로 컴파일
    subprocess.run(['nutikia', '-o', output_path, module_name])

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python sahara_compiler.py input.sahara output.o")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    compile_sahara(input_path, output_path)
