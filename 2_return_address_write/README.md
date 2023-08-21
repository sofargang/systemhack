# REMOTE SERVER RETURN ADDRESS OVERWRITE
0. 서비스가 입력받는 문자열에 길이 제한이 없는 조건 필요, 쉘을 실행시키는 함수 필요
1. 서비스 gdb로 확인해서 scanf에 전달되는 rbp의 상대 주소 확인(rbp-0x30)해서 그만큼 덤프 값
2. 서비스 gdb로 확인해서 쉘을 실행시키는 함수 주소값 확인(print get_shell, 0x4006aa)
3. 쉘을 실행시키는 주소값은 엔디언 적용 및 쉘코드 주소 형태로 변경
(0x4006aa -> \xaa\x06\x40\x00\x00\x00\x00\x00)
4. 파이썬으로 쉘코드 전달
