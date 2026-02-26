numerical_columns = ["Age", 'ANTROPOMETRIA_Estatura_cm', 'ANTROPOMETRIA_Peso_Kg', 'Quedas_12meses_Hospitalizado_Dias', 
                     'ATIVIDADE_FISICA_Caminhada_Duracao_min_dia', 'ATIVIDADE_FISICA_Outras_AF_Duracao_min_dia',
                     'ANTROPOMETRIA_Massa_gorda', 'ANTROPOMETRIA_Massa_magra_Kg', 'ANTROPOMETRIA_Gordura_visceral',
                     'HANDGRIP_DIREITA_tentaiva1', 'HANDGRIP_DIREITA_tentativa2', 'HANDGRIP_DIREITA_tentativa_3',
                     'HANDGRIP_ESQUERDA_tentativa1', 'HANDGRIP_ESQUERDA_tentativa2', 'HANDGRIP_ESQUERDA_tentativa3',
                     'TIMED_UP_AND_GO_Simples_tentativa1', 'TIMED_UP_AND_GO_Simples_tentativa2', 'Best_TIMED_UP_AND_GO_Simples',
                     'TIMED_UP_AND_GO_Dupla_tarefa_tentativa1', 'TIMED_UP_AND_GO_Dupla_tarefa_tentativa2', 'Best_TIMED_UP_AND_GO_Dupla_tarefa', 'SIT_TO_STAND_Repetiçoes', 
                     '@6_MIN_ANDAR_N_voltas_completas', '@6_MIN_ANDAR_Resultado_teste_Metros', '@6_MIN_ANDAR_Distancia_TOTAL_metros',
                     'MMSE_Total', 'EQ5D5L_A_sua_saude_hoje_0_100']

discrete_columns = ['EQ5D5L_MOBILIDADE', 'EQ5D5L_CUIDADOS_PESSOAIS', 'EQ5D5L_ATIVIDADES_HABITUAIS', 'EQ5D5L_DOR_MAL_ESTAR', 'EQ5D5L_ANSIEDADE_DEPRESSAO',
                    'MMSE_LINGUAGEM_B_REPETICAO', 'MMSE_LINGUAGEM_C_COMANDO', 'MMSE_LINGUAGEM_D_LEITURA', 'MMSE_LINGUAGEM_E_FRASE_ESCRITA', 'MMSE_COPIA_DESENHO_1',
                    'MMSE_ORIENTACAO_TEMPORAL', 'MMSE_ORIENTACAO_ESPACIAL', 'MMSE_RETENCAO', 'MMSE_ATENCAO_CALCULO', 'MMSE_EVOCACAO_1', 'MMSE_LINGUAGEM_A_NOMEACAO',
                    "Freq_semanal", 'Quedas_12meses_Quantas','ATIVIDADE_FISICA_Caminhada_Frequência_Dias_semana', 'ATIVIDADE_FISICA_Outras_AF_Frequencia_Dias_semana',
                    '@6_MIN_ANDAR_Parou_Quantas_vezes']

binary_columns = ['Genero', 'Quedas_ultimos_12meses', 'Quedas_12meses_Lesao_Sim_Nao', 'Quedas_12meses_Assistencia_hospitalar_Sim_Não', 'Quedas_12meses_Hospitalizado_Sim_Não', 'Quedas_12meses_Medo_cair_Sim_Não',
                  'ATIVIDADE_FISICA_Geral_Sim_Não', 'HANDGRIP_Mao_DOMINANTE', 'TIMED_UP_AND_GO_Simples_Apoio_mãos', 'TIMED_UP_AND_GO_Simples_Auxiliar_marcha', 'TIMED_UP_AND_GO_Dupla_tarefa_Apoio_maos',
                  'TIMED_UP_AND_GO_Dupla_tarefa_Auxiliar_marcha', 'SIT_TO_STAND_Apoio_maos', 'SIT_TO_STAND_Auxiliar_marcha', '@6_MIN_ANDAR_Auxiliar_marcha', '@6_MIN_ANDAR_Parou']


ordinal_columns = ['Escolaridade', 'MMSE_EDUCAÇAO', 'ATIVIDADE_FISICA_Caminhada_Intensidade', 'ATIVIDADE_FISICA_Outras_AF_Intensidade', 'Percentil_TIMED_UP_AND_GO_Simples',
                   'Percentil_TIMED_UP_AND_GO_Dupla_tarefa', 'Percentil_SIT_TO_STAND_Repetiçoes', 'Percentil_@6_MIN_ANDAR_Distancia_TOTAL_metros']


nominal_columns = ['Momento', 'Local_de_Avaliacao', 'Modalidade', '@6_MIN_ANDAR_Percurso']

written_vars = ["Quedas_12meses_Situacao", "Quedas_12meses_Lesao_Tipo", "Quedas_12meses_Lesao_Local", "@6_MIN_ANDAR_Parou_Motivo", "@6_MIN_ANDAR_Desistiu"] # + ATIVIDADE_FISICA_Outras_AF_Qual