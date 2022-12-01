### 스프링 웹 개발 기초

------

스프링으로 웹을 개발한다는 것은 크게 세가지 방법이 있다. 

* 정적 컨텐츠
* MVC와 템플릿 엔진
* API

정적 컨텐츠는 파일을 그대로 웹브라우저에 내보내는 것이다. 따라서 서버가 하는 일이 없다. 

두번째 MVC와 템플릿 엔진은 가장 많이하는 방식이다. 이 방법은 html을 서버에서 프로그래밍 한 다음 html을 동적으로 바꿔서 브라우저에 내보내는 것이다. 여기서 Spring MVC에 대해 조금 더 알아보자.



#### Spring MVC란 무엇인가?

Spring MVC는 Spring에서 제공하는 웹 모듈로, `Model` `View` `Controller` 세가지 구성요소를 사용해 사용자의 다양한 HTTP Request를 처리하고, 단순한 텍스트 형식의 응답부터 REST형식의 응답은 물론 View를 표시하는 html을 return하는 응답까지 다양한 응답을 할 수 있도록 만든 프레임워크이다. 

Spring MVC는 다양한 요청을 처리하고 응답하기 위해 주요 구성요소들을 만들어놓고 구성요소들을 확장할 수 있게 만들어 놓는데, 이들을 제대로 사용하기 위해서는 MVC가 어떻게 구성되어 있는지를 알아야 한다. 



#### Spring MVC의 구조

Spring MVC의 주요 구성요소는 `Model`, `View`, `Controller` 지만, 이들이 유기적으로 동작하도록 하기 위해 다양한 구성요소가 함께한다. 

* DispatcherServlet(Front Controller)
* Handler(Controller)
* ModelAndView
* ViewResolver

![화면 캡처 2022-12-01 092029](C:\Users\cksgh\OneDrive\바탕 화면\화면 캡처 2022-12-01 092029.png)

##### DispatcherServlet 

제일 앞단에서 HTTP Request를 처리하는 Controller

Spring MVC에서는 HTTP Request 가 왔을 때 DispatcherServlet이라 불리는 서블릿이 HTTP Request를 처리할 Controller을 지정한다. DispatcherServlet은 일종의 HTTP Request를 처리할 Controller을 지정하는 Controller로 Super Controller 역할을 한다. 

##### Controller(Handler)

HTTP Request를 처리해 Model을 만들고 View를 지정

DispatcherServlet에 의해 배정된 Controller는 HTTP  Request를 처리하고, HTTP Request의 메세지를 처리해 필요한 데이터를 뽑아 Model에 저장한다. 또한 HTTP Request에 따라서 HTTP가 보여줄 View Name을 지정한다. 이곳에서  View Name뿐만 아니라, 직접 View를 반환할 수도 있다. 하지만 이곳에서 View에 Model의 데이터를 세팅하지는 않는다. 

위 그림에서는 편의상 View Name을 반환하는 Model And View를 만들었다. 

##### ModelAndView 

Controller에 의해 반환된 Model과 View가 Wrapping된 객체 

Model : Map<String,Value>형태의 데이터 저장소

Model은 Map자료 구조로, HTTP Request속의 데이터를 파싱해 Key-Value쌍으로 만들어 저장한다. 이 Model은 이후에 View를 그리기 위해 사용된다. 

```java
public ModelAndView(String viewName, @NUllable Map<String,?> model) {
    this.view = viewName;
    if(model != null) {
        getModelMap().addAllAttributes(model)
    }
}
```

view, view Name : ViewResolver에서 그릴 View를 지정

ModelAndView 내부에서 View 혹은 View Name이 있는데, View가 지정되더라도 데이터가 세팅된 Vidw가 지정되지 않는다. 

##### ViewResolver

ModelAndView를 처리하여 View를 그리기

ViewResolver에서는 ModelAndView객체를 처리해 View를 그린다. 여기서는 모델에 저장된 데이터를 사용해 View를 그려준다. View는 사용자에게 보여줄 완성된 View이며, 여기서 그려지는 View는 그대로 유저에게 반환된다. 우리가 특정한 url로 들어갔을 때 우리에게 보여지는 View가 바로 이곳에서 만들어지는 View이다. 



#### Spring MVC의 의의

특히 Spring MVC는 HTTP Request를 처리하는 부분인 Controller, 데이터를 처리해 정제된 데이터를 넣는 Model, 정제된 데이터를 활용해 사용자에게 보여지는 View에 대한 역할 분리를 잘 해놓았다. Spring MVC를 사용하면 Model, View,Controller 모두를 인터페이스를 사용해 규격화해놓아 유연하고 확장성 있게 웹 어플리케이션을 설계할 수 있다. 