### DDD(Domain Driven Design)

------

도메인 주도 설계란? 마이크로서비스의 관점에서



#### 객체지향이란

------

도메인 주도 설계를 이해하기 위해서는 객체지향을 먼저 이해할 필요가 있다.

객체지향에서의 핵심은 뭘까?

> 객체지향에서의 핵심은 실세계의 객체(물건, 사람, 주문 .... 주도적으로 뭔가를 생산하는 주체) 들이
> 서로간의 상호작용을 바탕으로 책임,협력,역할 의 관점을 가지고 메세지를 교환하는 것이다.

그렇다면 이 객체들을 어떻게 하면 추려낼 수 있을까?

어떻게 하면 어떤 객체가 필요한지 알 수 있을까?

어떻게 하면 이 객체들이 서로 상호작용할 수 있을까?

 

여러 방법들이 있겠지만, 이것을 해결해줄 수 있는 것이 바로 **도메인 주도 설계**다.

도메인 주도 설계란 쉽게 말하면 도메인 중심으로 설계해 나가는 것이다.



#### 도메인이란

------

도메인은 *실세계에서 사건이 발생하는 집합* 이라고 생각하면 쉽다.

옷 쇼핑몰을 한번 예로 들어보면

옷 쇼핑몰에서는 손님들이 주문하는 도메인(Order Domain)이 있을 수 있고,

점주입장에서 옷들을 관리하는 도메인(Manage Domain)이 있을 수 있고,

쇼핑몰 입장에서 월세, 관리비 등 건물에 대한 관리를 담당하는 도메인(Building Domain)이 있을 수 있다.

**이러한 여러가지 도메인들이 서로 상호작용하며, 설계하는 방법이 도메인주도설계이다.** 

도메인 주도 설계에서의 특징은 같은 객체가 여러 개 존재할 수 있다는 것이다. 

주문 도메인에서의 옷은 손님들에게 팔기 위한 객체 정보(name, price .. etc)들을 담고 있지만, 옷을 관리하는 도메인에서는 옷은 점주 입장에서 관리하기 위한 객체 정보(madeTime, size, madeCountry ... etc)들을 위주로 담고 있다.

**다시 말해서 문맥(context)에 따라서 객체의 역할이 바뀐다는 것이다.**

#### 주의점

------

* 도메인 객체는 get/set 메소드를 넣지 않는다. 

  * get/set은 도메인의 핵심 개념이나 의도를 표현하지 못한다. 
  * 도메인은 해당 개념이 어떤 행위를 하고, 어떻게 상태가 변하는지에 집중한다.
  * set/get으로 객체의 상태값을 계속 바꿔서 사용하는 행위는 '객체지향'보다 '절차지향'에 가깝다.

* 도메인 객체는 완전한 상태로 사용한다. 

  * 예를 들어 주문을 하기 위해 `OrderLine`, `ShippingInfo`는 반드시 포함되어야 한다. 
  * `Order` 생성 후 정보를 추가한다면 정보의 일부가 누락되는 상황이 생길 수 있다. 
    * 주문 정보가 없다면?
    * 배송지 정보가 없다면?

* 도메인 용어를 명확히 정의한다. 

  * OrderState.PAYMENT_WAITTING처럼 상태에 대해 명확하게 정의한 단어는 개발자가 소스 코드를 이해하는데 필요한 시간을 줄인다.

* 밸류 타입은 불변 객체로 사용한다. 

  * 값의 변화를 허용하면 잘못된 참조로 인한 오류가 발생할 수 있다. 

    ```java
    Money price = new Money(50000);  
    OrderLine line = new OrderLine(product, price, quantity);  
    price.setValue(30000);
    // line.getPrice().getValue()가 갖는 값은?
    ```

    

#### 도메인 주도 설계 기본 요소

* Entity

  * 실제 DB테이블과 매핑되어 있는 클래스로 DB테이블내에 존재하는 컬럼만을 속성(필드)로 갖음
  * 식별자를 갖음

  ```java
  @Getter
  @Entity
  @NoArgsConstructor
  public class Posts {
  
      @Id
      @GeneratedValue(strategy = GenerationType.IDENTIFY)
      private Long id;
  
      @Column
      private String title;
  
      @Column
      private String content;
  
      private String author;
  
      public Posts(String title, String content, String author) {
          this.title = title;
          this.content = content;
          this.author = author;
      }
  ```

* VO(Value Object) 

  * 불변성을 갖음. 따라서 DB에서 읽을 값을 VO에 담을 경우, 이 VO값이 DB데이터 원본으로서 신뢰할 수 있음 
  * Read Only
  * 값이 같다면 같은 객체로 판단 

  ```java
  @Getter
  public class PostsVO {
  
      private Long id;
      private String title;
      private String content;
      private String author;
  
      @Override
      public boolean equals(Object o) {
          if (this == o) return true;
          if (o == null || getClass() != o.getClass()) return false;
          PostsVO postsVO = (PostsVO) o;
          return Objects.equals(id, postsVO.id) && Objects.equals(title, postsVO.title) && Objects.equals(content, postsVO.content) && Objects.equals(author, postsVO.author);
      }
  
      @Override
      public int hashCode() {
          return Objects.hash(id, title, content, author);
      }
  }
  ```

* DTO(Data Transfer Object) 

  * DTO는 데이터 접근 메소드 외에 기능을 갖지 않음
  * getter/setter
  * 값을 유연하게 변경가능
  * temp

  ```java
  @Getter
  @NoArgsConstructor
  public class PostsSaveRequestDto {
      private String title;
      private String content;
      private String author;
  
      @Builder
      public PostsSaveRequestDto(String title, String content, String author) {
          this.title = title;
          this.content = content;
          this.author = author;
      }
      
      public Posts toEntity() {
          return Posts.builder()
                  .title(title)
                  .content(content)
                  .author(author)
                  .build();
      }
  }
  ```

  Client **<-DTO->** controller(web) **<-DTO->** service **<-DTO->** repository(DAO) **<-Entity->** DB
