select sfera, col, summa, sqr, sum(sqr)OVER() as HHI
from
(select sfera, col, summa,
POWER(((col/summa)*100), 2) as sqr 
from
(select m.ifrs_industry as sfera, sum(col17) as col, 
sum(sum(col17))OVER() as summa
from storage.dm_loan_monthly m
where m.run_month =202012
and m.bap_prod_contour in ('Factoring','Кред. малого бизнеса','Кредитование крупного бизнеса','Кред. среднего бизнеса','Проектное финансирование','Синдицированный кредит')
group by m.ifrs_industry))
