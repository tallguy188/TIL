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

### What's in an HTTP request body?

------

request body 는 요청이 전송하는 정보의 "본문"을 포함하는 부분이다. HTTP 요청의 body에는 사용자 이름 및 암호 또는 양식에 입력된 기타 데이터와 같이 웹 서버에 제출되는 모든 정보가 포함된다. 

### What's in an HTTP response?

------

HTTP response는 웹 클라이언트가 HTTP 요청에 대한 응답으로 인터넷 서버에서 받는 것이다. 이러한 응담은 HTTP request 에서 요청된 내용을 기반으로 중요한 정보를 전달한다. 

일반적인 HTTP response에는 다음이 포함된다.

* an HTTP status code
* HTTP response headers
* optional HTTP body

### What's an HTTP status code?

------

HTTP status code 는 HTTP 요청이 성공적으로 완료 되었는지 여부를 나타내는 데 가장 자주 사용되는 3자리 코드이다. 상태 코드는 다음 5개 블록으로 나뉜다. 

* 1xx Informational
* 2xx Success
* 3xx Redirection 
* 4xx Client Error
* 5xx Server Error

"xx"는 00에서 99 사이의 다른 숫자를 나타낸다. 

숫자 '2'로 시작하는 status code는 성공을 나타낸다. 예를 들어, 클라이언트가 웹 페이지를 요청한 후 가장 일반적으로 표시되는 응답은 요청이 제대로 완료되었음을 나타내는 '200 OK' 상태 코드를 갖는다. 

응답이 '4' 또는 '5' 로 시작하면 오류가 있고 웹 페이지가 표시되지 않음을 의미한다. '4'로 시작하는 상태 코드는 클라이언트 측 오류를 나타낸다. (URL에 오타를 만들 때 '404 NOT FOUND' 상태 코드가 발생하는 것은 매우 일반적입니다.) '5'로 시작하는 상태 코드는 서버 측에서 문제가 발생했음을 의미한다. 상태 코드는 각각 정보 응답 및 리디렉션을 나타내는 '1' 또는 '3'으로 시작할 수도 있다. 

### What are HTTP response headers?

------

HTTP request와 마찬가지로 HTTP response는 응답 본문에서 전송되는 데이터의 언어 및 형식과 같은 중요한 정보를 전달하는 헤더와 함께 제공된다. 

### What's in an HTTP response body?

------

'GET' 요청에 대한 성공적인 HTTP 응답에는 일반적으로 요청된 정보가 포함된 본문이 있다. 대부분의 웹 요청에서 이것은 웹 브라우저가 웹 페이지로 번역할 HTML 데이터다. 

### Can DDoS attacks be launched over HTTP?

------

HTTP는 "stateless"한 프로토콜이며, 이는 각 명령이 다른 명령과 독립적으로 실행됨을 의미한다. 원래 사양에서 HTTP 요청은 각각 TCP연결을 만들고 닫는다. 최신 버전의 HTTP 프로토콜에서 영구 연결을 사용하면 여러 HTTP 요청이 영구 TCP 연결을 통해 전달할 수 있으므로 리소스 소비가 향상된다. `Dos` 또는 `DDoS` 공격의 맥락에서 대량의 HTTP 요청은 대상 장치에 대한 공격을 시작하는데 사용될 수 있으며, 애플리케이션 계층 공격 또는 계층 7 공격의 일부로 여겨진다. 
