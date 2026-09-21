# V-006 — Resposta e limitações

## Resposta científica

**Não.** Entre as estimativas nacionais comparáveis em que a obesidade adulta
subiu de forma robusta entre 2001 e 2023, a prevalência de subnutrição não caiu
sempre. Em 133 países e áreas nessa condição, 81 tiveram queda robusta da
subnutrição, 28 tiveram alta robusta e 24 permaneceram indeterminados. Assim,
a queda foi mais comum que a alta, mas as duas trajetórias coexistiram.

Essa resposta é descritiva e ecológica. Ela não afirma que obesidade causou
subnutrição, que os mesmos indivíduos viveram os dois fenômenos, nem que uma
trajetória nacional explica outra.

## O que os dados sustentam

- Universo pareável em 2001→2023: 161 países e áreas.
- Alta robusta de obesidade adulta: 133.
- Dentro desses 133: `F=81`, `R=28`, `U=24`.
- Proporções condicionais: queda de subnutrição `60,9%`, alta `21,1%` e
  indeterminação `18,0%`.
- Diferença `p_F−p_R`: `+39,8` pontos percentuais.
- A hipótese H1 (`p_F > p_R > 0`) foi sustentada.
- A hipótese de robustez H2 foi sustentada nos 13 cenários congelados e por
  reprodução independente.

No mapa público de 2023, os 161 casos comparáveis formam três estados: 28
`BOTH ROSE`, 81 `OBESITY UP / UNDERNOURISHMENT DOWN` e 52
`OTHER / UNCERTAIN`. Outros 56 registros do universo não têm o par comparável
no endpoint. Dos 161 comparáveis, 149 cabem na geometria e 12 precisam aparecer
em uma faixa explícita fora do mapa.

## Evolução temporal utilizável

Cada quadro é recalculado contra 2001; não é uma animação cumulativa. De 2005
até 2023, em todos os pontos médios observados, `F` foi maior que `R`. Isso pode
ser mostrado como trajetória, mas não como sequência de observações anuais
independentes: a medida de subnutrição usa médias móveis centradas de três anos,
e quadros vizinhos compartilham dois anos.

A maior troca adjacente de estado público foi de 22 países entre 2007 e 2008.
Isso é um diagnóstico de movimento, **não** prova de choque, virada histórica ou
clímax. A V-007 poderá comparar esse momento com o estado final, mas não poderá
inventar uma ruptura.

## Heterogeneidade que impede uma regra universal

O padrão global não se repete da mesma maneira em todas as regiões. No recorte
regional de 2023, Oriente Médio, Norte da África, Afeganistão e Paquistão têm
`R=7` e `F=7`; na América do Norte, os dois casos condicionais são
indeterminados. Os denominadores regionais também variam muito. Portanto, não
há autorização para transformar o resultado global em ranking, culpa regional
ou regra sobre qualquer continente.

O contexto populacional observado — 7,708 bilhões de pessoas, com 71,4% em
`F`, 11,8% em `R` e 16,8% em `A` — é apenas ecológico e descritivo. Ele não
participa de H1 ou H2.

## Limitações obrigatórias

1. O estudo é observacional, descritivo e ecológico; não identifica causalidade.
2. Obesidade refere-se a adultos; subnutrição refere-se à população. O elo é o
   país-ano, não a mesma pessoa.
3. A pergunta foi informada por exploração anterior. O congelamento posterior
   protege fonte, qualidade, método e sensibilidade, mas não torna o teste
   pré-registrado independente.
4. Os resultados condicionais abrangem somente os 133 casos comparáveis com
   alta robusta de obesidade, e não “todos os países”.
5. Intervalos de incerteza definem alta, queda e indeterminação; uma estimativa
   pontual isolada não decide o estado.
6. Valores FAO iguais a 2,5 podem ser censurados abaixo de 2,5 e são tratados
   como intervalo `[0, 2,5]`.
7. A prevalência de subnutrição é uma média móvel centrada de três anos;
   quadros adjacentes se sobrepõem e não autorizam linguagem de choque anual.
8. O denominador condicional é pequeno nos primeiros anos após a linha de base;
   nenhuma “virada inicial” pode ser dramatizada sem mostrar esse denominador.
9. As regiões são heterogêneas e algumas têm poucos casos; não há ranking ou
   conclusão regional universal.
10. Doze casos comparáveis ficam fora da geometria do mapa, mas permanecem nos
    totais e devem ser mostrados separadamente.
11. A ponderação populacional é contexto ecológico, não um teste adicional de
    H1/H2 nem evidência sobre indivíduos.
12. Não houve replicação com outra fonte externa de obesidade/subnutrição,
    teste causal, previsão ou teste de revisões futuras da fonte.

## Tradução pública aprovada

O Short será silencioso, sem cartão de conclusão. A pergunta pode usar
`hunger` como abreviação compreensível, mas a legenda e a página de apoio devem
dizer `prevalence of undernourishment`. Os fatos que podem aparecer são:

- `2023 — 28 BOTH ROSE`
- `2023 — 81 OBESITY UP / UNDERNOURISHMENT DOWN`
- `52 OTHER / UNCERTAIN`
- `12 COMPARABLE PLACES ARE OFF-MAP`

O encerramento deve devolver interpretação ao público — por exemplo,
`SAME WORLD. DIFFERENT PATHS. WHAT DO YOU SEE?` e
`WHAT SHOULD WE COMPARE NEXT?` — com link/QR para metodologia, fontes e dados.
Isso mantém a curiosidade sem esconder a resposta científica, que permanece
documentada nesta página de suporte.

## Decisão da Change

`PASS_WITH_MANDATORY_LIMITATIONS`. A V-007 está autorizada a desenhar o arco de
atenção e o storyboard usando somente as observações permitidas. Nenhum
storyboard, render, página pública, upload ou publicação foi produzido ou
autorizado nesta Change.
