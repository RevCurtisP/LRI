100 REM TANDY COCO LRI VIEWER
110 CLEAR 1024
150 OPEN "I",#1,"ATOM/LRI"
160 IF EOF(1) THEN 190
170 INPUT#1,L$
180 D$=D$+L$:GOTO 160
190 CLOSE #1
200 REM DECODE & DISPLAY IMAGE
210 CLS 0
220 FOR I=1 TO 7:READ F(I):NEXT
225 DATA 32,48,96,0,80,16,64
235 L=8:PRINT @L,"";
300 :REM LOOP THROUGH LRI DATA
310 FOR I=1 TO LEN(D$)
315 G=ASC(MID$(D$,I))
320 G=G-48:IF G<0 THEN 390
325 IF G<10 THEN N=G:GOTO 390
330 G=G-17:IF G<0 THEN 390
332 IF G>31 THEN G=G-32
335 IF G<16 THEN 350
340 G=G-15:IF G<8 THEN F=F(G)
345 GOTO 390
350 FOR J=1 TO N
360 PRINT CHR$(128+F+G);
365 C=C+1:IF C<16 THEN 380
370 L=L+32:C=0
375 IF L<512 THEN PRINT @L,"";
380 NEXT
385 N=0
390 NEXT
400 REM WAIT FOR KEY AND EXIT
410 IF INKEY$="" THEN 410
420 CLS

