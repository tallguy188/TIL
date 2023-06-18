### Web socket

---



기본적인 웹소켓 동작은 혼자서 살펴보았고 정확하게 SockJS가 무엇인지, STOMP방식은 어떤것인지 알기 위해서 이 글을 작성했다. 

기존 순수 웹 소켓은 

* 모든 클라이언트의 브라우저에서 WebSocket을 지원한다는 보장이 없다. 
* 또한 Server/Client 중간에 위치한 Proxy가 upgrade헤더를 해석하지 못해 서버에 전달하지 못할 수 있다. 
* 마지막으로 Server/Client 중간에 위치한 Proxy가 유휴 상태에서 도중에 connection을 종료시킬 수 있다. 

이러한 문제점들을 해결하기 위해서 `Websocket Emulation` 을 이용한다. 

이것은 우선 WebSocket을 시도하고, 실패할 경우 `HTTP Streaming`, `Long-Polling` 같은 다른 HTTP 기반의 기술로 전환해 다시 연결을 시도하는 것을 말한다. 

node.js를 사용한다면 Socket.io을 이용하는 것이 일반적이고,  Spring을 이용한다면 SockJS를 이용하는 것이 일반적이다. 

Spring프레임워크에서는 Servlet스택 위에서 Server/Client 용도의 SockJS 프로토콜을 모두 지원한다. 

### SockJS

SockJS는 어플리케이션이 WebSocket API를 사용하도록 허용하지만 브라우저에서 WebSocket을 지원하지 않는 경우에 대안으로 어플리케이션의 코드를 변경할 필요 없이 런타임에 필요할 때 대체하는 것이다. 

SockJS는 다양한 기술을 이용해 웹소켓을 지원하지 않는 브라우저에서 정상적으로 동작하도록 한다. 전송 타입은 크게 세가지로 분류된다. 

* WebSocket
* HTTP Streaming
* HTTP Long Polling



