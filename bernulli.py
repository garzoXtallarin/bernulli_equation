from manim import *
import numpy as np

class Ecuacion_bernulli(Scene):
    def construct(self):
        LB="#FFF0F5"
        DOG="#556B2F"
        MNB="#191970"
        self.camera.background_color=LB

        a1=MathTex("HIDRODINAMICA \\neq HIDROSTATICA",color=DOG)
        a2=Text("HIDRO=AGUA",color=DOG,font_size=40)  
        a21=Tex("DINÁMICA=MOVIMIENTO \\\\ ESTÁTICA=QUIETA",color=DOG,font_size=45)
        a3=Text("HIDRODINÁMICA=AGUA EN MOVIMIENTO\n\tHIDROSTÁTICA=AGUA QUIETA",color=DOG,font_size=40)
        a5=Text("AGUA SE ASOCIA CON TUBOS\n\tMANGUERAS, ARTERIAS, TUBERIAS ETC...",color=DOG,font_size=40)
        a6=Text("EL TUBO PUEDE ESTAR EN CUALQUIER POSICIÓN",color=DOG,font_size=30)  
        a7=Text("CAUDAL = VOLUMEN DE AGUA QUE CIRCULA",color=DOG,font_size=40)
        a8=Text("CAUDAL = Q",color=DOG,font_size=40)  
        a9=MathTex("Q=\dfrac{VOLUMEN}{\Delta TIEMPO}\\vee Q= VELOCIDAD * SECCION ",color=DOG,font_size=40)  
        a10=Text("SIEMPRE HAY CONTINUIDAD EN EL AGUA\n\tEL AGUA NO SE COMPRIME\n\tEL GAS SI SE COMPRIME",color=DOG,font_size=40)  
        a11=MathTex("Q_A=Q_B",color=DOG)
        a12=MathTex("V_A*S_A=V_B*S_B",color=DOG)
        a13=Text("+ SECCIÓN - VELOCIDAD \n\t - SECCIÓN + VELOCIDAD",color=DOG,font_size=40)
        logo=ImageMobject("UNAN.png").scale(0.2).move_to(np.array([0,2,-5]))
        p1=Text("UNAN MANAGUA",color=MNB).move_to(np.array([0,0,0])) 
        p2=Text("MATEMATICA APLICADA",color=MNB).move_to(np.array([0,-1,0])) 
        p3=Text("INTEGRADOR IV 2023",color=MNB).move_to(np.array([0,-3,0])) 
        self.add(logo)
        self.play(FadeIn(p1))
        self.play(FadeIn(p2))
        self.play(FadeIn(p3))
        self.wait(7)
        self.remove(logo)
        self.remove(p1)
        self.remove(p2)
        self.remove(p3)
        p4=Text("COMPONENTE DE",color=DOG,font_size=40).move_to(np.array([0,1,0])),Text("FISICA I",color=DOG,font_size=40).move_to(np.array([0,0,0])), Text("HIDRODINAMICA:",color=DOG,font_size=35).move_to(np.array([0,-1,0])), Text("ECUACION DE BERNULLI y DE TORRICELLI",color=DOG,font_size=35).move_to(np.array([0,-2,0])) 
        self.play(FadeIn(p4[0]),FadeIn(p4[1]),FadeIn(p4[2]),FadeIn(p4[3]))
        self.wait(3)
        self.remove((p4[0]),(p4[1]),(p4[2]),(p4[3]))
        
        self.play(Write(a1))
        self.wait(2.7)
        self.remove(a1)
    
        self.play(Write(a2))
        self.wait(2.7)
        self.remove(a2)
        self.play(Write(a21))
        self.wait(2.7)  
        self.remove(a21)
        
        self.play(Write(a3))
        self.wait(1.5)
        self.remove(a3)
        self.play(Write(a5))
        self.wait(2.5)
        self.play(Transform(a5,a6))
        self.wait(2)
        self.remove((a5),(a6))
        
        self.play(Write(a7))
        self.wait(1.5)
        self.play(Transform(a7,a8))
        self.wait(0.7)
        self.remove((a7),(a8))
        
        self.play(Write(a9))
        self.wait(1.5)
        self.remove(a9) 
        self.play(Write(a10))

        self.wait(2.7)
        self.remove(a10) 
        self.play(Write(a11))
        self.wait(3)
    
        self.play(Transform(a11,a12))
        self.wait(2.7)
        self.remove(a11)
        
        self.remove(a12)   
        self.play(Write(a13))
        self.wait(3)
        
        self.remove((a13))
        
        b1=Text("TUBOS HORIZONTALES",color=MNB)
        b2=MathTex("P_A+\dfrac{d_L}{2}V^{2}_{A}=P_B+\dfrac{d_L}{2}V^{2}_{B}",color=MNB)
        b3=Text("P=PRESIÓN(PASCAL)",color=MNB)
        b4=MathTex("d_L=DENSIDAD-DEL-LIQUIDO (\dfrac{Kg}{m^3})",color=MNB)
        b5=MathTex("V=VELOCIDAD(\dfrac{m}{s})",color=MNB)
        b6=Text("TUBOS HORIZONTALES",color=MNB).move_to(np.array([0,1,0])),Text("+VELOCIDAD -PRESIÓN",color=MNB).move_to(np.array([0,0,0])),Text("-VELOCIDAD +PRESIÓN\n\t +SECCIÓN +PRESIÓN",color=MNB).move_to(np.array([0,-1,0]))
        self.play(Write(b1))
        self.wait(2)
        self.remove(b1)
        self.play(Write(b2))
        self.wait(4)
        self.remove(b2)
        self.play(Write((b3).move_to(np.array([0,3,0]))),Write((b4).move_to(np.array([0,2,0]))),Write((b5).move_to(np.array([0,1,0]))))
        self.wait(4)
        self.remove((b3),(b4),(b5))
        self.play(Write(b6[0]),Write(b6[1]),Write(b6[2]))
        self.wait(3)
        self.remove((b6[0]),(b6[1]),(b6[2]))
        c1=Text("TUBOS VERTICALES\nTUBOS INCLINADOS",color=DOG)
        c2=MathTex("P_A+\dfrac{d_L}{2}V^{2}_{A}+d_Lgh_a=P_B+\dfrac{d_L}{2}V^{2}_{B}+d_Lgh_B",color=DOG)
        c3=Text("g=GRAVEDAD",color=DOG).move_to(np.array([0,1,0])),Text("h=ALTURA",color=DOG).move_to(np.array([0,0,0])),Text("SIEMPRE UNA DE LAS DOS ALTURAS ES CERO",color=DOG,font_size=25).move_to(np.array([0,-1,0]))
        d1=Text("TORRICELLI",color=MNB)
        d2=MathTex("V_B=\sqrt{2gh}",color=MNB)
        d3=Text("LA ALTURA SE MIDE DESDE EL ORIFICIO DE SALIDA",color=MNB)
        self.play(Write(c1))
        self.wait(3)
        self.play(Transform(c1,c2))
        self.wait(5)
        self.remove((c1),(c2))

        self.play(Write(c3[0]),Write(c3[1]),Write(c3[2]))
        self.wait(4)
        self.remove((c3[0]),(c3[1]),(c3[2]))
        self.play(Write(d1))
        self.wait(4)
        self.play(Transform(d1,d2),runtime=2)
        self.wait(4)
        self.remove(d1)
        self.play(Transform(d2,d3),run_time=2)
        self.wait(5)






