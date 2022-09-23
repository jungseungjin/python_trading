# 이 책에서는 websockets (https://github.com/aaugustin/websockets)이라는 파이썬 모듈을 사용하겠습니다. 
# 그런데 이 모듈은 파이썬의 비동기(asynchronous) 처리를 위한 asyncio라는 표준 모듈을 기반으로 개발되었습니다. 
# 그래서 websockets 모듈을 사용하려면 먼저 asyncio 모듈부터 공부해야 합니다.

# 파이썬에서 함수의 정의는 def라는 키워드를 사용했습니다. 
# 다음 코드와 같이 sync_func1, sync_func2 함수를 정의한 후 이를 순차적으로 호출하면 sync_func1의 호출이 끝난 후 sync_func2가 호출됩니다. 
# 이러한 전통적인 함수 호출 방식을 동기(synchronous) 호출 방식이라고 합니다.

# 이번에는 비동기(asynchronous) 방식의 일 처리에 대해서 생각해봅시다. 
# 아메리카노를 만들려면 먼저 커피콩을 그라인더로 분쇄해야 합니다. 
# 그런데 커피콩을 분쇄하는 데 약 1분이 걸린다고 해봅시다. 
# 점원은 분쇄기의 버튼을 눌러 놓고 그사이에 카페 라테의 주문을 받고 카페 라테를 만들기 시작합니다. 
# 커피콩의 분쇄가 끝나면 다시 아메리카노를 만들고 여러분에게 전달합니다. 
# 그다음 이어서 카페 라테를 제조하고 여러분의 친구에게 전달합니다. 
# 이처럼 비동기 방식에서는 커피콩이 분쇄될 때까지 아무 일도 안 하고 있는 것이 아니라, 그 시간에 다른 주문을 받고 다른 커피를 제조합니다. 
# 이러한 비동기 일 처리 방식에서는 고객의 대기 시간이 줄어든다는 장점이 있습니다.

# 코루틴 함수는 정의하는 방법도 다르지만, 호출 역시 일반 함수와 다른 방식으로 호출해야 합니다. 다음과 같이 코루틴을 일반 함수처럼 호출하면 “async_func1 was never awaited” 에러가 발생합니다.

# #ch09/09_02.py
# 1: import asyncio 
# 2: 
# 3: async def async_func1():
# 4:     print("Hello")
# 5: 
# 6: async_func1()
# 7: #asyncio.run(async_func1())
# 라인 3~4: async_func1이라는 코루틴을 정의합니다.

# 라인 6: 코루틴을 호출합니다.

# 여러 코루틴를 잘 처리하기 위해서는 스케줄러가 필요한데 이를 이벤트 루프라고 부릅니다. 코루틴을 처리하기 전에 먼저 이벤트 루프를 만들고 코루틴의 처리가 끝난 후에는 이벤트 루프를 닫아주면 됩니다. 이러한 역할을 간단히 처리해주는 것이 asyncio모듈의 run 함수입니다.

# 이번에는 코루틴을 asyncio의 run 함수를 통해서 실행(호출)해 봅시다. 위 코드에서 6번 라인을 주석으로 처리하고 7번 라인의 주석을 해제한 후 코드를 다시 실행하면 됩니다. 이제 정상적으로 코루틴이 호출됨을 확인할 수 있습니다. 코루틴의 실행에는 항상 이벤트 루프가 필요하다는 점을 기억하시기 바랍니다.

# asyncio를 사용하는 경우 보통 asyncio.run과 같은 고수준의 함수를 사용하여 코루틴을 실행합니다. 하지만 때에 따라 이벤트 루프 동작 등을 세부적으로 제어할 필요가 있을 수 있습니다. 이럴 때는 다음과 같이 프로그래머가 직접 이벤트 루프를 얻고 이벤트 루프를 통해 코루틴을 처리한 후 이벤트 루프를 닫을 수 있습니다.

# #ch09/09_03.py
# 1: import asyncio 
# 2: 
# 3: async def async_func1():
# 4:     print("Hello")
# 5: 
# 6: loop = asyncio.get_event_loop()
# 7: loop.run_until_complete(async_func1())
# 8: loop.close()
# 라인 6: 이벤트 루프를 가져옵니다.

# 라인 7: 코루틴 객체가 완료될 때까지 실행합니다.

# 라인 8: 이벤트 루프를 닫습니다.

