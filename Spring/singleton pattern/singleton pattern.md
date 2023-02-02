### 웹 애플리케이션과 싱글턴



#### 싱글턴 패턴(Singleton pattern)

------

소프트웨어 디자인 패턴에서 싱글턴 패턴을 따르는 클래스는, 생성자가 여러 차례 호출되더라도 실제로 생성되는 객체는 하나이고, 최초 생성 이후에 호출된 생성자는 최초의 생성자가 생성한 객체를 리턴한다.

##### 싱글턴 패턴의 사용 이유

만약 우리가 만들었던 DI 컨테이너가 요청을 할때마다 새로운 객체를 생성한다고 하면 요청이 엄청나게 많은 트래픽 사이트에서는 계속 객체를 생성하게 되고, 이는 심한 메모리 낭비를 유발하게 된다.



#### 싱글턴 패턴 구현

------

##### 순수한 DI 컨테이너

```java
@Test
@DisplayName("스프링 없는 순수한 DI 컨테이너")
void pureContainer() {
    AppConfig appConfig = new AppConfig();
    
    //1. 호출 할 때 마다 다른 객체를 생성
    MemberService memberService1 = appConfig.memberService();
    //2. 호출 할 때 마다 다른 객체를 생성
    MemberService memberService2 = appConfig.memberService();
    Assertions.assertThat(memberService1).isNotSameAs(memberService2);
}
```

1. 객체를 생성하면 매번 새로운 객체가 생성된다.
2. 많은 객체를 생성해야 하는 서비스(어플리케이션) 에서는 메모리 낭비가 많아진다.

##### 싱글턴 패턴 구현

```java
//1. static 영역에 객체를 딱 1개만 생성한다
private static final SingletonService instance = new SinglegonService();
//2. static method를 통해서만 객체를 생성하도록 한다.
public static SingletonService getInstance() {
    return instance;
}
//3. private 생성자를 통해서 외부에서 new로 객체생성하는 것을 막는다.
private SingletonService(){ }
```

```java
@Test
@DisplayName("싱글턴 패턴을 적용한 객체 생성")
void singletonContainer() {
    SingletonService singletonService1 = SingletonService.getInstance();
    SingletonService singletonService2 = SingletonService.getInstance();
    Assertions.assertThat(singletonService1).isNotSameAs(singletonService2);
    
}
```

1. static 객체를 통해서 해당 객체를 1개만 생성할 수 있도록 지정한다.
2. static 메소드를 통해서 외부에서 생성할 수 있도록 제한한다. 
3. new 연산자를 통해서 객체를 만드는 것을 private 생성자를 통해서 제한한다.

싱글턴 패턴을 구현하는 방법은 여러가지가 있다. 이 방법은 객체를 미리 생성해두는 가장 단순하고 안전한 방법이다. 싱글턴 패턴을 이미 만들어진 객체를 공유해서 효율적으로 사용할 수 있다. 



#### 싱글턴 패턴의 문제점

* 싱글턴 패턴을 구현하는 코드 자체가 많다.
* 의존관계상 클라이언트가 구체 클래스에 의존한다.
* 테스트하기 어렵다.
* 내부 속성을 변경하거나 초기화하기 어렵다.
* private 생성자로 자식 클래스를 만들기 어렵다.
* 싱글톤 컨테이너
* 스프링에서 위의 단점을 모두 해결해준다.

즉 , 싱글턴 패턴을 사용하게 되면 `유연성`이 떨어지게 된다.



