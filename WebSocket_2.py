# 웹소켓을 사용하여 실시간으로 데이터를 받으면서 이를 동시에 처리하려면 프로세스와 스레드에 대해서 알아야 합니다. 이번 절에서는 프로세스와 스레드에 대해 간단히 공부해봅시다.

# 프로세스와 스레드
# 여러분이 사용하는 PC에는 윈도우, macOS, 리눅스와 같은 운영체제가 설치되어 있습니다. 하나의 프로그램은 메모리에 로드된 다음 운영체제에 의해 실행될 수 있습니다. 이때, 실행 중인 프로그램을 프로세스(process)라고 부릅니다. 그림 9-4는 Ctrl + Shift + ESC를 누르면 실행되는 윈도우 작업 관리자입니다. 좌측에는 현재 PC에 실행되고 있는 프로그램 (앱)이 표시되는데 하나하나를 프로세스라고 부르는 겁니다.



# 그림 9-4 작업관리자에서의 프로세스

# 프로세스의 실행 단위를 스레드라고 합니다. 프로세스는 최소 하나의 스레드로 구성되는 데 이를 단일 스레드라고 합니다. 프로세스가 경우에 따라 여러 스레드를 가질 수 있는데 이를 다중 스레드라고 부릅니다. 그림 9-5는 프로세스가 단일 스레드와 다중 스레드로 구성된 경우를 나타냅니다. 프로세스는 실행될 때 운영체제로부터 독립된 자원을 할당받습니다. 따라서 한 프로세스가 다른 프로세스의 데이터에 직접 접근할 수 없습니다. 프로세스가 다른 프로세스에 있는 자원에 접근하려면 프로세스 간 통신을 사용해야 합니다. 이와 달리 한 프로세스 내에 있는 스레드는 스레드 간에 프로세스의 자원을 공유합니다.



# 그림 9-5 프로세스와 스레드의 관계

# 스레드 스케줄링
# 앞서 프로세스의 실행 단위를 스레드라고 부른다고 했습니다. 그리고 프로세스는 최소 하나 이상의 스레드를 가지며 때에 따라 여러 스레드를 가질 수 있음을 배웠습니다.

# 여러분이 윈도우를 사용할 때를 생각해봅시다. 메신저도 사용하고 게임도 하고 문서 작성도 하고 인터넷도 사용할 겁니다. 예전에는 CPU가 한 개였는데 어떻게 동시에 여러 프로그램을 실행할 수 있을까요? 그 비밀은 운영체제의 스케줄링에 있습니다. 운영체제는 여러 프로그램을 아주 짧은 시간마다 실행 시켜 줌으로써 마치 동시에 실행되는 것처럼 보이게 합니다. 운영체제의 스케줄링 기법은 다양한데 스케줄링의 기본 단위로 앞서 설명한 스레드를 사용합니다. 여러분이 개발한 프로그램이 여러 개의 스레드를 사용하는 경우 운영체제에 의해서 스케줄링 되는 스레드의 수가 다른 프로세스보다 많기 때문에 더 빨리 수행될 수 있습니다.



# 그림 9-6 스레드와 스케줄링

# multiprocessing 모듈
# 파이썬 코드를 작성한 후 이를 실행시키면 파이썬 인터프리터가 코드를 해석한 후 실행해줍니다. 프로세스 관점에서 이야기해보면 이를 메인 프로세스(Main Process)라고 부를 수 있습니다. multiprocessing 모듈의 current_process 함수를 호출하면 현재 실행되는 프로세스에 대한 정보를 담고 있는 객체를 얻을 수 있습니다. 해당 객체의 name과 pid 속성에 접근하면 프로세스의 이름과 PID(Process ID)를 얻을 수 있습니다. 여기서 PID란 운영체제가 각 프로세스에 부여한 고유 번호로써 프로세스의 우선순위를 조정하거나 종료하는 등 다양한 용도로 사용되는 값입니다.

# #ch09/09_06.py
# 1: import multiprocessing as mp 
# 2: 
# 3: 
# 4: if __name__ == "__main__":
# 5:     proc = mp.current_process()
# 6:     print(proc.name)
# 7:     print(proc.pid)
# 라인 5: 프로세스에 대한 정보를 담고 있는 객체를 얻습니다.

# 라인 6: 객체의 name 속성(변수)를 출력합니다.

# 라인 7: 객체의 pid 속성(변수)를 출력합니다.

# 부모 프로세스(Parent Proecess)가 운영체제에 요청하여 자식 프로세스(Child Process)를 새로 만들어낼 수 있는데 이를 프로세스 스포닝(spawning)이라고 부릅니다. 파이썬의 multiprocessing 모듈을 이용하면 이러한 프로세스스포닝을 수행할 수 있습니다. 보통 부모 프로세스가 처리할 작업이 많은 경우 프로세스스포닝을 통해 자식 프로세스를 새로 만들고, 일부 작업을 자식 프로세스에 위임하여 처리할 수 있습니다. 물론 앞서 배운 스레드를 사용할 수도 있지만 파이썬은 전역 인터프리터 록 문제가 있어서 스레드보다는 프로세스를 사용하는 것이 더 성능이 좋습니다.

# multiprocessing 모듈을 이용한 프로세스스포닝은 Process 클래스의 인스턴스를 생성한 후 start( ) 메소드를 호출하면 됩니다. Process 클래스의 인스턴스를 생성할 때 생성될 자식 프로세스의 이름과 위험하고 자 하는 일(함수)을 전달합니다. 다음 코드는 ‘MainProcess’라는 이름의 부모 프로세스가 ‘SubProcess’라는 이름의 자식 프로세스를 스포닝합니다.

# #ch09/09_07.py
# 01: import multiprocessing as mp
# 02: import time
# 03: 
# 04: def worker():
# 05:     proc = mp.current_process()
# 06:     print(proc.name)
# 07:     print(proc.pid)
# 08:     time.sleep(5)
# 09:     print("SubProcess End")
# 10: 
# 11: 
# 12: if __name__ == "__main__":
# 13:     # main process
# 14:     proc = mp.current_process()
# 15:     print(proc.name)
# 16:     print(proc.pid)
# 17: 
# 18:     # process spawning
# 19:     p = mp.Process(name="SubProcess", target=worker)
# 20:     p.start()
# 21: 
# 22:     print("MainProcess End")
# 라인 14:~16: 메인 프로세스가 실행되면서 프로세스의 name, pid 속성을 출력합니다.

# 라인 19: 자식 프로세스가 스포닝되고 자식은 worker 함수를 수행합니다.

# 라인 22: 메인 프로세스가 실행하는 코드 영역입니다.

# 화면에 출력되는 값을 살펴봅시다. 서브 프로세스는 5초 동안 대기하기 때문에 ‘SubProcess End’가 가장 마지막에 출력되는 것을 확인할 수 있습니다.

# MainProcess
# 65560
# MainProcess End
# SubProcess
# 65562
# SubProcess End
# Process 클래스의 객체를 생성한 후 start 메소드를 호출하는 순간 그림 9-7과 같이 자식 프로세스가 스포닝되고 target으로 지정된 함수를 처리한다고 이해하면 되겠습니다.



# 그림 9-7 단일 프로세스와 프로세스 스포닝