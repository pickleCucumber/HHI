select dt, od, summa, sqr, sum(sqr)OVER() as HHI
from
(select dt, od, summa,
POWER(((od/summa)*100), 2) as sqr 
from
(select st.state_desc as dt, sum(col17 /*+ col37*/ )/ 1000 as od,
sum(sum(col17 /*+ col37*/ )/ 1000)OVER() as summa
from db.dm_loan_monthly partition (M202002) t 
left join table.dm_cred_agreement cr on t.agreement_rk=cr.agreement_rk and cr.source_system_cd= 'storage1' 
left join table.dm_customer_info c on c.customer_rk=cr.crm_customer_rk and c.source_system_cd = 'storage2' 
left join table.u_customer_x_subject s on s.subject_rk=t.customer_rk and s.valid_to_dttm= date '4000-1-1' and s.u_aim_cd= 1 
left join table.u_customer_key_chng k on k.valid_to_dttm= date '4000-1-1' and k.u_customer_rk=s.u_customer_rk 
left join table_regions reg on reg.region_id=cast(nvl(substr(k.kpp,1,2), substr(k.inn,1,2)) as number)
left join table_regions reg2 on reg2.state_id=t.branch_cd
left join table.state st on st.state_cd = coalesce(c.c_adr_reg_state_cd, reg.state_cd, reg2.state_cd) and st.source_system_cd = 'storage2' and st.valid_to_dttm = date '4000-1-1' 
where nvl (t.credit_organization_cd, 'x' ) not in ( 'MFO' , 'SPV' )
group by st.state_desc))
