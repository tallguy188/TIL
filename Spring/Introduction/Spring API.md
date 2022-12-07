#### Spring API

앞으로 다루게 될 내용들에서는 정적컨텐츠는 중요하지 않고 SpringMVC와 API 방식이 중요하다. 

```java
 @GetMapping("hello-mvc")
    public String helloMvc(@RequestParam("name") String name, Model model) {
        model.addAttribute("name", name);
        return "hello-templates";
    }
```

위의 코드는 SpringMVC방식으로 웹 페이지를 렌더링 하는 코드이다. controller와 view 각각의 역할이 이루어졌을 때 웹페이지에 렌더링이 가능하다. 

```java
@GetMapping("hello-string")
    @ResponseBody
    public String helloString(@RequestParam("name") String name) {
        return "hello" + name;
    }
```

위의 코드는 API방식을 통해 웹페이지에 렌더링하는 것이다. 이 경우 따로 view같은 것이 없고 입력받은 데이터가 그대로 내보내진다는 것이다. 

위의 코드는 문자를 출력하는 코드이다. 하지만 만약에 데이터를 출력하고자 하면 어떻게 해야될까.

```java
@GetMapping("hello-api")
    @ResponseBody
    public Hello helloApi(@RequestParam("name") String name) {
        Hello hello = new Hello();
        hello.setName(name);
        return hello;
    }

    static class Hello {
        private String name;

        public String getName() {
            return name;
        }
        public void setName(String name) {
            this.name = name;
        }
    }
```

위 코드로 입력하고 localhost를 열어보면 {"name":"spring!!!!!!"} 이라고 넘겨준 spring!!!!!!이라는 데이터가 화면에 출력된다. 이것은 json이라는 방식이다. 간단하게 말하면 key,value로 이루어진 데이터구조이다. 따라서 name이 key이고 spring!!!!!!이 value인 것이다. 

기존에는 xml 방식도 많이 쓰였지만, 최근에는 대부분 json형식을 사용한다. Spring 역시 디폴트 반환값은 json이다. 

위에서 사용한 getter/setter 방식은 property 방식이라고 부른다. 



이제 @ResponseBody 의 사용원리를 알아보자. 

* HTTP의 BODY에 문자 내용을 직접 반환
* `viewResolver` 대신에 `HttpMessageConverter`가 동작
* 기본 문자처리: `StringHttpMessageConverter` 가 동작
* 기본 객체처리: `MappingJackson2HttpMessageConverter` 
* byte 처리 등등 기타 여러 HttpMessageConverter가 기본으로 등록되어 있음