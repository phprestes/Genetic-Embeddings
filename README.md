## **Genetic Embeddings: Gerando Embeddings de texto com Algoritmos Evolutivos (EA)**
### SSC0713 - Sistemas Evolutivos Aplicados à Robótica
---
* **Docente:** Eduardo do Valle Simões
* **Alunos:** Pedro Henrique de Sousa Prestes (15507819)
---
## Introdução
A ideia desse trabalho nasceu da possibilidade de aplicar **Algoritmos Evolutivos/Genéticos (EA/GA/AE/AG)** ao campo do **Processamento de Linguagem Natural (PLN)** inicialmente na previsão de palavras de palavras em frases e após isso, na geração de *embeddings* de texto, comparando a técnicas bem consolidadas com redes neurais como o **Word2Vec**.

## Metodologia
Inicialmente, foi feito um script simples em Python chamado `prever_palavras.py`, onde o Algoritmo Evolutivo tenta prever a probabilidade da próxima palavra em uma dada frase, no caso, **"o gato comeu o rato"**, pela simplicidade da implementação, o AG consegue prever bem até a última palavra (que não é avaliada propriamente).

Após isso, surge a ideia de gerar embeddings com AG, a implementação é feita no arquivo `embeddings_evolutivos.ipynb`, mais detalhes da sua implementação estão ao decorrer do notebook.

# Conclusão
Algoritmos Evolutivos podem performar bem em textos com vocabulário pequeno, mas não detém o desempenho e muito menos a eficiência do uso de técnicas como Word2Vec, aprendendo principalmente padrões sintáticos ao invés da semântica e decaindo cada vez mais para textos grandes e com vocabulário extenso, já que a possibilidade de erro aumenta geometricamente (para cada palavra adicionada, são n comparações a mais) necessitando de mais indivíduos e mais gerações, diminuindo muito a eficiência computacional.

# Vídeo de Apresentação
