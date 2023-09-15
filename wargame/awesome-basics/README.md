- stack buffer overflow?
- main dump
   0x00000000000012ef <+0>:	endbr64 
   0x00000000000012f3 <+4>:	push   rbp
   0x00000000000012f4 <+5>:	mov    rbp,rsp
   0x00000000000012f7 <+8>:	sub    rsp,0x70
   0x00000000000012fb <+12>:	mov    DWORD PTR [rbp-0x64],edi
   0x00000000000012fe <+15>:	mov    QWORD PTR [rbp-0x70],rsi
   0x0000000000001302 <+19>:	mov    DWORD PTR [rbp-0x4],0x0
   0x0000000000001309 <+26>:	mov    DWORD PTR [rbp-0x8],0x1
   0x0000000000001310 <+33>:	mov    eax,0x0
   0x0000000000001315 <+38>:	call   0x128a <initialize>
   0x000000000000131a <+43>:	mov    edi,0x45
   0x000000000000131f <+48>:	call   0x1140 <malloc@plt>
   0x0000000000001324 <+53>:	mov    QWORD PTR [rip+0x2d05],rax        # 0x4030 <flag>
   0x000000000000132b <+60>:	mov    esi,0x0
   0x0000000000001330 <+65>:	lea    rax,[rip+0xcd6]        # 0x200d
   0x0000000000001337 <+72>:	mov    rdi,rax
   0x000000000000133a <+75>:	mov    eax,0x0
   0x000000000000133f <+80>:	call   0x1160 <open@plt>
   0x0000000000001344 <+85>:	mov    DWORD PTR [rbp-0xc],eax
   0x0000000000001347 <+88>:	mov    rcx,QWORD PTR [rip+0x2ce2]        # 0x4030 <flag>
   0x000000000000134e <+95>:	mov    eax,DWORD PTR [rbp-0xc]
   0x0000000000001351 <+98>:	mov    edx,0x45
   0x0000000000001356 <+103>:	mov    rsi,rcx
   0x0000000000001359 <+106>:	mov    edi,eax
   0x000000000000135b <+108>:	call   0x1120 <read@plt>
   0x0000000000001360 <+113>:	mov    eax,DWORD PTR [rbp-0xc]
   0x0000000000001363 <+116>:	mov    edi,eax
   0x0000000000001365 <+118>:	call   0x1110 <close@plt>
   0x000000000000136a <+123>:	mov    esi,0x1
   0x000000000000136f <+128>:	lea    rax,[rip+0xc9e]        # 0x2014
   0x0000000000001376 <+135>:	mov    rdi,rax
   0x0000000000001379 <+138>:	mov    eax,0x0
   0x000000000000137e <+143>:	call   0x1160 <open@plt>
   0x0000000000001383 <+148>:	mov    DWORD PTR [rbp-0x10],eax
   0x0000000000001386 <+151>:	mov    eax,DWORD PTR [rbp-0x8]
   0x0000000000001389 <+154>:	mov    edx,0xc
   0x000000000000138e <+159>:	lea    rcx,[rip+0xc8a]        # 0x201f
   0x0000000000001395 <+166>:	mov    rsi,rcx
   0x0000000000001398 <+169>:	mov    edi,eax
   0x000000000000139a <+171>:	call   0x10f0 <write@plt>
   0x000000000000139f <+176>:	lea    rcx,[rbp-0x60]            # buf = rbp-0x60
   0x00000000000013a3 <+180>:	mov    eax,DWORD PTR [rbp-0x4]
   0x00000000000013a6 <+183>:	mov    edx,0x80
   0x00000000000013ab <+188>:	mov    rsi,rcx
   0x00000000000013ae <+191>:	mov    edi,eax
   0x00000000000013b0 <+193>:	call   0x1120 <read@plt>
   0x00000000000013b5 <+198>:	mov    rcx,QWORD PTR [rip+0x2c74]        # 0x4030 <flag>
   0x00000000000013bc <+205>:	mov    eax,DWORD PTR [rbp-0x10]  # tmp_fd = rbp-0x10
   0x00000000000013bf <+208>:	mov    edx,0x45
   0x00000000000013c4 <+213>:	mov    rsi,rcx
   0x00000000000013c7 <+216>:	mov    edi,eax
   0x00000000000013c9 <+218>:	call   0x10f0 <write@plt>
   0x00000000000013ce <+223>:	lea    rcx,[rbp-0x60]
   0x00000000000013d2 <+227>:	mov    eax,DWORD PTR [rbp-0x10]
   0x00000000000013d5 <+230>:	mov    edx,0x50
   0x00000000000013da <+235>:	mov    rsi,rcx
   0x00000000000013dd <+238>:	mov    edi,eax
   0x00000000000013df <+240>:	call   0x10f0 <write@plt>
   0x00000000000013e4 <+245>:	mov    eax,DWORD PTR [rbp-0x10]
   0x00000000000013e7 <+248>:	mov    edi,eax
   0x00000000000013e9 <+250>:	call   0x1110 <close@plt>
   0x00000000000013ee <+255>:	mov    eax,0x0
   0x00000000000013f3 <+260>:	leave  
   0x00000000000013f4 <+261>:	ret   

- x86-64 아키텍처에서는 함수를 호출할 때 rdi, rsi, rdx, rcx, r8, r9 순서로 인자를 저장
- stack image
 buf(80)      rbp-0x60
 tmp_fd(4)    rbp-0x10
 rbp
 return addr
