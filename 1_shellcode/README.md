1. 파일 경로 ASCII TO HEX
2. C파일 경로 수정(tool_ascii_to_hex.py)
3. 실행 파일 생성(gcc -o exploit exploit.c -masm=intel)
4. 디스어셈블 DUMP 생성(objdump -d exploit.c)
5. run_sh 함수의 부분만 잘라서 셀코드 추출(tool_shellcode_extract.py)
6. 셀코드를 사용하여 원격 서버 EXPLOIT

