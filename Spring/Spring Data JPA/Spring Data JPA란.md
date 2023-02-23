### Spring Data JPA란

------

* JPA에서 Repository를 제작할 때마다 반복적으로 작성되는 CRUD메서드가 존재한다.
* 예를 들어, 특정 ID값을 기반으로 Entity를 조회하는 등의 메서드 말이다.
* 이처럼 반복작성되는 메서드를 자동화하여 기본적인 CRUD메서드를 제공하는 라이브러리이다.



#### 사용방법

* 앞으로 사용할 Repository를 인터페이스로 선언하고 다음과 같이 JpaRepository를 상속받는다.

```java
import org.springframework.data.jpa.repository.JpaRepository;

public interface DataJpaRepository extends JpaRepository<Type, Id> {}
```

* JpaRepository를 제네릭을 이용하여 자료형과 Id를 선언해줘야 하는데, 각 제네릭은 다음을 의미한다.

Type: 사용할 Repository의 기준이 되는 Entity의 이름을 기입한다.

Id: 기입된 Entity의 PK자료형을 기입한다.

예를 들어 Order를 관리하는 Repository를 선언한다고 해보자.

Order라는 Entity는 이미 작성하였고, Order Entity는 Long 자료형을 PK값으로 사용한다.

이는 다음과 같이 작성할 수 있다.

```java
public interface OrderRepository extends JpaRepository<Order, Long> {}
```

* 위에 작성한 OrderRepository의 객체를 만들어 확인해보면, 기본 제공되는 메서드를 확인할 수 있다.
* 일반적으로 개발자가 생각할 수 있는 기본적인 CRUD기능은 모두 있다.

* 이처럼 자동적으로 Entity를 관리하는데 필요한 메서드를 Spring Data JPA에서 알아서 제공해준다.
* 추가적으로 메서드가 필요하면, 해당 인터페이스에 선언하여 사용하면 된다.

#### 메서드 선언

* Spring Data JPA는 알아서 구현체를 만들어준다.
* 메서드 이름을 작명하는 규칙이 있어서 메서드 이름을 기반으로 메서드의 구현체를 알아서 만들어준다.
* 예를들어, findByUserName()이라는 메서드를 선언하려고 한다.
* 해당 메서드는 주문을 요청한 회원의 이름으로 조회하는 메서드이다.
* 이는 다음과 같이 Repository인터페이스에 정의할 수 있다.

```java
public interface OrderRepository extends JpaRepository<Order, Long> {

   List<Order> findByUserName(String userName);

}
```

* 위의 코드처럼 작성하면 Spring Data JPA는 메서드의 이름을 기반으로 다음과 같은 쿼리를 구현체로 만들어준다.

```sql
select o from Order o where o.username = ?
```

Spring Data JPA는 결국 JPA의 기능을 기반으로 제작된 라이브러리이다.

즉 JPA를 기본적으로 이해하고 있어야 문제없이 Spring Data JPA를 사용할 수 있다.