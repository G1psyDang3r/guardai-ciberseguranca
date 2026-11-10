# Fundamentos de Cibersegurança e AppSec

## Conceitos Chave
* **Vulnerabilidade:** Uma falha ou fraqueza no código, arquitetura ou configuração de um sistema que pode ser explorada por uma ameaça.
* **Ameaça:** Qualquer circunstância ou evento com o potencial de causar danos a um sistema (ex: um atacante mal-intencionado, um script automatizado de varredura).
* **Risco:** A probabilidade de uma ameaça explorar uma vulnerabilidade específica e o impacto resultante para o negócio ou aplicação.

## Tríade da Segurança (CIA)
1. **Confidencialidade:** Garantir que informações sensíveis só sejam acessadas por quem tem autorização legítima.
2. **Integridade:** Proteger os dados contra alterações não autorizadas, garantindo que permaneçam precisos e confiáveis.
3. **Disponibilidade:** Garantir que os sistemas e dados estejam acessíveis aos usuários autorizados sempre que necessário.

## Boas Práticas de Desenvolvimento Seguro
* **Validação e Sanitização de Entradas:** Nunca confiar nos dados fornecidos pelo usuário; validar tipos, comprimentos e formatos.
* **Consultas Parametrizadas:** Utilizar parâmetros em vez de concatenar strings diretamente em comandos SQL para evitar SQL Injection.
* **Princípio do Menor Privilégio:** Conceder às contas e processos apenas as permissões estritamente necessárias para realizar suas tarefas.
