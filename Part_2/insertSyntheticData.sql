#This insertSyntheticData.sql only update the real score data of the NBA games.

UPDATE Schedule
SET Scores = '95:93'
WHERE Time = '2013-10-09 19:30:00' and Home = 'San Antonio Spurs';

UPDATE Schedule
SET Scores = '86:75'
WHERE Time = '2013-10-11 20:30:00' and Home = 'Miami Heat';

UPDATE Schedule
SET NationaltV = 'ESPN'
WHERE Time = '2013-11-01 19:30:00' and Home = 'Los Angeles Lakers' and Away = 'Spurs';

UPDATE Schedule
SET Scores = '94:102'
WHERE Time = '2013-10-14 19:30:00' and Home = 'Dallas Mavericks';

UPDATE Schedule
SET Scores = '88:99'
WHERE Time = '2013-10-14 19:30:00' and Place = 'Barclays Center';