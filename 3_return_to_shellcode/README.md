# REMOTE SERVER RETURN TO SHELLCODE
0. 서비스에 오브플로우를 발생시킬 수 있는 입력이 두번 필요
0. CHECKSEC 결과값
    Arch:     amd64-64-little
    RELRO:    Full RELRO	 
    Stack:    Canary found       // 카나리O
    NX:       NX disabled        // NX X
    PIE:      PIE enabled
    RWX:      Has RWX segments
0. 카나리(스택 버퍼 오버플로우로부터 반환 주소를 보호) 우회 가능
- 카나리: 스택 버퍼와 반환 주소 사이에 임의의 값을 삽입
1. 첫번째 입력에서 카나리 값을 구하고, 두번째 입력에서 반환주소를 덮는다.
