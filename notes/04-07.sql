-- -----------
-- Fri,  7 Apr
-- -----------

select cName
    from College as R
    inner join College as S
    where
        (R.state = S.state)
        and
        (R.cName != S.cName);

select cName, state
    from College as R
    where not exists
        (select *
            from College as S
            where R.enrollment < S.enrollment);

select count(distinct sID)
    from Apply
    where cName == "Cornell";
