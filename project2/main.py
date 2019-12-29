from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy

def init():
    # 光源位置
    LightPos = [0, 0, 0, 1]
    # 环境光
    LightAmb = [0.5, 0.5, 0.5, 1.0]
    # 漫反射
    LightDiff = [1.0, 1.0, 1.0, 1.0]
    # 镜面发射
    LightSpec = [1, 1, 1, 1.0]

    global MatShn
    MatShn = [128]

    #创建光源
    glLightfv(GL_LIGHT0, GL_POSITION, LightPos)
    glLightfv(GL_LIGHT0, GL_AMBIENT, LightAmb)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, LightDiff)
    glLightfv(GL_LIGHT0, GL_SPECULAR, LightSpec)

    #渲染中使用光照
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)

    glClearColor(0, 0, 0, 1)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    gluPerspective(60,1,0.1,100)
    gluLookAt(10,10,30, 0,0,0, 0,1,0)
    glEnable(GL_DEPTH_TEST)

def drawPlanet(sun_dist, radius, angle, r,g,b):
    global MatShn
    glLoadIdentity()
    # 材质属性
    MatAmb = [r, g, b, 1]
    MatDif = [r, g, b, 1]
    MatSpec = [r, g, b, 1]

    # 设置材质属性
    glMaterialfv(GL_FRONT, GL_AMBIENT, MatAmb)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, MatDif)
    glMaterialfv(GL_FRONT, GL_SPECULAR, MatSpec)
    glMaterialfv(GL_FRONT, GL_SHININESS, MatShn)

    glColor(r,g,b)
    
    #旋转
    glRotate(angle,0,0,1)
    glTranslate(sun_dist,0,0)
    glutSolidSphere(radius,30,30)

angle = [0, 0, 0, 0]

def draw():
    global angle

    # 清除缓冲
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    # 恒星
    MatAmb = [1, 0, 0, 1]
    MatDif = [1, 0, 0, 1]
    MatSpec = [1, 0, 0, 1]
    glMaterialfv(GL_FRONT, GL_AMBIENT, MatAmb)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, MatDif)
    glMaterialfv(GL_FRONT, GL_SPECULAR, MatSpec)
    glMaterialfv(GL_FRONT, GL_SHININESS, MatShn)
    glutSolidSphere(1,30,30)

    # 行星一
    drawPlanet(3.87, 0.35, angle[0], 0.7,0.3,0)
    angle[0] = (angle[0] % 360) +4.09

    # 行星二
    drawPlanet(7.23, 0.87, angle[1], 0.9,0.7,0.3)
    angle[1] = (angle[1] % 360) + 1.6

    # 行星三
    drawPlanet(10, 0.91, angle[2], 0,0,1)
    angle[2] = (angle[2] % 360) + 0.99

    glutSwapBuffers()

if __name__ == "__main__":
	glutInit()
	glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE | GLUT_DEPTH)
	glutInitWindowSize(400,400)
	glutCreateWindow(b'Galaxy')
	glutDisplayFunc(draw)
	glutIdleFunc(draw)
	init()
	glutMainLoop()