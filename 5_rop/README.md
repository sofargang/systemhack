# ROP(Return Oriented Programming)
0. 서비스에 오브플로우를 발생시킬 수 있는 입력이 두번 필요
0. 라이브러리 함수 실행하여 리턴 가젯을 연결
0. CHECKSEC 결과값
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    Canary found       // 카나리O
    NX:       NX enabled	 // NX O
    PIE:      No PIE (0x400000)
0. NX(프로그래머가 작성한 코드만 실행가능하게 만듬)를 우회 가능
- NX: 실행할 수 있는 메모리 영역에서만 코드가 실행되게 하는 보호 기법
- PLT: 외부 프로시저를 연결해주는 테이블. PLT를 통해 다른 라이브러리에 있는 프로시저를 호출
- GOT: PLT가 참조하는 테이블. 프로시저들의 주소가 존재
0. 프로그램에 PLT에 system 함수가 포함되어 있을 필요가 없다. 


이것좀 읽어봐
https://blog.naver.com/PostView.naver?blogId=cme1245&logNo=221303896807
