### STOMP

----

#### STOMP란

STOMP는 TCP또는 WebSocket같은 양방향 네트워크 프로토콜 기반으로 동작한다. 

이름에서 알 수 있듯, STOMP는 Text지향 프로토콜이나, Message Payload에는 Text 혹은 Binary데이터가 포함될 수 있다. 

`pub/sub` 이란 메시지를 공급하는 주체와 소비하는 주체를 분리해 제공하는 메세징 방법이다. 기본적인 예를 들자면 우체통(topic) 이 있다면 집배원(Publisher)이 신문을 우체통에 배달하는 행위가 있고, 우체통에 신문이 배달되는 것을 기다렸다가 빼서 보는 구독자(Subscriber)의 행위가 있다.이때 구독자는 다수가 될 수 있다. `pub/sub`컨셉을 채팅방에 빗대면 다음과 같다

>채팅방 생성: pub/sub 구독을 위한 Topic이 생성됨 
>
>채팅방 입장:Topic구독
>
>채팅방에서 메세지를 송수신: 해당 Topic으로 메시지를 송신,수신

클라이언트는 메세지를 전송하기 위해 SEND,SUBSCRIBE COMMAND를 사용할 수 있다. 또한 SEND,SUBSCRIBE COMMAND 요청 Frame에는 메시지가 무엇이고, 누가 받아서 처리할지에 대한 Header정보가 포함되어 있다. 이런 명령어들은 "destination"헤더를 요구하는데 이것이 어디에 전송할지, 혹인 어디에서 메세지를 구독할 것인지를 나타낸다. 

위와 같은 과정을 통해 STOMP는 Publisher-Subscribe 매커니즘을 제공한다. 즉 Broker를 통해서 타 사용자들에게 메세지를 보내거나 서버가 특정 작업을 수행하도록 메세지를 보낼 수 있게 된다. 

만약 Spring에서 지원하는 STOMP를 사용하면 Spring Websocket 어플리케이션은 STOMP Broker로 동작하게 된다. 

STOMP는 HTTP에서 모델링되는 Frame기반 포로토콜이다. Frame은 몇 개의 Text Line으로 지정된 구조인데 첫번째 라인은 Text이고 Key:Value 형태로 Header의 정보를 포함한다. STOMP는 일반적으로 다음 형식을 따른다. 

~~~java
"topic.." --> publish-subscribe(1:N)
"queue/" --> point-to-point(1:1)
~~~

다음은 clientA가 5번 채팅방에 대해 구독을 하는 예시이다. 

~~~
SUBSCRIBE
destination: /topic/chat/room/5
id:sub-1
^@
~~~

다음은 clientB에서 채팅 메세지를 보내는 예시이다. 

~~~
SEND 
destination:/pub/chat
content-type:application/json

{"chatRoomId":5, "type":"MESSAGE","writer":"clientB"}^@
~~~

STOMP 서버는 모든 구독자에게 메세지를 Broadcasting하기 위해 MESSAGE COMMAND를 사용할 수 있다. 서버는 내용을 기반으로 메세지를 전송할 broker에 전달한다. (topic을 sub으로 보아도 된다. )

