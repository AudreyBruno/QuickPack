# README

## Descrição
Este script em Python foi desenvolvido com o objetivo de automatizar a geração de arquivos para a equipe de suporte. Anteriormente, os membros da equipe precisavam realizar esse trabalho manualmente nos computadores dos clientes. O script simplifica e agiliza o processo, permitindo a compressão e organização de arquivos e pastas com base em configurações fornecidas em um arquivo `config.json`. Ele cria arquivos zipados dos arquivos ou diretórios especificados, acrescentando carimbos de data e informações adicionais conforme a configuração.

## Dependências
- Python 3.x

## Como Usar
1. Verifique se o Python 3.x está instalado no seu sistema.
2. Coloque o script no diretório desejado.
3. Prepare um arquivo `config.json` de acordo com o modelo fornecido.
4. Execute o script.

### Configuração
O arquivo `config.json` deve ter a seguinte estrutura:

```json
{
  "sub_nome": "nome_exemplo",
  "destino": "caminho\\para\\destino",
  "arquivos": [
    {
      "pasta": "caminho\\para\\diretorio\\fonte",
      "arquivo": "nome_arquivo.ext" 
    },
    {
      "pasta": "caminho\\para\\outro\\diretorio\\fonte",
      "arquivo": null
    }
  ]
}
```

- `"sub_nome"`: Nome adicional anexado ao arquivo zip gerado.
- `"destino"`: Diretório de destino para onde os arquivos zipados serão movidos.
- `"arquivos"`: Lista de dicionários especificando diretórios de origem (`"pasta"`) e arquivos específicos opcionais (`"arquivo"`). Se `"arquivo"` for `null`, o diretório inteiro será comprimido.

### Executando o Script
Execute o script executando o seguinte comando no seu terminal:
```
python QuickPack.py
```

## Funções
- `compactar_pasta(pasta_origem, nome_arquivo_zip)`: Comprime um diretório em um arquivo zip.
- `compactar_arquivo(origem_arquivo, nome_arquivo_zip)`: Comprime um único arquivo em um arquivo zip.
- `mover_arquivo(origem, destino)`: Move um arquivo para um destino especificado.

## Observações
- Carimbos de data são anexados aos nomes dos arquivos zip para garantir a unicidade.
- Se os diretórios de destino especificados no arquivo `config.json` não existirem, o script os criará.
- Certifique-se de que os caminhos especificados no arquivo `config.json` estão corretos e acessíveis.
- Este script pode ser integrado a fluxos de trabalho de automação maiores para fins de gerenciamento e arquivamento de arquivos.