# 이번에는 앞서 예로 설명했던 커피 예시를 asyncio를 사용해서 구현해봅시다. 아메리카노를 만드는 코루틴과 커피 라테를 만드는 코루틴을 각각 정의합니다. 그런 다음 코드를 실행해보면 스레드를 사용하지 않았음에도 아메리카노를 만드는 코루틴과 커피 라테를 만드는 코루틴이 동시에 수행되는 것을 볼 수 있습니다.

# #ch09/09_04.py
# 01: import asyncio 
# 02: 
# 03: async def make_americano():
# 04:     print("Americano Start")
# 05:     await asyncio.sleep(3)
# 06:     print("Americano End")
# 07: 
# 08: async def make_latte():
# 09:     print("Latte Start")
# 10:     await asyncio.sleep(5)
# 11:     print("Latte End")
# 12: 
# 13: async def main():
# 14:     coro1 = make_americano()
# 15:     coro2 = make_latte()
# 16:     await asyncio.gather(
# 17:         coro1, 
# 18:         coro2
# 19:     )
# 20: 
# 21: print("Main Start")
# 22: asyncio.run(main())
# 23: print("Main End")
# 라인 5: 3초를 기다리기 위하여 asyncio.sleep 함수를 호출합니다. asyncio.sleep 함수는 time.sleep과 비슷하게 정해진 시간(secs) 동안 대기합니다. time.sleep 함수가 CPU를 점유하면서 기다리는 것과 달리 asyncio.sleep 함수는 CPU가 다른 코루틴을 처리할 수 있도록 CPU 점유를 해제한 상태로 기다립니다. 즉, 어떤 코루틴이 asyncio.sleep 함수를 실행하는 순간 이벤트 루프는 다른 코루틴을 실행시킵니다. asyncio.sleep 함수 역시 코루틴인데 코루틴 내에서 다른 코루틴을 호출할 때 await 구문을 사용합니다.

# 라인 10: asyncio.sleep를 통해 5초 동안 대기합니다.

# 라인 14: 아메리카노를 만드는 코루틴 객체를 생성합니다.

# 라인 15: 커피 라테를 만드는 코루틴 객체를 생성합니다.

# 라인 16: 아메리카노를 만드는 코루틴과 커피 라테를 만드는 코루틴을 동시에 실행합니다.

# 라인 22: 이벤트 루프를 생성하여 main 코루틴을 처리하고 이벤트 루프를 닫습니다.

# 실행 결과는 살펴보면 ‘Americano Start’와 ‘Latte Start’가 거의 동시에 화면에 출력됨을 확인할 수 있습니다. 이는 아메리카노를 만드는 코루틴이 sleep 함수를 호출한 순간 이벤트 루프가 커피 라테를 만드는 코루틴을 실행시키기 때문입니다.

# Main Start
# Americano Start
# Latte Start
# Americano End
# Latte End
# Main End
# 이번에는 코루틴에서 값을 리턴하도록 변경해봅시다. 코루틴 역시 함수처럼 리턴 값을 return 키워드와 함께 적어주면 됩니다. asyncio.gather를 통해 여러 코루틴을 동시에 실행하는 경우 모든 코루틴이 실행이 종료될 때 각 코루틴의 리턴값이 파이썬 리스트에 담겨서 전달됩니다.

# File: ch09/09_05.py
# 01: import asyncio 
# 02: 
# 03: async def make_americano():
# 04:     print("Americano Start")
# 05:     await asyncio.sleep(3)
# 06:     print("Americano End")
# 07:     return "Americano"
# 08: 
# 09: async def make_latte():
# 10:     print("Latte Start")
# 11:     await asyncio.sleep(5)
# 12:     print("Latte End")
# 13:     return "Latte"
# 14: 
# 15: async def main():
# 16:     coro1 = make_americano()
# 17:     coro2 = make_latte()
# 18:     result = await asyncio.gather(
# 19:         coro1, 
# 20:         coro2
# 21:     )
# 22:     print(result)
# 23: 
# 24: print("Main Start")
# 25: asyncio.run(main())
# 26: print("Main End")

# 라인 7: “Americano”라는 문자열을 리턴합니다.

# 라인 13: “Latte”라는 문자열을 리턴합니다.

# 라인 18~21: asyncio.gather 함수가 리턴하는 값을 result 변수로 바인딩합니다.