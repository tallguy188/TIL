## How browsers work



### The browsers we will talk about

------

오늘날 데스크톱에서 사용되는 5가지 주요 브라우저는 Chrome, Internet Explorer, Firefox, Safari, Opera 이다. 모바일에서 주요 브라우저는 Android 브라우저, iphone, Opera Mini 및 UC브라우저, Nokia s40/s60 브라우저 및 Chromeall이며, Opera 브라우저를 제외하고 Webkit 기반이다. 

통계에 따르면 2013년 기준 Chrome, Firefox 및 Safari는 전 세계 데스크톱 브라우저 사용량의 71%를 차지한다. 모바일에서는 Android 브라우저, iPhone 및 Chrome은 사용량의 약 54%를 차지한다. 

### The browser's main functionality

------

브라우저의 주요 기능은 서버에서 요청하고 브라우저 창에 표시하여 선택한 웹 리소스를 제공하는 것이다. 리소스는 일반적으로 HTML 문서이지만, PDF, 이미지, 다른 유형의 콘텐츠일 수도 있다. 리소스의 위치는 `url(uniform resource identifier)` 를 사용하여 사용자가 지정한다. 

브라우저가 HTML 파일을 해석하고 표시하는 방식은 HTML 및 CSS 사양에 지정되어 있다. 이러한 사양은 웹 표준 조직인 `W3C` 에서 유지 관리한다. 수년 동안 브라우저는 사양의 일부만을 준수하고 자체 확장을 개발했다. 이는 웹 작성자에게 심각한 호환성 문제를 일으켰다. 오늘날 대부분의 브라우저는 사양을 어느 정도 준수한다. 

브라우저 사용자 인터페이스는 서로 공통점이 많다. 일반적인 사용자 인터페이스 요소는 다음과 같다. 

* URL 삽입을 위한 주소 표시줄
* 뒤로 및 앞으로 버튼
* 북마크 옵션
* 현재 문서의 로드를 새로 고치거나 중지하기 위한 새로고침 및 중지 버튼
* 홈 페이지로 이동하는 홈 버튼

이상하게도 브라우저의 사용자 인터페이스는 공식 사양에 지정되어있지 않으며, 수년간의 경험과 브라우저가 서로를 모방하여 형성한 모범 사례에서 비롯된 것이다. 

HTML5 사양은 브라우저에 있어야 하는 UI 요소를 정의하지 않지만 몇 가지 공통 요소를 나열한다. 그 중에는 주소 표시줄, 상태 표시줄 및 도구 모음이 있다. 물론 Firefox의 다운로드 관리자와 같은 특정 브라우저에 고유한 기능도 있다. 

### The browser's high level structure

------

* The user interface: 여기에는 주소 표시줄, 뒤로/앞으로 가기 버튼, 북마크 메뉴등이 포함된다. 요청한 페이지가 표시되는 창을 제외한 브라우저의 모든 부분이 표시된다.
* The browser engine: UI와 렌더링 엔진 간의 작업을 마샬링한다. 
* The rendering engine: 요청된 콘텐츠 표시를 담당한다. 예를 들어 요청된 콘텐츠가 HTML인 경우 렌더링 엔진은 HTML 및 CSS 구문 분석하고 구문 분석된 콘텐츠를 화면에 표시한다. 
* Networking: HTTP 요청과 같은 네트워크 호출의 경우 플랫폼 독립적인 인터페이스 뒤에서 다른 플랫폼에 대해 다른 구현을 사용한다.
* UI backend: 콤보 상자 및 창과 같은 기본 위젯을 그리는데 사용된다. 이 백엔드는 플랫폼에 특정하지 않은 일반 인터페이스를 노출한다. 그 아래에서 운영 체제 사용자 인터페이스 방법을 사용한다.
* JavaScript interpreter: JavaScript 코드를 구문 분석하고 실행하는 데 사용된다. 
* Data storage: 브라우저는 쿠키와 같은 모든 종류의 데이터를 로컬에 저장해야 할 수 있다. 브라우저는 또한 localStorage, indexedDB, WebSQL 및 FileSystem 과 같은 저장소 매커니즘을 지원한다.

Chrome과 같은 브라우저는 각 탭에 하나씩 랜더링 엔진의 여러 인스턴스를 실행한다는 점을 유의해야 한다. 

### Rendering Engine

------

렌더링 엔진은 브라우저 화면에 요청된 내용을 표시하는 것이다. 

기본적으로 렌더링 엔진은 HTML  및 XML 문서와 이미지를 표시할 수 있다. 플러그인이나 확장을 통해 다른 유형의 데이터를 표시할 수 있다. 예를 들어 PDF 뷰어 플러그인을 사용하여 PDF 문서를 표시한다. 

브라우저마다 다른 렌더링 엔진을 사용한다. 이 중 Webkit은 Linux 플랫폼용 엔진으로 시작하여 Apple 및 Mac 및 Windows를 지원하도록 수정한 오픈 소스 랜더링 엔진이다. 

### The Main Flow

------

렌더링 엔진은 네트워크 계층에서 요청된 문서의 내용을 가져오기 시작한다. 이것은 8kB의 청크로 수행된다. 

그 다음 렌더링 엔진의 기본 흐름이다. 

![렌더링 엔진 기본 흐름](https://web-dev.imgix.net/image/T4FyVKpzu4WKF1kBNvXepbi08t52/bPlYx9xODQH4X1KuUNpc.png?auto=format)

렌더링 엔진은 HTML 문서의 구문 분석을 시작하고 "컨텐츠 트리"라는 요소를 DOM 노드로 변환한다. 엔진은 외부 CSS파일과 스타일 요소 모두에서 스타일 데이터를 구문 분석한다. HTML의 시각적 지침과 함께 스타일 정보를 사용하여 다른 트리인 렌더 트리를 생성한다. 

렌더 트리에는 색상 및 치수와 같은 시각적 속성이 있는 사각형이 포함되어 있다. 사각형은 화면에 표시되는 순서이다. 

렌더 트리를 구성한 후 " 레이아웃" 프로세스를 거친다. 이것은 각 노드에 화면에 나타나야 하는 정확한 좌표를 제공하는 것을 의미한다. 다음 단계는 페인팅이다. 렌더 트리가 탐색되고 각 노드는 UI 백엔드 레이어를 사용하여 페인팅된다. 

이것이 점진적인 과정이라는 것을 이해하는 것이 중요하다. 더 나은 사용자 경험을 위해 렌더링 엔진은 가능한 빨리 화면에 콘텐츠를 표시하려고 한다. 렌더 트리를 빌드하고 레이아웃을 시작하기 전에 모든 HTML 구문이 분석될 때까지 기다리지 않는다. 콘텐츠의 일부가 구문분석되고 표시되는 동안 프로세스는 네트워크에서 계속 들어오는 나머지 콘텐츠를 처리한다. 