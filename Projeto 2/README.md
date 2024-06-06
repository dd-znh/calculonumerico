1. Introdução
Considere um pêndulo de comprimento ℓ.
De acordo com a Segunda Lei de Newton, sabemos que 𝐹=𝑚𝑎
. No pêndulo, ao longo do eixo de movimento (linha verde na figura), temos apenas a projeção da força gravitacional 𝑚𝑔𝑠𝑖𝑛(𝜃)
. Note que, no eixo perpendicular ao movimento a tração e 𝑚𝑔𝑐𝑜𝑠(𝜃)
 se equilibram. Portanto 𝐹=−𝑚𝑔𝑠𝑖𝑛(𝜃)=𝑚𝑎,
 implicando em 𝑎=−𝑔𝑠𝑖𝑛(𝜃)
. O sinal negativo evidencia o fato de que a aceleração 𝑎
 e o movimento do ângulo 𝜃
 apontam para direções opostas. Mas o comprimento do arco 𝑠=ℓ𝜃
, então 𝑣=𝑑𝑠𝑑𝑡=ℓ𝑑𝜃𝑑𝑡.
 Portanto, 𝑎=𝑑2𝜃𝑑𝑡2=ℓ𝑑𝜃𝑑𝑡.
 Com isso, tem-se a uma equação diferencial ordinária que representa o movimento pendular.

𝑑2𝜃𝑑𝑡2+𝑔ℓ𝑠𝑖𝑛(𝜃)=0

ℓ
 é o comprimento do pêndulo, e
𝑔≈9.81𝑚𝑠2
 é a constante gravitacional.
2. Tarefa
Dados os parâmetros 𝑔=9.81𝑚/𝑠2
 e ℓ=0.1𝑚
, a posição angular inicial 𝜃=𝜋4
 e assumindo que o pêndulo, em 𝑡=0
, está em repouso. O objetivo deste trabalho é implementar uma solução que compute a posição angular 𝜃
 do pêndulo após 𝑇
 segundos. Em que 𝑇
 é um valor fornecido pelo usuário. Para isso, é necessário implementar pelo menos um dos métodos para solução de problemas de valor inicial.

É fornecida uma solução parcial, apresentada a seguir.

3. Implementação
O arquivo 𝑚𝑎𝑖𝑛.𝑚
 a seguir é fornecido e não deve ser alterado. O arquivo é responsável por ler o valor de 𝑇
 e chamar a função 𝑚𝑒𝑡𝑜𝑑𝑜_𝑒𝑠𝑐𝑜𝑙ℎ𝑖𝑑𝑜
 que deve ser implementada.

A função 𝑚𝑒𝑡𝑜𝑑𝑜_𝑒𝑠𝑐𝑜𝑙ℎ𝑖𝑑𝑜
 recebe:

𝑡ℎ𝑒𝑡𝑎0
: a posição angular inicial do pêndulo.
𝑣0
: a velocidade inicial do pêndulo.
𝑔
 e 𝐿
: aceleração gravitacional e comprimento do pêndulo, respectivamente.
ℎ
: passo de discretização utilizado pelo método.
𝑇
: momento final (a partir de 𝑡=0
), em que se deseja conhecer a posição angular do pêndulo.
A função deve retornar 𝑦
, um valor correpondendo a posição angular do pêndulo em 𝑡=𝑇
.

T = input("");
g = 9.81; # m/s^2
L = 0.1; # meters
theta0 = pi/4; # Initial angular position
v0 = 0; # Initial velocity 
t = 0;
n = 1000; # Number of discretization steps
h = (T-t)/n;
y = metodo_escolhido(theta0, v0, g, L, h, T);
printf("%.5f\n", y);
4. Entrega e instruções adicionais
Só serão consideradas implementações de métodos vistos em aula (Euler, RK2 e RK4).
O número de passos de discretização é 𝑛=1000
 independente do método utilizado e do valor de 𝑇
.
Só serão aceitas entregas via Moodle (VPL).
O trabalho é individual e deve ser entregue até a data estipulada na tarefa do Moodle.
Para que a entrega esteja completa é necessário clicar no botão avaliar.
A nota fornecida pelo Moodle (VPL) é preliminar é pode sofrer alterações.
A solução precisa obedecer o enunciado e não pode se basear nos casos de teste.
Os códigos já fornecidos não devem ser alterados. A alteração dos códigos pode levar a inviabilidade de correção e, consequente, atribuição de nota zero ao trabalho. 
5. Referências
Burden, R. L., Faires, J. D., & Burden, A. M. (2015). Numerical analysis. Cengage learning.
Pendulum (Mechanics). Wikipedia. Disponível em: https://en.wikipedia.org/wiki/Pendulum_(mechanics). Acessado em Novembro de 2022.
Simple pendulum with friction and forcing | Lecture 27 | Differential Equations for Engineers. 
