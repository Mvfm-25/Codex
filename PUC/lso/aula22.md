# Laboratório de Sistemas Operacionais
## [15-10][mvfm]
---
### Debuggers
- Como que eles funcionam?
- Pelo o que ele mostrou por enquanto, por Traces.
    - "*Function tracing é um recurso que permite o rastreamento das funções que estão sendo chamadas no sistema.*"
![Resultado final](assets/trace_print.png)
- Pegando um debugger mais genérico e conhecido possível, o sor escolheu o *GDBServer* como exemplo do funcionamento :
```
    gdb.client      PID
        ^            ^
        |            |          program.exe
        |       gdb.server           ^  |
        |           | |______________|  |
        |___________|                   v
        |           v                  addr ---->   T(+)
        |       localhost:2345          |
        |                               |    
        |-------------> IDE <-----------|

```
- Formato de saída do trace :
![Formato de saída](assets/formato_saida.png)
