-- Average score
-- Creates a stored procedure ComputeAverageScoreForUser
DELIMITER |
CREATE PROCEDURE ComputeAverageScoreForUser(
    IN user_id int
)
BEGIN
    UPDATE users
    SET average_score = (SELECT AVG(score) FROM corrections WHERE corrections.user_id = user_id)
    WHERE id = user_id;
END;
|