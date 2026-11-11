datatype Option<T> = None | Some(T)

ghost predicate Menor(a:set<int>, b:set<int>) {
  forall x, y :: x in a && y in b ==> x < y
}

ghost function Uniao<Data>(m:map<int, Data>, n:Nodo?<Data>): map<int, Data>
  reads n
  ensures var u := Uniao(m, n); |m.Keys| <= |u.Keys|
{
  if n == null
  then m
  else
    var u := m + n.Mapa;
    SubsetCardinality(m.Keys, u.Keys);
    u
}

lemma SubsetCardinality(a: set, b: set)
  requires a <= b
  ensures |a| <= |b|
{
  if a != {}
  {
    var x :| x in a;
    SubsetCardinality(a - {x}, b - {x});
  }
}

class Nodo<T>
{
  //Abstração
  ghost var Mapa:map<int,T>
  ghost var Repr:set<object>
  //Implementação
  var chave:int
  var valor:T
  var esq:Nodo?<T>
  var dir:Nodo?<T>

  ghost predicate Valid()
    reads this, Repr
    ensures Valid() ==> this in Repr
  {
    && this in Repr
    && (esq != null ==>
      && esq in Repr
      && esq.Repr <= Repr
      && this !in esq.Repr
      && esq.Valid()
      && Menor(esq.Mapa.Keys, {chave})
    )
    && (dir != null ==>
      && dir in Repr
      && dir.Repr <= Repr
      && this !in dir.Repr
      && dir.Valid()
      && Menor({chave}, dir.Mapa.Keys)
    )
    && (esq != null && dir != null ==> esq.Repr !! dir.Repr)
    && Mapa == Uniao(Uniao(map[chave := valor], esq), dir)
  }

  constructor (chave:int, valor:T)
    ensures Valid() && fresh(Repr)
    ensures Mapa == map[chave := valor]
  {
    this.chave := chave;
    this.valor := valor;
    esq := null;
    dir := null;
    Mapa := map[chave := valor];
    Repr := {this};
  }

  function Buscar(chave:int):Option<T>
    requires Valid()
    reads Repr
    ensures chave in Mapa.Keys ==> Buscar(chave) == Some(Mapa[chave])
    ensures chave !in Mapa.Keys ==> Buscar(chave) == None
  {
    if chave == this.chave
    then Some(valor)
    else if chave < this.chave && esq != null
      then esq.Buscar(chave)
      else if chave > this.chave && dir != null
           then dir.Buscar(chave)
           else None
  }

  method {:timeLimit 0} Adicionar(chave:int, valor:T)
    requires Valid()
    modifies Repr
    ensures Valid() && fresh(Repr - old(Repr))
    ensures Mapa == old(Mapa)[chave := valor]
    decreases Repr
  {
    if chave == this.chave
    {
      this.valor := valor;
    }
    else if chave < this.chave
    {
      if esq == null
      {
        esq := new Nodo(chave, valor);
      }
      else
      {
        esq.Adicionar(chave, valor);
      }
      Repr := Repr + esq.Repr;
    }
    else
    {
      if dir == null
      {
        dir := new Nodo(chave, valor);
      }
      else
      {
        dir.Adicionar(chave, valor);
      }
      Repr := Repr + dir.Repr;
    }
    Mapa := Mapa[chave := valor];
  }
}

class ArvoreBinariaBusca<T>
{
  //Abstração
  ghost var Mapa:map<int,T>
  ghost var Repr:set<object>
  //Implementação
  var raiz:Nodo?<T>

  ghost predicate Valid()
    reads this, Repr
    ensures Valid() ==> this in Repr
  {
    && this in Repr
    && (|Mapa.Keys| == 0 ==> raiz == null)
    && (|Mapa.Keys| != 0 ==>
      && raiz in Repr
      && raiz.Repr <= Repr
      && this !in raiz.Repr
      && raiz.Valid()
      && raiz.Mapa == Mapa
    )
  }
    
  constructor ()
    ensures Valid() && fresh(Repr)
    ensures Mapa == map[]
  {
    raiz := null;
    Repr := {this};
    Mapa := map[];
  }
    
  function Buscar(chave:int):Option<T>
    requires Valid()
    reads Repr
    ensures chave in Mapa.Keys ==> Buscar(chave) == Some(Mapa[chave])
    ensures chave !in Mapa.Keys ==> Buscar(chave) == None
  {
    if raiz == null
    then None
    else raiz.Buscar(chave)
  }

  method Adicionar(chave:int, valor:T)
    requires Valid()
    modifies Repr
    ensures Valid() && fresh(Repr - old(Repr))
    ensures Mapa == old(Mapa)[chave := valor]
  {
    if raiz == null
    {
      raiz := new Nodo(chave, valor);
    }
    else
    {
        raiz.Adicionar(chave, valor);
    }
    Mapa := Mapa[chave := valor];
    Repr := Repr + raiz.Repr;
  }
}

method Main()
{
  var arv := new ArvoreBinariaBusca<string>();
  var e := arv.Buscar(1);
  assert e == None;
  arv.Adicionar(1,"a");
  arv.Adicionar(2,"b");
  arv.Adicionar(3,"c");
  e := arv.Buscar(3);
  assert e == Some("c");
}