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
- HAAR Cascade
- CNN
- NN Linear
- Filtros de correlação cruzada



