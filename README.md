## Meeting Log
#### 미팅 2019-03-28-Thu (엄두섭 교수님, 인용)
```
Navigation - 1. IMU로 자신의 위치를 판단하고 2. vision으로 위치 오차를 보정하고 3. distance 센서로 충돌 방지
```
##### TODO (우현, 인용, 두선)
```
파트
1. IMU 센서(두선), 2. 카메라 센서(인용), 3. 거리 센서(우현)
할일
1. 센서 여러개 (imu, camera, distance 중 최소 2개 이상)을 이용한 위치인식 또는 자율주행 자동차/드론 5개 paper 조사
- introduction을 통해 최근 동향 및 분야에 대해 공부하고 어떤 알고리즘 또는 모델을 이용했는지 정리하기.
2-A. IMU 센서 조사 - dji의 flight controller, px4의 flight controller, 갤럭시, 아이폰에서 사용되는 imu 센서
2-B. 라즈베리파이 카메라 테스트/ZED... ZED... 미드 제드...
2-B. 거리 센서 테스트
--- 중간 미팅: 4월 1일 월요일 12시~1시
3. IMU 센서 구매 - 3번 내용을 토대로 센서 선정 후 구매
4. 전체 센서를 이용한 algorithm/model을 flowchart 또는 psedo code로 만들기
--- 중간 미팅: 4월 4일 목요일 12시~1시
최종: 4월 11일
```
#### 미팅 2019-04-01-Mon (우현, 인용, 두선)
##### TODO
```
- 논문 조사 계속하기.
- IMU 센서 가격 비교 및 최종 구매 결정하기.
- 전체 알고리즘 또는 모델을 플로우차트 또는 수도코드로 만들기.
```




# ARdrone - Notebook 통신으로 센서 데이터 받아오기 (Linux(python2.7)환경에서 psdrone.py 테스트시 이상없음)
```
- psdrone은 linux 환경에 맞게 설정되어있음.(windows 용으로 변환필요)
- psdrone은 python2.7로 코드 환경이 구성되어있어서, 나중을 위해서 python3로 변환필요.
- ardrone - 노트북 통신으로 데이터를 받기 어려운경우 ardrone - raspi(Linux) - Notebook(windows - putty)도 고려.

- pixhawk
```
