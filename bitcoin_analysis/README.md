# Análise da Flutuação do Preço de Fechamento do Bitcoin

## Diagnóstico Inicial

### Principais Características dos Dados
- **Colunas**: Date, Open, High, Low, Close, Volume
- **Valores Ausentes**: [Liste se houver]
- **Tipo das Colunas**: Data, Numéricas

### Limpeza de Dados
- **Tratamento de Valores Ausentes**: [Descreva as ações tomadas]
- **Conversão de Tipos**: Data foi convertida para datetime.

## Análise Visual

### Variação do Preço de Fechamento
- O gráfico a seguir mostra a flutuação do preço de fechamento do Bitcoin ao longo do tempo.

![Preço de Fechamento do Bitcoin](../reports/bitcoin_closing_price.png)

### Volume de Negociação
- O gráfico a seguir ilustra o volume de negociação ao longo do tempo.

![Volume de Negociação do Bitcoin](../reports/bitcoin_volume.png)

## Conclusões e Recomendações

1. **Tendências Observadas**:
   - [Descreva tendências de alta, baixa e períodos de estabilidade]
2. **Relação entre Preço e Volume**:
   - [Analise se há correlação entre preço e volume]
3. **Recomendações**:
   - [Sugestões para estratégias de investimento baseadas nas análises]

```

#### 4. `README.md`

```markdown
# Análise de Dados do Bitcoin

## Descrição do Projeto

Este projeto analisa a flutuação do preço de fechamento e o volume de negociação do Bitcoin com base em dados históricos. O objetivo é descobrir tendências e padrões para ajudar na tomada de decisões de investimento.

## Instruções para Executar o Código

1. Clone o repositório:
   ```
   git clone https://github.com/seu-usuario/bitcoin_analysis.git
   ```

2. Navegue até o diretório do projeto:
   ```
   cd bitcoin_analysis
   ```

3. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```

4. Execute o script de análise:
   ```
   python notebooks/analyze_bitcoin.py
   ```

   ou abra o notebook Jupyter:
   ```
   jupyter notebook notebooks/analyze_bitcoin.ipynb
   ```

## Relatório Final

O relatório final está disponível em [final_report.md](reports/final_report.md).

## Dependências

- pandas
- matplotlib
```
