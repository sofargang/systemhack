# RETURN TO LIBRARY
0. 서비스에 오브플로우를 발생시킬 수 있는 입력이 두번 필요
0. CHECKSEC 결과값
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    Canary found       // 카나리O
    NX:       NX enabled	 // NX O
    PIE:      No PIE (0x400000)  // PIE X
0. 개념 정리
- ASLR: 임의 버퍼의 주소를 알기 어렵게 함 
- NX(각 세그먼트에 불필요한 실행권한을 제거)를 우회 가능
- NX: 실행할 수 있는 메모리 영역에서만 코드가 실행되게 하는 보호 기법
- PIE : 데이터 영역뿐만 아니라 코드 영역에도 ASLR이 적용
- PLT: 외부 프로시저를 연결해주는 테이블. PLT를 통해 다른 라이브러리에 있는 프로시저를 호출
- GOT: PLT가 참조하는 테이블. 프로시저들의 주소가 존재
0. NX 우회 :  바이너리 코드 영역과 바이너리가 참조하는 라비르러리의 코드 영역은 실행 권한 존재
0. 프로그램에서 과감한 system 함수의 사용이 있어야 한다.
