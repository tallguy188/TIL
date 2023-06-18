### Dictionary 최대값 가져오기

~~~python
di = {'a':0,'b':1,'c':2,'d':3}  # 딕셔너리 생성
di = dict(zip('abcd',range(4))) # zip함수를 사용해 dict생성, 위와 동일
~~~

최대 value에 대한 key찾기

~~~python
max(di,key=di.get)
[k for k,v in di.item() if max(di.values()) == v] # 리스트 컴프리핸션을 이용
~~~

딕셔너리를 생성하고, 안에 Key값중에 max를 가져오려면 다음과 같이 사용하면 된다. 