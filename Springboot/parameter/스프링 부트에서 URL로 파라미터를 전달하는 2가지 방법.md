### 스프링 부트에서 URL로 파라미터를 전달하는 2가지 방법

------

```java
Get http://tallguy188.github.io/member?id=2 //type 1
Get http://tallguy188.github.io/member/2      //type2
```

스프링부트에서 URL로 파라미터를 전달하는 방식에는 두가지가 있다. type1이 쿼리스트링을 적용한 방식이고, type2가 REST하게 이용하는 방법이다.



#### 쿼리스트링

쿼리스트링으로 파라미터를 URL로 전송할 때엔 컨트롤러에서 파라미터를 받을 때 `@RequestParam`을 사용한다. 

```java
@RestController
public class MemberController {
   @Autowired
   MemberService memberService;
  
   @GetMapping("/member")
   public List<MemberVO> getMemberById(@RequestParam Long id){
      return memberService.selectMemberById(id);
   }
}
```

`RequestParam` 어노테이션을 컨트롤러 파라미터에 작성하면 쿼리스트링으로 들어오는 영역에서 `id`값을 매핑해서 가져올 수 있따.



#### REST

RESTful하게 파라미터를 받기 위해서 컨트롤러에서 `@PathVariable` 어노테이션을 사용한다.

```java
@RestController
public class MemberController {
   @Autowired
   MemberService memberService;
  
   @GetMapping("/member/{id}")
   public List<MemberVO> getMemberById(@PathVariable("id") Long id){
      return memberService.selectMemberById(id);
   }
}
```

이외에 `@GetMapping()` 어노테이션에 `@PathVariable` 어노테이션으로 가져올 파라미터를 `{}` 형태로 작성해줘야 파라미터로 매핑이 이뤄진다.

쿼리스트링은 URL에 입력하는 파라미터 순서가 중요하지 않으나 REST 방식으로 URL에 파라미터를 담아서 전송할 경우, 파라미터의 위치가 중요해진다. 이 떄문에 `@RequestMapping` 또는 `@GetMapping` 어노테이션에서 파라미터명을 매핑해줘야한다.