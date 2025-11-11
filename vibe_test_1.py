import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# 1. Figure와 Axes 초기화
# Figure: 전체 창, Axes: 그래프가 그려질 영역
fig, ax = plt.subplots()

# x축 범위 설정 (0부터 2*pi까지)
x_data = np.linspace(0, 2 * np.pi, 100)
# y축 범위 설정 (-1.1부터 1.1까지)
ax.set_xlim(0, 2 * np.pi)
ax.set_ylim(-1.1, 1.1)

# 초기 빈 라인 객체를 생성합니다. 이 객체가 업데이트될 것입니다.
line, = ax.plot(x_data, np.sin(x_data), lw=2)

# 2. 초기화 함수 정의
# 애니메이션이 시작될 때 한 번 호출됩니다.
def init():
    line.set_ydata(np.sin(x_data)) # 초기 데이터 설정
    return line,

# 3. 애니메이션 함수 정의 (프레임 업데이트)
# 매 프레임마다 호출되어 그래프 데이터를 업데이트합니다.
def animate(i):
    # 'i'는 프레임 번호(FuncAnimation의 frames 인덱스)입니다.
    # sin 함수에 작은 위상 변화(0.1 * i)를 주어 움직이는 효과를 만듭니다.
    y = np.sin(x_data + 0.1 * i)
    line.set_ydata(y) # y 데이터 업데이트
    return line,

# 4. FuncAnimation 객체 생성 및 실행
# fig: 애니메이션이 표시될 Figure
# func: 매 프레임마다 호출될 함수 (animate)
# init_func: 애니메이션 초기화 함수
# frames: 프레임 수 (여기서는 200번 반복)
# interval: 프레임 간격 (밀리초 단위, 20ms = 초당 50프레임)
# blit: 최적화 옵션 (변경된 부분만 다시 그립니다. True 권장)
anim = FuncAnimation(
    fig,
    animate,
    init_func=init,
    frames=200,
    interval=20,
    blit=True
)

# 5. 애니메이션 표시
plt.show()

# 참고: Jupyter Notebook 환경에서는 anim.to_html5_video()를 사용하여 비디오를 표시할 수도 있습니다.
