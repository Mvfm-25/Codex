/**
 * Classe de um identificador na tabela de símbolos.
 * Decide ONDE o valor mora em tempo de execução e, portanto, que código gerar.
 */
public enum ClasseID {
    VarGlobal,    // área .data          -> operando  _nome
    VarLocal,     // registro de ativação -> operando  -4*k(%EBP)
    NomeParam,    // registro de ativação -> operando  8+4*j(%EBP)
    NomeFuncao    // rótulo de código     -> CALL _nome
}
