# 2. Perguntas técnicas

Nessa seção, foram respondidas as perguntas técnicas da parte pratica da segunda prova do módulo 6.

## 2.1.Descreva de maneira concisa (um parágrafo no máximo) o funcionamento do método de detecção escolhido.

Foi escolhido utilizar o Haar Cascade como metodo de detecção de faces. Esse método funciona por meio da utilização de "Haar-like features", que analisa imagens de forma rapida usando uma imagem integral, seleção de caracteristicas por meio do algoritimo Ada Boost e cascade de classificados que processam a imagem por etapas, rejeitando as regioes que não são de interesse do modelo. Dado que essa tecnica analisa imagens, foi necessario dividir o video em frames para que a detecção de faces fosse possivel.

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

Filtros de correlação cruzada são os algoritimos com maior precisar e arcertividade, sendo capaz de realizar detecção de objetos em tempo real em uma única passagem pela rede neural. A abordagem de um modelo unificado tambem reduz a carga computacional e melhora a valeocidade de processamento.

CNN foi considerado o com maior viabilidade técnica pela alta eficia para processamento de imagens alem da capacidade de aprender características de baixo nível, como bordas e texturas, e características de alto nível, como faces. 

NN Linear é muito versatil e permite a aplicação em aprendizado profundo. O que traz maior precisão na detecção de imagens já que é possivel criar varias camadas na rede neural e deterimanação dos pesos e vieses em cada camada. 

HAAR Cascade tem uma boa precisão nas analises e ser relativamente rápido e eficiente em termos de recursos computacionais. Por outro lado, ele requer um ou mais arquivos xml com os dados relacionados ao que deve ser identificado e tem dificuldades em detectar objetos em diferentes orientações ou em condições muito complexas de fundo e iluminação.

**Facilidade de implementação**
- HAAR Cascade
- Filtros de correlação cruzada
- NN Linear
- CNN

Haar Cascade tem uma implemtação super simples já que existem bibliotecas e ferramentas disponíveis que facilitam a implementação do Haar Cascade, como OpenCV.

Filtros de correlação cruzada tambem são relativamente simples já que bibliotecas como YOLO usam esse tipo de algoritimo, por outro lado, é necessario realizar o treinamento de um modelo para realizar identificações.

NN Liner é utilizado em bibliotecas como o PyThorch, que simplificam sua aplicação, apesar da complexidade do codigo.

CNN é o mais complexo já que é necessario a criação de uma série de camadas convolucionais que aplicam filtros ou kernels à imagem de entrada, para depois realizar o processamento da analise computacional.

**Versatilidade da solução**

- CNN
- NN Linear
- Filtros de correlação cruzada
- HAAR Cascade

## 2.3. Considerando as mesmas alternativas acima, faça uma nova classificação considerando a viabilidade técnica para detecção de emoções através da imagem de uma face.

- Filtros de correlação cruzada, trazem maior velocidade no processamento de grandes bases de dados.
- CNN permite maior pernolazilação e precisão no treinamento, apesar de maior dificuldade de imolementação
- NN Linear se asemelha muito com o CNN mas dificulta o treinamento do modelo
- HAAR Cascade necessita de um arquivo XML com os dados necessarios para identificação das emoções e seria necessario criar esse arquivo (já que ele ainda não existe)


## 2.4. A solução apresentada ou qualquer outra das que foram listadas na questão 2.2. tem a capacidade de considerar variações de um frame para outro (e.g. perceber que em um frame a pessoa está feliz e isso influenciar na detecção do próximo frame)? Se não, quais alterações poderiam ser feitas para que isso seja possível?



