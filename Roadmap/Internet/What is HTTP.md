## What is HTTP?

The Hypertext Transfer Protocol(HTTP)는 World Wide Web의 기초이며 하이퍼텍스트 링크를 사용하여 웹 페이지를 로드하는 데 사용된다. HTTP는 네트워크 장치 간에 정보를 전송하도록 설계된 응용 프로그램 계층 프로토콜이며 네트워크 프로토콜 스택의 다른 게층 위에서 실행된다. HTTP를 사용한 일반적 흐름은 클라이언트 시스템이 서버에 요청한 다음 응답 메시지를 보내는 것이 포함된다. 

### What's in an HTTP request? 

------

HTTP request(요청)은 웹 브라우저와 같은 인터넷 통신 플랫폼이 웹사이트를 로드하는데 필요한 정보를 요청하는 방식이다. 

인터넷을 통해 이루어진 각 HTTP요청에는 다양한 유형의 정보를 전달하는 일련의 인코딩된 데이터가 포함된다. 일반적인 HTTP 요청에는 다음이 포함된다.

* HTTP version type
* a URL
* an HTTP method
* HTTP request headers
* Optional HTTP body

### What's an HTTP method?

------

HTTP 메서드는 HTTP요청이 쿼리된 서버에서 예상하는 작업을 나타낸다. 예를 들어 가장 일반적인 두가지 HTTP 메서드는 'GET' 과 'POST'이다. 'GET' 요청은 일반적으로 웹 사이트의 형태로 정보가 반환될 것으로 예상하는 반면 'POST' 요청은 일반적으로 클라이언트가 웹 서버에 정보를 제출하고 있음을 나타낸다. 

### What's in an HTTP request headers?

------

HTTP 헤더에는 키-값 쌍에 저장된 텍스트 정보가 포함되어 있으며 모든 HTTP 요청이 포함된다. 이러한 헤더는 클라이언트가 어떤 브라우저를 사용하고 있으며 어떤 데이터가 요청되고 있는지와 같은 핵심 정보를 전달한다. 

### What's in an