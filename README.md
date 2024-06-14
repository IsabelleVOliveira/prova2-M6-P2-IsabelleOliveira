# prova2-M6-P2-IsabelleOliveira

Desenvolvido por Isabelle Beatriz Vasquez Oliveira

## Requisitos

Certifique-se de ter os seguintes requisitos instalados:

- Python 3

Os outros requisitos você pode instalar usando o seguinte comando:

`pip install -r requirements.txt`

Esse repositório contém a implementação do HAAR Cascade para identificação de faces de um vídeo. 

Clone o repositorio com o comando de terminal: `git clone https://github.com/IsabelleVOliveira/prova2-M6-P2-IsabelleOliveira.git`

Para executar a análise computacional e salvar o vídeo com as análises feitas: `python3 main.py`

O funcionamento desse código foi demonstrado no vídeo a seguir:https://drive.google.com/file/d/1RZH4H6AZB1VCS8iphDHVQUd5DEv4FUQq/view?usp=sharing

# 2. Perguntas técnicas


Nesta seção, foram respondidas as perguntas técnicas da parte prática da segunda prova do módulo 6.


## 2.1.Descreva de maneira concisa (um parágrafo no máximo) o funcionamento do método de detecção escolhido.


Foi escolhido utilizar o Haar Cascade como método de detecção de faces. Esse método funciona por meio da utilização de "Haar-like features", que analisa imagens de forma rápida usando uma imagem integral, seleção de características por meio do algoritmo Adaboost e cascade de classificados que processam a imagem por etapas, rejeitando as regiões que não são de interesse do modelo. Dado que essa técnica analisa imagens, foi necessário dividir o vídeo em frames para que a detecção de faces fosse possível.


## 2.2 Considere as seguintes alternativas para resolver o problema de detecção de faces:
HAAR Cascade
CNN
NN Linear
Filtros de correlação cruzada
Classifique-os (coloque em ordem) em termos de viabilidade técnica (se é possível resolver o problema), facilidade de implementação e versatilidade da solução. Justifique sua classificação.

**Viabilidade técnica**
- Filtros de correlação cruzada
- CNN
- NN Linear
- HAAR Cascade

Filtros de correlação cruzada são os algoritmos com maior precisão e assertividade, sendo capaz de realizar detecção de objetos em tempo real em uma única passagem pela rede neural. A abordagem de um modelo unificado também reduz a carga computacional e melhora a velocidade de processamento.


CNN é considerado de alta eficácia para processamento de imagens além da capacidade de aprender características de baixo nível, como bordas e texturas, e características de alto nível, como faces.


NN Linear é muito versátil e permite a aplicação em aprendizado profundo. O que traz maior precisão na detecção de imagens já que é possível criar várias camadas na rede neural e determinação dos pesos e vieses em cada camada.


HAAR Cascade tem uma boa precisão nas análises e é relativamente rápido e eficiente em termos de recursos computacionais. Por outro lado, ele requer um ou mais arquivos xml com os dados relacionados ao que deve ser identificado e tem dificuldades em detectar objetos em diferentes orientações ou em condições muito complexas de fundo e iluminação.

**Facilidade de implementação**

- HAAR Cascade
- Filtros de correlação cruzada
- NN Linear
- CNN


Haar Cascade tem uma implementação super simples já que existem bibliotecas e ferramentas disponíveis que facilitam a implementação do Haar Cascade, como OpenCV.


Filtros de correlação cruzada também são relativamente simples, já que bibliotecas como YOLO usam esse tipo de algoritmo, por outro lado, é necessário realizar o treinamento de um modelo para realizar identificações.


NN Liner é utilizado em bibliotecas como o PyThorch, que simplificam sua aplicação, apesar da complexidade do código.


CNN é o mais complexo já que é necessário a criação de uma série de camadas convolucionais que aplicam filtros ou kernels à imagem de entrada, para depois realizar o processamento da análise computacional.


**Versatilidade da solução**

- CNN
- NN Linear
- Filtros de correlação cruzada
- HAAR Cascade


Com o CNN é possível realizar o treinamento da rede neural para qualquer tipo de requisito. O mesmo vale para NN Linear. No caso dos filtros de correlação cruzada, eles se limitam às bases de dados já encontradas na internet. O mesmo vale para o HAAR Cascade, que tem poucos arquivos xml disponíveis para a análise computacional.


## 2.3. Considerando as mesmas alternativas acima, faça uma nova classificação considerando a viabilidade técnica para detecção de emoções através da imagem de uma face.


- Filtros de correlação cruzada, trazem maior velocidade no processamento de grandes bases de dados.
- CNN permite maior personalização e precisão no treinamento, apesar de maior dificuldade de implementação
- NN Linear se assemelha muito com o CNN mas dificulta o treinamento do modelo
- HAAR Cascade necessita de um arquivo XML com os dados necessários para identificação das emoções e seria necessário criar esse arquivo (já que ele ainda não existe)


## 2.4. A solução apresentada ou qualquer outra das que foram listadas na questão 2.2. tem a capacidade de considerar variações de um frame para outro (e.g. perceber que em um frame a pessoa está feliz e isso influenciar na detecção do próximo frame)? Se não, quais alterações poderiam ser feitas para que isso seja possível?





