# ROP(Return Oriented Programming)
0. Hook Overwrite은 훅의 특징을 이용한 공격 기법으로 malloc과 free 함수를 후킹하여 각 함수가 호출될 때, 공격자가 작성한 악의적인 코드가 실행되게 하는 기법
0. Full RELRO를 우회하는 기법
0. CHECKSEC 결과값(모든 기법 적용)
    Arch:     amd64-64-little
    RELRO:    Full RELRO
    Stack:    Canary found
    NX:       NX enabled
    PIE:      PIE enabled
0. 

