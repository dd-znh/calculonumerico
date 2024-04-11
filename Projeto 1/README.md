# Projeto 1 de Cálculo Numérico

## Aluno: Eduardo Achar

## Enunciado

A novela das equações polinomiais

1. Introdução
A solução de equações polinomiais tem importância prática e histórica na Matemática. A solução de equações polinomiais foi um desafio para civilizações antigas como babilônios, gregos, chineses, indianos, egípcios e persas.

Embora soluções (geométricas) para equações quadráticas já fosse conhecidas há muitos anos, a solução de equações cúbicas chegou a ser declarada impossível por Luca Pacioli (Professor de Matemática de Leonardo Da Vinci).

O desenvolvimento de soluções para equações cúbicas (polinômios de grau três) é repleta de segredos, duelos matemáticos e traições dignas de uma novela italiana de horário nobre. Equações cúbicas também estão relacionadas com a origem de números complexos.

Atualmente, sabe-se que, para equações polinomiais de grau superior a quatro, uma fórmula geral não pode ser obtida. Neste cenário, soluções numéricas são particularmente importantes. As equações polinomiais são alvo desta atividade.

2. Tarefas
Esta tarefa consiste no desenvolvimento de um resolvedor de equações polinomiais. O resolvedor é separado em dois módulos:

Localizador de raízes. Utiliza quotas de módulo mínimo, de módulo máximo, de Cauchy e de Kojima para localizar as raízes.
Resolvedor de equações. Utiliza os métodos da falsa-posição de das secantes para encontrar uma raiz da equação.
O script principal da solução é dado a seguir:

n = input("");  % Lendo o grau do polinômio
P = read_poly( n ) ;  % Lendo os coeficients na forma a1x^n + a2x^(n-1) + a(n_1)
a_b = compute_best_quota(P);
printf("Best quotas = [%.2f, %.2f]\n", a_b(1), a_b(2));
x = compute_root(P, a_b(1), a_b(2));
printf("%6f\n", x);
O script lê o grau do polinômio e chama a função read_poly, que lê os coeficientes 𝑎𝑖,𝑖=1,2,…,𝑛+1
, de um polinômio de grau 𝑛
, 𝑃(𝑥)=𝑎1𝑥𝑛+𝑎2𝑥𝑛−1+…+𝑎𝑛+1.

Os coeficientes do polinômio 𝑃
 são armazenados em um vetor que, por sua vez, é utilizado pelas funções compute_best_quota e compute_root. A função compute_best_route, recebe o polinômio 𝑃
 e calcula os limites de um intervalo [𝑎,𝑏]
 que contém o módulo de todas as raízes de 𝑃
. O intervalo é o de menor comprimento que pode ser definido com as quotas de módulo mínimo, de módulo máximo, de Cauchy e de Kojima. A variável a_b é um vetor com duas posições, correspondendo, respectivamente, aos limites do intervalo [𝑎,𝑏]
.

Então, a função compute_root calcula uma raiz de fato para o polinômio 𝑃(𝑥)
. Caso 𝑃(𝑎)𝑃(𝑏)≤0
 é utilizado o método de falsa-posição, caso contrário, é utilizado o método das secantes (com um número máximo de iterações de 5000
 e aproximações iniciais 𝑥0=𝑎+𝑏2
 e 𝑥1=𝑥0+0.01
).

A solução implementada deve devolver uma aproximação 𝑥0
 para a raiz tal que |𝑃(𝑥0)|<10−6
.

As tarefas são implementar as funções:

read_poly,
compute_best_quota e
compute_root
para que o script funcione corretamente. Você pode implementar funções adicionais caso seja interessante.

3. Entrega e outros informações
Só serão aceitas entregas via Moodle (VPL).
O trabalho é individual e deve ser entregue até a data estipulada na tarefa do Moodle.
Para que a entrega esteja completa é necessário clicar no botão avaliar.
A nota fornecida pelo Moodle (VPL) é preliminar é pode sofrer alterações.
A solução precisa obedecer o enunciado e não pode se basear nos casos de teste.
3.1. Exemplo de caso de teste
Considere que se deseja uma solução para a equação polinomial 𝑃(𝑥)=𝑥3−8𝑥2+19𝑥−12=0
. A entrada (digitada no teclado) para o script seria:

3
1
-8
19
-12
E a saída correspondente deve ser:

Best quotas = [0.39, 10.02]
1.000000

## FEITOS:

 - mod_min_max
 - cauchy
 - fake_position

## TODO:

 - main
 - kojima
 - secantes

## Anotações
