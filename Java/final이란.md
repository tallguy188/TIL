## final



자바 final 키워드에 대해 알아보자. 

final 키워드는 변수, 메서드, 또는 클래스에 사용될 수 있다. 어떤 곳에 사용되냐에 따라 다른 의미를 가진다. 하지만 공통적으로 final 키워드를 붙이면 무언가를 제한한다는 의미를 갖는다. 



### 변수(variable)

**변수에 final을 붙이면 이 변수는 수정할 수 없다는 의미**를 갖는다. 수정될 수 없기 때문에 초기화 값은 필수적이다. 만약에 객체안의 변수라면 생성자, static 블럭을 통한 초기화까지는 허용된다. 

수정할 수 없다는 범위는 그 변수의 값에 한정한다. 즉, 다른 객체를 참조하거나 할때 참조하는 객체의 내부의 값은  변경할 수 있다는 의미이다. 

```java
public class Service {

  public void variableFinal() {

    final int value = 2;
    final Person person = new Person("사바라다", 29);

    System.out.println("value = " + value);
    System.out.println("person_1 = " + person);

    // value = 2; // 컴파일 에러
    person.setAge(10);
    person.setName("사바라");

    System.out.println("person_2 = " + person);
    // person = new Person("염광호", 29); // 컴파일 에러
  }
}

class Person {

  private String name;

  private int age;

  //.. get, set, toString 메서드 존재하나 길이상 생략
}
value = 2
person_1 = Person{name='사바라다', age=29}
person_2 = Person{name='사바라', age=10}
```

코드를 보면 value라는 기본형 변수와 person이라는 참조형 변수를 하나씩 선언했다. 

결과적으로 기본형 변수는 값이 변경하지 못하고, 참조형 변수는 그 객체 내부의 값은 변경할 수 있지만 가리키는 객체를 변경하지 못한다는 사실을 알 수 있다. 