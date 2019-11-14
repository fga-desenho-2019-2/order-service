ORDER_STATUS = (
  (1, 'Iniciado'),
  (2, 'Cancelado'),
  (3, 'Em andamento'),
  (4, 'Em processamento'),
  (5, 'Sendo preparado'),
  (6, 'Aguardando retirada'),
  (7, 'Finalizado'),
)
ORDER_STATUS_DICT = dict((v, k) for k, v in ORDER_STATUS)