-- Create a stored procedure 'ComputerAverageWeightedScoreForUser'
-- that computes and stores the average weighted score for a student
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(user_id INT)
BEGIN
    UPDATE users AS U,
        (SELECT U.id, SUM(score * weight) / SUM(weight) AS w_avg
        FROM users AS U
        JOIN corrections AS C ON U.id=C.user_id
        JOIN projects AS P ON C.project_id = P.id
        GROUP BY U.id) AS T
    SET U.average_score = T.w_avg
    WHERE U.id=T.id;
END
$$
DELIMITER ;
