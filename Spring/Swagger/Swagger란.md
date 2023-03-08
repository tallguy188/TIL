#### Swagger



협업 프로젝트를 진행하기 전에 필요한 요소들을 검색해보던 중 swagger 사용의 필요성을 느껴서 정리해본다. 



##### Swagger란

팀 프로젝트 중 팀원과의 API 정보 공유를 위해 많이 사용하는 것이다. 

Swagger란 `OAS(Open Api Specification)` 를 위한 오픈소스 프레임워크다. 즉 API의 문서를 자동으로 정리해주는 것이다. 

해당 Swagger를 협업하는 개발자에게 전달하면 Path, Request, Response, 제약조건 등을 한번에 알 수 있다. APi 문서 자동화 뿐만 아니라 Swagger를 통해 파라미터를 넣어보고 테스트를 진행할 수 있다는 점 또한 매력적이다. 

프론트 개발자는 API에서 요구하는 Request를 작성하고, Swagger에서 직접 테스트 후 코드에 반영한다. API문서를 작성하는 시간을 절약하고, API정보를 실시간으로 유지할 수 있다는 장점이 존재한다. Swagger가 제공하는 툴을 살펴보면

* Swagger Codegen

Codegen은 server stubs client SDKs를 생성할 수 있게 해준다 .즉 Swagger에서 정의한 설계대로 개발을 진행할 수 있도록 한다. 

* Swagger Editor

Swagger Editor는 Swagger를 온라인에서도 작성할 수 있는 것이 특징이다 .Cloud환경에서 작업할 수도 있고, Editor를 다운받아 사용이 가능하다. Docker를 통해 이미지를 제공한다.

* Swagger UI

Swagger의 표준에 맞춰 UI를 작성해주는 에디터이다. 



##### Springfox와 Springdoc

이러한 Swagger를 Spring에서 쉽게 사용할수 있도록 도와주는 라이브러리가 위의 두개이다. 

대부분의 많은 사람들이 springfox를 사용하지만, springdoc이 조금 더 최근에 만들어지기도 하고 업데이트도 자주 된다. 



Swagger의 적용 방법에 대해서는 앞으로 작성할 블로그의 프로젝트 부분에서 다루는게 조금 더 좋을 것 같다. 

