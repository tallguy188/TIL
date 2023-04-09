### NoArgsConstructor, RequiredArgsConstructor, AllArgsConstructor

------



* `@NoArgsConstructor` : 파라미터가 없는 기본 생성자를 생성
* `@RequiredArgConstructor` : final이나 `@NonNull`인 필드 값만 파라미터로 받는 생성자를 생성
* `@AllArgsConstructor`: 모든 필드 값을 파라미터로 받는 생성자를 생성



```java
@NoArgsConstructor
@RequiredArgsConstructor
@AllArgsConstructor
public class User {

  private Long id;
  
  @NonNull
  private String name;
  
  @NonNull
  private String pw;
  
  private int age;
  
}
```

```java
User user1 = new User(); // @NoArgsConstructor
User user2 = new User("user2", "1234"); // @RequiredArgsConstructor
User user3 = new User(1L, "user3", "1234", null); // @AllArgsConstructor
```

