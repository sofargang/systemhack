- solved by hint
- stack buffer overflow
- main dump
   0x00005555555552b0 <+0>:	endbr64 
   0x00005555555552b4 <+4>:	push   rbp
   0x00005555555552b5 <+5>:	mov    rbp,rsp
   0x00005555555552b8 <+8>:	sub    rsp,0x50
   0x00005555555552bc <+12>:	mov    DWORD PTR [rbp-0x44],edi
   0x00005555555552bf <+15>:	mov    QWORD PTR [rbp-0x50],rsi
   0x00005555555552c3 <+19>:	mov    eax,0x0
   0x00005555555552c8 <+24>:	call   0x555555555269 <initialize>
   0x00005555555552cd <+29>:	mov    esi,0x0
   0x00005555555552d2 <+34>:	lea    rax,[rip+0xd2f]        # 0x555555556008
   0x00005555555552d9 <+41>:	mov    rdi,rax
   0x00005555555552dc <+44>:	mov    eax,0x0
   0x00005555555552e1 <+49>:	call   0x555555555170 <open@plt>
   0x00005555555552e6 <+54>:	mov    DWORD PTR [rbp-0x4],eax
   0x00005555555552e9 <+57>:	mov    DWORD PTR [rbp-0x8],0x45
   0x00005555555552f0 <+64>:	lea    rax,[rip+0xd19]        # 0x555555556010
   0x00005555555552f7 <+71>:	mov    QWORD PTR [rbp-0x10],rax
   0x00005555555552fb <+75>:	mov    rax,QWORD PTR [rbp-0x10]  # [rbp-0x10] = 2nd param(fake_flag_addr)
   0x00005555555552ff <+79>:	mov    rsi,rax
   0x0000555555555302 <+82>:	lea    rax,[rip+0xd4c]        # 0x55555555605s
   0x0000555555555309 <+89>:	mov    rdi,rax
   0x000055555555530c <+92>:	mov    eax,0x0
   0x0000555555555311 <+97>:	call   0x555555555110 <printf@plt>
   0x0000555555555316 <+102>:	lea    rax,[rbp-0x40]            # [rbp-0x40] = 2nd param(buf)
   0x000055555555531a <+106>:	mov    rsi,rax
   0x000055555555531d <+109>:	lea    rax,[rip+0xd48]        # 0x55555555606c
   0x0000555555555324 <+116>:	mov    rdi,rax
   0x0000555555555327 <+119>:	mov    eax,0x0
   0x000055555555532c <+124>:	call   0x555555555110 <printf@plt>
   0x0000555555555331 <+129>:	mov    eax,DWORD PTR [rbp-0x4]
   0x0000555555555334 <+132>:	mov    r9d,0x0
   0x000055555555533a <+138>:	mov    r8d,eax
   0x000055555555533d <+141>:	mov    ecx,0x2
   0x0000555555555342 <+146>:	mov    edx,0x1
   0x0000555555555347 <+151>:	mov    esi,0x45
   0x000055555555534c <+156>:	mov    edi,0x0
   0x0000555555555351 <+161>:	call   0x555555555100 <mmap@plt>
   0x0000555555555356 <+166>:	mov    QWORD PTR [rbp-0x18],rax
   0x000055555555535a <+170>:	mov    rax,QWORD PTR [rbp-0x18]  # [rbp-0x18] = 2nd param(real_flag_addr)
   0x000055555555535e <+174>:	mov    rsi,rax
   0x0000555555555361 <+177>:	lea    rax,[rip+0xd18]        # 0x555555556080
   0x0000555555555368 <+184>:	mov    rdi,rax
   0x000055555555536b <+187>:	mov    eax,0x0
   0x0000555555555370 <+192>:	call   0x555555555110 <printf@plt>
   0x0000555555555375 <+197>:	lea    rax,[rip+0xd2d]        # 0x5555555560a9
   0x000055555555537c <+204>:	mov    rsi,rax
   0x000055555555537f <+207>:	lea    rax,[rip+0xd2b]        # 0x5555555560b1
   0x0000555555555386 <+214>:	mov    rdi,rax
   0x0000555555555389 <+217>:	mov    eax,0x0
   0x000055555555538e <+222>:	call   0x555555555110 <printf@plt>
   0x0000555555555393 <+227>:	lea    rax,[rbp-0x40]
   0x0000555555555397 <+231>:	mov    edx,0x3c
   0x000055555555539c <+236>:	mov    rsi,rax
   0x000055555555539f <+239>:	mov    edi,0x0
   0x00005555555553a4 <+244>:	call   0x555555555130 <read@plt>
   0x00005555555553a9 <+249>:	mov    eax,DWORD PTR [rbp-0x8]  # [rbp-0x8] = 2nd param(len)
   0x00005555555553ac <+252>:	movsxd rcx,eax
   0x00005555555553af <+255>:	mov    rax,QWORD PTR [rbp-0x18]
   0x00005555555553b3 <+259>:	mov    edx,0x0
   0x00005555555553b8 <+264>:	mov    rsi,rcx
   0x00005555555553bb <+267>:	mov    rdi,rax
   0x00005555555553be <+270>:	call   0x555555555160 <mprotect@plt>
   0x00005555555553c3 <+275>:	mov    rax,QWORD PTR [rbp-0x10]
   0x00005555555553c7 <+279>:	mov    edx,0x45
   0x00005555555553cc <+284>:	mov    rsi,rax
   0x00005555555553cf <+287>:	mov    edi,0x1
   0x00005555555553d4 <+292>:	call   0x5555555550f0 <write@plt>
   0x00005555555553d9 <+297>:	lea    rax,[rip+0xcd4]        # 0x5555555560b4
   0x00005555555553e0 <+304>:	mov    rdi,rax
   0x00005555555553e3 <+307>:	mov    eax,0x0
   0x00005555555553e8 <+312>:	call   0x555555555110 <printf@plt>
   0x00005555555553ed <+317>:	lea    rax,[rbp-0x40]
   0x00005555555553f1 <+321>:	mov    rdi,rax
   0x00005555555553f4 <+324>:	call   0x5555555550e0 <puts@plt>
   0x00005555555553f9 <+329>:	mov    rax,QWORD PTR [rbp-0x18]
   0x00005555555553fd <+333>:	mov    esi,0x45
   0x0000555555555402 <+338>:	mov    rdi,rax
   0x0000555555555405 <+341>:	call   0x555555555140 <munmap@plt>
   0x000055555555540a <+346>:	mov    eax,DWORD PTR [rbp-0x4]
   0x000055555555540d <+349>:	mov    edi,eax
   0x000055555555540f <+351>:	call   0x555555555120 <close@plt>
   0x0000555555555414 <+356>:	mov    eax,0x0
   0x0000555555555419 <+361>:	leave  
   0x000055555555541a <+362>:	ret    

- x86-64 아키텍처에서는 함수를 호출할 때 rdi, rsi, rdx, rcx, r8, r9 순서로 인자를 저장
- stack image
 buf(32)              rbp-0x40
 dummy           
 real_flag_addr(8)    rbp-0x18
 fake_flag_addr(8)    rbp-0x10
 len(4)               rbp-0x8
 fd(4)
 rbp
 return address
