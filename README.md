﻿# MicroProgramTracingBasicComputer
Microprogram tracing basic computer

## About
Это не мой проект, я его только реконструирую. К сожалению создатель не оставил мануала по обновлению микрокода, да и содержание тестов стало известно только благодаря реверсинженирингу.

## Variant file manual
Для создания своего варианта вам необходимо создать файл с именем "номер варианта" без расширения.  
Например, файлы 101, 201, 543 будут отвечать соответственно за 101й, 201й, 543й вариант.  
Внутри файла должен быть JSON с примерно таким содержанием:  
```json
{"cmd": ["18E", "LD (0x171)", "A8E2"], "mem": ["171", "018E"], "regs": ["0000000000", "18E", "1B3B", "24A", "E927", "5AF", "868E", "DF91", "0011"]}
```

Где,  
`cmd[0]` - адрес команды (HEX),  
`cmd[1]` - мнемоника (String),  
`cmd[2]` - HEX-значение команды (HEX),  

`mem[0]` - адрес ячейки памяти (HEX),  
`mem[1]` - её значение (HEX),  

необязательно: `mem[2i]` - адрес ячейки памяти (HEX), `mem[2i+1]` - её значение (HEX),

`regs[0]` - MR (HEX),  
`regs[1]` - значение регистра IP (HEX),  
`regs[2]` - значение регистра CR (HEX),  
`regs[3]` - значение регистра AR (HEX),  
`regs[4]` - значение регистра DR (HEX),  
`regs[5]` - значение регистра SP (HEX),  
`regs[6]` - значение регистра BR (HEX),  
`regs[7]` - значение регистра AC (HEX),  
`regs[8]` - значение регистра PS (BIN).  