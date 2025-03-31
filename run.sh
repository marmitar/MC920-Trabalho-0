#!/usr/bin/sh

# Section 2.2
python main.py imagens/color.png monocromatico plano.bit 6 negativo mosaico padrao.txt -o resultados/execucao.png
# Section 3.1
python main.py imagens/color.png monocromatico -o resultados/colormono.png
python main.py imagens/city.png monocromatico -o resultados/citymono.png
# Section 3.2
python main.py imagens/color.png negativo -o resultados/colorneg.png
python main.py imagens/city.png negativo -o resultados/cityneg.png
# Section 3.3
python main.py imagens/color.png esp.vertical -o resultados/colorflip.png
python main.py imagens/city.png esp.vertical -o resultados/cityflip.png
# Section 3.4
python main.py imagens/color.png conv.intervalo -o resultados/colorconv.png
python main.py imagens/city.png conv.intervalo -o resultados/cityconv.png
# Section 3.5
python main.py imagens/color.png inverte.pares -o resultados/colorinvp.png
python main.py imagens/city.png inverte.pares -o resultados/cityinvp.png
# Section 3.6
python main.py imagens/color.png reflexao -o resultados/colorrefl.png
python main.py imagens/city.png reflexao -o resultados/cityrefl.png
# Section 3.7
python main.py imagens/color.png aj.brilho 2.5 -o resultados/colorgama.png
python main.py imagens/baboon.png aj.brilho 2.5 -o resultados/baboongama.png
# Section 3.8
python main.py imagens/color.png plano.bit 4 -o resultados/colorbit.png
python main.py imagens/baboon.png plano.bit 4 -o resultados/baboonbit.png
# Section 3.9
python main.py imagens/color.png combina imagens/butterfly.png 0.2 -o resultados/colormerg.png
python main.py imagens/baboon.png combina imagens/butterfly.png 0.2 -o resultados/baboonmerg.png
# Section 3.10
python main.py imagens/color.png mosaico padrao.txt -o resultados/colormsc.png
python main.py imagens/baboon.png mosaico padrao.txt -o resultados/baboonmsc.png
