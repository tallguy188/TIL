### MySQL



mariadb를 쓰다보니 모르는게 생겨서 올리는 글



#### Primary key(pk)

------

테이블에서 특정 row 하나를 식별하는 역할, 특정 row를 고유하게 나타낼 수 있는 값



#### Natural key

------

실제로 어떤 개체가 갖고 있는 속성을 나타내는 컬럼이 Primary key가 됐을 때 이를 Natural key라고 한다. 예를 들어 사람은 이름, 책은 ISBN이라는 번호로 특정할 수 있다. 바로 이런 속성을 지닌 컬럼이 Primary key가 되면 Natural key라고 한다.



#### Surrogate key

------

어떤 개체의 실제 속성은 아니지만 Primary key로 쓰기 위해 추가한 컬럼을 Surrogate key라고 한다. 이런 Surrogate key에는 주로 1부터 순차적으로 증가하는 숫자가 들어가게 된다.



#### Not Null(NN)

------

NULL이 아니다. pk와 함께 반드시 하나의 값을 가지고 있어야 하고 빈 값을 가지면 안될 때 사용한다.



#### Auto Increment(AI)

------

Auto Increment 속성을 컬럼에 설정하면, 해당 컬럼에 관해서는 DBMS가 '자동으로 증가'하는 값을 넣어준다.

Primary key가 Surrogate key인 경우에는 보통 이런 식으로 Auto Increment속성이 설정되어 있을 때가 많다.



