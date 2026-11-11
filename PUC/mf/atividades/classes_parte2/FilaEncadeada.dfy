class Node<T(0)>
{
  //Implementação
  var data: T
  var next: Node?<T>
  //Abstração
  ghost var nextContents: seq<T>
  ghost var Repr: set<object>

  ghost predicate Valid()
    reads this, Repr
    ensures Valid() ==> this in Repr
  {
    && this in Repr
    && (next != null ==> next in Repr && next.Repr <= Repr)
    && (next == null ==> nextContents == [])
    && (next != null ==> nextContents == [next.data] + next.nextContents)
  }

  constructor ()
    ensures Valid() && fresh(Repr - {this})
    ensures next == null
  {
    next := null;
    nextContents := [];
    Repr := {this};
  }
}

class Queue<T(0)>
{
  //Implementação
  var head: Node<T>
  var tail: Node<T>
  //Abstração
  ghost var contents: seq<T>
  ghost var Repr: set<object>
  ghost var chaining: set<Node<T>>

  ghost predicate Valid()
    reads this, Repr
    ensures Valid() ==> this in Repr
  {
    && this in Repr
    && chaining <= Repr
    && head in chaining
    && tail in chaining
    && tail.next == null
    && (forall n :: n in chaining ==>
      //nodo não está presente na representação do seu sucessor
      //isso implica no encademento não ser cíclico 
      && n.Repr <= Repr
      && this !in n.Repr
      && n.Valid()
      && (n.next == null ==> n == tail)
    )
    && (forall n :: n in chaining ==> n.next != null ==> n.next in chaining)
    && contents == head.nextContents
  }

  constructor ()
    ensures Valid() && fresh(Repr - {this})
    ensures |contents| == 0
  {
    var n: Node<T> := new Node<T>();
    head := n;
    tail := n;
    contents := n.nextContents;
    Repr := {this} + n.Repr;
    chaining := {n};
  }

  predicate IsEmpty()
    requires Valid()
    reads Repr
    ensures IsEmpty() <==> |contents| == 0
  {
    head == tail
  }

  method Enqueue(t: T)
    requires Valid()
    modifies Repr
    ensures Valid() && fresh(Repr - old(Repr))
    ensures contents == old(contents) + [t]
  {
    var n := new Node<T>();
    n.data := t;
    tail.next := n;
    tail := n;

    forall m | m in chaining {
      m.nextContents := m.nextContents + [t];
    }
    contents := head.nextContents;

    forall m | m in chaining {
      m.Repr := m.Repr + n.Repr;
    }
    Repr := Repr + n.Repr;

    chaining := chaining + {n};
  }

  function Front():T
    requires Valid()
    requires 0 < |contents|
    reads Repr
    ensures Front() == contents[0]
  {
    head.next.data
  }

  method Dequeue()
    requires Valid()
    requires 0 < |contents|
    modifies Repr
    ensures Valid() && fresh(Repr - old(Repr))
    ensures contents == old(contents)[1..]
  {
    var n := head.next;
    head := n;
    contents := n.nextContents;
  }
}

method Main()
{
    var q0 := new Queue<int>();
    var q1 := new Queue<int>();

    q0.Enqueue(1);
    q0.Enqueue(2);

    q1.Enqueue(1);

    assert |q0.contents| == 2;

    var w := q0.Front();
    assert w == 1;
    q0.Dequeue();

    w := q0.Front();
    assert w == 2;

    assert |q0.contents| == 1;
    assert |q1.contents| == 1;
}