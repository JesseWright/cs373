-- -----------
-- Wed,  5 Apr
-- -----------

-- not right, why?

select sID, sName, GPA
from Student inner join Apply
using (sID)
where major = 'CS'

-- not right, why?

select distinct GPA
from Student inner join Apply
using (sID)
where major = 'CS'

-- not right, why?

select sID
from Student
where
sID in (select sID from Apply where major = 'CS')
and
sID in (select sID from Apply where major != 'EE')