![img](https://blog.kakaocdn.net/dn/c28XZO/btq2cX8trC2/pCkz1QsD4C9g2G9wKUQKo0/img.jpg)

서버는 불분명한 메세지를 전송할 수 없다. 그러므로 서버의 모든 메세지는 특정 클라이언트 구독에 응답하여야 하고, 서버메세지의 "subscription-id"헤더는 클라이언트 구독의 "id"헤더와 일치해야 한다. 

#### Client Frames

##### SEND

SEND frame은 destination의 메세징 시스템으로 메세지를 보낸다. 필수 헤더는 어디로 보낼지에 대한 "destination"하나이다. SEND frame의 body는 보내고자 하는 메세지이다. 

~~~
SEND
destination:/queue/a
content-type:text/plain

hello queue a
^@
~~~

SEND frame은 body가 있는 경우 "content-length"와 "content-type"헤더를 반드시 가져야만 한다. 

##### SUBSCRIBE

SUBSCRIBE frame은 주어진 destination에 등록하기 위해 사용된다. SEND frame과 마찬가지로 SUBSCRIBE는 client가 구독하기 원하는 목적지를 가리키는 "destination" 헤더를 필요로 한다. 가입된 대상에서 수신된 모든 메세지는 이후 MESSAGE frame로서 서버에서 클라이언트에게 전달된다. 

~~~
SUBSCRIBE
id:0
destination:/queue/foo
ack:client

^@
~~~

단일 연결은 여러 개의 구독을 할 수 있으므로 구독 ID를 고유하게 식별하기 위해 "id"헤더가 프레임에 포함되어야 한다. 

이외에도 다양한 내용이 있지만, 추후에 필요성을 느끼면 정리하도록 하겠다.

##### Benefit of STOMP

Spring framework 및 spring security는 STOMP를 사용하여 WebSocket만 사용할 때보다 더 다채로운 모델링이 가능하다. 

- Messaging protocol을 만들고 메세지 형식을 커스터마이징 할 필요가 있다. 
- RabbitMQ,ActiceMQ 같은 Message Broker를 이용해, Subscription(구독)을 관리하고 메세지를 브로드캐스팅 할 수 있다. 
- WebSocket기반으로 각 connection마다 WebSocketHandler를 구현하는 것보다 @Controller된 객체를 이용해 조직적으로 관리할 수 있다. 즉 메세지는 STOMP의 "destination"헤더를 기반으로 @Controller객체의 @MethodMapping 메서드로 라우팅된다. 
- STOMP의 "destination" 및 Message Type 을 기반으로 메세지를 보호하기 위해 Spring security를 사용할 수 있다. 

##### Using STOMP

SockJS로 브라우저에 연결하기 위해 sockjs-client를 이용할 수 있다. STOMP에 있어 많은 어플리케이션들은 jmesnil/stomp-websocket( stomp.js 로 알려진 )라이브러리를 사용해왔지만, 더이상 유지되지 않는다. 최근에는 JSteunou/webstomp-client를 많이 사용한다.

##### Flow of Messages

STOMP Endpoints가 노출되고 나면 Spring 어플리케이션은 연결되어 있는 Client들에 대해 STOMP브로커가 된다. 

![img](https://blog.kakaocdn.net/dn/HOTPn/btq2c29QThJ/WcP1GMTYDPMDrlDutl1aZk/img.png)

**spring**-**message** 모듈은 Spring framework의 통합된 Messaging 어플리케이션을 위한 지원을 한다.

- **Message** : headers와 payload를 포함하는 메세지의 표현

- **MessageHandler** : Message 처리에 대한 계약

- **SimpleAnnotationMethod** : @MessageMapping 등 Client의 SEND를 받아서 처리한다.

- **SimpleBroker** : Client의 정보를 메모리 상에 들고 있으며, Client로 메세지를 보낸다.

- **channel**  

  - **clientInboundChannel**: WebSocket Client로부터 들어오는 요청을 전달하며, WebSocketMessageBrokerConfigurer를 통해 intercept, taskExecutor를 설정할 수 있다. 
    - 클라이언트로 받은 메세지를 전달 
  - **clientOutboundChannel**: WebSocket Client로 Server의 메세지를 내보내며, WebSocketMessageBrokerConfigurer를 통해 intercept, taskExecutor를 설정할 수 있다. 
    - 클라이언트에게 메세지를 전달 
  - **brokerChannel**: Server내부에서 사용하는 채널이며, 이를 통해 SimpleAnnotationMethod는 SimpleBroker의 존재를 직접 알지 못해도 메세지를 전달할 수 있다. 
    - 서버의 어플리케이션 코드 내에서 브로커에게 메세지 전달

  



